from unittest.mock import patch

from fastapi.testclient import TestClient

from omnillm.server import app

client = TestClient(app)


def test_chat_completions_endpoint():
    with patch("omnillm.server.manager.achat") as mock_achat:
        mock_achat.return_value = "Mock response"

        response = client.post(
            "/v1/chat/completions", json={"model": "ollama/test", "messages": [{"role": "user", "content": "hi"}]}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["choices"][0]["message"]["content"] == "Mock response"

        # Verify call arguments
        mock_achat.assert_called_once()
        kwargs = mock_achat.call_args.kwargs
        assert kwargs["backend"] == "ollama"
        assert kwargs["model"] == "test"
        assert kwargs["messages"][0]["content"] == "hi"


def test_chat_completions_tools():
    with patch("omnillm.server.manager.achat") as mock_achat:
        mock_achat.return_value = {"content": "", "tool_calls": [{"function": {"name": "get_weather"}}]}

        response = client.post(
            "/v1/chat/completions",
            json={
                "model": "ollama/test",
                "messages": [{"role": "user", "content": "weather in tokyo"}],
                "tools": [{"type": "function", "function": {"name": "get_weather"}}],
            },
        )

        assert response.status_code == 200
        data = response.json()
        msg = data["choices"][0]["message"]
        assert msg["tool_calls"][0]["function"]["name"] == "get_weather"
        assert data["choices"][0]["finish_reason"] == "tool_calls"
