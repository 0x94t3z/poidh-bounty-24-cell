# Daftar Kerja

[English](./CHECKLIST.md) | **Bahasa Indonesia**

Untuk setiap pekerjaan yang selesai, tambahkan tanggal, lokasi bukti, hash transaksi, atau catatan singkat jika diperlukan. Kotak yang dicentang tanpa bukti pendukung tidak dianggap sebagai milestone bounty yang selesai.

## Kendali proyek

- [ ] Catat alamat wallet pengklaim.
- [ ] Catat saldo dan status awal bounty.
- [x] Tetapkan commit CELL `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`.
- [x] Simpan dokumen asli bounty dan perakitan.
- [ ] Buat `BUILD_LOG.md`, `CHANGES.md`, `COSTS.csv`, dan `RISKS.md`.
- [ ] Tetapkan batas pengeluaran tunai.
- [ ] Tetapkan batas jam kerja.
- [ ] Tetapkan saldo minimum bounty yang masih layak dikerjakan.
- [ ] Pastikan repository dan paket bukti tidak memuat rahasia.

## Pemeriksaan software

- [x] Catat sistem operasi dan versi Python.
- [x] Pasang semua dependency.
- [x] Jalankan `python firmware/run_tests.py`: 41 dari 41 rangkaian pengujian lulus.
- [ ] Simpan seluruh log mentah pengujian.
- [x] Jelaskan setiap kegagalan atau pengujian yang dilewati: pengujian opsional diulang tanpa ada yang dilewati dan vektor resmi RFC telah disediakan.
- [x] Pastikan semua path dan perintah tersedia pada commit acuan.
- [x] Jalankan pemeriksaan silang Bitcoin, libsecp256k1, dan Microchip tanpa ada yang dilewati.
- [x] Verifikasi vektor resmi RFC 8554 Appendix F.
- [x] Jalankan pengujian Solidity: 19 dari 19 lulus.
- [x] Jalankan regtest Bitcoin Core: semua jenis skrip diterima dan ditambang.
- [x] Catat hasilnya di `SOFTWARE_BASELINE.id.md`.

## Persiapan keselamatan

- [ ] Baca seluruh isi `SAFETY.md`.
- [ ] Pastikan peralatan yang bersentuhan dengan darah tidak akan dipakai bersama.
- [ ] Siapkan lancet steril, tersegel, dan sekali pakai.
- [ ] Siapkan kapas alkohol dan perlengkapan perawatan luka ringan.
- [ ] Siapkan wadah benda tajam.
- [ ] Pastikan prosedur pembuangan limbah setempat.
- [ ] Atur bantuan tenaga medis yang kompeten untuk pengambilan sampel jika diperlukan.
- [ ] Periksa kondisi penyedia sampel terhadap kontraindikasi dalam spesifikasi.
- [ ] Atur jarak waktu pengambilan sampel dengan aman; jangan melakukan tusukan jari berulang secara terburu-buru.
- [ ] Terapkan pengamanan laser sebelum perangkat pertama kali dinyalakan.

## Pengadaan reader

- [ ] Raspberry Pi Zero 2 W.
- [ ] Breakout AS7341 dengan pin LDR yang dapat diakses.
- [ ] Kamera Pi tipe OV5647.
- [ ] Kabel CSI sempit untuk Pi Zero.
- [ ] Modul laser 650 nm dengan driver, maksimal 5 mW.
- [ ] LED putih dan LED inframerah 940 nm.
- [ ] MOSFET dan komponen pasif.
- [ ] Microswitch untuk cartridge.
- [ ] Breadboard dan kabel jumper.
- [ ] microSD kelas A2, minimal 16 GB.
- [ ] PETG hitam.
- [ ] PETG putih.
- [ ] Film PET dan perekat 3M 300LSE.
- [ ] Catu daya 5 V/2 A yang stabil beserta kabelnya.
- [ ] Akses ke printer yang mampu mencetak PETG.
- [ ] Solder dan alat untuk memasang heat-set insert.
- [ ] Kaliper, pisau, obeng, cat, dan multimeter.
- [ ] Catat invoice, penjual, nomor komponen, ongkir, pajak, dan penggantian komponen.

## Milestone 1: Pi

