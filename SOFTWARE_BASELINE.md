# Software Test Record

**English** | [Bahasa Indonesia](./SOFTWARE_BASELINE.id.md)

## Test environment

- Date: `2026-08-26`
- Computer: Apple Silicon
- Operating system: macOS `15.3.2` (`24D81`)
- Python: `3.11.15`
- Source directory: `upstream/cell`
- Source commit: `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`
- Git state: detached HEAD
- Python environment: local `.venv`
- Installed package versions: `software/requirements-lock.txt`

## Results

| Test area | Result | Detail |
|---|---|---|
| Firmware test runner | PASS | 41 of 41 suites passed |
| Hashes, keys, addresses, transactions, and signatures | PASS | BIP, RFC, EIP, OpenSSL, and internal differential tests passed |
| Wallet and application loop | PASS | Software-device paths and hostile-input cases passed |
| Synthetic blood and touch gates | PASS | Software pipeline only; no physical sample was tested |
| Calibration read/write cycle | PASS | Capture, threshold sweep, serialization, loading, and classification passed |
| Bitcoin script cross-check | PASS | `python-bitcointx` executed legacy, SegWit, and multisig scripts |
| secp256k1 cross-check | PASS | `coincurve`/libsecp256k1 passed, including a 300-key differential run |
| Microchip cross-check | PASS | `cryptoauthlib` matched the configuration-zone layout and CheckMac construction |
| Hardware-library interfaces | PASS | Display, Pillow, QR, GPIO, OpenCV, and cryptoauthlib interfaces matched the code |
| RFC 8554 LMS vectors | PASS | The official Appendix F vector was parsed and verified |
| Mechanical drawing generation | PASS | Envelope and feature checks passed |
| Printable geometry | PASS | Manifold, fit, and guard checks passed |
| Solidity attestation contracts | PASS | 19 passed; 0 failed; 0 skipped |
| Bitcoin Core regtest | PASS | Core 31.1 accepted, finalized, and mined every tested script type |

## What these tests do not prove

- Synthetic gate tests do not show that the optical reader works with real blood.
- A fake ATECC chip and the Microchip library cannot confirm the state of the physical chip. Run `verify --behaviour` on the real device before permanently locking its data zone.
- Library-interface tests do not validate wiring, camera focus, display offsets, switch bounce, power stability, or sensor accuracy.
- Regtest success does not replace the required public-testnet demonstration on the assembled hardware.

## STL difference on macOS

The print files regenerated successfully on macOS/ARM64, but these two files did not have the same bytes as the Linux-generated files stored in Git LFS:

- `models/print/display_bezel.stl`
- `models/print/optical_head.stl`

The geometry itself did not change:

- Triangle counts and file sizes match.
- The differences affect 54 triangle records in the bezel and 6 in the optical head.
- The largest floating-point difference is about `2.2e-14`.
- After normalizing values close to zero, each generated file matches its stored counterpart byte for byte.

The cause is near-zero normal-vector noise from the platform math library, not a printable shape change. Use the committed STL files for this build. A separate upstream fix could normalize near-zero floats in `tools/stl.py` and regenerate the Git LFS files under review.

## Regtest coverage

The repository's end-to-end test ran on a temporary private regtest network using Bitcoin Core `31.1.0`. It covered:

- p2wpkh
- p2sh-p2wpkh
- p2pkh
- p2tr with the default sighash
- p2tr with explicit `SIGHASH_ALL`
- 2-of-3 p2wsh multisig

For every path, Core funded the firmware-derived address, parsed and finalized the firmware-produced PSBT, accepted the transaction into its mempool, and mined it. CI is pinned to Core 28.0. This local run shows compatibility with 31.1.0 but does not replace the pinned CI result.

## Decision

The software-only checks are complete. Hardware procurement can begin. None of these results should be presented as proof of physical or biometric security.
