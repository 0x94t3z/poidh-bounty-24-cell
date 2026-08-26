# Catatan Pengujian Software

[English](./SOFTWARE_BASELINE.md) | **Bahasa Indonesia**

## Lingkungan pengujian

- Tanggal: `2026-08-26`
- Komputer: Apple Silicon
- Sistem operasi: macOS `15.3.2` (`24D81`)
- Python: `3.11.15`
- Direktori sumber: `upstream/cell`
- Commit sumber: `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`
- Status Git: detached HEAD
- Lingkungan Python: `.venv` lokal
- Versi paket yang terpasang: `software/requirements-lock.txt`

## Hasil

| Bagian yang diuji | Hasil | Rincian |
|---|---|---|
| Pengujian utama firmware | LULUS | 41 dari 41 rangkaian pengujian lulus |
| Hash, key, alamat, transaksi, dan tanda tangan | LULUS | Pengujian BIP, RFC, EIP, OpenSSL, dan perbandingan internal lulus |
| Wallet dan alur utama aplikasi | LULUS | Alur perangkat lunak dan masukan berbahaya lulus |
| Gerbang darah dan sentuhan sintetis | LULUS | Hanya menguji alur software; belum menggunakan sampel fisik |
| Siklus baca/tulis kalibrasi | LULUS | Pengambilan data, pencarian ambang, serialisasi, pemuatan, dan klasifikasi lulus |
| Pemeriksaan silang skrip Bitcoin | LULUS | `python-bitcointx` berhasil menjalankan skrip legacy, SegWit, dan multisig |
| Pemeriksaan silang secp256k1 | LULUS | `coincurve`/libsecp256k1 lulus, termasuk perbandingan terhadap 300 key |
| Pemeriksaan silang Microchip | LULUS | `cryptoauthlib` sesuai dengan tata letak zona konfigurasi dan konstruksi CheckMac |
| Antarmuka pustaka perangkat keras | LULUS | Antarmuka display, Pillow, QR, GPIO, OpenCV, dan cryptoauthlib sesuai dengan kode |
| Vektor LMS RFC 8554 | LULUS | Vektor resmi Appendix F berhasil dibaca dan diverifikasi |
| Pembuatan gambar mekanis | LULUS | Pemeriksaan batas ukuran dan fitur lulus |
| Geometri komponen cetak | LULUS | Pemeriksaan manifold, kecocokan, dan batas pengaman lulus |
| Kontrak atestasi Solidity | LULUS | 19 lulus; 0 gagal; 0 dilewati |
| Regtest Bitcoin Core | LULUS | Core 31.1 menerima, memfinalisasi, dan menambang semua jenis skrip yang diuji |

## Hal yang belum dibuktikan

- Pengujian gerbang sintetis tidak membuktikan bahwa reader optik bekerja dengan darah asli.
- Chip ATECC tiruan dan pustaka Microchip tidak dapat memastikan kondisi chip fisik. Jalankan `verify --behaviour` pada perangkat asli sebelum mengunci zona datanya secara permanen.
- Pengujian antarmuka pustaka tidak memeriksa sambungan kabel, fokus kamera, offset display, pantulan tombol, kestabilan daya, atau akurasi sensor.
- Keberhasilan regtest tidak menggantikan demonstrasi wajib pada testnet publik menggunakan perangkat yang sudah dirakit.

## Perbedaan STL pada macOS

Semua file cetak berhasil dibuat ulang pada macOS/ARM64. Namun, dua file berikut tidak identik secara byte dengan file hasil Linux yang tersimpan di Git LFS:

- `models/print/display_bezel.stl`
- `models/print/optical_head.stl`

Bentuk geometrinya tidak berubah:

- Jumlah segitiga dan ukuran file sama.
- Perbedaan terdapat pada 54 catatan segitiga di bezel dan 6 di optical head.
- Selisih angka floating-point terbesar sekitar `2.2e-14`.
- Setelah angka yang sangat dekat dengan nol dinormalisasi, setiap file hasil pembuatan ulang identik secara byte dengan file yang tersimpan.

Penyebabnya adalah perbedaan perhitungan vektor normal yang sangat dekat dengan nol pada pustaka matematika tiap platform, bukan perubahan bentuk yang akan dicetak. Gunakan file STL dari commit acuan untuk perakitan ini. Perbaikan upstream dapat dilakukan secara terpisah dengan menormalisasi angka mendekati nol di `tools/stl.py`, lalu membuat ulang file Git LFS melalui proses peninjauan.

## Cakupan regtest

Pengujian menyeluruh milik repository dijalankan pada jaringan regtest privat dan sementara dengan Bitcoin Core `31.1.0`. Jenis skrip yang diuji:

- p2wpkh
- p2sh-p2wpkh
- p2pkh
- p2tr dengan sighash bawaan
- p2tr dengan `SIGHASH_ALL` eksplisit
- multisig p2wsh 2-dari-3

Pada setiap jalur, Core mengirim dana ke alamat yang diturunkan oleh firmware, membaca dan memfinalisasi PSBT buatan firmware, menerima transaksi ke mempool, lalu menambangnya. CI menggunakan Core 28.0 sebagai versi tetap. Hasil lokal ini membuktikan kompatibilitas dengan 31.1.0, tetapi tidak menggantikan hasil CI pada versi yang telah ditetapkan.

## Keputusan

Seluruh pemeriksaan yang tidak memerlukan perangkat keras telah selesai. Pengadaan perangkat keras dapat dimulai. Hasil ini tidak boleh disebut sebagai bukti keamanan fisik atau biometrik.