- [ ] Pi dapat menyala dengan stabil.
- [ ] Radio dinonaktifkan sesuai persyaratan.
- [ ] Setiap perubahan antena telah didokumentasikan.
- [ ] Keluaran pemeriksaan radio telah disimpan.
- [ ] Konfigurasi daya telah dicatat.

## Milestone 2: AS7341

- [ ] Sensor terdeteksi dengan benar.
- [ ] Pengukuran kartu putih selesai.
- [ ] Seluruh 100 pembacaan mentah disimpan.
- [ ] Simpangan baku relatif dihitung.
- [ ] RSD di bawah 1%.
- [ ] Sambungan dan susunan pengujian telah difoto.

## Milestone 3: cartridge

- [ ] Satu cartridge percobaan dicetak dan diperiksa.
- [ ] Bidang putih hasil ironing halus dan konsisten.
- [ ] Dua puluh cartridge dicetak dari satu gulungan dalam satu sesi.
- [ ] REFERENCE dan NULL dicetak pada sesi yang sama.
- [ ] Hasil ukur setiap cartridge disimpan.
- [ ] Sebaran setelah normalisasi di bawah 3%.

## Milestone 4: ruang optik

- [ ] Komponen optik dicetak dengan orientasi yang diwajibkan.
- [ ] Saluran optik dicat hitam doff.
- [ ] Kecocokan ruang dan pergerakan cartridge diperiksa.
- [ ] Pembacaan cahaya lingkungan saat LED mati disimpan.
- [ ] Pembacaan saat LED menyala disimpan.
- [ ] Pembacaan cahaya lingkungan kurang dari 0,5% pembacaan saat LED menyala.

## Milestone 5: pemisahan spektrum

- [ ] Sampel darah segar diambil dengan aman.
- [ ] Kontrol pewarna diukur.
- [ ] Spektrum mentah disimpan.
- [ ] Pemisahan pada 415 nm dihitung.
- [ ] Hasil difoto dan dijelaskan.
- [ ] Keputusan lanjut atau berhenti dicatat.

## Milestone 6: rangkaian speckle

- [ ] Pengambilan data darah selama 600 detik selesai.
- [ ] Pengambilan data pewarna/kontrol selama 600 detik selesai.
- [ ] Dekorelasi awal dicatat.
- [ ] Dekorelasi akhir dicatat.
- [ ] Penurunan dan arah perubahan dicatat.
- [ ] Data mentah dipertahankan.
- [ ] Perilaku fisik sesuai harapan atau penyebab kegagalannya dijelaskan.

## Milestone 7: spoof panel

- [ ] Daftar semua jenis sampel dari `BUILD.md` pada commit acuan dibuat.
- [ ] Jumlah percobaan minimum untuk setiap jenis terpenuhi.
- [ ] ID sampel dan waktu pengambilan diperiksa.
- [ ] Data mentah `.npz` disimpan.
- [ ] `thresholds.json` dibuat.
- [ ] Tabel hasil untuk setiap jenis sampel dibuat.
- [ ] Tingkat penolakan palsu dihitung.
- [ ] Batas keyakinan *rule of three* dilaporkan.
- [ ] Susunan perangkat keras dan kondisi lingkungan dicatat lengkap.
- [ ] Hasil tak terduga dan kegagalan dipertahankan.
- [ ] Paket klaim reader atau kegagalan disiapkan.
- [ ] Keputusan mengenai pengeluaran untuk wallet dicatat.

## Pengadaan wallet

- [ ] Breakout ATECC608B; pastikan jenis chip yang tepat.
- [ ] Display ST7789 240 × 240 dengan pin CS.
- [ ] Webcam USB dengan jarak fokus yang sesuai.
- [ ] Adaptor micro-USB OTG.
- [ ] Empat tombol beserta penutupnya.
- [ ] Breakout USB-C khusus daya dengan resistor pulldown CC.
- [ ] Baut dan heat-set insert.
- [ ] Diffuser kaca buram dan epoksi kedap cahaya.
- [ ] Jendela cincin.

## Milestone 8: secure element

- [ ] Pastikan jenis chip dan sambungan kabel benar.
- [ ] Jalankan verifikasi perilaku sebelum penguncian.
- [ ] Simpan keluaran verifikasi.
- [ ] Pastikan semua perilaku wajib lulus.
- [ ] Tinjau konfigurasi permanen sebanyak dua kali.
- [ ] Lakukan penguncian hanya setelah tinjauan dinyatakan lulus.
- [ ] Pastikan proses probe tetap berhasil setelah konfigurasi.
- [ ] Dokumentasikan perilaku PIN/penghapusan destruktif menggunakan bahan uji yang boleh dibuang.

