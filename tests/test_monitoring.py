"""
Tests for Proactive Monitor
"""

import pytest
from gemmolt.monitoring import ProactiveMonitor, MonitoringLevel


def test_proactive_monitor_initialization():
    """Test ProactiveMonitor initialization."""
    config = {'max_history': 100}
    monitor = ProactiveMonitor(config)
    
    assert monitor is not None
    assert monitor.is_monitoring is False
    assert monitor.max_history == 100


def test_proactive_monitor_start_stop():
    """Test starting and stopping monitoring."""
    config = {}
    monitor = ProactiveMonitor(config)
    
    # Start monitoring
    monitor.start()
    assert monitor.is_monitoring is True
    assert len(monitor.event_history) > 0
    
    # Stop monitoring
    monitor.stop()
    assert monitor.is_monitoring is False


def test_proactive_monitor_event_handler():
    """Test event handler registration."""
    config = {}
    monitor = ProactiveMonitor(config)
    
    handler_called = []
    
    def test_handler(event):
        handler_called.append(event)
    
    monitor.register_handler(test_handler)
    monitor.start()
    
    assert len(handler_called) > 0


def test_proactive_monitor_check_health():
    """Test system health checking."""
    config = {}
    monitor = ProactiveMonitor(config)
    monitor.start()
    
    health = monitor.check_system_health()
    
    assert health is not None
    assert 'overall' in health
    assert 'checks' in health
    
    monitor.stop()


def test_proactive_monitor_get_event_history():
    """Test getting event history."""
    config = {}
    monitor = ProactiveMonitor(config)
    monitor.start()
    
    events = monitor.get_event_history()
    
    assert events is not None
    assert len(events) > 0
    for event in events:
        assert 'id' in event
        assert 'level' in event
        assert 'message' in event
    
    monitor.stop()


def test_proactive_monitor_get_status():
    """Test getting monitor status."""
    config = {}
    monitor = ProactiveMonitor(config)
    monitor.start()
    
    status = monitor.get_status()
    
    assert status is not None
    assert 'active' in status
    assert 'total_events' in status
    assert 'recent_events' in status
    assert status['active'] is True
    
    monitor.stop()
