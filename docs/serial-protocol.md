# Serial Communication Protocol

## Overview

The Arduino Due firmware and the Python GUI communicate over USB serial at **9600 baud, 8N1**. The Arduino sends ASCII text lines; the Python app only reads (the Arduino does not accept commands).

---

## Message Format

Each message is one line terminated by `\r\n` (Arduino `Serial.println`):

```
<AXIS><SIDE><DELTA>\r\n
```

| Field  | Length | Values | Description |
|--------|--------|--------|-------------|
| AXIS   | 1 char | `X`, `Y`, `Z`, `D` | Which axis changed |
| SIDE   | 1 char | `L`, `R` | Left or Right manipulator |
| DELTA  | variable | signed integer | Change in encoder counts since last poll |

### Examples

| Message | Meaning |
|---------|---------|
| `XL-5\r\n` | X-axis, Left manipulator moved −5 counts |
| `YR3\r\n`  | Y-axis, Right manipulator moved +3 counts |
| `DL0\r\n`  | Depth, Left — no change (not normally sent) |

### Sign convention

The firmware computes `delta = oldPosition − newPosition`, so:

- **Positive delta** → encoder turned in the decreasing direction (depends on physical mounting)
- **Negative delta** → encoder turned in the increasing direction

This is inverted from the raw encoder library output. If the display counts in the wrong direction for a given axis, reverse the encoder A/B wires for that axis.

---

## Firmware Behaviour

- Poll interval: **300 ms** (`delay(300)` at the end of `loop()`)
- A message is only sent when an axis position has changed since the previous poll
- Multiple axes can change within a single 300 ms window; each sends its own line
- The encoder library uses interrupts internally, so no counts are lost between polls

---

## Python Parsing

`Counter_set1.py` reads one line per GUI event-loop iteration:

```python
line = ser.readline()          # blocks up to timeout=1 s
string = line.decode()         # bytes → str
axis = string[0]               # 'X', 'Y', 'Z', or 'D'
side = string[1]               # 'L' or 'R'
delta = int(string[2:])        # signed integer remainder
```

The parsed delta is added to the running counter for that axis/side combination. On any `ValueError` or `IndexError` (malformed line, e.g. during Arduino reset) all eight counters are reset to zero as a safety measure.

---

## Display Scaling

Raw counts are scaled for display using:

```python
integer_part  = counter // 200
decimal_part  = abs(counter // 2) % 100
display       = f"{integer_part:04d}.{decimal_part:02d}"
```

With ×4 quadrature decoding, a 50 CPR encoder produces 200 counts per revolution. If your encoders have a different CPR, adjust the divisors accordingly (`200` for the integer part, `2` for the decimal part).
