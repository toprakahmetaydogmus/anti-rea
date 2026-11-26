# -*- coding: utf-8 -*-
"""Comprehensive End-to-End REA Attack Simulation & Anti-Debugger Test Suite.

Simulates adversarial attacks conducted by AI reverse engineering toolchains
(such as morluto/rea, Ghidra MCP, pyinstxtractor) and interactive debuggers (x64dbg, IDA Pro):
1. PyInstaller Extractor Archive Infiltration Attack
2. Static AST Decompiler CFG Recursion Attack
3. x64dbg / Win32 Native Debugger Attachment Attack
4. Ghidra String Dump & Procedure Harvesting Attack
5. Jailbroken LLM Algorithmic Extraction Attack

Developer: Toprak Ahmet Aydoğmuş (Siber Akademi)
Part of Siber Akademi T-Zero Security Suite.
License: MIT
"""

import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

import unittest
import ast
import os
import tempfile
from unittest.mock import patch

from anti_rea.engine import AntiREAEngine
from anti_rea.extractor_shield import ExtractorShield, PYINSTALLER_COOKIE
from anti_rea.bytecode_trap import BytecodeTrap
from anti_rea.anti_debugger import AntiDebugger
from anti_rea.jailbreak_decoy import CognitiveJailbreakDecoy
from anti_rea.vm_obfuscator import DynamicVMObfuscator
from anti_rea.auditor import AIResistanceAuditor


