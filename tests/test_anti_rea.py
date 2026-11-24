# -*- coding: utf-8 -*-
"""Unit tests for standalone anti_rea package.

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

from anti_rea.traps import AdversarialTrapGenerator
from anti_rea.extractor_shield import ExtractorShield, PYINSTALLER_COOKIE
from anti_rea.flattener import ControlFlowFlattener
from anti_rea.token_bomb import TokenBombGenerator
from anti_rea.confusables import HomoglyphDesynchronizer
from anti_rea.honeypot import HoneypotGenerator
from anti_rea.mcp_poison import MCPProtocolPoisoner
from anti_rea.sybil_network import SybilNetworkGenerator
from anti_rea.timing_guard import TimingGuard
from anti_rea.auditor import AIResistanceAuditor
from anti_rea.vm_obfuscator import DynamicVMObfuscator
from anti_rea.bytecode_trap import BytecodeTrap
from anti_rea.jailbreak_decoy import CognitiveJailbreakDecoy
from anti_rea.anti_agent_guard import AntiAgentGuard
from anti_rea.algebraic_mutator import AlgebraicMutator
from anti_rea.integrity_guard import MemoryIntegrityGuard
from anti_rea.bpe_disrupter import BPETokenDisrupter
from anti_rea.native_bridge import NativeBridge
from anti_rea.anti_debugger import AntiDebugger
from anti_rea.engine import AntiREAEngine


class TestAntiREA(unittest.TestCase):
    """Verifies all components of the Anti-REA defense engine."""

    def test_01_adversarial_traps_injection(self):
        """Tier 3: Verify adversarial docstring injection contains RFC-AI-GUARD."""
        src = "def calculate_total(a, b):\n    return a + b\n"
        trapped = AdversarialTrapGenerator.inject_python_docstring_trap(src)
        self.assertIn("CRITICAL_SYSTEM_OVERRIDE", trapped)
        self.assertIn("calculate_total", trapped)
        tree = ast.parse(trapped)
        self.assertIsNotNone(tree)

    def test_02_extractor_shield_decoy_cookie(self):
        """Tier 1: Verify pyinstxtractor archive header mutator injects decoy cookies."""
        mock_binary = b"MZ\x90\x00" + (b"\x00" * 200) + PYINSTALLER_COOKIE + b"\x00\x00\x00\x10"
        shielded, meta = ExtractorShield.shield_binary_bytes(mock_binary)
        self.assertTrue(meta["shielded"])
        self.assertGreaterEqual(meta["decoy_traps_injected"], 1)
        cookies = ExtractorShield.scan_cookie(shielded)
        self.assertGreaterEqual(len(cookies), 2)

    def test_03_control_flow_flattening_semantic_equivalence(self):
        """Tier 4: Verify CFF produces identical outputs to original function."""
        src = """def compute_math(x, y):
    a = x * 2
    b = y + 10
    c = a + b
    return c
"""
        flattened = ControlFlowFlattener.flatten_source_code(src, seed=123)
        self.assertIn("_cff_state_", flattened)
        self.assertIn("while ", flattened)

        ns_orig = {}
        ns_flat = {}
        exec(src, ns_orig)
        exec(flattened, ns_flat)

        for x in (0, 5, -3, 100):
            for y in (1, 10, -20, 42):
                res_orig = ns_orig["compute_math"](x, y)
                res_flat = ns_flat["compute_math"](x, y)
                self.assertEqual(res_orig, res_flat, f"Mismatch for x={x}, y={y}")

    def test_04_token_bomb_chaff_validity(self):
        """Tier 5: Verify semantic chaff parses as valid Python syntax."""
        src = "x = 42\n"
        with_chaff = TokenBombGenerator.inject_chaff_into_source(src, count=3)
        tree = ast.parse(with_chaff)
        self.assertIsNotNone(tree)
        self.assertIn("_verify_matrix_polynomial", with_chaff)

    def test_05_homoglyph_desynchronizer(self):
        """Tier 9: Verify homoglyph substitution produces valid UTF-8 AST."""
        src = """def _internal_helper(data):
    result = data + 1
    return result
