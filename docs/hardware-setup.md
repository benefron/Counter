# Hardware Setup

## Components

### Arduino Due

The Arduino Due is required (not Uno or Mega). Key reasons:

- All digital pins support interrupts, allowing full quadrature decoding on every encoder channel without performance degradation.
- The PJRC Encoder library's `ENCODER_OPTIMIZE_INTERRUPTS` mode (enabled in the firmware) gives the highest count accuracy.
- 3.3 V logic levels — verify your encoder outputs are 3.3 V compatible or use a level shifter.

### Rotary Encoders

Any quadrature (incremental) rotary encoder with A and B outputs. The firmware uses the PJRC Encoder library which counts all four edges per cycle (×4 decoding), so a 50 CPR encoder yields 200 counts per revolution.

---

## Wiring

Each encoder requires four connections to the Arduino Due:

| Encoder pin | Arduino Due |
|-------------|-------------|
| A (Channel 1) | Signal pin A (see table) |
| B (Channel 2) | Signal pin B (see table) |
| VCC | 3.3 V |
| GND | GND |

### Pin assignment table

| Label | Axis | Manipulator | Pin A | Pin B |
|-------|------|-------------|-------|-------|
| XLEnc | X    | Left  | 5  | 6  |
| DLEnc | Depth | Left | 7  | 8  |
| YLEnc | Y    | Left  | 9  | 10 |
| ZLEnc | Z    | Left  | 11 | 12 |
| YREnc | Y    | Right | 13 | 14 |
| XREnc | X    | Right | 15 | 16 |
| ZREnc | Z    | Right | 17 | 18 |
| DREnc | Depth | Right | 19 | 20 |

### Physical zero button (optional)

A momentary pushbutton can be wired to the Depth encoder axis to trigger a software zero:

- Short press → zero the Depth counter for that side
- Long press → zero all counters for that manipulator

The button logic is handled in the Python GUI event loop; no additional Arduino firmware changes are needed beyond having the encoder signal reflect the button press.

---

## USB Connection

Connect the Arduino Due to the PC via the **Programming USB port** (the micro-B port closest to the power jack). The operating system will enumerate it as a virtual COM port:

- **Windows:** `COMx` — check Device Manager under "Ports (COM & LPT)"
- **Linux:** `/dev/ttyACM0` or `/dev/ttyACM1` — check with `ls /dev/ttyACM*` after plugging in

The firmware communicates at **9600 baud, 8N1**, no flow control.

---

## Signal Quality Tips

- Keep encoder cable runs short and away from motor drive lines to reduce noise.
- Twisted-pair or shielded cable is recommended for runs longer than ~30 cm.
- Add 100 nF decoupling capacitors between VCC and GND at the encoder connector if spurious counts are observed.
- The 300 ms firmware poll interval means very fast movements between polls may accumulate more counts than the display shows between refreshes, but no counts are lost — the encoder library uses interrupts internally.
