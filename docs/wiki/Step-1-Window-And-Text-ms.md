[English](Step-1-Window-And-Text) · [Dansk](Step-1-Window-And-Text-da) · **Bahasa Malaysia**

# Langkah 1: tetingkap dan teks contoh

Program membuka tetingkap, `start_test` memilih teks contoh, dan tetingkap menunjukkan teks itu dengan medan input yang kosong. Masa tidak berjalan sehingga anda menaip, jadi anda boleh membaca teks dahulu.

![Tetingkap semasa dibuka](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-1-window.png)

![Medan input mendapat fokus](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-1-text.png)

## Jalankannya

```bash
python -m typing_speed_test
```

## Apa yang diajar oleh langkah 1

- **Reka bentuk berlapis.** Peraturan berada dalam pakej `domain` dan `application`. Tetingkap berada dalam `presentation` dan tidak tahu sebarang peraturan. Pakej `infrastructure` menyimpan senarai teks.
- **Satu port dengan versi palsu.** Kes guna meminta teks daripada `SampleTextSource`. Sumber sebenar ialah senarai teks; ujian menggunakan yang palsu, jadi tiada tetingkap dan tiada kerawakan diperlukan.
- **Paparan tanpa peraturan.** `TypingViewModel` memberi tetingkap teks dan baris status. Ia tidak mengimport Tkinter, jadi ujian biasa boleh menyemaknya.

Fail langkah ini: `start_test.py`, `typing_view_model.py`, `typing_view.py`, `composition_root.py`.

[Home-ms](Home-ms) · [Setup-ms](Setup-ms)