## Milestone 9: firmware perangkat

- [ ] Pasang firmware pada Pi.
- [ ] Jalankan seluruh rangkaian pengujian dengan sukses pada Pi.
- [ ] Periksa display.
- [ ] Periksa tombol.
- [ ] Periksa kamera QR.
- [ ] Hubungkan gerbang reader dengan modul penandatanganan.
- [ ] Simpan log lengkap.

## Milestone 10: provisioning

- [ ] Buat seed baru khusus pengujian.
- [ ] Selesaikan provisioning.
- [ ] Pastikan penyimpanan seed dapat dibuka kembali dengan benar.
- [ ] Buat cadangan offline.
- [ ] Pastikan cadangan tidak masuk ke foto, video, Git, atau bukti di cloud.
- [ ] Catat keputusan mengenai pendaftaran ruang yang bersifat opsional.

## Milestone 11: regtest

- [ ] Jalankan regtest tanpa peer eksternal.
- [ ] Kirim dana ke alamat yang diturunkan oleh perangkat.
- [ ] Tampilkan dan konfirmasi transaksi atau PSBT.
- [ ] Tandatangani melalui gerbang fisik.
- [ ] Pastikan node menerima transaksi.
- [ ] Tambang transaksi.
- [ ] Simpan masukan, hasil bertanda tangan, dan log.

## Milestone 12: testnet publik

- [ ] Catat nama testnet dan chain ID.
- [ ] Demonstrasikan tanda tangan yang diotorisasi dengan denyut nadi.
- [ ] Demonstrasikan tanda tangan yang diotorisasi dengan darah segar.
- [ ] Siarkan transaksi.
- [ ] Simpan tautan explorer.
- [ ] Simpan hash transaksi.
- [ ] Rekam video perangkat lengkap saat beroperasi.
- [ ] Hubungkan hasil gerbang dengan transaksi yang ditandatangani dalam paket bukti.
- [ ] Pastikan media tidak membuka rahasia atau data pribadi yang tidak diperlukan.

## Paket bukti

- [ ] `README.md` menjelaskan klaim dan langkah reproduksi.
- [ ] `MANIFEST.json` mencantumkan artefak utama.
- [ ] `CHECKSUMS.txt` berisi hash SHA-256.
- [ ] Catatan perakitan lengkap.
- [ ] Perubahan dari upstream telah didokumentasikan.
- [ ] Biaya dan penggantian komponen telah didokumentasikan.
- [ ] Foto dan video memiliki label yang jelas.
- [ ] Data mentah dan hasil kalibrasi disertakan.
- [ ] Hasil pengujian dan bukti transaksi testnet disertakan.
- [ ] Pemeriksaan untuk memastikan tidak ada rahasia atau data pribadi yang terbuka telah selesai.
- [ ] Paket IPFS telah diunggah.
- [ ] Paket dapat diambil melalui lebih dari satu gateway.

## Klaim POIDH

- [ ] Pastikan bounty masih aktif.
- [ ] Pastikan saldo terbarunya.
- [ ] Pastikan tidak ada voting yang sedang berjalan.
- [ ] Pastikan pengklaim bukan pembuat bounty.
- [ ] Pastikan dana gas Mainnet cukup.
- [ ] Tinjau judul, deskripsi, dan URI IPFS akhir.
- [ ] Kirim klaim.
- [ ] Catat ID klaim, hash transaksi, dan nomor blok.

## Voting dan pembayaran

- [ ] Pembuat bounty memasukkan klaim ke voting.
- [ ] Catat batas waktu voting.
- [ ] Bagikan ringkasan bukti dan tautan yang tidak dapat diubah.
- [ ] Pantau voting.
- [ ] Selesaikan voting setelah batas waktu jika diperlukan.
- [ ] Pastikan imbalan tercatat di `pendingWithdrawals`.
- [ ] Kirim transaksi penarikan dana.
- [ ] Catat hash penarikan dan jumlah akhir ETH yang diterima.
- [ ] Tulis evaluasi akhir proyek.
