"""
In-house replacement for stopit.ThreadingTimeout.

Originally used the stopit package, but it pulled in a setuptools transitive
dependency (pkg_resources) that was removed in setuptools 80+.
The API is intentionally identical to stopit's (ThreadingTimeout +
TimeoutException + state constants) so all call sites only changed their import.

Uses PyThreadState_SetAsyncExc to raise the exception in the context-manager's
thread. Caveats: (a) cannot interrupt blocking C-level calls like socket reads
or time.sleep — exception is only raised at the next Python bytecode boundary;
(b) relies on CPython internals, will not work on PyPy/Jython.
"""
import ctypes
import threading


class TimeoutException(Exception):
    pass


class ThreadingTimeout:
    TIMED_OUT = "timed_out"
    EXECUTING = "executing"
    FINISHED = "finished"

    def __init__(self, seconds):
        self._seconds = seconds
        self.state = self.EXECUTING
        self._timer = None
        self._thread_id = None
        self._lock = threading.Lock()

    def __enter__(self):
        self._thread_id = threading.current_thread().ident
        self._timer = threading.Timer(self._seconds, self._raise_in_thread)
        self._timer.daemon = True
        self._timer.start()
        return self

    def _raise_in_thread(self):
        with self._lock:
            if self.state != self.EXECUTING:
                return
            result = ctypes.pythonapi.PyThreadState_SetAsyncExc(
                ctypes.c_ulong(self._thread_id),
                ctypes.py_object(TimeoutException),
            )
            if result > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(
                    ctypes.c_ulong(self._thread_id), ctypes.c_long(0)
                )

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self._lock:
            self._timer.cancel()
            timed_out = exc_type is not None and issubclass(exc_type, TimeoutException)
            self.state = self.TIMED_OUT if timed_out else self.FINISHED
        return timed_out
