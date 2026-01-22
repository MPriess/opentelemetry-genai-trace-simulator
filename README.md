# OpenTelemetry GenAI Trace Simulator

This repository contains a simple script to generate traces for GenAI applications using OpenTelemetry. 
It simulates interactions with a language model and records the traces for analysis.

## Disclaimer

**This is an incubator project currently in development phase.**

## Getting Started

1. Prerequisites
    - Python 3.11+
    - An OTLP-compatible tracing backend and an API key
    - macOS/Linux shell (commands below use POSIX style).

```bash
python3 -m venv ven
source ven/bin/activate
pip install -r requirements.txt
```

2. Export required environment variable (replace with your real key)
```bash
export OTEL_EXPORTER_OTLP_HEADERS=Authorization="Bearer ..."
export OTEL_EXPORTER_OTLP_ENDPOINT=ingress.eu-west-1.aws.dash0.com:4317
export OTEL_SERVICE_NAME=opentelemetry-genai-trace-simulator
```

3. Run evaluation
```bash
opentelemetry-instrument python3 trace.py
```