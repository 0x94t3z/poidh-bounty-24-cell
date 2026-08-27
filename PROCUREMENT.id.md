# Pengadaan di Indonesia

[English](./PROCUREMENT.md) | **Bahasa Indonesia**

Harga diperiksa pada `2026-08-27` dari penjual yang dapat mengirim ke Indonesia. Angka di bawah adalah anggaran pembelian, bukan jaminan harga. Ongkir, pajak impor, kupon, dan perubahan stok belum dihitung.

## Ringkasan anggaran

| Tahap | Perkiraan lokal |
|---|---:|
| Reader: perangkat keras dan pencetakan | Rp2.050.000–Rp3.240.000 |
| Reader: bahan habis pakai | Rp240.000–Rp530.000 |
| **Reader sampai milestone 7** | **Rp2.290.000–Rp3.770.000** |
| Tambahan untuk wallet | Rp890.000–Rp2.160.000 |
| **Perangkat lengkap** | **Rp3.170.000–Rp5.930.000** |
| Alat kerja jika belum punya | Rp730.000–Rp1.730.000 |
| **Perangkat lengkap dan semua alat** | **Rp3.900.000–Rp7.660.000** |

Tambahkan cadangan 15–25% untuk ongkir, impor, komponen gagal, dan cetak ulang. Dengan cadangan tersebut, batas aman perangkat lengkap tanpa membeli alat baru adalah sekitar **Rp3.700.000–Rp7.500.000**.

## Status pengadaan

- **LOKAL:** ada listing Indonesia yang sesuai secara umum.
- **KONFIRMASI:** tersedia, tetapi foto pin, tipe chip, ukuran, atau stok harus diperiksa dengan penjual.
- **IMPOR:** belum ditemukan listing domestik yang dapat dipastikan memenuhi spesifikasi.
- **JANGAN BELI:** produk tampak mirip, tetapi tidak cocok dengan rancangan.

## Reader: beli lebih dahulu

