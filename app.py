import time
import random

from tracing import getTracer

tracer = getTracer()

def hello_world():
    with tracer.start_as_current_span("hello_world") as parent:
        text = "<p>Hello, World!</p>"
        with tracer.start_as_current_span("print") as child:
            print(text)
        while True:
            with tracer.start_as_current_span("sleep") as child:
                time.sleep(random.uniform(1.1,2.1))
        return text

hello_world()