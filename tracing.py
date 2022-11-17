from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (OTLPSpanExporter, parse_headers)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)

resource = Resource(attributes={
    SERVICE_NAME: "123"
})

def getTracer():
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(
        OTLPSpanExporter(
            endpoint="",
            headers=parse_headers("")
        )
    )
    #processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)

    # Sets the global default tracer provider
    trace.set_tracer_provider(provider)

    # Creates a tracer from the global tracer provider
    tracer = trace.get_tracer(__name__)

    return tracer