**English** · [Dansk](Step-1-Window-And-Text-da) · [Bahasa Malaysia](Step-1-Window-And-Text-ms)

# Step 1: window and sample text

The program opens a window, `start_test` chooses a sample text, and the window shows the text with an empty input field. The time does not run until you type, so you can read the text first.

![The window as it opens](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-1-window.png)

![The input field has the focus](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-1-text.png)

## Run it

```bash
python -m typing_speed_test
```

## What step 1 taught

- **A layered design.** The rules live in the `domain` and `application` packages. The window is in `presentation` and knows no rule. The `infrastructure` package holds the list of texts.
- **A port with a fake.** The use case asks a `SampleTextSource` for a text. The real source is a list of texts; the tests use a fake, so no window and no randomness is needed.
- **A view that holds no rule.** `TypingViewModel` gives the window the text and the status line. It does not import Tkinter, so a plain test can check it.

Files of this step: `start_test.py`, `typing_view_model.py`, `typing_view.py`, `composition_root.py`.

[Home](Home) · [Setup](Setup)
