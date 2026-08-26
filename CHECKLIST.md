# Working Checklist

**English** | [Bahasa Indonesia](./CHECKLIST.id.md)

For every completed item, add the date, evidence path, transaction hash, or a short note where applicable. A checked box without supporting evidence does not count as a completed bounty milestone.

## Project controls

- [ ] Record the claimant wallet address.
- [ ] Record the initial bounty balance and status.
- [x] Pin CELL commit `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`.
- [x] Keep the original bounty and build documents.
- [ ] Create `BUILD_LOG.md`, `CHANGES.md`, `COSTS.csv`, and `RISKS.md`.
- [ ] Set the maximum cash spend.
- [ ] Set the maximum engineering hours.
- [ ] Set the minimum acceptable bounty balance.
- [ ] Confirm that the repository and evidence contain no secrets.

## Software checks

- [x] Record the operating system and Python version.
- [x] Install dependencies.
- [x] Run `python firmware/run_tests.py`: 41 of 41 suites passed.
- [ ] Save the full raw test logs.
- [x] Explain every failure or skip: optional checks were rerun without skips and the official RFC vector was supplied.
- [x] Confirm that all referenced paths and commands exist at the pinned commit.
- [x] Run the Bitcoin, libsecp256k1, and Microchip cross-checks without skips.
- [x] Verify the official RFC 8554 Appendix F vector.
- [x] Run the Solidity tests: 19 of 19 passed.
- [x] Run Bitcoin Core regtest: all script types were accepted and mined.
- [x] Record the result in `SOFTWARE_BASELINE.md`.

## Safety setup

- [ ] Read all of `SAFETY.md`.
- [ ] Confirm that blood-contact items will never be shared.
- [ ] Obtain sealed sterile single-use lancets.
- [ ] Obtain alcohol pads and basic aftercare supplies.
- [ ] Obtain a sharps container.
- [ ] Confirm the local disposal procedure.
- [ ] Arrange qualified help for any required sample collection.
- [ ] Check sample providers against the contraindications in the specification.
- [ ] Plan safe sampling intervals; do not rush repeated finger pricks.
- [ ] Put laser-safety controls in place before bring-up.

## Reader procurement

- [ ] Raspberry Pi Zero 2 W.
- [ ] AS7341 breakout with LDR pin available.
- [ ] OV5647-type Pi camera.
- [ ] Narrow Pi Zero CSI cable.
- [ ] Driver-equipped 650 nm laser module, no more than 5 mW.
- [ ] White LED and 940 nm IR LED.
- [ ] MOSFETs and passive components.
- [ ] Cartridge microswitch.
- [ ] Breadboard and jumper wires.
- [ ] A2-rated microSD, at least 16 GB.
- [ ] Black PETG.
- [ ] White PETG.
- [ ] PET film and 3M 300LSE adhesive.
- [ ] Stable 5 V/2 A supply and cable.
- [ ] Access to a PETG-capable printer.
- [ ] Soldering iron and heat-set insert tool.
- [ ] Calipers, knife, screwdrivers, paint, and multimeter.
- [ ] Record invoices, suppliers, part numbers, shipping, tax, and substitutions.

## Milestone 1: Pi

- [ ] Pi boots reliably.
- [ ] Radios are disabled as required.
- [ ] Antenna changes are documented.
- [ ] Radio-check output is saved.
- [ ] Power configuration is recorded.

## Milestone 2: AS7341

- [ ] Sensor is detected correctly.
- [ ] White-card measurement is complete.
- [ ] All 100 raw readings are saved.
- [ ] Relative standard deviation is calculated.
- [ ] RSD is below 1%.
- [ ] Wiring and test setup are photographed.

## Milestone 3: cartridges

- [ ] One test cartridge is printed and inspected.
- [ ] The ironed white patch is smooth and consistent.
- [ ] A batch of 20 cartridges is printed from one spool in one session.
- [ ] REFERENCE and NULL are printed in the same session.
- [ ] Measurements for every cartridge are saved.
- [ ] Normalized spread is below 3%.

## Milestone 4: optical chamber

- [ ] Optical parts are printed in the required orientation.
- [ ] The optical bore is painted matte black.
- [ ] Chamber fit and cartridge movement are checked.
- [ ] LEDs-off ambient readings are saved.
- [ ] LEDs-on readings are saved.
- [ ] Ambient reading is below 0.5% of the LEDs-on reading.

## Milestone 5: spectrum separation

- [ ] Fresh-blood sample is collected safely.
- [ ] Dye control is measured.
- [ ] Raw spectra are saved.
- [ ] Separation at 415 nm is calculated.
- [ ] Result is photographed and explained.
- [ ] Continue/stop decision is recorded.

## Milestone 6: speckle series

