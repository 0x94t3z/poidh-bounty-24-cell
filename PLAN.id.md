# Rencana Perakitan dan Klaim

[English](./PLAN.md) | **Bahasa Indonesia**

## Sasaran

Bangun CELL secara bertahap agar biaya penuh tidak dikeluarkan sebelum reader memberikan hasil yang layak diklaim:

1. Selesaikan pengujian software tanpa membeli perangkat keras.
2. Rakit dan uji reader sampai milestone 7.
3. Simpan seluruh hasil reader, termasuk kegagalan yang berguna.
4. Beli komponen wallet hanya jika reader menghasilkan bukti yang dapat diajukan.
5. Selesaikan milestone 8–12 dan kirim hasil lengkap selama bounty masih aktif.

## Status saat ini

- Spesifikasi ditetapkan pada commit `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`.
- Pengujian software selesai. Lihat [SOFTWARE_BASELINE.id.md](./SOFTWARE_BASELINE.id.md).
- Langkah berikutnya: tetapkan batas anggaran dan beli komponen reader.

## Waktu dan biaya

| Fase | Perkiraan waktu | Biaya baru | Hasil wajib |
|---|---:|---:|---|
| 0. Tetapkan versi acuan | 0,5 hari | $0 | Sumber dan syarat dapat dipulihkan |
| 1. Uji software | 1 hari | $0 | Tidak ada kegagalan software yang belum dijelaskan |
| 2. Beli komponen reader | 3–14 hari | Rp2,29–3,77 juta | Komponen dan bahan habis pakai reader telah diterima |
| 3. Rakit reader | 2–4 hari | — | Milestone 1–6 selesai |
| 4. Jalankan spoof panel | 1–3+ minggu | Bergantung pada sampel | Bukti milestone 7 |
| 5. Rakit wallet | 2–4 hari | Tambahan Rp0,89–2,16 juta | Milestone 8–12 selesai |
| 6. Publikasi dan klaim | 1–2 hari | Gas Mainnet | Klaim tercatat di POIDH |
| 7. Voting dan pembayaran | Minimal 2 hari | Gas Mainnet | Imbalan ditarik jika klaim menang |

Sediakan waktu sekitar 3–6 minggu. Jadwal terutama bergantung pada ketersediaan komponen dan akses yang aman ke sampel yang diwajibkan.

## 0. Tetapkan versi acuan

1. Simpan repository CELL di `upstream/` pada commit `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`.
2. Simpan salinan `BOUNTY.md`, `BUILD.md`, `BOM.csv`, `SAFETY.md`, `VALIDATION.md`, `PRINTING.md`, dan `CONTRIBUTING.md`.
3. Catat saldo bounty, pembuat bounty, klaim yang masuk, status voting, dan tanggal pemeriksaan.
4. Pisahkan semua bahan pengujian dari rahasia wallet pribadi.

Fase ini selesai jika sumber dan persyaratan tetap dapat dipulihkan walaupun repository upstream berubah.

## 1. Uji software

1. Catat sistem operasi, versi Python, dan dependency.
2. Jalankan pengujian repository:

```bash
pip install -r firmware/requirements.txt
python firmware/run_tests.py
```

3. Simpan kegagalan dan pengujian yang dilewati, bukan hanya hasil yang lulus.
4. Periksa kode yang menangani perangkat keras, kalibrasi, penandatanganan, penyimpanan seed, dan ATECC.
5. Jalankan pemeriksaan kriptografi, kontrak, dan regtest secara independen.

Fase ini telah selesai. Hasilnya tercatat di [SOFTWARE_BASELINE.id.md](./SOFTWARE_BASELINE.id.md).

## 2. Beli komponen reader

Periksa spesifikasi sebelum memesan:

- Raspberry Pi Zero 2 W.
- Breakout AS7341 yang menyediakan pin LDR/pengendali LED.
- Kamera Pi tipe OV5647 dengan lensa yang dapat dilepas.
- Kabel CSI 22-pin yang sempit untuk Pi Zero.
- Modul laser 650 nm dengan driver dan daya maksimal 5 mW.
- PETG putih dan hitam.
- LED, MOSFET, komponen pasif, sakelar cartridge, microSD, dan komponen prototipe sesuai BOM.
- Lancet steril, kapas alkohol, film PET untuk jendela, perekat yang ditentukan, dan wadah benda tajam.

Alat atau jasa yang harus tersedia:

