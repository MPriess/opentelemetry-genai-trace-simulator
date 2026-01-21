"""
Example GenAI tracing application with OpenTelemetry.
Shows how to send traces to various observability backends using standardized GenAI attributes directly.
"""
import json
from opentelemetry import trace

from opentelemetry.semconv._incubating.attributes.gen_ai_attributes import (
    GEN_AI_PROVIDER_NAME,
    GEN_AI_REQUEST_MODEL,
    GEN_AI_OPERATION_NAME,
    GEN_AI_USAGE_INPUT_TOKENS,
    GEN_AI_USAGE_OUTPUT_TOKENS, GEN_AI_REQUEST_TEMPERATURE, GEN_AI_REQUEST_MAX_TOKENS, GEN_AI_REQUEST_CHOICE_COUNT,
    GEN_AI_SYSTEM_INSTRUCTIONS, GEN_AI_INPUT_MESSAGES, GEN_AI_OUTPUT_MESSAGES,
)

from opentelemetry.trace import SpanKind
from opentelemetry.trace import Status
from opentelemetry.trace import StatusCode


def chat_complete_operation():
    """Example GenAI operation with comprehensive tracing using direct attributes"""

    # Get tracer after configuration
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("llm_call", kind=SpanKind.CLIENT) as span:
        span.set_attribute(GEN_AI_PROVIDER_NAME, "openai")
        span.set_attribute(GEN_AI_OPERATION_NAME, "chat")

        # Request attributes
        span.set_attribute(GEN_AI_REQUEST_MODEL, "gpt-4")
        span.set_attribute(GEN_AI_REQUEST_TEMPERATURE, 0.7)
        span.set_attribute(GEN_AI_REQUEST_MAX_TOKENS, 100)
        span.set_attribute(GEN_AI_REQUEST_CHOICE_COUNT, 1)

        # Input messages and system instructions
        span.set_attribute(GEN_AI_SYSTEM_INSTRUCTIONS, "You are a helpful AI assistant")
        span.set_attribute(GEN_AI_INPUT_MESSAGES, json.dumps([
            {"role": "user", "content": "Explain quantum computing"}
        ]))

        # Response attributes
        span.set_attribute(GEN_AI_OUTPUT_MESSAGES, json.dumps([
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Quantum computing is a revolutionary approach .."
                },
                "finish_reason": "stop"
            }
        ]))
        span.set_attribute("gen_ai.response.id", "chatcmpl-123abc")
        span.set_attribute("gen_ai.response.model", "gpt-4-0613")
        span.set_attribute("gen_ai.response.finish_reason", "stop")

        # Usage attributes
        span.set_attribute(GEN_AI_USAGE_INPUT_TOKENS, 50)
        span.set_attribute(GEN_AI_USAGE_OUTPUT_TOKENS, 180)

        span.set_status(Status(StatusCode.OK))

    # Simulate some processing
        import time
        time.sleep(0.1)

if __name__ == "__main__":
    print("🔄 Running example GenAI operation...")
    chat_complete_operation()
    print("✅ GenAI operation completed with tracing")
