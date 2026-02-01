"""
Proactive Monitoring and Capabilities

Monitors system state and proactively responds to events.
"""

import logging
from typing import Dict, Any, List, Callable
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class MonitoringLevel(Enum):
    """Monitoring severity levels."""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class MonitoringEvent:
    """Represents a monitoring event."""
    
    def __init__(self, level: MonitoringLevel, message: str, data: Dict[str, Any]):
        self.id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.level = level
        self.message = message
        self.data = data
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary."""
        return {
            "id": self.id,
            "level": self.level.value,
            "message": self.message,
            "data": self.data,
            "timestamp": self.timestamp.isoformat()
        }


class ProactiveMonitor:
    """
    Proactive monitoring system.
    
    Features:
    - Continuous system monitoring
    - Event detection and alerting
    - Proactive response capabilities
    - Event history and analysis
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize Proactive Monitor.
        
        Args:
            config: Monitoring configuration
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.is_monitoring = False
        self.event_history: List[MonitoringEvent] = []
        self.max_history = config.get('max_history', 1000)
        self.handlers: List[Callable] = []
        
        self.logger.info("ProactiveMonitor initialized")
    
    def start(self) -> None:
        """Start proactive monitoring."""
        if self.is_monitoring:
            self.logger.warning("Monitoring is already active")
            return
        
        self.logger.info("Starting proactive monitoring...")
        self.is_monitoring = True
        
        # Record startup event
        self._record_event(MonitoringLevel.INFO, "Monitoring started", {})
    
    def stop(self) -> None:
        """Stop proactive monitoring."""
        if not self.is_monitoring:
            self.logger.warning("Monitoring is not active")
            return
        
        self.logger.info("Stopping proactive monitoring...")
        
        # Record shutdown event
        self._record_event(MonitoringLevel.INFO, "Monitoring stopped", {})
        
        self.is_monitoring = False
    
    def _record_event(self, level: MonitoringLevel, message: str, data: Dict[str, Any]) -> None:
        """
        Record a monitoring event.
        
        Args:
            level: Event severity level
            message: Event message
            data: Event data
        """
        event = MonitoringEvent(level, message, data)
        self.event_history.append(event)
        
        # Log based on level
        if level == MonitoringLevel.CRITICAL:
            self.logger.critical(message)
        elif level == MonitoringLevel.WARNING:
            self.logger.warning(message)
        else:
            self.logger.info(message)
        
        # Trigger handlers
        for handler in self.handlers:
            try:
                handler(event)
            except Exception as e:
                self.logger.error(f"Event handler failed: {e}")
        
        # Maintain history size
        if len(self.event_history) > self.max_history:
            self.event_history = self.event_history[-self.max_history:]
    
    def register_handler(self, handler: Callable) -> None:
        """
        Register an event handler.
        
        Args:
            handler: Callable that accepts a MonitoringEvent
        """
        self.handlers.append(handler)
        self.logger.info("Event handler registered")
    
    def check_system_health(self) -> Dict[str, Any]:
        """
        Proactively check system health.
        
        Returns:
            System health status
        """
        # In production, this would perform actual health checks
        health_status = {
            "overall": "healthy",
            "checks": {
                "connectivity": "ok",
                "resources": "ok",
                "services": "ok"
            }
        }
        
        if health_status["overall"] != "healthy":
            self._record_event(
                MonitoringLevel.WARNING,
                "System health degraded",
                health_status
            )
        
        return health_status
    
    def get_event_history(self) -> List[Dict[str, Any]]:
        """Get monitoring event history."""
        return [event.to_dict() for event in self.event_history]
    
    def get_status(self) -> Dict[str, Any]:
        """Get monitoring status."""
        return {
            "active": self.is_monitoring,
            "total_events": len(self.event_history),
            "recent_events": [e.to_dict() for e in self.event_history[-5:]],
            "handlers_registered": len(self.handlers)
        }
