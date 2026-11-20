# Wireframe: Take a typing test

The wireframe of the main window of use case UC-001. The Product Owner gave no wireframe, so this is the first edition, built from the use case and the web version named in the assignment. It changes only on input from the Product Owner or from the use case; the code follows it.

## Layout

```text
+--------------------------------------------------------------+
| Typing Speed Test                                    [_][x]  |
+--------------------------------------------------------------+
| Text: [ sample 3 v ]                         Time left: 60 s |
+--------------------------------------------------------------+
|  The quick brown fox jumps over the lazy dog ...             |
|  (sample text; typed characters are green or red)            |
+--------------------------------------------------------------+
|  [ type here ______________________________________ ]        |
+------------------------------------------+-------------------+
| Result                                   | High scores       |
|  Words per minute: 42                    |  1. 61 wpm  98 %  |
|  Accuracy: 96 %                          |  2. 55 wpm  97 %  |
|  Right: 210   Wrong: 9                   |  ...              |
|  [ Try again ]                           |                   |
+------------------------------------------+-------------------+
| Status: message line                                         |
+--------------------------------------------------------------+
```

## States

| State | Sample text | Input | Time left | Result panel | High scores | Status line |
| --- | --- | --- | --- | --- | --- | --- |
| Ready | shown, nothing marked | enabled and empty; the text chooser is enabled | 60 s, not running | empty | the ten best, or empty | "Type to start" |
| Typing | typed characters marked right (green) or wrong (red) | enabled | counts down | empty | unchanged | "Typing" |
| Finished | marked as typed | disabled | stopped | words per minute, accuracy, right and wrong characters | updated | "Time is up" or "Text complete" |
| Error | unchanged | unchanged | unchanged | unchanged | unchanged | the reason, for example "Could not remember the result" |

The text chooser is usable only in the Ready state. The **Try again** button is enabled in every state except Ready and starts a new test with a new sample text.