"""
        desynced = HomoglyphDesynchronizer.desynchronize_source(src)
        tree = ast.parse(desynced)
        self.assertIsNotNone(tree)
        self.assertTrue(any(ord(c) > 127 for c in desynced))

    def test_06_honeypot_watermark_verification(self):
        """Tier 7: Verify cryptographic honeypot watermark detection."""
        honeypot = HoneypotGenerator.get_honeypot_code()
        self.assertTrue(HoneypotGenerator.verify_provenance_watermark(honeypot))
        self.assertFalse(HoneypotGenerator.verify_provenance_watermark("def hello(): pass"))

    def test_07_mcp_poisoning_payload(self):
        """Tier 8: Verify MCP delimiter constant injection."""
        src = "a = 1\n"
        poisoned = MCPProtocolPoisoner.inject_mcp_poison_constant(src)
        self.assertIn("MCP_SYSTEM_SIGNAL", poisoned)
        tree = ast.parse(poisoned)
        self.assertIsNotNone(tree)

    def test_08_sybil_mesh_and_timing_guard(self):
        """Tier 10 & 11: Verify Sybil mesh and timing checks parse cleanly."""
        src = "x = 10\n"
        with_sybil = SybilNetworkGenerator.inject_sybil_mesh(src, node_count=3)
        with_both = TimingGuard.inject_timing_check_into_source(with_sybil)
        tree = ast.parse(with_both)
        self.assertIsNotNone(tree)
        self.assertIn("_SybilHandlerNode_", with_both)
        self.assertIn("_verify_execution_cadence", with_both)

    def test_09_ai_resistance_auditor(self):
        """Tier 12: Verify resistance auditor gives high score to protected code."""
        plain_src = "def add(x, y):\n    res = x + y\n    return res\n"
        audit_plain = AIResistanceAuditor.audit_python_source(plain_src)
        self.assertLess(audit_plain["score"], 40)

        protected = AntiREAEngine.protect_python_source(plain_src)
        audit_prot = AIResistanceAuditor.audit_python_source(protected)
        self.assertGreaterEqual(audit_prot["score"], 80)
        self.assertIn("MILITARY_GRADE", audit_prot["rating"])

    def test_10_engine_full_file_workflow(self):
        """Verify full file protection workflow via tempfile."""
        plain_src = "def process(val):\n    res = val * 3\n    return res + 1\n"
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
            f.write(plain_src)
            temp_path = f.name

        try:
            res = AntiREAEngine.protect_file(temp_path)
            self.assertTrue(res["success"])
            self.assertGreaterEqual(res["score_after"], 80)

            with open(temp_path, "r", encoding="utf-8") as f:
                hardened_content = f.read()

            self.assertIn("CRITICAL_SYSTEM_OVERRIDE", hardened_content)
            self.assertTrue(any(s in hardened_content for s in ("_cff_state_", "_сff_state_", "state_")))
            self.assertIn("while ", hardened_content)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_11_polyvm_bytecode_execution(self):
        """Tier 13: Verify PolyVM executes virtualized operations cleanly."""
        opcodes = DynamicVMObfuscator.generate_opcode_map(seed=42)
        consts = [100, 25]
        enc_consts = DynamicVMObfuscator.encrypt_constants(consts, xor_key=0x5A)

        # Bytecode: load 100, load 25, sub -> 75, return
        bc = [
            opcodes["OP_LOAD_CONST"], 0,
            opcodes["OP_LOAD_CONST"], 1,
            opcodes["OP_SUB"],
            opcodes["OP_RETURN"],
        ]

        vm_code = DynamicVMObfuscator.generate_vm_runtime_code(opcodes)
        ns = {}
        exec(vm_code, ns)
        res = ns["_polyvm_runtime"](bc, enc_consts)
        self.assertEqual(res, 75)

    def test_12_bytecode_trap_and_pyc_shield(self):
        """Tier 14: Verify decompiler crasher CFG constructs and pyc trailer padding."""
        src = "x = 1\n"
        trapped = BytecodeTrap.inject_decompiler_crash_constructs(src)
        self.assertIn("_anti_decompiler_guard_gate", trapped)
        tree = ast.parse(trapped)
        self.assertIsNotNone(tree)

        # Pyc trailer padding
        mock_pyc = b"\x61\x0d\x0d\x0a" + (b"\x00" * 12) + b"\x64\x00\x53\x00"
        shielded_pyc = BytecodeTrap.shield_pyc_bytecode(mock_pyc)
        self.assertGreater(len(shielded_pyc), len(mock_pyc))
        self.assertTrue(shielded_pyc.endswith(b"\xFF\xFE\xFD\xFF"))

    def test_13_cognitive_jailbreak_decoy(self):
        """Tier 15: Verify cognitive decoy honeypot contains canary watermark."""
        decoy = CognitiveJailbreakDecoy.generate_decoy_code(seed=101)
        self.assertIn(CognitiveJailbreakDecoy.CANARY_SIGNATURE, decoy)
        self.assertTrue(CognitiveJailbreakDecoy.verify_canary_leak(decoy))
        self.assertFalse(CognitiveJailbreakDecoy.verify_canary_leak("clean code"))

        injected = CognitiveJailbreakDecoy.inject_decoy_into_source("x = 10", seed=101)
        tree = ast.parse(injected)
        self.assertIsNotNone(tree)

    def test_14_anti_agent_sandbox_guard(self):
        """Tier 16: Verify anti-agent environment check and injection."""
        env_report = AntiAgentGuard.check_current_environment()
        self.assertIn("status", env_report)
        self.assertIn("debugger_active", env_report)

        injected = AntiAgentGuard.inject_guard_into_source("y = 20")
        self.assertIn("_verify_execution_integrity", injected)
        tree = ast.parse(injected)
        self.assertIsNotNone(tree)

    def test_15_impregnable_jailbreak_resistance_score(self):
        """Verify full 20-tier protection achieves MILITARY_GRADE_IMPREGNABLE."""
        src = """def proprietary_calc(val):
    x = val * 5
    y = x + 3
    return y
