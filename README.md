# Crash At

Python decorate to force a method to crash after a certain date:

```python
from crash_after import crash_after

@crash_after(date="09/07/1985")
def old_bad_code():
    pass
```

This packge has a single manual test, and no input validation. It works sorta. Enjoy.
