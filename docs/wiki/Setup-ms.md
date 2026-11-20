[English](Setup) · [Dansk](Setup-da) · **Bahasa Malaysia**

# Persediaan

Halaman ini menunjukkan cara menjalankan projek pada komputer anda sendiri. Anda memerlukan Python 3.13 atau lebih baharu.

## Cipta persekitaran

Cipta persekitaran maya setempat bernama `.venv` dalam folder projek, aktifkannya dan naik taraf pip:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Pada Linux dan macOS, aktifkannya dengan `source .venv/bin/activate`.

## Pasang projek

```powershell
python -m pip install -e ".[dev]"
```

Arahan ini membaca `pyproject.toml`. Program ini tidak mempunyai kebergantungan masa jalan; kumpulan `dev` menambah alat ujian dan semakan.

## Jalankan aplikasi

Dengan persekitaran aktif, mulakan program dari folder projek (tersedia dari langkah 1):

```powershell
python -m typing_speed_test
```

## Jalankan ujian

```powershell
python -m pytest
```

## Apa yang kita peroleh dalam langkah ini

- **Satu fail konfigurasi.** `pyproject.toml` menyimpan nama projek, versi Python yang diperlukan, senarai kebergantungan masa jalan yang kosong dan tetapan semua alat.
- **Persekitaran maya.** `.venv` mengasingkan pakej projek daripada bahagian lain komputer, jadi projek berjalan sama di mana-mana.
- **Ujian sejak hari pertama.** Ujian pertama sudah menyemak pemalar, jadi tabiat menjalankan `pytest` bermula sebelum sebarang ciri wujud.
- **Pemalar di satu tempat.** `constants.py` menyimpan semua nilai tetap, seperti 60 saat ujian dan lima aksara bagi satu perkataan, jadi tiada nombor diulang dalam kod.
- **Kod sumber berdokumen.** Komen Doxygen dan `Doxyfile` menukar komen menjadi manual yang boleh dilayari.
- **Pintu kualiti.** `scripts/check.sh` menjalankan ujian, linter, penyemak jenis dan imbasan keselamatan sebelum setiap push.
- **Tempat selamat untuk ujian grafik.** Bekas Linux dengan paparan maya menjalankan ujian tetingkap dan mengambil tangkapan skrin, jadi ujian tidak pernah mengambil alih tetikus dan papan kekunci anda.
