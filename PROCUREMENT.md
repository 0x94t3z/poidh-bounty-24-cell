# Procurement in Indonesia

**English** | [Bahasa Indonesia](./PROCUREMENT.id.md)

Prices were checked on `2026-08-27` from sellers that can deliver to Indonesia. These are purchase budgets, not guaranteed checkout prices. Shipping, import tax, coupons, and stock changes are excluded.

## Budget summary

| Stage | Indonesian estimate |
|---|---:|
| Reader hardware and printing | IDR 2,050,000–3,240,000 |
| Reader consumables | IDR 240,000–530,000 |
| **Reader through milestone 7** | **IDR 2,290,000–3,770,000** |
| Wallet addition | IDR 890,000–2,160,000 |
| **Complete device** | **IDR 3,170,000–5,930,000** |
| Tools, if none are owned | IDR 730,000–1,730,000 |
| **Complete device and all tools** | **IDR 3,900,000–7,660,000** |

Add 15–25% for shipping, imports, failed parts, and reprints. With that reserve, a sensible complete-device limit without new tools is about **IDR 3,700,000–7,500,000**.

## Availability labels

- **LOCAL:** a broadly suitable Indonesian listing exists.
- **CONFIRM:** available, but pinout, chip revision, dimensions, or stock must be confirmed with the seller.
- **IMPORT:** no verified domestic listing was found.
- **DO NOT BUY:** looks similar but does not meet the reference design.

## Reader: buy first

