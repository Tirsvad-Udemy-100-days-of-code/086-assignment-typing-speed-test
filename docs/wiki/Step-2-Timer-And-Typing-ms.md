[English](Step-2-Timer-And-Typing) · [Dansk](Step-2-Timer-And-Typing-da) · **Bahasa Malaysia**

# Langkah 2: pemasa dan menaip

Masa bermula dengan aksara pertama yang anda taip, bukan apabila tetingkap dibuka. Semasa anda menaip, aksara yang betul bertukar hijau dan aksara yang salah bertukar merah dalam teks contoh, dan baris status mengira detik dari 60 saat. Ujian tamat apabila anda telah menaip seluruh teks atau masa tamat, dan input dikunci.

![Menaip dengan satu kesilapan dan 42 saat lagi](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-2-typing.png)

![Ujian telah tamat dan input dikunci](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-2-finished.png)

## Jalankannya

```bash
python -m typing_speed_test
```

## Apa yang diajar oleh langkah 2

- **Masa sebagai port.** Domain tidak pernah membaca jam. `RecordInput` meminta masa daripada port `Clock` dan menyampaikannya, jadi ujian menggunakan jam palsu dan tidak pernah tidur.
- **Peraturan dalam objek nilai.** `TypingTest.with_typed_text` menanda setiap aksara, menetapkan permulaan pada input pertama dan menamatkan ujian. Setiap perubahan memberi ujian baharu.
- **Peristiwa kekunci dalam Tkinter.** Satu jejak pada pemboleh ubah input melaporkan setiap perubahan, jadi memadam aksara berfungsi sama seperti menaipnya.
- **Panggilan balik `after` yang berulang.** Tetingkap memanggil `check_time` setiap 200 ms, jadi kiraan detik bergerak tanpa thread dan tetingkap kekal responsif.

Fail langkah ini: `typing_test.py`, `clock.py`, `record_input.py`, `system_clock.py`, `typing_view.py`.

[Home-ms](Home-ms) · [Setup-ms](Setup-ms)
