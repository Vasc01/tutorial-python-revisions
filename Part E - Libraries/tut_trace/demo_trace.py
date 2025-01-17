import sys
import trace


def test():
    l = []
    for i in range(100):
        l.append(i)


# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

# run the new command using the given tracer
tracer.runfunc(test)

# make a report, placing output in the current directory
result = tracer.results()
result.write_results(show_missing=True, coverdir=".")