| Part | Non-negotiable specification | Availability and example source | Budget |
|---|---|---|---:|
| Raspberry Pi Zero 2 W | Zero **2 W**, not Zero W or Orange Pi | **LOCAL:** [Blibli](https://www.blibli.com/jual/raspberry-pi-zero-w) lists boards around IDR 959,000–988,000 | IDR 959,000–988,000 |
| AS7341 breakout | AS7341 with the `LDR`/LED-driver pin exposed | **CONFIRM:** [Mouser Indonesia, Adafruit 4698](https://www.mouser.co.id/en/ProductDetail/Adafruit/4698) is IDR 347,657 before delivery; a [local listing](https://shopee.co.id/AS7341-AS734x-Visible-Spectral-Sensors-Module-Color-Temperature-illuminance-High-Accuracy-Color-Detection-For-Arduino-i.1696239063.58153336210) starts at IDR 289,600 but does not prove the LDR pin | IDR 290,000–590,000 |
| Speckle camera and cable | OV5647/v1, removable lens, 22-pin Pi Zero CSI cable | **CONFIRM:** [OV5647 and 15-to-22-pin cable listing](https://shopee.co.id/Raspberry-Pi-Zero-Camera-Module-5MP-1080P-OV5647-Mini-Webcam-15-PIN-To-22PIN-for-Raspberry-Pi-5-Zero-2-W-Optional-5cm-30cm-i.1683140146.53302792766) is IDR 275,500–318,500 | IDR 276,000–319,000 |
| Laser module | 650 nm red dot, 3–5 V, no more than 5 mW, driver and adjustable lens | **CONFIRM:** [5 mW listing](https://shopee.co.id/Laser-Module-5mW-650nm-3V-5V-Red-Point-Cross-Line-Industrial-Laser-i.292092948.19558329929) is about IDR 36,122. Select **point**, not line/cross | IDR 25,000–45,000 |
| LEDs and drivers | 5 mm 5000 K white ×2, 940 nm IR ×1, 2N7002 SOT-23 ×3, BOM resistors and capacitors | **LOCAL:** buy the active parts separately; generic kits are useful only for breadboard and passives | IDR 45,000–90,000 |
| Microswitch | SPDT snap-action lever switch | **LOCAL:** common part; require `COM`, `NO`, and `NC` terminals | IDR 10,000–30,000 |
| Breadboard and jumpers | Small breadboard and male/female jumpers | **LOCAL:** a [basic kit](https://shopee.co.id/Breadboard-LED-Jumper-Wire-Button-Diy-Kit-Basic-Starter-Kit-arduino-i.380441770.7378850880) is about IDR 30,000 | IDR 30,000–60,000 |
| microSD | A2, at least 16 GB; a documented 32/64 GB substitution is acceptable | **CONFIRM:** small A2 cards are scarce; a [64 GB SanDisk Extreme A2](https://www.jakartanotebook.com/cari/ulutan-a2) was IDR 380,400 | IDR 250,000–440,000 |
| Power supply | Stable 5 V/2 A supply and cable; no battery | **LOCAL:** use a reputable charger and short cable | IDR 60,000–150,000 |
| PETG prints | Black PETG for optics and white PETG for cartridges; no PLA | Choose one printing route below | IDR 100,000–520,000 |

### Printing options

A print service is cheaper for one device:

- [Astha Hub](https://shopee.co.id/Jasa-cetak-3D-Print-PETG-per-gram-dan-sedia-jasa-Request-Baca-Deskripsi-i.19106145.54863163308) lists IDR 350–930 per gram.
- [Pegangind](https://www.pegangind.com/services/3d-printing) lists PETG at IDR 329–799 per gram depending on layer height.
- Require consistent black and white PETG. The cartridges, REFERENCE, and NULL must use the same white spool and print session.
- Send the committed STL files from the pinned commit, not locally regenerated files.

If a printer is already available, one kilogram per color leaves ample material for reprints. [eSUN PETG](https://toko.evolusi3d.com/product/esun-petg-filament-1-75mm-1-kg/) is available in black and white at about IDR 259,000/kg; refill material has been listed at [IDR 165,000/kg](https://www.blibli.com/p/esun-1-kg-refilament-petg-refill-for-esun-filament-spool/is--3DZ-60022-01679-00003).

## Reader consumables

| Item | Non-negotiable specification | Availability and example source | Budget |
|---|---|---|---:|
| Safety lancets ×100 | Sterile, single-use, contact-activated, 28G/1.8 mm | **CONFIRM:** [ENDO EI.SL](https://endo.id/id/catalog/product/endo-ei-sl) has the exact variant but requires a quote. A OneMed listing was [IDR 66,500](https://shopee.co.id/SAFETY-LANCET-28G-ONEMED-ISI-100-%28JARUM%29-i.136245202.7557577307) but was out of stock when checked | IDR 67,000–150,000 |
| Alcohol prep pads ×100 | 70% IPA, sterile, individually wrapped | **LOCAL:** pharmacies and medical suppliers | IDR 20,000–35,000 |
| 0.10 mm PET film | Clear laser transparency or 100-micron laminating pouch | **LOCAL:** [E-Print, 100 sheets](https://e-print.co.id/product/laminating-pouch-f4/) is IDR 159,200; SIPLah alternatives were about IDR 105,000 | IDR 105,000–160,000 |
| Adhesive | 3M 300LSE, 0.05 mm total thickness; `93005LE` is an unambiguous part number | **CONFIRM:** marketplace products at IDR 24,500–33,500 often omit thickness. Compare the product with the [3M data sheet](https://multimedia.3m.com/mws/media/2366070O/3M-Double-Coated-Tape-93005LE.pdf) | IDR 25,000–150,000 |
| Sharps container | 1 litre with locking lid | **LOCAL:** [Medstuff](https://shopee.co.id/Sharp-Container-1L-Tempat-Limbah-Tajam-Medis-i.23942834.6635180555) is IDR 20,200; [Innodia](https://www.innodia.co.id/product-category/sharps-container/) is IDR 33,000 | IDR 20,000–33,000 |

Ordinary 28G needles used with a lancing pen are **not** a substitute for the required contact-activated safety lancets.

## Wallet: buy after milestone 7

| Part | Non-negotiable specification | Availability and decision | Budget |
|---|---|---|---:|
| Secure element | **ATECC608B** breakout with I2C | **IMPORT/BLOCKER:** no verified domestic stock found. [Adafruit 4314](https://www.adafruit.com/product/4314) is $4.95, but the page says only ATECC608; obtain written confirmation of a **608B** chip before payment. Mouser Indonesia marks the product unavailable for this region | IDR 300,000–700,000 including import allowance |
| Display | 1.3-inch ST7789, 240×240, SPI, **eight pins including CS** | **IMPORT/CONFIRM:** [Waveshare 1.3inch LCD](https://www.waveshare.com/product/displays/lcd-oled/lcd-oled-3/1.3inch-lcd-module.htm) exposes CS and is $9.49 before delivery. Common local IDR 70,900 boards have seven pins and **must not be bought** | IDR 250,000–500,000 |
| QR camera | USB webcam able to resolve QR at arm's length | **LOCAL:** basic webcams start near [IDR 125,000](https://www.blibli.com/jual/microphone-webcam-usb) | IDR 125,000–300,000 |
| OTG adapter | Micro-USB male to USB-A female with data | **LOCAL:** [SYMTEC](https://itech.quantum.co.id/getdetailproductpage/1263) is IDR 8,000 and listed in stock | IDR 8,000–25,000 |
| Buttons and caps ×4 | 12 mm tactile switches; CONFIRM has a dedicated pin | **LOCAL:** common parts | IDR 30,000–80,000 |
| USB-C power input | Power breakout with 5.1 kΩ pulldowns on both CC1 and CC2 | **CONFIRM:** require a photo or schematic; a four-pin board without CC pulldowns is unsuitable | IDR 20,000–100,000 |
| Fasteners and inserts | M2.5×8 plus heat-set inserts ×8; M2×6 self-tapping ×4 | **LOCAL:** fastener shop or marketplace | IDR 50,000–150,000 |
| Diffuser, epoxy, and ring window | Ø6 mm ground glass; opaque black two-part epoxy; Ø10 × 0.5 mm clear disc | **CONFIRM:** material will probably need to be cut to size | IDR 100,000–300,000 |

ATECC608A, ATECC508A, seven-pin ST7789 boards without CS, Pi Camera v3, and a bare laser diode without a driver are **DO NOT BUY** items.

## Tools

| Tool | Use | Purchase budget |
|---|---|---:|
| Temperature-controlled soldering station | Wiring and breakout assembly | IDR 250,000–450,000 |
| Heat-set insert tip | Install M2.5 inserts | IDR 40,000–100,000 |
| Digital multimeter | Continuity, voltage, polarity, and bring-up | IDR 160,000–370,000 |
| Digital calipers | Inspect cartridges and printed parts | IDR 79,000–260,000 |
| Precision drivers, knife, tweezers, and small tools | Mechanical assembly | IDR 70,000–180,000 |
| Matte-black paint and small brush | Optical chamber interior | IDR 30,000–70,000 |
| 650 nm laser safety glasses | Laser bring-up; require a stated wavelength rating | IDR 100,000–300,000 |

As a price reference, Monotaro lists [INGCO calipers from IDR 78,900 and multimeters from IDR 159,900](https://www.monotaro.id/c35.html?product_brand=14783). Do not buy a 3D printer for one build; use a PETG print service first.

## Purchase order

1. Ask for front and rear AS7341 photos showing the LDR pin.
2. Confirm an OV5647 camera and an included 22-pin CSI cable.
3. Confirm a 650 nm point module with a driver, 3–5 V input, and no more than 5 mW.
4. Obtain a quote for black and white PETG printing from the pinned STL files.
5. Order the reader and consumables; defer wallet parts.
6. After milestone 7 produces claimable evidence, source the ATECC608B and CS-equipped display, preferably in one import order.

Before payment, copy the URL, seller, price, shipping, pin photos, and seller answers into `COSTS.csv`. Marketplace listings can change variants without notice.
