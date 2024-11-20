"""Tests the `mistral._utils.convert_message_params` function."""

import pytest
from mistralai.models import (
    AssistantMessage,
    SystemMessage,
    ToolMessage,
    UserMessage,
)
from mistralai.types.basemodel import Unset

from mirascope.core.base import AudioPart, BaseMessageParam, ImagePart, TextPart
from mirascope.core.mistral._utils._convert_message_params import convert_message_params


def test_convert_message_params() -> None:
    """Tests the `convert_message_params` function."""

    message_params: list[
        BaseMessageParam | AssistantMessage | SystemMessage | ToolMessage | UserMessage
    ] = [
        UserMessage(content="Hello"),
        BaseMessageParam(role="user", content="Hello"),
        BaseMessageParam(role="user", content=[TextPart(type="text", text="Hello")]),
        BaseMessageParam(role="assistant", content="Hello"),
        BaseMessageParam(role="system", content="Hello"),
        BaseMessageParam(role="tool", content="Hello"),
        AssistantMessage(
            content="Hello", tool_calls=Unset(), prefix=False, role="assistant"
        ),
        SystemMessage(content="Hello", role="system"),
        ToolMessage(content="Hello", tool_call_id=Unset(), name=Unset(), role="tool"),
    ]
    converted_message_params = convert_message_params(message_params)
    assert converted_message_params == [
        UserMessage(content="Hello"),
        UserMessage(role="user", content="Hello"),
        UserMessage(role="user", content="Hello"),
        AssistantMessage(content="Hello"),
        SystemMessage(content="Hello"),
        ToolMessage(content="Hello", tool_call_id=Unset(), name=Unset(), role="tool"),
        AssistantMessage(
            content="Hello", tool_calls=Unset(), prefix=False, role="assistant"
        ),
        SystemMessage(content="Hello", role="system"),
        ToolMessage(content="Hello"),
    ]

    with pytest.raises(
        ValueError,
        match="Mistral currently only supports text parts.",
    ):
        convert_message_params(
            [
                BaseMessageParam(
                    role="user",
                    content=[
                        ImagePart(
                            type="image",
                            media_type="image/jpeg",
                            image=b"image",
                            detail="auto",
                        )
                    ],
                )
            ]
        )

    with pytest.raises(
        ValueError,
        match="Mistral currently only supports text parts.",
    ):
        convert_message_params(
            [
                BaseMessageParam(
                    role="user",
                    content=[
                        AudioPart(
                            type="audio",
                            media_type="audio/wav",
                            audio=b"audio",
                        )
                    ],
                ),
            ]
        )
