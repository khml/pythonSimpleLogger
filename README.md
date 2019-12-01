# Python Simple Logger
Python Simple Logger is a thin wrapper for Python Standart Logger.

cf. Python Logger
https://docs.python.org/ja/3/library/logging.html#logging.Logger


# Usage
Clone this repository, or copy and paste `Loggers.py` file.

Using this logger from your code.

```
from Loggers import get_io_stream_logger

# getting a logger, this is a instance of logging.Logger
logger = get_io_stream_logger(__name__)

logger.debug("info level message")
logger.info("info level message")
```
