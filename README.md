# Anti-REA v5.0.0 🛡️
### Sovereign 180-Tier Defense Engine Against AI-Driven Reverse Engineering & Jailbroken LLMs

<p align="center">
  <img src="https://raw.githubusercontent.com/toprakahmetaydogmus/TZeroAlgorithm/main/assets/siber_akademi_logo.png" width="110" height="110" alt="Siber Akademi Emblem" />
</p>

[![Version: 5.0.0](https://img.shields.io/badge/version-5.0.0-10b981.svg)](pyproject.toml)
[![Tiers: 180 Verified](https://img.shields.io/badge/Defense%20Matrix-180%20Tiers%20(12%20Domains)-06b6d4.svg)](anti_rea/tier_catalog.py)
[![Product Hunt](https://img.shields.io/badge/Product%20Hunt-T--Zero%20Launch-DA552F?style=flat-square&logo=producthunt&logoColor=white)](https://www.producthunt.com/products/tzeroalgorithm?launch=tzeroalgorithm)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero-Leak Certified](https://img.shields.io/badge/Security-100%25%20Zero--Leak-success)](https://github.com/toprakahmetaydogmus/TZeroAlgorithm)

**Anti-REA** is an open-source security engine engineered specifically to neutralize **AI-driven automated reverse engineering toolchains** such as [`morluto/rea`](https://github.com/morluto/rea), automated Ghidra MCP bridges, IDA Pro LLM plugins, `pyinstxtractor`, `uncompyle6`, `pycdc`, and **uncensored / jailbroken LLMs** — while preserving **100% lossless runtime compatibility** for protected applications (classes, `@dataclass`, `async`/`await`, generators, UTF-8, `sys.argv`).

---

## 180-Tier Sovereign Defense Matrix (12 Domains × 15 Layers)

Inspect all 180 individual tiers (`REA-001` through `REA-180`) programmatically via `anti-rea matrix --json`.

| Domain ID | Tier Range | Security Domain | Neutralized Vectors & Guarantees |
| :--- | :--- | :--- | :--- |
| **D01** | `REA-001..015` | **Archive & PE Binary Hardening** | Multi-cave PyInstaller `MEI` decoys, CArchive length mismatch traps, PE MSVC `Rich`/`DanS` header zeroization & COFF `TimeDateStamp` scrubbing. |
| **D02** | `REA-016..030` | **Control-Flow Flattening** | Randomized state ID dispatchers, modulo-2 opaque predicates, docstring/`async`/`yield` preservation. |
| **D03** | `REA-031..045` | **Dynamic PolyVM Bytecode Virtualizer** | Per-build randomized opcodes (`10..249`), rolling encrypted constant pools, custom stack VM runtime & load-time integrity attestation. |
| **D04** | `REA-046..060` | **HKDF-SHA256 & HMAC Bytecode Envelope** | Multi-share split keys, CTR keystream + `HMAC-SHA256` authenticated `zlib(marshal(code))` capsule, `bytearray` RAM wipe, full app parity. |
| **D05** | `REA-061..075` | **Decompiler & AST Parser Crash Barriers** | Nested recursive `try/except/yield from` CFG traps + `0xFF 0xFE 0xFD` trailing opcodes breaking `uncompyle6` & `pycdc`. |
| **D06** | `REA-076..090` | **Type-Safe MBA & Algebraic Mutation** | Mixed Boolean-Arithmetic identities with strict `int` (non-`bool`) checks — zero crashes on strings, floats, lists, or objects. |
| **D07** | `REA-091..105` | **Native Ring-3 & POSIX Anti-Debugger** | Zero-subprocess Win32 `CreateToolhelp32Snapshot` (<2ms), `IsDebuggerPresent`, `NtSetInformationThread`, Linux `TracerPid`, `sys.gettrace`/`sys.monitoring`. |
| **D08** | `REA-106..120` | **Anti-VM, Hypervisor & Sandbox Filter** | VirtualBox/VMware/QEMU driver & process scans, NIC OUI registry, headless agent env & symbolic micro-cadence checks. |
| **D09** | `REA-121..135` | **RDTSC & Hardware Stepping Timing Guards** | Nanosecond `perf_counter_ns` checkpoint deltas blocking F7/F8 single-stepping with immediate `0xC0000409` exit. |
| **D10** | `REA-136..150` | **Memory Integrity & In-Flight String Vault** | Live `co_code` SHA-256 attestation + per-literal UTF-8 encrypted string blobs with in-place RAM buffer zeroization. |
| **D11** | `REA-151..165` | **Electron `.asar` & JS Archive Shield** | Poisoned ASAR headers/canary trailers (`npx asar extract` abort) + JS anti-debug timer & `Object.prototype` freeze traps. |
| **D12** | `REA-166..180` | **Adversarial AI, LLM & MCP Neutralizers** | `RFC-AI-GUARD` prompt traps, MCP JSON-RPC poisons, Sybil meshes, cognitive decoys, Cyrillic homoglyphs, BPE bombs, opt-in-only telemetry. |

---

## Quick Installation & CLI Usage

```bash
# Install via pip
pip install anti-rea

# Protect a Python application with the full 180-Tier Matrix + Authenticated Bytecode Envelope
anti-rea protect my_app.py --output protected_app.py

# Shield a compiled PyInstaller executable against pyinstxtractor & scrub PE toolchain headers
anti-rea shield-exe dist/my_app.exe

# Audit a protected module across all 12 Domains / 180 Tiers
anti-rea audit protected_app.py --json

# Print the complete 180-Tier matrix catalog
anti-rea matrix
```

---

## Developed by Siber Akademi
Developer: **Toprak Ahmet Aydoğmuş**  
Core integration inside [T-Zero Context Architect](https://github.com/toprakahmetaydogmus/TZeroAlgorithm).  
Live Interactive 180-Tier Simulator: [https://tzero-indol.vercel.app/anti_rea_lab.html](https://tzero-indol.vercel.app/anti_rea_lab.html)
