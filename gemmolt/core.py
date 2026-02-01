"""
Core GemMolt System

Central nervous system for autonomous operations.
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

from .security import SecurityManager
from .tasks import TaskExecutor
from .integration import SystemIntegration
from .monitoring import ProactiveMonitor

logger = logging.getLogger(__name__)


class GemMolt:
    """
    GemMolt - Master Coding and Manager Assistant
    
    Autonomous, secure central nervous system for home and digital workspace.
    Inspired by OpenClaw.ai with focus on security, integration, and proactive capabilities.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize GemMolt system.
        
        Args:
            config: Configuration dictionary for GemMolt
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        
        # Initialize core components
        self.security_manager = SecurityManager(self.config.get('security', {}))
        self.task_executor = TaskExecutor(self.config.get('tasks', {}))
        self.system_integration = SystemIntegration(self.config.get('integration', {}))
        self.proactive_monitor = ProactiveMonitor(self.config.get('monitoring', {}))
        
        self.is_running = False
        self.start_time: Optional[datetime] = None
        
        self.logger.info("GemMolt initialized successfully")
    
    def start(self) -> None:
        """Start the GemMolt system."""
        if self.is_running:
            self.logger.warning("GemMolt is already running")
            return
        
        self.logger.info("Starting GemMolt...")
        
        # Authenticate with GCP
        if not self.security_manager.authenticate():
            raise RuntimeError("Failed to authenticate with GCP")
        
        # Start monitoring
        self.proactive_monitor.start()
        
        # Initialize system integration
        self.system_integration.initialize()
        
        self.is_running = True
        self.start_time = datetime.now()
        
        self.logger.info("GemMolt started successfully")
    
    def stop(self) -> None:
        """Stop the GemMolt system."""
        if not self.is_running:
            self.logger.warning("GemMolt is not running")
            return
        
        self.logger.info("Stopping GemMolt...")
        
        # Stop monitoring
        self.proactive_monitor.stop()
        
        # Cleanup system integration
        self.system_integration.cleanup()
        
        self.is_running = False
        
        self.logger.info("GemMolt stopped successfully")
    
    def execute_task(self, task_description: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute an autonomous task.
        
        Args:
            task_description: Description of the task to execute
            context: Optional context for task execution
            
        Returns:
            Result of task execution
        """
        if not self.is_running:
            raise RuntimeError("GemMolt is not running. Call start() first.")
        
        self.logger.info(f"Executing task: {task_description}")
        
        # Verify security context
        if not self.security_manager.verify_permissions(task_description):
            raise PermissionError("Insufficient permissions for task execution")
        
        # Execute the task
        result = self.task_executor.execute(task_description, context or {})
        
        return result
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of GemMolt system."""
        return {
            "running": self.is_running,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "uptime_seconds": (datetime.now() - self.start_time).total_seconds() if self.start_time else 0,
            "security": self.security_manager.get_status(),
            "tasks": self.task_executor.get_status(),
            "monitoring": self.proactive_monitor.get_status()
        }