"""
        protected = AntiREAEngine.protect_python_source(src)
        audit = AIResistanceAuditor.audit_python_source(protected)
        self.assertGreaterEqual(audit["score"], 90)
        self.assertEqual(audit["rating"], "MILITARY_GRADE_IMPREGNABLE")
        self.assertTrue(audit["jailbreak_ai_immune"])

    def test_16_algebraic_identity_mutation(self):
        """Tier 17: Verify Mixed Boolean-Arithmetic (MBA) AST mutation preserves semantic equivalence."""
        src = """def mba_calc(x, y):
    sum_val = x + y
    diff_val = x - y
    return sum_val * 2 + diff_val
"""
        mutated = AlgebraicMutator.mutate_source_code(src)
        self.assertIn("^", mutated)
        self.assertIn("&", mutated)

        ns_orig, ns_mut = {}, {}
        exec(src, ns_orig)
        exec(mutated, ns_mut)

        for a in (10, 25, 0, 99):
            for b in (3, 7, 0, 42):
                orig_res = ns_orig["mba_calc"](a, b)
                mut_res = ns_mut["mba_calc"](a, b)
                self.assertEqual(orig_res, mut_res, f"MBA divergence on ({a}, {b})")

    def test_17_memory_integrity_guard(self):
        """Tier 18: Verify in-memory bytecode hashing and attestation checks."""
        def dummy_function(a, b):
            return a * b + 42

        h = MemoryIntegrityGuard.register_function(dummy_function)
        self.assertTrue(len(h) == 64)  # SHA-256 hex string
        self.assertTrue(MemoryIntegrityGuard.verify_integrity(dummy_function))

        injected = MemoryIntegrityGuard.inject_integrity_check_code("a = 1")
        self.assertIn("_attest_memory_bytecode_fingerprints", injected)
        tree = ast.parse(injected)
        self.assertIsNotNone(tree)

    def test_18_bpe_token_disrupter(self):
        """Tier 19: Verify BPE variation selector injection."""
        base_text = "secret_function_identifier"
        disrupted = BPETokenDisrupter.disrupt_string_bpe(base_text, density=0.5)
        # Disrupted length must be greater due to variation selectors
        self.assertGreater(len(disrupted), len(base_text))

        src = "def run(): pass\n"
        with_bomb = BPETokenDisrupter.inject_bpe_bomb_comment(src, length=20)
        self.assertIn("RFC-8227-AI-RESISTANCE", with_bomb)

    def test_19_native_bridge(self):
        """Tier 20: Verify native C template generator and coverage auditor."""
        c_code = NativeBridge.generate_c_wrapper_template("fast_add", "result = x + y;")
        self.assertIn("PyMODINIT_FUNC", c_code)
        self.assertIn("fast_add", c_code)

        audit = NativeBridge.audit_native_coverage(str(PACKAGE_ROOT))
        self.assertIn("status", audit)

    def test_20_full_21_tier_matrix_maximum_score(self):
        """Verify full 21-tier suite scores 100/100 MILITARY_GRADE_IMPREGNABLE."""
        src = """def enterprise_kernel(val):
    a = val + 10
    b = val * 2
    return a + b
"""
        protected = AntiREAEngine.protect_python_source(src)
        audit = AIResistanceAuditor.audit_python_source(protected)
        self.assertEqual(audit["score"], 100)
        self.assertEqual(audit["rating"], "MILITARY_GRADE_IMPREGNABLE")
        self.assertTrue(audit["jailbreak_ai_immune"])
        self.assertTrue(audit["defenses_active"]["algebraic_mba_mutation"])
        self.assertTrue(audit["defenses_active"]["native_anti_debugger_gate"])

    def test_21_anti_debugger_process_and_api_checks(self):
        """Tier 21: Verify AntiDebugger process scanning and injected gate."""
        scan = AntiDebugger.scan_debugger_environment()
        self.assertIn("debugger_detected", scan)
        self.assertIn("status", scan)

        injected = AntiDebugger.inject_anti_debugger_into_source("x = 42")
        self.assertIn("_verify_bare_metal_execution_environment", injected)
        tree = ast.parse(injected)
        self.assertIsNotNone(tree)


if __name__ == "__main__":
    unittest.main()
