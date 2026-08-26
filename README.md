# POIDH Bounty #24: CELL Hardware Wallet

**English** | [Bahasa Indonesia](./README.id.md)

This directory contains the plan, checklist, and test record for an attempt at [POIDH Mainnet bounty #24](https://poidh.xyz/mainnet/bounty/24). The task is to build CELL and prove that it can authorize signatures using both a pulse and fresh blood.

## Source documents

- [Bounty requirements](https://github.com/z0r0z/cell/blob/main/BOUNTY.md)
- [Build instructions](https://github.com/z0r0z/cell/blob/main/BUILD.md)
- [Bill of materials](https://github.com/z0r0z/cell/blob/main/BOM.csv)
- [Safety rules](https://github.com/z0r0z/cell/blob/main/SAFETY.md)
- [Known validation status](https://github.com/z0r0z/cell/blob/main/VALIDATION.md)
- [Printing instructions](https://github.com/z0r0z/cell/blob/main/PRINTING.md)
- [POIDH V3 contract](https://etherscan.io/address/0xE731dFadBFf20542E10D09D26Fc71445C70d4232)

## Fixed reference point

- CELL branch: `main`
- Pinned commit: `9ae536c92186ba7d0d8e0f1a12ccf68c7f27446e`
- Network: Ethereum Mainnet
- Bounty ID: `24`
- POIDH contract: `0xE731dFadBFf20542E10D09D26Fc71445C70d4232`
- Issuer: `0x1C0Aa8cCD568d90d61659F060D1bFb1e6f855A20`
- Recorded on: `2026-08-26`

The bounty can change on-chain. Check its status and balance again before buying parts and before submitting a claim.

## What qualifies as a claim

### Full build

Complete milestones 1–12 in section 15 of `BUILD.md`, then provide:

1. Photos or video of the assembled device running.
2. A pulse-authorized signature.
3. A fresh-blood-authorized signature.
4. The resulting on-chain transaction. A testnet transaction is allowed.
5. A complete record of changes made to the reference build.

### Reader-only result

Complete milestone 7 and publish the spoof-panel results, `thresholds.json`, raw files under `captures/`, and the hardware and calibration notes.

### Reproducible failure

The bounty also accepts useful real-hardware failures. Keep the raw data if a fake sample passes, genuine blood fails, or the documented optical design cannot reproduce the expected result.

## Cost stated by the project

| Stage | Cost |
|---|---:|
| Reader hardware | $62.25 |
| Reader consumables | $31.00 |
| Wallet hardware | $35.30 |
| Total | **$128.55** |

This total excludes shipping, tax, tools, sample collection, replacement parts, failed prints, and Mainnet gas. Reserve another 25–35% for hardware problems and keep gas funds separate.

## Non-negotiable safety rules

- Read `SAFETY.md` before handling any sample.
- Use sealed, sterile, single-use commercial lancets.
- Never share anything that touches blood.
- Put used lancets in a sharps container and follow local disposal rules.
- Do not attempt a venous blood draw without qualified medical staff.
- Use a new test seed and testnet funds. Do not use a personal wallet.
- Never commit or publish a PIN, mnemonic, private key, or secret-bearing screen.
- Test the ATECC608B thoroughly before any irreversible lock command.

Next documents: [execution plan](./PLAN.md), [working checklist](./CHECKLIST.md), and [software test record](./SOFTWARE_BASELINE.md).
