**English** · [Dansk](Step-2-Timer-And-Typing-da) · [Bahasa Malaysia](Step-2-Timer-And-Typing-ms)

# Step 2: timer and typing

The time starts with the first character you type, not when the window opens. While you type, right characters turn green and wrong characters turn red in the sample text, and the status line counts down from 60 seconds. The test ends when you have typed the whole text or the time is over, and the input is locked.

![Typing with one mistake and 42 seconds left](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-2-typing.png)

![The test has ended and the input is locked](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-2-finished.png)

## Run it

```bash
python -m typing_speed_test
```

## What step 2 taught

- **Time as a port.** The domain never reads a clock. `RecordInput` asks a `Clock` port for the time and passes it in, so a test uses a fake clock and never sleeps.
- **Rules in the value object.** `TypingTest.with_typed_text` marks each character, sets the start at the first input and ends the test. Each change returns a new test.
- **Key events in Tkinter.** A trace on the input variable reports every change, so deleting a character works as well as typing one.
- **A repeating `after` callback.** The window asks `check_time` every 200 ms, so the countdown moves without a thread and the window stays responsive.

Files of this step: `typing_test.py`, `clock.py`, `record_input.py`, `system_clock.py`, `typing_view.py`.

[Home](Home) · [Setup](Setup)
