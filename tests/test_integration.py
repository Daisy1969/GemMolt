"""
Tests for System Integration
"""

import pytest
from gemmolt.integration import SystemIntegration


def test_system_integration_initialization():
    """Test SystemIntegration initialization."""
    config = {}
    integration = SystemIntegration(config)
    
    assert integration is not None
    assert integration.initialized is False


def test_system_integration_initialize():
    """Test system integration initialization."""
    config = {}
    integration = SystemIntegration(config)
    
    result = integration.initialize()
    
    assert result is True
    assert integration.initialized is True
    assert len(integration.system_info) > 0
    assert 'platform' in integration.system_info


def test_system_integration_cleanup():
    """Test system integration cleanup."""
    config = {}
    integration = SystemIntegration(config)
    integration.initialize()
    
    integration.cleanup()
    
    assert integration.initialized is False


def test_system_integration_get_system_info():
    """Test getting system information."""
    config = {}
    integration = SystemIntegration(config)
    integration.initialize()
    
    info = integration.get_system_info()
    
    assert info is not None
    assert 'platform' in info
    assert 'architecture' in info
    assert 'hostname' in info


def test_system_integration_execute_command():
    """Test system command execution (simulated)."""
    config = {}
    integration = SystemIntegration(config)
    integration.initialize()
    
    result = integration.execute_system_command("ls -la")
    
    assert result is not None
    assert 'command' in result
    assert 'status' in result


def test_system_integration_monitor_resources():
    """Test resource monitoring."""
    config = {}
    integration = SystemIntegration(config)
    integration.initialize()
    
    resources = integration.monitor_resources()
    
    assert resources is not None
    assert 'cpu_percent' in resources
    assert 'memory_percent' in resources
    assert 'disk_percent' in resources


def test_system_integration_get_workspace_info():
    """Test getting workspace information."""
    config = {}
    integration = SystemIntegration(config)
    integration.initialize()
    
    workspace = integration.get_workspace_info()
    
    assert workspace is not None
    assert 'cwd' in workspace
    assert 'home' in workspace
