from unittest.mock import patch
from omnillm.adapters.ollama_adapter import OllamaAdapter

@patch("omnillm.adapters.ollama_adapter.ollama")
def test_ollama_json_mode(mock_ollama):
    mock_ollama.chat.return_value = {"message": {"content": '{"name": "test"}'}}
    adapter = OllamaAdapter()
    
    res = adapter.chat("test-model", [], json_mode=True)
    assert res == '{"name": "test"}'
    
    # Check that format='json' was passed
    args, kwargs = mock_ollama.chat.call_args
    assert kwargs.get("format") == "json"

@patch("omnillm.adapters.ollama_adapter.ollama")
def test_ollama_tools(mock_ollama):
    mock_ollama.chat.return_value = {
        "message": {
            "content": "",
            "tool_calls": [{"function": {"name": "test_tool"}}]
        }
    }
    adapter = OllamaAdapter()
    
    tools = [{"type": "function", "function": {"name": "test_tool"}}]
    res = adapter.chat("test-model", [], tools=tools)
    
    assert isinstance(res, dict)
    assert len(res["tool_calls"]) == 1
    assert res["tool_calls"][0]["function"]["name"] == "test_tool"
    
    args, kwargs = mock_ollama.chat.call_args
    assert kwargs.get("tools") == tools