- Printer 3D yang mampu mencetak PETG dengan bidang cetak minimal 120 × 80 mm.
- Solder dan mata solder untuk heat-set insert.
- Multimeter, kaliper digital, pisau kerajinan, obeng, dan cat hitam doff.
- Catu daya 5 V/2 A yang stabil beserta kabelnya.
- Bantuan tenaga medis yang kompeten jika ada sampel yang harus diambil dari vena.

Catat penjual, nomor komponen, jumlah, harga, ongkir, pajak, dan setiap penggantian komponen dalam `COSTS.csv`. Foto label dan tulisan pada papan elektronik ketika barang tiba. Jangan mengganti tata letak sensor, jenis kamera, antarmuka display, secure element, laser, ketebalan perekat, atau bahan cetak tanpa catatan teknis.

Gunakan [PROCUREMENT.id.md](./PROCUREMENT.id.md) untuk harga Indonesia, contoh sumber, dan daftar barang yang tidak boleh dibeli.

## 3. Rakit reader: milestone 1–6

### Milestone 1: Pi dan radio

Pastikan Pi dapat menyala dengan stabil dan nonaktifkan radio sesuai persyaratan. Simpan log boot, keluaran pemeriksaan radio, rincian catu daya, dan foto setiap perubahan antena.

### Milestone 2: kestabilan AS7341

Ambil 100 pembacaan dari kartu putih. Simpangan baku relatif harus di bawah 1%. Simpan data, perhitungan, foto sambungan, model papan sensor, rincian LED, dan kondisi pencahayaan.

### Milestone 3: cartridge

Cetak satu cartridge terlebih dahulu, lalu periksa ukuran dan permukaannya. Setelah sesuai, cetak 20 cartridge serta REFERENCE dan NULL dalam satu sesi menggunakan gulungan PETG putih yang sama. Sebaran hasil setelah normalisasi harus di bawah 3%.

### Milestone 4: ruang optik kedap cahaya

Pada tingkat cahaya lingkungan yang ditentukan, pembacaan kanal jernih ketika LED mati harus kurang dari 0,5% pembacaan ketika LED menyala. Simpan pengaturan cetak, pengerjaan akhir, rincian cat, hasil ukur, dan koreksi kecocokan komponen.

### Milestone 5: pemisahan spektrum

Pastikan pengukuran 415 nm dapat membedakan pewarna dari darah asli dengan jelas. Jika gagal, periksa kesejajaran, kontaminasi, saturasi, normalisasi bidang putih, geometri optik, dan komponen pengganti sebelum melanjutkan.

Milestone ini merupakan keputusan lanjut atau berhenti yang pertama.

### Milestone 6: pengukuran 600 detik

Rekam darah dan pewarna selama 600 detik. Darah segar seharusnya mulai dalam keadaan tidak berkorelasi lalu berhenti berubah; pewarna tidak boleh menunjukkan pola yang sama. Simpan seluruh data mentah serta laporkan dekorelasi awal, dekorelasi akhir, penurunan, dan arah perubahan. Jangan mengubah nilai ambang hanya agar hasil terlihat lulus.

## 4. Jalankan milestone 7

Uji setiap jenis sampel tiruan dan jumlah sampel minimum yang diwajibkan oleh `BUILD.md` pada commit acuan. Gunakan ID sampel, kondisi, dan waktu yang jelas.

Simpan:

- Data mentah `.npz`.
- `thresholds.json`.
- Hasil untuk setiap jenis sampel.
- Konfigurasi perangkat keras dan sistem optik.
- Nomor komponen printer, filamen, sensor, LED, kamera, dan laser.
- Tingkat penolakan palsu serta batas keyakinan *rule of three*.
- Perintah dan log kalibrasi.
- Hasil tak terduga dan kegagalan.

Keputusan setelah milestone 7:

- Jika lulus, amankan bukti reader lalu setujui anggaran wallet.
- Jika perangkat menghasilkan kegagalan yang berguna dan dapat direproduksi, siapkan klaim kegagalan.
- Jika penyebabnya cacat perakitan, perbaiki lalu ulangi hanya pengukuran yang terdampak.
- Jika sampel tidak aman atau tidak tersedia, hentikan pekerjaan sampai sampel dapat ditangani dengan benar.

Klaim reader dapat dikirim pada tahap ini. Klaim lengkap masih dapat diajukan kemudian jika bounty tetap terbuka.

## 5. Rakit wallet: milestone 8–12

### Milestone 8: ATECC608B

Pastikan jenis chip dan breakout sesuai. Jalankan `atecc_config.py verify --behaviour` selagi konfigurasinya masih dapat dipulihkan. Tinjau keluaran yang disimpan sebelum mengunci apa pun. Penguncian bersifat permanen; kegagalan yang belum diketahui penyebabnya menghentikan fase ini. Gunakan bahan uji yang memang boleh dihapus untuk pengujian PIN atau penghapusan destruktif.

