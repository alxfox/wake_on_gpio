import gpiod
import time
from gpiod.line import Direction, Value
LINE = 17

# This script activates GPIO signal pin <LINE> and deactivates it again after 5s
# May be used to simulate a long power button press when combined with a relay (to force a shutdown)

with gpiod.request_lines(
    "/dev/gpiochip0",
    consumer="blink-example",
    config={
        LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        )
    },
) as request:
        request.set_value(LINE, Value.ACTIVE)
        time.sleep(5)
        request.set_value(LINE, Value.INACTIVE)
