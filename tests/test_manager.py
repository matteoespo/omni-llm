import pytest
from unittest.mock import patch
from omnillm import LocalLLMManager

@patch("omnillm.adapters.ollama_adapter.ollama")
def test_manager_chat(mock_ollama):
    mock_ollama.chat.return_value = {"message": {"content": "Hello world!"}}
    
    manager = LocalLLMManager()
    response = manager.chat(
        backend="ollama",
        model="test-model",
        messages=[{"role": "user", "content": "hi"}]
    )
    
    assert response == "Hello world!"
    mock_ollama.chat.assert_called_once()
    
def test_manager_unsupported_backend():
    manager = LocalLLMManager()
    with pytest.raises(ValueError):
        manager.chat(backend="invalid", model="test", messages=[])