#!/usr/bin/env python3
"""Build Indonesian CELL diagrams from the pinned upstream SVG files."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "cell" / "diagrams"
OUTPUT = ROOT / "assets" / "diagrams" / "id"
UPSTREAM_COMMIT = "9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e"


TRANSLATIONS = {
    "how-it-works.svg": {
        "A hardware wallet that takes your pulse. Or your blood.": "Hardware wallet yang membaca denyut nadi. Atau darah.",
        "Pulse for everyday. Blood for what matters.": "Denyut untuk harian. Darah untuk hal penting.",
        "TWO TIERS": "DUA TINGKAT",
        "TOUCH": "SENTUH",
        'Fingertip on the ring. <tspan fill="#D8D2C8">15 seconds.</tspan> No consumable.': 'Ujung jari pada cincin. <tspan fill="#D8D2C8">15 detik.</tspan> Tanpa bahan habis pakai.',
        "Light in, light out. Your pulse shows up as": "Cahaya masuk dan kembali. Denyut terlihat sebagai",
        "a flicker in what returns.": "kedipan pada cahaya yang dipantulkan.",
        'Someone alive <tspan fill="#D8D2C8">is</tspan> here.': 'Ada orang <tspan fill="#D8D2C8">hidup</tspan> di sini.',
        "The everyday default.": "Pilihan untuk penggunaan harian.",
        ">BLOOD<": ">DARAH<",
        'A drop in a cartridge. <tspan fill="#D8D2C8">10 minutes.</tspan>': 'Setetes darah dalam cartridge. <tspan fill="#D8D2C8">10 menit.</tspan>',
        "A laser watches the sample until it stops moving.": "Laser mengamati sampel sampai gerakannya berhenti.",
        'Someone <tspan fill="#D8D2C8">bled</tspan> here, minutes ago.': 'Seseorang <tspan fill="#D8D2C8">berdarah</tspan> di sini beberapa menit lalu.',
        "You choose it. Policy can demand it.": "Anda memilihnya. Kebijakan dapat mewajibkannya.",
        "Nothing talks it back down.": "Tidak dapat diturunkan melalui perintah.",
        "THE FLOW": "ALUR KERJA",
        "Unsigned tx": "Tx belum ditandatangani",
        "shown as a QR": "ditampilkan sebagai QR",
        "Device reads it": "Perangkat membacanya",
        "camera · no radios": "kamera · tanpa radio",
        "You verify": "Anda memeriksa",
        "on its own screen": "pada layar perangkat",
        "PIN + PULSE": "PIN + DENYUT",
        "or BLOOD": "atau DARAH",
        "Signed tx": "Tx bertanda tangan",
        "back out as a QR": "dikeluarkan sebagai QR",
        "WHAT IT PROVES": "HAL YANG DIBUKTIKAN",
        "Someone alive did this on purpose.": "Orang yang hidup melakukannya dengan sengaja.",
        "Your laptop can be fully owned. It cannot bleed.": "Laptop dapat dikuasai penyerang. Ia tidak dapat berdarah.",
        "No script has a bloodstream.": "Tidak ada skrip yang memiliki aliran darah.",
        "Nothing signs at 3am while you sleep.": "Tidak ada penandatanganan saat Anda tidur.",
        "One drop, one signature. Your body sets the rate.": "Satu tetes, satu tanda tangan. Tubuh membatasi frekuensinya.",
        "Identity is the PIN's job.": "PIN bertugas memastikan identitas.",
        "The gate asks whether someone alive is here.": "Gerbang memastikan ada orang hidup yang hadir.",
        "The PIN asks who.": "PIN memastikan siapa orangnya.",
        "Blood says someone alive is doing this.": "Darah membuktikan orang hidup sedang melakukannya.",
        "The PIN says it is you. You need both.": "PIN membuktikan orang itu adalah Anda. Keduanya wajib.",
        ">HOW IT KNOWS<": ">CARA PERANGKAT MENGETAHUINYA<",
        "Is it blood?": "Apakah ini darah?",
        "Haemoglobin swallows violet at 415 nm, from the iron": "Hemoglobin menyerap cahaya ungu 415 nm melalui cincin",
        "ring at its centre. Ketchup, dye, beet juice, stage blood": "besi di pusatnya. Saus, pewarna, jus bit, dan darah palsu",
        "are all red. None do that. A $16 sensor sees it in seconds.": "sama-sama merah, tetapi tidak menyerapnya. Sensor $16 mendeteksinya.",
        "Is it alive?": "Apakah masih hidup?",
        "Laser on the drop. Moving cells scatter it into a grainy": "Laser menyinari tetesan. Sel bergerak menyebarkannya menjadi",
        'pattern that <tspan fill="#D8D2C8">shimmers</tspan>. When fibrin locks them it <tspan fill="#D8D2C8">stops</tspan>.': 'pola berbintik yang <tspan fill="#D8D2C8">berkilau</tspan>. Saat fibrin mengunci sel, pola itu <tspan fill="#D8D2C8">berhenti</tspan>.',
        "A camera watches for ten minutes.": "Kamera mengamatinya selama sepuluh menit.",
        'Blood you can store has been anticoagulated, so it <tspan fill="#C9707A">never clots</tspan>. Blood that wasn\'t has <tspan fill="#C9707A">already clotted</tspan>.': 'Darah simpan telah diberi antikoagulan sehingga <tspan fill="#C9707A">tidak membeku</tspan>. Darah tanpa antikoagulan <tspan fill="#C9707A">sudah membeku</tspan>.',
    },
    "build-sheet.svg": {
        "CELL — BUILD SHEET": "CELL — LEMBAR PERAKITAN",
        "OPTICAL HEAD — CHEMISTRY (45°/0°) + LIVENESS (SPECKLE)": "KEPALA OPTIK — KIMIA (45°/0°) + DETEKSI HIDUP (SPECKLE)",
        "aperture Ø3.0 × 6.0": "bukaan Ø3.0 × 6.0",
        "matte black": "hitam doff",
        "0° observe": "pengamatan 0°",
        "LED #1 white": "LED #1 putih",
        "+ IR940 co-sited": "+ IR940 satu posisi",
        ">650 nm laser<": ">laser 650 nm<",
        "camera, no lens": "kamera, tanpa lensa",
        "LED #2 white": "LED #2 putih",
        "specular exits at 45°": "pantulan spekular keluar 45°",
        "BLOOD": "DARAH",
        ">white ref<": ">acuan putih<",
        "cartridge, white PETG": "cartridge, PETG putih",
        "Why this geometry": "Alasan geometri ini",
        "Wet blood is glossy. A normal-incidence lamp would swamp": "Darah basah mengilap. Cahaya tegak lurus akan membanjiri",
        "the sensor with surface reflection carrying zero chemical": "sensor dengan pantulan permukaan yang tidak membawa informasi",
        "information. At 45° the specular lobe exits at 45° and misses.": "kimia. Pada 45°, pantulan spekular keluar 45° dan melewati sensor.",
        "Two opposed LEDs cancel shading from droplet asymmetry.": "Dua LED berlawanan mengurangi bayangan akibat bentuk tetesan.",
        "The well is optically semi-infinite (≥0.4 deep): reflectance is": "Sumur bersifat semi-tak-hingga secara optik (kedalaman ≥0.4):",
        "independent of fill volume and of the backing. That is why": "pantulan tidak bergantung pada volume isi atau alas. Karena itu",
        "8–15 µL is fine and FDM roughness doesn't matter.": "8–15 µL dapat digunakan dan kekasaran FDM tidak berpengaruh.",
        'Do not "improve" it by making the well thinner.': 'Jangan "memperbaiki" desain dengan menipiskan sumur.',
        "Second path: speckle": "Jalur kedua: speckle",
        "650 nm laser at ~30°, camera at ~20 mm with the": "Laser 650 nm pada ~30°, kamera berjarak ~20 mm dengan",
        '<tspan fill="#D8D2C8">lens removed</tspan>, off the specular axis. Fixed exposure,': '<tspan fill="#D8D2C8">lensa dilepas</tspan>, di luar sumbu spekular. Exposure,',
        "gain and AWB — auto adjustment destroys the": "gain, dan AWB harus tetap; penyesuaian otomatis merusak",
        "correlation measurement.": "pengukuran korelasi.",
        "The two paths never run at once: the laser": "Kedua jalur tidak berjalan bersamaan: laser mengganggu",
        "contaminates 630 nm, the LEDs wash out speckle.": "kanal 630 nm, sedangkan LED menghilangkan speckle.",
        "CARTRIDGE — 45 × 14 × 2.4, WHITE PETG, 0.15 LAYERS, IRONING ON  ·  600 s CAPTURE": "CARTRIDGE — 45 × 14 × 2.4, PETG PUTIH, LAYER 0.15, IRONING AKTIF  ·  REKAM 600 s",
        "well Ø4.0 × 0.55 deep  ·  moat Ø7.0  ·  ≈7 µL": "sumur Ø4.0 × kedalaman 0.55  ·  parit Ø7.0  ·  ≈7 µL",
        "white ref printed on · dark = LEDs off": "acuan putih ikut dicetak · gelap = LED mati",
        "PET film lid, taped edge = the hinge": "penutup film PET, sisi berperekat = engsel",
        "Per-cartridge references": "Acuan pada setiap cartridge",
        "LED aging, sensor drift and print variation are": "Penuaan LED, pergeseran sensor, dan variasi cetak",
        "first-order effects. Left alone they walk your": "berpengaruh langsung. Tanpa koreksi, ketiganya membuat",
        "thresholds out of spec in weeks, silently.": "nilai ambang keluar spesifikasi dalam hitungan minggu.",
        "Normalising against a patch printed in the same": "Normalisasi terhadap bidang yang dicetak pada layer",
        "layer, same filament, cancels nearly all of it.": "dan filamen yang sama menghilangkan hampir seluruh efeknya.",
        "Biosafety": "Keselamatan biologis",
        'One cartridge, one use, then a <tspan fill="#D8D2C8">sharps container</tspan>.': 'Satu cartridge untuk sekali pakai, lalu buang ke <tspan fill="#D8D2C8">wadah benda tajam</tspan>.',
        "Commercial sterile single-use lancets only. Never reuse,": "Gunakan hanya lancet komersial steril sekali pakai. Jangan",
        "never substitute a blade or needle.": "gunakan ulang atau menggantinya dengan pisau maupun jarum.",
        "One device, one person. Never share.": "Satu perangkat untuk satu orang. Jangan berbagi.",
        "HBV survives on dry surfaces up to 7 days.": "HBV bertahan pada permukaan kering hingga 7 hari.",
        "WIRING — BCM NUMBERING, I²C1 @ 400 kHz": "PENGKABELAN — NOMOR BCM, I²C1 @ 400 kHz",
        "UP · DOWN · BACK": "ATAS · BAWAH · KEMBALI",
        "CONFIRM — own pin, RC debounced, shares no bus": "KONFIRMASI — pin sendiri, debounce RC, tanpa bus bersama",
        "SPI0 → ST7789 display": "SPI0 → display ST7789",
        "display D/C · RESET · backlight": "D/C display · RESET · lampu latar",
        "white LED #2 · IR940 (2N7002, 68R / 47R)": "LED putih #2 · IR940 (2N7002, 68R / 47R)",
        "650 nm laser — interlocked to the cartridge switch": "laser 650 nm — interlock ke sakelar cartridge",
        "cartridge switch · speckle camera": "sakelar cartridge · kamera speckle",
        "Two things that will bite you": "Dua sumber masalah utama",
        '<tspan fill="#D8D2C8">1.</tspan> Both I²C breakouts ship with pull-ups fitted. Remove one': '<tspan fill="#D8D2C8">1.</tspan> Kedua breakout I²C memiliki pull-up. Lepas salah satu pasang',
        "2.2 kΩ pair or the bus may not enumerate. This is the number": "2.2 kΩ agar bus dapat terdeteksi. Ini penyebab kegagalan",
        "one first-build failure.": "paling umum pada perakitan pertama.",
        '<tspan fill="#D8D2C8">2.</tspan> Disable the radios in config.txt <tspan fill="#D8D2C8">and cut the antenna</tspan>': '<tspan fill="#D8D2C8">2.</tspan> Nonaktifkan radio di config.txt <tspan fill="#D8D2C8">dan potong jalur</tspan>',
        '<tspan fill="#D8D2C8">feed trace.</tspan> Firmware-only disabling is reversible by anyone': '<tspan fill="#D8D2C8">umpan antena.</tspan> Penonaktifan melalui firmware dapat dibatalkan oleh siapa pun',
        'who touches the SD card. Verify with <tspan font-family="monospace" fill="#D8D2C8">iw dev</tspan> returning nothing.': 'yang mengakses kartu SD. Pastikan <tspan font-family="monospace" fill="#D8D2C8">iw dev</tspan> tidak menghasilkan keluaran.',
    },
    "mechanical.svg": {
        "CELL — MECHANICAL": "CELL — MEKANIS",
        "Every dimension read from instrument.obj at generation time. Regenerate after any model change. Millimetres.": "Semua ukuran dibaca dari instrument.obj saat dibuat. Buat ulang setelah model berubah. Satuan milimeter.",
        "99 objects · 295,366 verts": "99 objek · 295.366 verteks",
        "TOP": "ATAS",
        "compute bay 72 × 16, rear": "ruang komputasi 72 × 16, belakang",
        "60 ticks @ R21.2, every 5th steel": "60 tanda @ R21.2, tiap tanda ke-5 baja",
        "dish Ø47.2 × 2.0 deep": "cekungan Ø47.2 × kedalaman 2.0",
        "ring Ø14.4/Ø9.8, 1.5 proud": "cincin Ø14.4/Ø9.8, menonjol 1.5",
        "sample slot 34.0 × 3.0, front": "slot sampel 34.0 × 3.0, depan",
        "CARTRIDGE FIT": "KECOCOKAN CARTRIDGE",
        ">front face<": ">sisi depan<",
        "well, under the ring": "sumur, di bawah cincin",
        "travel 31.6": "langkah 31.6",
        "13.4 proud": "menonjol 13.4",
        "45 × 14 × 2.4 overall": "ukuran total 45 × 14 × 2.4",
        "the proud end is the grip tab": "ujung menonjol adalah pegangan",
        'display 49.7 × 37.7  ·  buttons Ø5.8, <tspan fill="#B23A48">CONFIRM Ø8.6</tspan>  ·  pad 24.0 × 12.0 <tspan fill="#6F7178">(reserved, print flat)</tspan>': 'display 49.7 × 37.7  ·  tombol Ø5.8, <tspan fill="#B23A48">KONFIRMASI Ø8.6</tspan>  ·  bidang 24.0 × 12.0 <tspan fill="#6F7178">(cadangan, cetak rata)</tspan>',
        "FRONT": "DEPAN",
        "sample slot 34.0 × 3.0": "slot sampel 34.0 × 3.0",
        "15 vents — MUST BE BLIND": "15 ventilasi — WAJIB BUNTU",
        "parting seam @ 11.4 from base": "garis sambungan @ 11.4 dari dasar",
        "slotted fastener ×2": "baut minus ×2",
        "REAR": "BELAKANG",
        "Pi Zero 2 W bay — 72 × 16 × 3.2": "ruang Pi Zero 2 W — 72 × 16 × 3.2",
        "RIGHT   (front →)": "KANAN   (depan →)",
        "USB-C 9.0 × 3.2 — power only": "USB-C 9.0 × 3.2 — hanya daya",
        "THREE CHOICES THAT LOOK COSMETIC AND ARE NOT": "TIGA PILIHAN YANG TAMPAK KOSMETIK, TETAPI BUKAN",
        "Vents must be blind pockets.": "Ventilasi harus berupa ceruk buntu.",
        "15 slots on the front face, 3.0 deep. If any becomes a through-hole, ambient light reaches the optical chamber and the 415 nm gate fails. Print them blind and verify with the light-tightness test.": "Lima belas slot di sisi depan berkedalaman 3.0. Jika tembus, cahaya lingkungan mencapai ruang optik dan gerbang 415 nm gagal. Cetak sebagai ceruk buntu dan uji kekedapan cahaya.",
        "The pad is reserved, not fitted.": "Bidang disiapkan, tetapi tidak dipasangi sensor.",
        "24.0 × 12.0 printed marking sizing the optional fingerprint sensor. Deliberately flat, not a pocket: an unpopulated recess on the deck collects blood. The base build leaves it blank — the PIN does identity.": "Tanda cetak 24.0 × 12.0 menentukan ukuran sensor sidik jari opsional. Bidang sengaja rata, bukan ceruk, karena ceruk kosong dapat menampung darah. Perakitan dasar membiarkannya kosong; identitas ditangani oleh PIN.",
        "The dish is the reader, not a dial.": "Cekungan adalah reader, bukan kenop.",
        "The ring is a bezel, not a control. Nothing rotates. The cartridge enters through the front slot and sits under the dish.": "Cincin adalah bezel, bukan alat kendali. Tidak ada bagian yang berputar. Cartridge masuk melalui slot depan dan berada di bawah cekungan.",
    },
    "wiring.svg": {
        "CELL — PHASE 1 WIRING": "CELL — PENGKABELAN FASE 1",
        "The reader only. Read from the pin table in BUILD.md section 11 at generation time. BCM numbering. No display, no buttons, no secure element — those are Phase 2.": "Hanya reader. Dibuat dari tabel pin pada BUILD.md bagian 11. Penomoran BCM. Display, tombol, dan secure element dipasang pada Fase 2.",
        "radios disabled, antenna trace cut": "radio nonaktif, jalur antena dipotong",
        "AS7341 spectrometer": "spektrometer AS7341",
        "8 colour channels + Clear + NIR.": "8 kanal warna + Clear + NIR.",
        "Drives white LED #1 on its LDR pin.": "Mengendalikan LED putih #1 melalui pin LDR.",
        "White LED #2": "LED putih #2",
        "45° opposed to LED #1, so droplet": "Berhadapan 45° dengan LED #1 sehingga",
        "asymmetry cancels.": "asimetri tetesan berkurang.",
        "650 nm laser, ≤5 mW": "laser 650 nm, ≤5 mW",
        "COHERENT SOURCE IS MANDATORY.": "SUMBER KOHEREN WAJIB DIGUNAKAN.",
        "An LED produces no speckle.": "LED tidak menghasilkan speckle.",
        "940 nm IR LED": "LED IR 940 nm",
        "Co-sited with LED #1. Gives touch": "Satu posisi dengan LED #1. Menyediakan",
        "mode its infrared channel.": "kanal inframerah untuk mode sentuh.",
        "Cartridge microswitch": "Microswitch cartridge",
        "pull-up, LOW when seated": "pull-up, LOW saat terpasang",
        "Gates the laser. Wire the interlock": "Mengaktifkan gerbang laser. Pasang interlock",
        "even though the chamber is sealed.": "meskipun ruang optik tertutup.",
        "Pi Camera, LENS REMOVED": "KAMERA PI, LENSA DILEPAS",
        "Fixed exposure ≤2 ms, fixed gain,": "Exposure tetap ≤2 ms, gain tetap,",
        "AWB and denoise off.": "AWB dan denoise nonaktif.",
        "WHAT EATS A FIRST BUILD": "PENYEBAB UMUM KEGAGALAN PERTAMA",
        "Both I²C breakouts ship with pull-ups fitted.": "Kedua breakout I²C sudah dilengkapi pull-up.",
        "Remove one 2.2 kΩ pair. With both fitted the bus may not enumerate, and it presents as a dead sensor rather than as a wiring fault. This is the most": "Lepas salah satu pasang 2.2 kΩ. Jika keduanya terpasang, bus mungkin tidak terdeteksi dan sensor tampak mati, bukan seperti kesalahan pengkabelan. Ini",
        "common first-build failure.": "adalah kegagalan paling umum pada perakitan pertama.",
        "The optical chamber must be light-tight before any reading means anything.": "Ruang optik harus kedap cahaya sebelum hasil pembacaan dapat digunakan.",
        "Black PETG, ≥4 perimeters, interior painted matte black. Test: cartridge in, room at 10,000 lux, all LEDs off, Clear channel under 0.5% of its LEDs-on": "Gunakan PETG hitam, ≥4 perimeter, dan cat hitam doff di bagian dalam. Uji dengan cartridge terpasang, ruangan 10.000 lux, semua LED mati; kanal Clear harus di bawah 0,5% nilai",
        "value. Thin PETG passes more light than you would expect, and a leak quietly ruins the 415 nm gate rather than failing loudly.": "saat LED menyala. PETG tipis meneruskan cukup banyak cahaya; kebocoran akan merusak gerbang 415 nm tanpa kegagalan yang terlihat jelas.",
        "The camera lens comes off, and the exposure is fixed.": "Lensa kamera harus dilepas dan exposure harus tetap.",
        "Lensless speckle grain is about 4 px on an IMX219 at 20 mm, which is well sampled; with the lens fitted it is ~1.6 px and undersampled. Any": "Butir speckle tanpa lensa berukuran sekitar 4 px pada IMX219 di jarak 20 mm sehingga tersampel dengan baik; jika lensa terpasang ukurannya ~1,6 px dan kurang tersampel. Setiap",
        "auto-exposure or auto-white-balance between frames destroys the correlation measurement outright.": "perubahan exposure otomatis atau white balance otomatis antarfoto akan merusak pengukuran korelasi.",
    },
}


def localize(name: str, replacements: dict[str, str]) -> None:
    source_path = SOURCE / name
    text = source_path.read_text(encoding="utf-8")

    for original, translated in replacements.items():
        count = text.count(original)
        if count != 1:
            raise RuntimeError(f"{name}: expected one occurrence of {original!r}, found {count}")
        text = text.replace(original, translated)

    marker = (
        f"<!-- Indonesian translation of z0r0z/cell@{UPSTREAM_COMMIT}; "
        "source licensed CC0 1.0. -->\n"
    )
    first_line, remainder = text.split("\n", 1)
    output_text = f"{first_line}\n{marker}{remainder}"

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / name).write_text(output_text, encoding="utf-8")


def main() -> None:
    for filename, replacements in TRANSLATIONS.items():
        localize(filename, replacements)
        print(f"wrote {OUTPUT / filename}")


if __name__ == "__main__":
    main()