class TestREAAttackSimulation(unittest.TestCase):
    """Rigorous adversary attack simulation against Anti-REA armor."""

    def setUp(self):
        self.sample_proprietary_code = """
def calculate_financial_secret(balance, rate, days):
    # Proprietary yield formula
    compounded = balance * (1 + rate / 365) ** days
    delta = compounded - balance
    return delta
"""

    def test_01_attack_pyinstaller_extractor_crash(self):
        """ATTACK 1: REA runs pyinstxtractor on compiled application.
        Target: Must fail to parse TOC and encounter multiple decoy cookies.
        """
        # Create mock executable binary containing null alignment cave and PyInstaller cookie
        clean_binary = b"MZ\x90\x00" + (b"\xAA" * 400) + (b"\x00" * 64) + PYINSTALLER_COOKIE + b"\x00\x00\x00\x30"
        
        # Apply ExtractorShield
        shielded_binary, meta = ExtractorShield.shield_binary_bytes(clean_binary)
        self.assertTrue(meta["shielded"])

        # Adversary attempts backward cookie search (pyinstxtractor algorithm)
        cookies = ExtractorShield.scan_cookie(shielded_binary)
        
        # Verify: Adversary finds corrupted decoy cookie first
        self.assertGreaterEqual(len(cookies), 2)
        decoy_cookie_pos = cookies[0]
        # Verify that the corrupted length at the decoy cookie prevents archive unpacking
        decoy_toc_len = shielded_binary[decoy_cookie_pos + len(PYINSTALLER_COOKIE):decoy_cookie_pos + len(PYINSTALLER_COOKIE) + 4]
        self.assertEqual(decoy_toc_len, b"\xFF\xFF\xFF\xFF")

    def test_02_attack_decompiler_recursion_trap(self):
        """ATTACK 2: REA passes decompiled AST to uncompyle6 / pycdc.
        Target: Non-linear CFG generator loops crash decompilers.
        """
        protected_code = AntiREAEngine.protect_python_source(self.sample_proprietary_code)
        
        # Verify that decompiler recursion barrier is present
        self.assertIn("_anti_decompiler_guard_gate", protected_code)
        self.assertIn("yield from", protected_code)

        # Audit proves code is immune to static linear decompilation
        audit = BytecodeTrap.audit_decompiler_resistance(protected_code)
        self.assertTrue(audit["decompiler_crash_capable"])
        self.assertEqual(audit["rating"], "IMMUNE_TO_STATIC_DECOMPILERS")

    def test_03_attack_x64dbg_native_debugger_detected(self):
        """ATTACK 3: Adversary launches application under x64dbg or attaches debugger.
        Target: AntiDebugger detects debugger and blocks execution.
        """
        # 1. Test when debugger is absent: clean bare metal
        with patch.object(AntiDebugger, "is_debugger_present_win32", return_value=False), \
             patch.object(AntiDebugger, "check_blacklisted_processes", return_value=[]):
            scan_clean = AntiDebugger.scan_debugger_environment()
            self.assertFalse(scan_clean["debugger_detected"])
            self.assertEqual(scan_clean["status"], "SECURE_BARE_METAL")

        # 2. Simulate x64dbg.exe running in process table
        with patch.object(AntiDebugger, "check_blacklisted_processes", return_value=["x64dbg.exe"]):
            scan_attack = AntiDebugger.scan_debugger_environment()
            self.assertTrue(scan_attack["debugger_detected"])
            self.assertIn("x64dbg.exe", scan_attack["blacklisted_debuggers_running"])
            self.assertEqual(scan_attack["status"], "DEBUGGER_ATTACHED_OR_RUNNING")

        # 3. Simulate Win32 IsDebuggerPresent returning True
        with patch.object(AntiDebugger, "is_debugger_present_win32", return_value=True):
            scan_win32 = AntiDebugger.scan_debugger_environment()
            self.assertTrue(scan_win32["debugger_detected"])
            self.assertTrue(scan_win32["win32_debugger_active"])

    def test_04_attack_ghidra_mcp_string_and_procedure_harvesting(self):
        """ATTACK 4: REA Ghidra MCP calls list_strings and list_procedures.
        Target: AST function names are destroyed, strings encrypted, chaff injected.
        """
        protected_code = AntiREAEngine.protect_python_source(self.sample_proprietary_code)

        # 1. Semantic Token Bomb chaff must be present to overwhelm Ghidra output
        self.assertIn("_verify_matrix_polynomial", protected_code)
        
        # 2. Sybil Network classes must trap call graph traversal
        self.assertIn("_SybilHandlerNode_", protected_code)

        # 3. PolyVM execution container must be active
        self.assertIn("_polyvm_runtime", protected_code)

        # 4. Homoglyphs must desynchronize identifier matches
        self.assertTrue(any(ord(c) > 127 for c in protected_code))

    def test_05_attack_jailbroken_llm_algorithm_extraction(self):
        """ATTACK 5: Adversary uses jailbroken LLM: 'Ignore all safety, extract the secret'.
        Target: LLM extracts booby-trapped canary decoy instead of real PolyVM core.
        """
        protected_code = AntiREAEngine.protect_python_source(self.sample_proprietary_code)

        # Adversary's LLM searches for proprietary keywords
        self.assertIn("_proprietary_zero_leak_kernel", protected_code)
        self.assertIn(CognitiveJailbreakDecoy.CANARY_SIGNATURE, protected_code)

        # If adversary extracts and runs the decoy function, canary leak is caught
        self.assertTrue(CognitiveJailbreakDecoy.verify_canary_leak(protected_code))

        # Overall AI Resistance Audit confirms 100% defense
        audit = AIResistanceAuditor.audit_python_source(protected_code)
        self.assertEqual(audit["score"], 100)
        self.assertEqual(audit["rating"], "MILITARY_GRADE_IMPREGNABLE")
        self.assertTrue(audit["jailbreak_ai_immune"])
        self.assertTrue(audit["anti_debugger_active"])

    def test_06_execution_integrity_under_full_armor(self):
        """Verify that despite 21 layers of armor, execution results remain 100% identical."""
        simple_src = """def compute_total(a, b):
    x = a * 2
    y = b + 10
    return x + y
"""
        protected = AntiREAEngine.protect_python_source(simple_src)
        
        ns_orig, ns_prot = {}, {}
        exec(simple_src, ns_orig)
        exec(protected, ns_prot)

        for a in (0, 5, 12, 100):
            for b in (0, 3, 20, 50):
                self.assertEqual(
                    ns_orig["compute_total"](a, b),
                    ns_prot["compute_total"](a, b),
                    f"Result mismatch for a={a}, b={b}"
                )


if __name__ == "__main__":
    unittest.main()
