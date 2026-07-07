from unittest.mock import patch

import pytest

from omnillm import LocalLLMManager


@patch("omnillm.adapters.ollama_adapter.ollama")
def test_session_history(mock_ollama):
    mock_ollama.chat.return_value = {"message": {"content": "I am an AI."}}

    manager = LocalLLMManager()
    session = manager.create_session(backend="ollama", model="test-model", system_prompt="Sys")

    # Check system prompt
    assert len(session.messages) == 1
    assert session.messages[0]["role"] == "system"

    # Send message
    resp = session.send("Who are you?")
    assert resp == "I am an AI."

    # Check history
    assert len(session.messages) == 3
    assert session.messages[1]["role"] == "user"
    assert session.messages[2]["role"] == "assistant"
    assert session.messages[2]["content"] == "I am an AI."


@pytest.mark.asyncio
@patch("ollama.AsyncClient")
@patch("omnillm.adapters.ollama_adapter.ollama")
async def test_async_session_history(mock_ollama, mock_async_client_cls):
    from unittest.mock import AsyncMock

    mock_instance = mock_async_client_cls.return_value
    mock_instance.chat = AsyncMock(return_value={"message": {"content": "Async AI."}})

    manager = LocalLLMManager()
    session = manager.create_session(backend="ollama", model="test-model")

    resp = await session.asend("Async test?")
    assert resp == "Async AI."
    assert len(session.messages) == 2
