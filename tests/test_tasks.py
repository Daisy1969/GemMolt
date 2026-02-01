"""
Tests for Task Executor
"""

import pytest
from gemmolt.tasks import TaskExecutor, TaskStatus


def test_task_executor_initialization():
    """Test TaskExecutor initialization."""
    config = {'max_history': 50}
    executor = TaskExecutor(config)
    
    assert executor is not None
    assert executor.max_history == 50
    assert len(executor.task_history) == 0


def test_task_executor_execute_success():
    """Test successful task execution."""
    config = {}
    executor = TaskExecutor(config)
    
    result = executor.execute("Test task", {"test": True})
    
    assert result is not None
    assert result['success'] is True
    assert 'task_id' in result
    assert 'result' in result


def test_task_executor_task_history():
    """Test task history tracking."""
    config = {'max_history': 10}
    executor = TaskExecutor(config)
    
    # Execute multiple tasks
    for i in range(5):
        executor.execute(f"Task {i+1}", {})
    
    history = executor.get_task_history()
    
    assert len(history) == 5
    for task in history:
        assert 'id' in task
        assert 'description' in task
        assert 'status' in task


def test_task_executor_max_history():
    """Test that task history respects max_history limit."""
    config = {'max_history': 3}
    executor = TaskExecutor(config)
    
    # Execute more tasks than max_history
    for i in range(5):
        executor.execute(f"Task {i+1}", {})
    
    assert len(executor.task_history) == 3


def test_task_executor_get_status():
    """Test getting task executor status."""
    config = {}
    executor = TaskExecutor(config)
    
    # Execute some tasks
    executor.execute("Task 1", {})
    executor.execute("Task 2", {})
    
    status = executor.get_status()
    
    assert status is not None
    assert 'total_tasks' in status
    assert 'completed' in status
    assert 'failed' in status
    assert status['total_tasks'] == 2
    assert status['completed'] == 2
