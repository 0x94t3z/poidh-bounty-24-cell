# Build and Claim Plan

**English** | [Bahasa Indonesia](./PLAN.id.md)

## Target

Build enough of CELL to submit a defensible claim without committing the full budget too early. Work in two spending stages:

1. Finish the software checks at no hardware cost.
2. Build and test the reader through milestone 7.
3. Preserve the reader result, including a useful failure.
4. Buy the wallet parts only if the reader produces claimable evidence.
5. Finish milestones 8–12 and submit the full result while the bounty is still active.

## Current status

- Specification fixed at commit `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`.
- Software checks complete. See [SOFTWARE_BASELINE.md](./SOFTWARE_BASELINE.md).
- Next action: confirm the budget and buy the reader parts.

## Time and cost

| Phase | Expected time | New cost | Required result |
|---|---:|---:|---|
| 0. Fix the reference version | 0.5 day | $0 | Recoverable source and requirements |
| 1. Test the software | 1 day | $0 | No unexplained software failures |
| 2. Buy reader parts | 3–14 days | IDR 2.29–3.77 million | Reader parts and consumables received |
| 3. Build the reader | 2–4 days | — | Milestones 1–6 complete |
| 4. Run the spoof panel | 1–3+ weeks | Depends on samples | Milestone 7 evidence |
| 5. Build the wallet | 2–4 days | IDR 0.89–2.16 million more | Milestones 8–12 complete |
| 6. Publish and claim | 1–2 days | Mainnet gas | Claim recorded on POIDH |
| 7. Vote and payment | At least 2 days | Mainnet gas | Reward withdrawn if the claim wins |

Allow roughly 3–6 weeks. Parts and safe access to the required samples are likely to determine the schedule.

## 0. Fix the reference version

1. Keep the CELL repository under `upstream/` at commit `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`.
2. Keep copies of `BOUNTY.md`, `BUILD.md`, `BOM.csv`, `SAFETY.md`, `VALIDATION.md`, `PRINTING.md`, and `CONTRIBUTING.md`.
3. Record the bounty balance, issuer, claims, vote state, and check date.
4. Keep all test material separate from personal wallet secrets.

Done when the source and requirements remain recoverable even if upstream changes.

## 1. Test the software

1. Record the operating system, Python version, and dependencies.
2. Run the repository tests:

```bash
pip install -r firmware/requirements.txt
python firmware/run_tests.py
```

3. Save failures and skipped tests, not just successful output.
4. Inspect the hardware, calibration, signing, seed-storage, and ATECC paths.
5. Run the independent cryptographic, contract, and regtest checks.

This phase is complete. The result is in [SOFTWARE_BASELINE.md](./SOFTWARE_BASELINE.md).

## 2. Buy the reader parts

Check the exact part before ordering:

- Raspberry Pi Zero 2 W.
- AS7341 breakout with the LDR/LED-driver pin available.
- OV5647-type Pi camera with a removable lens.
- Narrow 22-pin CSI cable for Pi Zero.
- Driver-equipped 650 nm laser module, no more than 5 mW.
- White and black PETG.
- LEDs, MOSFETs, passive components, cartridge switch, microSD, and prototyping parts listed in the BOM.
- Sterile lancets, alcohol pads, PET window film, specified adhesive, and a sharps container.

Required tools or services:

- PETG-capable 3D printer with a bed of at least 120 × 80 mm.
- Soldering iron and heat-set insert tip.
- Multimeter, digital calipers, craft knife, screwdrivers, and matte-black paint.
- Stable 5 V/2 A supply and cable.
- Qualified medical help for any sample that requires venous collection.

Record the supplier, part number, quantity, price, shipping, tax, and every substitution in `COSTS.csv`. Photograph board markings and labels on arrival. Do not silently substitute the sensor layout, camera type, display interface, secure element, laser, tape thickness, or print material.

Use [PROCUREMENT.md](./PROCUREMENT.md) for Indonesian prices, example sources, and the do-not-buy list.

## 3. Build the reader: milestones 1–6

### Milestone 1: Pi and radios

Boot the Pi reliably and disable its radios as required. Save the boot log, radio-check output, power details, and photos of any antenna modification.

### Milestone 2: AS7341 stability

Take 100 readings from a white card. Relative standard deviation must be below 1%. Save the readings, calculation, wiring photo, board model, LED details, and lighting conditions.

### Milestone 3: cartridges

Print one cartridge first and check its dimensions and surface. Then print 20 cartridges plus REFERENCE and NULL in one session from the same white PETG spool. Normalized spread across the batch must be below 3%.

### Milestone 4: light-tight chamber