### Milestone 9: firmware pada Pi

Jalankan pengujian yang diwajibkan langsung pada Pi. Periksa display, tombol, kamera QR, reader, dan secure element sebagai satu sistem.

### Milestone 10: provisioning dan cadangan

Buat seed baru khusus pengujian. Pastikan perangkat dapat membuka kembali penyimpanan seed terenkripsi miliknya, lalu buat cadangan offline. Jangan pernah memotret atau memublikasikan cadangan. Jalankan pendaftaran ruang opsional hanya setelah dampaknya terhadap pemulihan dipahami dan dicatat.

### Milestone 11: regtest

Jalankan proses regtest dari repository. Simpan transaksi masukan atau PSBT, hasil yang sudah ditandatangani, penerimaan oleh node, hasil penambangan, dan log lengkap.

### Milestone 12: testnet publik

Pada perangkat CELL yang sudah dirakit:

1. Tampilkan transaksi.
2. Buat tanda tangan yang diotorisasi dengan denyut nadi.
3. Buat tanda tangan yang diotorisasi dengan darah segar.
4. Siarkan transaksi testnet.
5. Simpan hash transaksi dan tautan explorer.
6. Buktikan bahwa hasil gerbang yang direkam terkait dengan transaksi yang sama.

Jangan gunakan seed pribadi atau dana Mainnet dalam jumlah berarti.

## 6. Susun paket bukti

Gunakan struktur berikut:

```text
evidence/
├── README.md
├── MANIFEST.json
├── CHECKSUMS.txt
├── BUILD_LOG.md
├── CHANGES.md
├── COSTS.csv
├── photos/
├── videos/
├── captures/
├── calibration/
│   ├── thresholds.json
│   └── touch_thresholds.json
├── test-results/
└── transactions/
```

README bukti harus memuat identitas bounty, jenis klaim, commit acuan, penggantian komponen, milestone yang selesai, metode kalibrasi, kegagalan, perubahan perakitan, bukti tanda tangan, transaksi testnet, petunjuk reproduksi, dan checksum.

Periksa setiap file agar tidak memuat PIN, seed, private key, data pribadi, atau informasi medis yang tidak diperlukan. Unggah direktori akhir ke IPFS, lalu uji pengambilannya melalui lebih dari satu gateway.

## 7. Kirim klaim POIDH

Sebelum menandatangani transaksi Mainnet, pastikan bounty #24 masih aktif, tidak ada voting untuk klaim lain, jumlah imbalan masih sepadan dengan biaya, pengklaim bukan pembuat bounty, konten IPFS dapat diakses, tidak ada rahasia yang terbuka, dan wallet klaim memiliki ETH yang cukup untuk gas.

Judul yang disarankan:

> CELL hardware build — pulse and fresh-blood authorized testnet signatures

Deskripsi yang disarankan:

> Completed CELL BUILD.md section 15 milestones 1–12 against commit 9ae536c. Evidence includes the running device, calibration data and thresholds, pulse- and fresh-blood-authorized signatures, testnet transaction, build changes, raw logs, and a reproducibility manifest. Full evidence: <IPFS URI>

Catat ID klaim, hash transaksi, nomor blok, waktu, dan URI IPFS persis seperti yang dikirim.

## 8. Voting dan penarikan dana

1. Pantau kapan pembuat bounty memasukkan klaim ke voting.
2. Catat batas waktu dua hari, pemilih, dan bobot suara.
3. Bagikan ringkasan bukti beserta tautan yang tidak dapat diubah.
4. Setelah batas waktu, selesaikan voting jika diperlukan.
5. Periksa saldo `pendingWithdrawals` milik pengklaim.
6. Panggil `withdraw()` lalu catat jumlah dan transaksinya.

## Hentikan dan tinjau ulang jika

- Bounty dibatalkan, diselesaikan, atau sedang melakukan voting atas klaim lain.
- Imbalan yang tersisa lebih rendah daripada batas kerugian yang telah disepakati.
- Sampel tidak dapat diperoleh atau ditangani dengan aman.
- Pemisahan pada 415 nm tetap gagal setelah kesalahan perakitan disingkirkan.
- Ruang optik tidak dapat memenuhi batas kebocoran cahaya.
- Kamera tidak dapat merekam speckle pada resolusi yang diwajibkan.
- Verifikasi perilaku ATECC gagal atau jenis chip belum pasti.
- Publikasi bukti akan membuka rahasia atau data pribadi yang sensitif.