| Komponen | Spesifikasi yang wajib | Status dan contoh sumber | Anggaran |
|---|---|---|---:|
| Raspberry Pi Zero 2 W | Zero **2 W**, bukan Zero W atau Orange Pi | **LOKAL:** [Blibli](https://www.blibli.com/jual/raspberry-pi-zero-w) mencatat board sekitar Rp959.000–Rp988.000 | Rp959.000–Rp988.000 |
| AS7341 breakout | AS7341; pin `LDR`/pengendali LED harus dapat diakses | **KONFIRMASI:** [Mouser Indonesia, Adafruit 4698](https://www.mouser.co.id/en/ProductDetail/Adafruit/4698) Rp347.657 sebelum ongkir; [listing lokal](https://shopee.co.id/AS7341-AS734x-Visible-Spectral-Sensors-Module-Color-Temperature-illuminance-High-Accuracy-Color-Detection-For-Arduino-i.1696239063.58153336210) mulai Rp289.600, tetapi pin LDR belum terbukti | Rp290.000–Rp590.000 |
| Kamera speckle dan kabel | OV5647/v1, lensa dapat dilepas, kabel CSI 22-pin untuk Pi Zero | **KONFIRMASI:** [paket OV5647 dan kabel 15-ke-22 pin](https://shopee.co.id/Raspberry-Pi-Zero-Camera-Module-5MP-1080P-OV5647-Mini-Webcam-15-PIN-To-22PIN-for-Raspberry-Pi-5-Zero-2-W-Optional-5cm-30cm-i.1683140146.53302792766) Rp275.500–Rp318.500 | Rp276.000–Rp319.000 |
| Modul laser | Titik merah 650 nm, 3–5 V, maksimal 5 mW, memiliki driver dan lensa yang dapat diatur | **KONFIRMASI:** [listing 5 mW](https://shopee.co.id/Laser-Module-5mW-650nm-3V-5V-Red-Point-Cross-Line-Industrial-Laser-i.292092948.19558329929) sekitar Rp36.122. Pilih varian **point**, bukan line/cross | Rp25.000–Rp45.000 |
| LED dan rangkaian pengendali | LED putih 5 mm 5000 K ×2, LED IR 940 nm ×1, 2N7002 SOT-23 ×3, resistor dan kapasitor sesuai BOM | **LOKAL:** beli komponen satuan; kit umum hanya membantu untuk breadboard dan komponen pasif | Rp45.000–Rp90.000 |
| Microswitch | SPDT snap-action dengan lever | **LOKAL:** komponen umum; pastikan tersedia terminal `COM`, `NO`, dan `NC` | Rp10.000–Rp30.000 |
| Breadboard dan jumper | Breadboard kecil dan jumper male/female | **LOKAL:** [kit dasar](https://shopee.co.id/Breadboard-LED-Jumper-Wire-Button-Diy-Kit-Basic-Starter-Kit-arduino-i.380441770.7378850880) sekitar Rp30.000 | Rp30.000–Rp60.000 |
| microSD | A2, minimal 16 GB; kapasitas 32/64 GB boleh digunakan dan harus dicatat sebagai substitusi | **KONFIRMASI:** kartu A2 kecil sulit ditemukan; [SanDisk Extreme 64 GB A2](https://www.jakartanotebook.com/cari/ulutan-a2) tercatat Rp380.400 | Rp250.000–Rp440.000 |
| Catu daya | 5 V/2 A yang stabil beserta kabel; tanpa baterai | **LOKAL:** charger berkualitas dan kabel pendek | Rp60.000–Rp150.000 |
| Komponen cetak PETG | PETG hitam untuk ruang optik dan PETG putih untuk cartridge; jangan gunakan PLA | Pilih salah satu jalur pencetakan di bawah | Rp100.000–Rp520.000 |

### Pilihan pencetakan

Jasa cetak lebih murah untuk satu perangkat dan tidak memerlukan pembelian printer:

- [Astha Hub](https://shopee.co.id/Jasa-cetak-3D-Print-PETG-per-gram-dan-sedia-jasa-Request-Baca-Deskripsi-i.19106145.54863163308) mencantumkan Rp350–Rp930 per gram.
- [Pegangind](https://www.pegangind.com/services/3d-printing) mencantumkan PETG Rp329–Rp799 per gram, bergantung pada tinggi layer.
- Minta PETG putih dan hitam dari spool yang konsisten. Cartridge, REFERENCE, dan NULL harus dicetak dari spool putih dan sesi yang sama.
- Kirim file STL dari commit acuan, bukan file yang dibuat ulang pada platform lain.

Jika sudah memiliki printer, satu kilogram PETG per warna jauh melebihi kebutuhan satu perangkat tetapi berguna untuk cetak ulang. [eSUN PETG](https://toko.evolusi3d.com/product/esun-petg-filament-1-75mm-1-kg/) tersedia dalam hitam dan putih sekitar Rp259.000 per kilogram; opsi refill pernah tercatat [Rp165.000 per kilogram](https://www.blibli.com/p/esun-1-kg-refilament-petg-refill-for-esun-filament-spool/is--3DZ-60022-01679-00003).

## Bahan habis pakai reader

| Barang | Spesifikasi yang wajib | Status dan contoh sumber | Anggaran |
|---|---|---|---:|
| Safety lancet ×100 | Steril, sekali pakai, contact-activated, 28G/1,8 mm | **KONFIRMASI:** [ENDO EI.SL](https://endo.id/id/catalog/product/endo-ei-sl) menyediakan varian tepat tetapi harga harus diminta. Listing OneMed pernah sekitar [Rp66.500](https://shopee.co.id/SAFETY-LANCET-28G-ONEMED-ISI-100-%28JARUM%29-i.136245202.7557577307) namun stoknya habis saat diperiksa | Rp67.000–Rp150.000 |
| Alcohol prep pad ×100 | 70% IPA, steril, bungkus satuan | **LOKAL:** apotek atau toko alat kesehatan | Rp20.000–Rp35.000 |
| Film PET 0,10 mm | Bening; transparansi laser atau laminating pouch 100 mikron | **LOKAL:** [E-Print 100 lembar](https://e-print.co.id/product/laminating-pouch-f4/) Rp159.200; alternatif SIPLah sekitar Rp105.000 | Rp105.000–Rp160.000 |
| Perekat | 3M 300LSE, ketebalan total 0,05 mm; nomor produk yang jelas adalah `93005LE` | **KONFIRMASI:** listing marketplace Rp24.500–Rp33.500 sering tidak menyebut ketebalan. Cocokkan dengan [lembar data 3M](https://multimedia.3m.com/mws/media/2366070O/3M-Double-Coated-Tape-93005LE.pdf) sebelum membeli | Rp25.000–Rp150.000 |
| Sharps container | Kapasitas 1 liter, dapat dikunci | **LOKAL:** [Medstuff](https://shopee.co.id/Sharp-Container-1L-Tempat-Limbah-Tajam-Medis-i.23942834.6635180555) Rp20.200; [Innodia](https://www.innodia.co.id/product-category/sharps-container/) Rp33.000 | Rp20.000–Rp33.000 |

Blood lancet 28G biasa yang dipasang ke lancing pen **bukan** pengganti safety lancet contact-activated yang diminta spesifikasi.

## Wallet: beli setelah milestone 7

| Komponen | Spesifikasi yang wajib | Status dan keputusan | Anggaran |
|---|---|---|---:|
| Secure element | **ATECC608B** breakout dengan I²C | **IMPOR/BLOCKER:** belum ada stok domestik yang dapat diverifikasi. [Adafruit 4314](https://www.adafruit.com/product/4314) berharga $4,95, tetapi halaman produknya hanya menulis ATECC608; minta konfirmasi chip **608B** sebelum membayar. Mouser Indonesia menyatakan produk ini dibatasi untuk wilayah Indonesia | Rp300.000–Rp700.000 termasuk perkiraan impor |
| Display | ST7789 1,3 inci, 240×240, SPI, **delapan pin termasuk CS** | **IMPOR/KONFIRMASI:** [Waveshare 1.3inch LCD](https://www.waveshare.com/product/displays/lcd-oled/lcd-oled-3/1.3inch-lcd-module.htm) memiliki pin CS dan berharga $9,49 sebelum ongkir. Listing lokal sekitar Rp70.900 umumnya hanya tujuh pin tanpa CS dan **jangan dibeli** | Rp250.000–Rp500.000 |
| Kamera QR | Webcam USB yang dapat membaca QR pada jarak tangan | **LOKAL:** webcam murah tersedia mulai sekitar [Rp125.000](https://www.blibli.com/jual/microphone-webcam-usb) | Rp125.000–Rp300.000 |
| Adaptor OTG | Micro-USB male ke USB-A female, mendukung data | **LOKAL:** [SYMTEC](https://itech.quantum.co.id/getdetailproductpage/1263) Rp8.000 dan tercatat tersedia | Rp8.000–Rp25.000 |
| Tombol dan cap ×4 | Tactile switch 12 mm; CONFIRM menggunakan pin sendiri | **LOKAL:** komponen umum | Rp30.000–Rp80.000 |
| Masukan daya USB-C | Breakout khusus daya dengan resistor pulldown 5,1 kΩ pada CC1 dan CC2 | **KONFIRMASI:** minta foto atau skema; breakout empat pin tanpa CC pulldown tidak boleh digunakan | Rp20.000–Rp100.000 |
| Baut dan insert | M2.5×8 + heat-set insert ×8; M2×6 self-tapping ×4 | **LOKAL:** toko baut atau marketplace | Rp50.000–Rp150.000 |
| Diffuser, epoksi, dan ring window | Diffuser kaca buram Ø6 mm; epoksi dua komponen hitam kedap cahaya; cakram bening Ø10 × 0,5 mm | **KONFIRMASI:** biasanya perlu membeli bahan lalu memotongnya sesuai ukuran | Rp100.000–Rp300.000 |

ATECC608A, ATECC508A, display ST7789 tujuh pin tanpa CS, Pi Camera v3, dan laser diode tanpa driver termasuk barang **JANGAN BELI**.

## Alat kerja

| Alat | Kebutuhan | Anggaran jika membeli |
|---|---|---:|
| Solder station dengan suhu terkontrol | Perakitan kabel dan breakout | Rp250.000–Rp450.000 |
| Mata solder heat-set insert | Pemasangan insert M2.5 | Rp40.000–Rp100.000 |
| Multimeter digital | Kontinuitas, tegangan, polaritas, dan bring-up | Rp160.000–Rp370.000 |
| Kaliper digital | Memeriksa cartridge dan komponen cetak | Rp79.000–Rp260.000 |
| Obeng presisi, cutter, pinset, dan alat kecil | Perakitan mekanis | Rp70.000–Rp180.000 |
| Cat hitam doff dan kuas kecil | Bagian dalam ruang optik | Rp30.000–Rp70.000 |
| Kacamata laser merah 650 nm | Bring-up laser; pilih produk dengan spesifikasi panjang gelombang yang jelas | Rp100.000–Rp300.000 |

Sebagai acuan harga alat, Monotaro mencantumkan [kaliper INGCO mulai Rp78.900 dan multimeter mulai Rp159.900](https://www.monotaro.id/c35.html?product_brand=14783). Jangan membeli printer 3D hanya untuk satu build; gunakan jasa cetak PETG terlebih dahulu.

## Urutan pembelian

1. Minta foto sisi depan dan belakang AS7341 untuk memastikan pin LDR tersedia.
2. Pastikan kamera benar-benar OV5647 dan paket menyertakan kabel CSI 22-pin.
3. Pastikan laser merupakan modul point 650 nm dengan driver, 3–5 V, dan maksimal 5 mW.
4. Dapatkan penawaran pencetakan PETG hitam dan putih dari file STL acuan.
5. Pesan reader dan bahan habis pakai; jangan membeli komponen wallet dulu.
6. Setelah milestone 7 menghasilkan bukti yang layak, cari ATECC608B dan display berpin CS sebagai satu pesanan impor jika memungkinkan.

Sebelum membayar, salin URL, nama toko, harga, ongkir, foto pin, dan jawaban penjual ke `COSTS.csv`. Listing dapat berubah atau diganti variannya tanpa pemberitahuan.
