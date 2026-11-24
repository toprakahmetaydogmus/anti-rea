# -*- coding: utf-8 -*-
"""Anti-REA: Military-Grade AI Reverse Engineering Defense Engine.

World-class, 20-tier anti-reverse-engineering defense matrix against autonomous
AI agents (morluto/rea, Ghidra MCP, pyinstxtractor, IDA LLM) and uncensored/jailbroken LLMs.

Developer: Toprak Ahmet Aydoğmuş (Siber Akademi)
Part of Siber Akademi T-Zero Security Suite.
License: MIT
"""

__version__ = "3.0.0"
__author__ = "Toprak Ahmet Aydoğmuş"
__license__ = "MIT"

from .engine import AntiREAEngine
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

__all__ = [
    "AntiREAEngine",
    "AdversarialTrapGenerator",
    "ExtractorShield",
    "ControlFlowFlattener",
    "TokenBombGenerator",
    "HomoglyphDesynchronizer",
    "HoneypotGenerator",
    "MCPProtocolPoisoner",
    "SybilNetworkGenerator",
    "TimingGuard",
    "AIResistanceAuditor",
    "DynamicVMObfuscator",
    "BytecodeTrap",
    "CognitiveJailbreakDecoy",
    "AntiAgentGuard",
    "AlgebraicMutator",
    "MemoryIntegrityGuard",
    "BPETokenDisrupter",
    "NativeBridge",
]
