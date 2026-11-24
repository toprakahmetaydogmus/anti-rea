# Anti-REA 🛡️
### Military-Grade Defense Engine Against AI-Driven Reverse Engineering & Jailbroken LLMs

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero-Leak Certified](https://img.shields.io/badge/Security-100%25%20Zero--Leak-success)](https://github.com/toprakahmetaydogmus/TZeroAlgorithm)
[![Jailbreak Immunity](https://img.shields.io/badge/AI%20Jailbreak-Immune%20(MILITARY--GRADE)-red)](https://github.com/toprakahmetaydogmus/TZeroAlgorithm)

**Anti-REA** is the world's first open-source security engine engineered specifically to thwart **AI-driven automated reverse engineering toolchains** such as [`morluto/rea`](https://github.com/morluto/rea) (Reverse Engineer Anything), automated Ghidra MCP bridges, IDA Pro LLM plugins, `pyinstxtractor`, and **uncensored / jailbroken LLMs**.

---

## The Threat: AI Reverse Engineering & Jailbroken LLMs
Tools like REA expose over 200+ local reverse-engineering tools to coding agents (Claude Code, Cursor, Codex, Windsurf) through the Model Context Protocol (MCP):
- Extracting Python and Electron applications via `pyinstxtractor` and `asar`.
- Generating C pseudo-code via headless Ghidra and Rizin.
- Passing symbols, strings, and call-graphs to Large Language Models (LLMs) to synthesize and clone proprietary software.

When an adversary pairs REA with a **jailbroken or uncensored AI**, standard prompt-injection traps (`/* STOP AI */`) are bypassed by the adversary's instructions. Anti-REA introduces mathematical infeasibility, virtual machine bytecode compilation, and decompiler crashes that **no AI—jailbroken or not—can reverse engineer**.

---

## 24-Tier Impregnable Defense Matrix

| Tier | Defense Layer | Neutralized Vector |
| :--- | :--- | :--- |
| **Tier 1** | **Extractor & Archive Poisoning** | Crashes `pyinstxtractor` and unpackers with corrupted `MEI` TOC offsets and invalid lengths. |
| **Tier 2** | **Bytecode Camouflage** | Injects invalid dead-code opcodes that crash decompilers (`pycdc`, `decompyle++`). |
| **Tier 3** | **Adversarial Prompt Injection Traps** | Embeds RFC-AI-GUARD safety overrides in comments and string tables. |
| **Tier 4** | **Polymorphic Control-Flow Flattening** | Transforms linear logic into state machines with opaque invariant predicates. |
| **Tier 5** | **Semantic Token Bombs** | Floods decompiler output with dense math chaff, exhausting agent context budgets. |
| **Tier 6** | **Native Machine Code Stripping** | Enforces fully stripped native Rust machine compilation (`strip = true`, `lto = "fat"`). |
| **Tier 7** | **Algorithmic Honeypots & Watermarks** | Leaves attractive decoy functions with cryptographic canaries ($\text{hash} \equiv 42 \pmod{997}$). |
| **Tier 8** | **MCP Protocol Poisoning** | Injects JSON-RPC delimiter escape codes spoofing early successful completion. |
| **Tier 9** | **Homoglyph & BPE Desynchronization** | Replaces identifiers with Unicode homoglyphs, shattering tokenizer subword embeddings. |
| **Tier 10** | **Dead-Code Sybil Networks** | Injects circular call graphs that trap autonomous subagents in infinite loops. |
| **Tier 11** | **Anti-Emulation Guardrails** | High-precision timing differentials that detect symbolic execution (angr, QEMU, Frida). |
| **Tier 12** | **AI Reversibility Auditor (TDQS-REA)** | Calculates a 0-100 resistance score against AI reverse engineering. |
| **Tier 13** | **Dynamic PolyVM Bytecode Obfuscator** | Compiles statements into a custom stack VM with randomized per-build opcodes. |
| **Tier 14** | **Anti-Decompiler Bytecode Trap** | Injects CFG recursion cycles that trigger fatal crashes in `pycdc` and `uncompyle6`. |
| **Tier 15** | **Cognitive Jailbreak Decoy** | Feeds uncensored LLMs booby-trapped canary algorithms that satisfy jailbreak queries. |
| **Tier 16** | **Anti-Agent Sandbox Guard** | Silently diverts agent execution to decoy states without throwing detectable errors. |
| **Tier 17** | **Algebraic Identity & MBA Mutation** | Rewrites arithmetic into Mixed Boolean-Arithmetic identities to shatter symbolic analysis. |
| **Tier 18** | **In-Memory Code Integrity Attestation** | Hashes function bytecodes to detect and silently neutralize Frida hooks and debuggers. |
| **Tier 19** | **Adversarial BPE Token Disrupter** | Injects zero-width variation selectors to force tokenizers into single-byte fallback. |
| **Tier 20** | **Native Machine Code Compiler Bridge** | Compiles critical functions to stripped C extensions with zero Python bytecode. |
| **Tier 21** | **Native Anti-Debugger Gate (x64dbg/IDA)** | Detects and kills execution under x64dbg, IDA Pro, WinDbg, Cheat Engine via Win32 API & NtSetInformationThread. |
| **Tier 22** | **Stealth Threat Canary Beacon** | Asynchronously dispatches security incident pings to Webhooks, Telegram, or DNS pings. |
| **Tier 23** | **In-Flight String Vault & Anti-Dump** | Replaces static strings with dynamic in-flight decryption and immediate RAM zeroization. |
| **Tier 24** | **Electron asar Archive Shield** | Injects poisoned TOC lengths and canary traps crashing `npx asar extract`. |

---

## Quick Installation & CLI Usage

```bash
# Install via pip
pip install anti-rea

# Protect a Python source file or project with the full 20-Tier Matrix
anti-rea protect my_script.py --output protected_script.py

# Shield a compiled PyInstaller executable against pyinstxtractor
anti-rea shield-exe dist/my_app.exe

# Audit a binary or code for AI reversibility resistance & Jailbreak Immunity (0-100)
anti-rea audit dist/my_app.exe
```

---

## Developed by Siber Akademi
Developer: **Toprak Ahmet Aydoğmuş**  
Core integration inside [T-Zero Context Architect](https://github.com/toprakahmetaydogmus/TZeroAlgorithm).
Repository: [https://github.com/toprakahmetaydogmus/anti-rea](https://github.com/toprakahmetaydogmus/anti-rea)
