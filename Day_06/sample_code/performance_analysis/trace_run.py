import trace

tracer = trace.Trace(count=False, trace=True)
tracer.run("recurse(2)")
