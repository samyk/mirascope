from unittest.mock import MagicMock, patch

from mirascope.integrations.langfuse._with_langfuse import with_langfuse


@patch(
    "mirascope.integrations.langfuse._with_langfuse.middleware_decorator",
    new_callable=MagicMock,
)
@patch(
    "mirascope.integrations.langfuse._with_langfuse.observe",
    new_callable=MagicMock,
)
def test_with_langfuse(
    mock_observe: MagicMock, mock_middleware_decorator: MagicMock
) -> None:
    """Tests the `with_langfuse` decorator."""
    mock_fn = MagicMock(__name__="mock_fn")
    mock_observe.return_value = MagicMock()
    with_langfuse(mock_fn)
    mock_middleware_decorator.assert_called_once()
    mock_observe.assert_called_once_with(
        name=mock_fn.__name__,
        as_type="generation",
        capture_input=False,
        capture_output=False,
    )
    call_args = mock_middleware_decorator.call_args[1]
    assert call_args["custom_decorator"] == mock_observe.return_value
    assert call_args["handle_response_model"] is not None
    assert call_args["handle_response_model_async"] is not None
    assert call_args["handle_call_response"] is not None
    assert call_args["handle_call_response_async"] is not None
    assert call_args["handle_stream"] is not None
    assert call_args["handle_stream_async"] is not None
    assert mock_middleware_decorator.call_args[0][0] == mock_fn
