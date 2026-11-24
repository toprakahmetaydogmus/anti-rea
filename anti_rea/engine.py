# -*- coding: utf-8 -*-
"""Master Anti-REA Engine.

Unified coordinator applying the 20-Tier Anti-REA Armor Matrix across
source files, packages, and compiled executables.

Developer: Toprak Ahmet Aydoğmuş (Siber Akademi)
Part of Siber Akademi T-Zero Security Suite.
License: MIT
"""

import os
from typing import Dict, Any, Optional

from .traps import AdversarialTrapGenerator
from .extractor_shield import ExtractorShield
from .flattener import ControlFlowFlattener
from .token_bomb import TokenBombGenerator
from .confusables import HomoglyphDesynchronizer
from .honeypot import HoneypotGenerator
from .mcp_poison import MCPProtocolPoisoner
from .sybil_network import SybilNetworkGenerator
from .timing_guard import TimingGuard
from .auditor import AIResistanceAuditor
from .vm_obfuscator import DynamicVMObfuscator
from .bytecode_trap import BytecodeTrap
from .jailbreak_decoy import CognitiveJailbreakDecoy
from .anti_agent_guard import AntiAgentGuard
from .algebraic_mutator import AlgebraicMutator
from .integrity_guard import MemoryIntegrityGuard
from .bpe_disrupter import BPETokenDisrupter
from .native_bridge import NativeBridge


class AntiREAEngine:
    """Master engine orchestrating military-grade Anti-REA code and binary protection."""

    @classmethod
    def protect_python_source(
        cls,
        source_code: str,
        flatten: bool = True,
        token_chaff: bool = True,
        prompt_traps: bool = True,
        homoglyphs: bool = True,
        honeypot: bool = True,
        mcp_poison: bool = True,
        sybil_mesh: bool = True,
        timing_guard: bool = True,
        decompiler_trap: bool = True,
        jailbreak_decoy: bool = True,
        anti_agent_guard: bool = True,
        vm_container: bool = True,
        algebraic_mutation: bool = True,
        integrity_guard: bool = True,
        bpe_disrupt: bool = True,
        seed: int = 42,
    ) -> str:
        """Applies comprehensive 20-tier Anti-REA protection passes to Python source code."""
        code = source_code

        # 1. Algebraic Identity Mutation (Mixed Boolean-Arithmetic)
        if algebraic_mutation:
            code = AlgebraicMutator.mutate_source_code(code)

        # 2. Control Flow Flattening (if enabled)
        if flatten:
            code = ControlFlowFlattener.flatten_source_code(code, seed=seed)

        # 3. Homoglyph Tokenizer Desynchronization
        if homoglyphs:
            code = HomoglyphDesynchronizer.desynchronize_source(code, seed=seed)

        # 4. Decompiler Crash Barrier
        if decompiler_trap:
            code = BytecodeTrap.inject_decompiler_crash_constructs(code, seed=seed)

        # 5. In-Memory Code Integrity Attestation
        if integrity_guard:
            code = MemoryIntegrityGuard.inject_integrity_check_code(code)

        # 6. Anti-Agent Sandbox & Emulation Guard
        if anti_agent_guard:
            code = AntiAgentGuard.inject_guard_into_source(code)

        # 7. Timing Guard
        if timing_guard:
            code = TimingGuard.inject_timing_check_into_source(code)

        # 8. Sybil Mesh
        if sybil_mesh:
            code = SybilNetworkGenerator.inject_sybil_mesh(code, node_count=4, seed=seed)

        # 9. Cognitive Jailbreak Decoy
        if jailbreak_decoy:
            code = CognitiveJailbreakDecoy.inject_decoy_into_source(code, seed=seed)

        # 10. Token Chaff
        if token_chaff:
            code = TokenBombGenerator.inject_chaff_into_source(code, count=3, seed=seed)

        # 11. Honeypot Decoy
        if honeypot:
            code = HoneypotGenerator.inject_honeypot_into_source(code)

        # 12. MCP Protocol Poison
        if mcp_poison:
            code = MCPProtocolPoisoner.inject_mcp_poison_constant(code)

        # 13. Dynamic PolyVM Bytecode Container
        if vm_container:
            code = DynamicVMObfuscator.protect_source_with_vm(code, seed=seed)

        # 14. BPE Token Collision Disruptor
        if bpe_disrupt:
            code = BPETokenDisrupter.inject_bpe_bomb_comment(code, length=50, seed=seed)

        # 15. Adversarial Prompt Injection Traps (in header)
        if prompt_traps:
            code = AdversarialTrapGenerator.inject_python_docstring_trap(code)

        return code

    @classmethod
    def protect_file(
        cls,
        file_path: str,
        output_path: Optional[str] = None,
        **options: Any
    ) -> Dict[str, Any]:
        """Protects a Python source file or compiled executable on disk."""
        if not os.path.isfile(file_path):
            return {"success": False, "error": f"File not found: {file_path}"}

        out = output_path or file_path

        # If it's a binary executable, apply ExtractorShield
        if file_path.lower().endswith((".exe", ".bin", ".elf", ".so", ".pyd")):
            return ExtractorShield.shield_file(file_path, output_path=out)

        # Otherwise assume Python source code
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            protected = cls.protect_python_source(content, **options)

            with open(out, "w", encoding="utf-8") as f:
                f.write(protected)

            audit_before = AIResistanceAuditor.audit_python_source(content)
            audit_after = AIResistanceAuditor.audit_python_source(protected)

            return {
                "success": True,
                "input_file": file_path,
                "output_file": out,
                "score_before": audit_before["score"],
                "score_after": audit_after["score"],
                "rating": audit_after["rating"],
                "status": "PROTECTED_MILITARY_GRADE" if audit_after["score"] >= 80 else "PROTECTED"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    @classmethod
    def audit_target(cls, path: str) -> Dict[str, Any]:
        """Runs the AI Resistance Auditor on a target file or directory."""
        return AIResistanceAuditor.audit_file(path)
