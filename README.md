# Python logger
Basic Python console logger.

### Usage:
```python
import logger as logging_lib
logger = logging_lib.Logger()

logger.log_suc("Text", [["field1", "data"], ["field2", "data"]])
logger.log_err("Text", [["field1", "data"], ["field2", "data"]])
logger.log_dbg("Text", [["field1", "data"], ["field2", "data"]])
logger.log_wrn("Text", [["field1", "data"], ["field2", "data"]])

# Would clear the terminal
# clear_terminal()
```

#### Output:
![Output of the example code](https://raw.githubusercontent.com/k6ster/python-console-logger/main/example.png)

### Customize
```python
logger.set_color('suc', '\x1b[30;42m')
logger.set_color('field', '\x1b[32;41;1m')
logger.log_suc("Hiya", [['Field', '123']])
```

#### Output:
![Output of the example code](https://raw.githubusercontent.com/k6ster/python-console-logger/main/example_2.png)