At the specified ambient light level, the clear-channel reading with the LEDs off must be below 0.5% of the LEDs-on reading. Save print settings, finishing work, paint details, measurements, and fit corrections.

### Milestone 5: spectrum separation

Confirm that the 415 nm measurement clearly separates dye from genuine blood. If it does not, check alignment, contamination, saturation, white-patch normalization, optical geometry, and substituted parts before continuing.

This is the first hard go/no-go point.

### Milestone 6: 600-second series

Record blood and dye for 600 seconds. Fresh blood should begin decorrelated and then arrest; dye must not show the same pattern. Save all raw readings and report early decorrelation, late decorrelation, drop, and direction. Do not tune thresholds merely to obtain a pass.

## 4. Run milestone 7

Run every spoof class and minimum sample count required by the pinned `BUILD.md`. Use clear sample IDs, conditions, and timestamps.

Keep:

- Raw `.npz` captures.
- `thresholds.json`.
- Results by sample class.
- Hardware and optical configuration.
- Part numbers for the printer, filament, sensor, LEDs, camera, and laser.
- False-reject result and rule-of-three confidence bound.
- Calibration commands and logs.
- Unexpected results and failures.

Decision after milestone 7:

- If it passes, preserve the reader evidence and approve the wallet budget.
- If the hardware produces a reproducible and useful failure, prepare a failure claim.
- If the build is defective, fix the defect and repeat only the affected measurements.
- If a sample is unsafe or unavailable, stop until it can be handled properly.

A reader claim can be submitted here. A later full claim remains possible if the bounty is still open.

## 5. Build the wallet: milestones 8–12

### Milestone 8: ATECC608B

Confirm the exact chip and breakout. Run `atecc_config.py verify --behaviour` while the configuration remains recoverable. Review the saved output before locking anything. Locking is permanent; any unexplained failure stops this phase. Use only disposable test material for wipe or destructive PIN tests.

### Milestone 9: firmware on the Pi

Run the expected tests on the Pi itself. Check the display, buttons, QR camera, reader, and secure element together.

### Milestone 10: provisioning and backup

Generate a new test-only seed. Confirm that the device can reopen its own encrypted seed store and make an offline backup. Never photograph or publish the backup. Perform optional chamber enrollment only after documenting its recovery consequences.

### Milestone 11: regtest

Run the repository's regtest process. Keep the input transaction or PSBT, signed result, node acceptance, mining result, and full logs.

### Milestone 12: public testnet

On the assembled CELL device:

1. Display the transaction.
2. Produce a pulse-authorized signature.
3. Produce a fresh-blood-authorized signature.
4. Broadcast the testnet transaction.
5. Save the transaction hash and explorer link.
6. Show that the recorded gate result belongs to the same transaction.

Use no personal seed and no meaningful Mainnet funds.

## 6. Package the evidence

Use this layout:

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

The evidence README must identify the bounty, claim type, pinned commit, BOM substitutions, completed milestones, calibration method, failures, build changes, signature proofs, testnet transaction, reproduction steps, and checksums.

Inspect every file for PINs, seeds, private keys, personal information, and unnecessary medical data. Upload the final directory to IPFS, then retrieve it through more than one gateway.

## 7. Submit the POIDH claim

Before signing the Mainnet transaction, confirm that bounty #24 is active, no competing vote is in progress, the amount still justifies the expense, the claimant is not the issuer, the IPFS content resolves, no secret is exposed, and the claim wallet has enough ETH for gas.

Suggested title:

> CELL hardware build — pulse and fresh-blood authorized testnet signatures

Suggested description:

> Completed CELL BUILD.md section 15 milestones 1–12 against commit 9ae536c. Evidence includes the running device, calibration data and thresholds, pulse- and fresh-blood-authorized signatures, testnet transaction, build changes, raw logs, and a reproducibility manifest. Full evidence: <IPFS URI>

Record the claim ID, transaction hash, block number, timestamp, and exact IPFS URI.

## 8. Vote and withdraw

1. Watch for the issuer to send the claim to a vote.
2. Record the two-day deadline, voters, and vote weights.
3. Share a short evidence summary and the immutable link.
4. After the deadline, resolve the vote if needed.
5. Check the claimant's `pendingWithdrawals` balance.
6. Call `withdraw()` and record the amount and transaction.

## Stop and reassess when

- The bounty is cancelled, finalized, or voting on another claim.
- The remaining reward falls below the agreed stop-loss amount.
- Samples cannot be obtained or handled safely.
- The 415 nm separation still fails after build faults are ruled out.
- The chamber cannot meet the light-leak limit.
- The camera cannot sample speckle at the required resolution.
- ATECC behavior verification fails or the chip model is uncertain.
- Publishing the evidence would expose a secret or sensitive personal data.
