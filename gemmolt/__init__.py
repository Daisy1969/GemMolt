"""
GemMolt - Master Coding and Manager Assistant

An autonomous, secure central nervous system for your home and digital workspace.
Inspired by OpenClaw.ai with deep system integration and proactive capabilities.
"""

__version__ = "0.1.0"
__author__ = "GemMolt Team"

from .core import GemMolt
from .security import SecurityManager
from .tasks import TaskExecutor

__all__ = ["GemMolt", "SecurityManager", "TaskExecutor"]