- [ ] Complete a 600-second blood capture.
- [ ] Complete a 600-second dye/control capture.
- [ ] Record early decorrelation.
- [ ] Record late decorrelation.
- [ ] Record drop and direction.
- [ ] Preserve raw data.
- [ ] Confirm the expected physical behavior or explain the failure.

## Milestone 7: spoof panel

- [ ] List every required class from the pinned `BUILD.md`.
- [ ] Meet the minimum trial count for each class.
- [ ] Check sample IDs and timestamps.
- [ ] Save raw `.npz` captures.
- [ ] Produce `thresholds.json`.
- [ ] Produce a result table by class.
- [ ] Calculate the false-reject rate.
- [ ] Report the rule-of-three confidence bound.
- [ ] Record the complete hardware and environmental setup.
- [ ] Preserve unexpected results and failures.
- [ ] Prepare a reader or failure claim package.
- [ ] Record the decision on wallet spending.

## Wallet procurement

- [ ] ATECC608B breakout; confirm the exact chip model.
- [ ] ST7789 240 × 240 display with CS pin.
- [ ] USB webcam with suitable focus.
- [ ] Micro-USB OTG adapter.
- [ ] Four buttons and caps.
- [ ] USB-C power-only breakout with CC pulldowns.
- [ ] Fasteners and heat-set inserts.
- [ ] Ground-glass diffuser and opaque epoxy.
- [ ] Ring window.

## Milestone 8: secure element

- [ ] Verify the chip model and wiring.
- [ ] Run behavior verification before locking.
- [ ] Save the verification output.
- [ ] Confirm that every required behavior passes.
- [ ] Review the permanent configuration twice.
- [ ] Lock only after the review gate passes.
- [ ] Confirm that probing still works after configuration.
- [ ] Document destructive PIN/wipe behavior using disposable test material.

## Milestone 9: device firmware

- [ ] Install firmware on the Pi.
- [ ] Run the test suites successfully on the Pi.
- [ ] Check the display.
- [ ] Check the buttons.
- [ ] Check the QR camera.
- [ ] Integrate the reader gates with the signer.
- [ ] Save complete logs.

## Milestone 10: provisioning

- [ ] Generate a new test-only seed.
- [ ] Complete provisioning.
- [ ] Confirm that the seed store reopens correctly.
- [ ] Create an offline backup.
- [ ] Keep the backup out of photos, video, Git, and cloud evidence.
- [ ] Record the decision on optional chamber enrollment.

## Milestone 11: regtest

- [ ] Start regtest without external peers.
- [ ] Fund an address derived by the device.
- [ ] Display and confirm the transaction or PSBT.
- [ ] Sign through the physical gate.
- [ ] Confirm node acceptance.
- [ ] Mine the transaction.
- [ ] Preserve the input, signed result, and logs.

## Milestone 12: public testnet

- [ ] Record the testnet and chain ID.
- [ ] Demonstrate a pulse-authorized signature.
- [ ] Demonstrate a fresh-blood-authorized signature.
- [ ] Broadcast the transaction.
- [ ] Save the explorer URL.
- [ ] Save the transaction hash.
- [ ] Record video of the assembled device running.
- [ ] Link the gate result to the signed transaction in the evidence.
- [ ] Confirm that the media exposes no secrets or unnecessary personal data.

## Evidence package

- [ ] `README.md` explains the claim and reproduction steps.
- [ ] `MANIFEST.json` lists the material artifacts.
- [ ] `CHECKSUMS.txt` contains SHA-256 hashes.
- [ ] Build log is complete.
- [ ] Changes from upstream are documented.
- [ ] Costs and substitutions are documented.
- [ ] Photos and videos have clear labels.
- [ ] Raw captures and calibration output are included.
- [ ] Test results and testnet proof are included.
- [ ] Secret and personal-data review is complete.
- [ ] IPFS bundle is uploaded.
- [ ] Bundle is retrievable through more than one gateway.

## POIDH claim

- [ ] Confirm that the bounty is still active.
- [ ] Confirm its current balance.
- [ ] Confirm that no vote is in progress.
- [ ] Confirm that the claimant is not the issuer.
- [ ] Confirm sufficient Mainnet gas funds.
- [ ] Review the final claim title, description, and IPFS URI.
- [ ] Submit the claim.
- [ ] Record the claim ID, transaction hash, and block number.

## Vote and payment

- [ ] Issuer sends the claim to a vote.
- [ ] Record the voting deadline.
- [ ] Share the evidence summary and immutable link.
- [ ] Monitor the vote.
- [ ] Resolve it after the deadline if needed.
- [ ] Verify the reward in `pendingWithdrawals`.
- [ ] Send the withdrawal transaction.
- [ ] Record the withdrawal hash and final ETH received.
- [ ] Write the project retrospective.
