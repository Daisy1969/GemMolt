"""
Tests for GemMolt core functionality
"""

import pytest
from gemmolt import GemMolt
from datetime import datetime


def test_gemmolt_initialization():
    """Test GemMolt initialization."""
    config = {
        'security': {'use_gcp': False},
        'tasks': {'max_history': 50},
        'monitoring': {'max_history': 100}
    }
    
    gemmolt = GemMolt(config)
    
    assert gemmolt is not None
    assert gemmolt.config == config
    assert gemmolt.is_running is False
    assert gemmolt.start_time is None


def test_gemmolt_start_stop():
    """Test starting and stopping GemMolt."""
    config = {'security': {'use_gcp': False}}
    gemmolt = GemMolt(config)
    
    # Start GemMolt
    gemmolt.start()
    assert gemmolt.is_running is True
    assert gemmolt.start_time is not None
    
    # Stop GemMolt
    gemmolt.stop()
    assert gemmolt.is_running is False


def test_gemmolt_execute_task():
    """Test task execution."""
    config = {'security': {'use_gcp': False}}
    gemmolt = GemMolt(config)
    gemmolt.start()
    
    # Execute a task
    result = gemmolt.execute_task(
        "Test task",
        context={"test": True}
    )
    
    assert result is not None
    assert 'success' in result
    assert result['success'] is True
    assert 'task_id' in result
    
    gemmolt.stop()


def test_gemmolt_execute_task_not_running():
    """Test task execution when GemMolt is not running."""
    config = {'security': {'use_gcp': False}}
    gemmolt = GemMolt(config)
    
    with pytest.raises(RuntimeError, match="GemMolt is not running"):
        gemmolt.execute_task("Test task")


def test_gemmolt_get_status():
    """Test getting system status."""
    config = {'security': {'use_gcp': False}}
    gemmolt = GemMolt(config)
    gemmolt.start()
    
    status = gemmolt.get_status()
    
    assert status is not None
    assert 'running' in status
    assert status['running'] is True
    assert 'security' in status
    assert 'tasks' in status
    assert 'monitoring' in status
    assert 'uptime_seconds' in status
    
    gemmolt.stop()


def test_gemmolt_multiple_tasks():
    """Test executing multiple tasks."""
    config = {'security': {'use_gcp': False}}
    gemmolt = GemMolt(config)
    gemmolt.start()
    
    # Execute multiple tasks
    results = []
    for i in range(3):
        result = gemmolt.execute_task(f"Task {i+1}")
        results.append(result)
    
    assert len(results) == 3
    for result in results:
        assert result['success'] is True
    
    # Check task history
    status = gemmolt.get_status()
    assert status['tasks']['total_tasks'] == 3
    assert status['tasks']['completed'] == 3
    
    gemmolt.stop()
