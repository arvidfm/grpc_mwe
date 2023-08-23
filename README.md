MWE for "Resource temporarily unavailable" error on `sys.exit()` immediately following channel close.

1. Run `poetry install` to install dependencies
2. Run `./run_server.sh` to start the gRPC server
3. Run `./run_client.sh` to run repeated gRPC requests

About 1/3 of the time, the following error is printed:

```
Attempt 20...
Exception in callback PollerCompletionQueue._handle_events(<_UnixSelecto...e debug=False>)()
handle: <Handle PollerCompletionQueue._handle_events(<_UnixSelecto...e debug=False>)()>
Traceback (most recent call last):
  File "/usr/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/asyncio/base_events.py", line 640, in run_until_complete
    self.run_forever()
  File "/usr/lib/python3.11/asyncio/base_events.py", line 607, in run_forever
    self._run_once()
  File "/usr/lib/python3.11/asyncio/base_events.py", line 1922, in _run_once
    handle._run()
  File "/usr/lib/python3.11/asyncio/events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
  File "/home/x/Documents/git/grpc_mwe/mwe.py", line 37, in main
    await run_client()
  File "/home/x/Documents/git/grpc_mwe/mwe.py", line 29, in run_client
    sys.exit(0)
SystemExit: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.11/asyncio/events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/completion_queue.pyx.pxi", line 147, in grpc._cython.cygrpc.PollerCompletionQueue._handle_events
BlockingIOError: [Errno 11] Resource temporarily unavailable
```

Removing the `sys.exit(0)` in `run_client` makes the error go away.
