# Manipulator Position Monitor

A real-time position readout system for two independent micrometer-precision manipulators, replacing a legacy LabVIEW GUI. An Arduino Due reads 8 rotary encoders and streams position deltas over USB serial; a Python/PySimpleGUI desktop app accumulates those deltas and displays live X/Y/Z/Depth coordinates for both manipulators.

---

## System Overview

```
[ Rotary Encoders x8 ]
        │  (quadrature signals)
        ▼
[ Arduino Due ]
        │  USB serial @ 9600 baud
        ▼
[ Counter_set1.py ]  ←→  [ PySimpleGUI window ]
```

The Arduino firmware polls all encoders every 300 ms and sends only axes that changed, keeping the serial link quiet. The Python GUI accumulates the signed deltas into running counters and converts raw counts to a human-readable `IIII.DD` display format.

---

## Hardware Requirements

| Component | Notes |
|-----------|-------|
| Arduino Due | 3.3 V logic; chosen for its large number of interrupt-capable pins |
| Rotary encoders × 8 | Quadrature (A/B) output; best performance when both phases are on interrupt pins |
| USB cable (micro-B) | Programming port **or** native USB port of the Due |
| PC running Windows or Linux | Tested on Windows (COM port); Linux path commented in source |

### Encoder Pin Assignments (Arduino Due)

| Axis | Side | Pin A | Pin B |
|------|------|-------|-------|
| X    | Left  | 5  | 6  |
| D (Depth) | Left | 7 | 8 |
| Y    | Left  | 9  | 10 |
| Z    | Left  | 11 | 12 |
| Y    | Right | 13 | 14 |
| X    | Right | 15 | 16 |
| Z    | Right | 17 | 18 |
| D (Depth) | Right | 19 | 20 |

All pins on the Arduino Due support interrupts, giving maximum encoder performance.

---

## Software Requirements

### Python dependencies

```
PySimpleGUI
pyserial
```

Install with:

```bash
pip install PySimpleGUI pyserial
```

### Arduino library

The [PJRC Encoder library](http://www.pjrc.com/teensy/td_libs_Encoder.html) must be installed in the Arduino IDE before compiling the firmware.

Install via **Arduino IDE → Tools → Manage Libraries → search "Encoder" by Paul Stoffregen**.

---

## Installation

### 1. Flash the firmware

1. Open `Basic/Basic.ino` in the Arduino IDE.
2. Select **Board → Arduino Due (Programming Port)**.
3. Click **Upload**.
4. Note the COM port (Windows: `COMx`; Linux: `/dev/ttyACM0` or similar).

### 2. Configure the COM port

Open `Counter_set1.py` and update the port on line 31:

```python
# Windows
port_name = 'COM7'   # ← change to your actual port

# Linux — replace the serial constructor on line 35 with:
# ser = serial.Serial(f"/dev/{port_name}", '9600', timeout=1)
```

### 3. Run the GUI

```bash
python Counter_set1.py
```

Or use the pre-built Windows executable:

```
dist/Counter_set1.exe
```

---

## Usage

When the application starts it connects to the Arduino and opens the monitor window.

### Display format

Each axis shows a value formatted as `IIII.DD`, where:

- `IIII` — integer part (encoder counts ÷ 200)
- `DD` — fractional part, two decimal digits (derived from `abs(counts ÷ 2) mod 100`)

This scaling matches the mechanical resolution of the manipulator screws so the display reads directly in the intended units.

### Controls

| Button | Action |
|--------|--------|
| `zeroXL` / `zeroYL` / `zeroZL` / `zeroDepthL` | Zero individual left-manipulator axis |
| `zeroXR` / `zeroYR` / `zeroZR` / `zeroDepthR` | Zero individual right-manipulator axis |
| `Zero All L` | Zero all four left-manipulator axes at once |
| `Zero All R` | Zero all four right-manipulator axes at once |
| `Quit` | Close the window and release the serial port |

The Depth axis also supports zeroing via a **physical button** wired to the Arduino (long press = zero all; short press = zero Depth).

---

## Repository Structure

```
Counter/
├── Basic/
│   └── Basic.ino          # Arduino Due firmware
├── Counter_set1.py        # Main GUI — dual manipulator (Left + Right)
├── Encoder_GUI.py         # Alternative GUI — single manipulator, dynamic port selection
├── Counter_set1.spec      # PyInstaller spec for building the Windows executable
├── dist/
│   └── Counter_set1.exe   # Pre-built Windows executable
└── docs/
    ├── hardware-setup.md  # Detailed wiring and hardware notes
    └── serial-protocol.md # Arduino ↔ Python serial message format
```

---

## Building the Windows Executable

```bash
pip install pyinstaller
pyinstaller Counter_set1.spec
```

The executable is written to `dist/Counter_set1.exe`.

---

## Alternative GUI (`Encoder_GUI.py`)

A simpler, single-manipulator version that prompts for the COM port at startup. Useful for initial hardware bring-up or when only one manipulator is connected. The Linux serial path is active by default in this file; comment/uncomment the relevant `serial.Serial` line to switch platforms.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `serial.SerialException` on startup | Wrong COM port | Update `port_name` in `Counter_set1.py` or check Device Manager |
| All counters reset to zero unexpectedly | Malformed serial byte (noise or disconnect) | Check USB cable; ensure Arduino is powered and firmware is running |
| Counts drift or skip | Encoder A/B wires swapped or loose | Verify wiring against pin table above |
| No position change detected | 300 ms firmware poll means slow movement may be missed between polls | Normal behaviour; firmware only reports non-zero deltas |
