"""
Autonomous Task Execution Engine

Executes tasks autonomously with intelligent planning and execution.
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class TaskStatus(Enum):
    """Task execution status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Task:
    """Represents a task to be executed."""
    
    def __init__(self, description: str, context: Dict[str, Any]):
        self.id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.description = description
        self.context = context
        self.status = TaskStatus.PENDING
        self.result: Optional[Any] = None
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary."""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "result": self.result
        }


class TaskExecutor:
    """
    Autonomous task execution engine.
    
    Features:
    - Intelligent task planning
    - Autonomous execution
    - Error handling and recovery
    - Task history and monitoring
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize Task Executor.
        
        Args:
            config: Task execution configuration
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.task_history: List[Task] = []
        self.max_history = config.get('max_history', 100)
        
        self.logger.info("TaskExecutor initialized")
    
    def execute(self, task_description: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a task autonomously.
        
        Args:
            task_description: Description of the task
            context: Execution context
            
        Returns:
            Task execution result
        """
        task = Task(task_description, context)
        self.task_history.append(task)
        
        try:
            self.logger.info(f"Starting task execution: {task.id}")
            task.status = TaskStatus.RUNNING
            
            # Analyze and plan the task
            plan = self._plan_task(task_description, context)
            
            # Execute the plan
            result = self._execute_plan(plan, context)
            
            # Mark task as completed
            task.status = TaskStatus.COMPLETED
            task.result = result
            task.completed_at = datetime.now()
            
            self.logger.info(f"Task completed successfully: {task.id}")
            
            return {
                "success": True,
                "task_id": task.id,
                "result": result
            }
            
        except Exception as e:
            self.logger.error(f"Task execution failed: {e}")
            task.status = TaskStatus.FAILED
            task.result = {"error": str(e)}
            task.completed_at = datetime.now()
            
            return {
                "success": False,
                "task_id": task.id,
                "error": str(e)
            }
        finally:
            # Maintain history size
            if len(self.task_history) > self.max_history:
                self.task_history = self.task_history[-self.max_history:]
    
    def _plan_task(self, description: str, context: Dict[str, Any]) -> List[str]:
        """
        Create an execution plan for the task.
        
        Args:
            description: Task description
            context: Execution context
            
        Returns:
            List of execution steps
        """
        self.logger.debug(f"Planning task: {description}")
        
        # In production, this would use AI/ML for intelligent planning
        # For now, we create a simple plan
        plan = [
            "Analyze task requirements",
            "Gather necessary resources",
            "Execute primary operations",
            "Verify results",
            "Cleanup and finalize"
        ]
        
        return plan
    
    def _execute_plan(self, plan: List[str], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the task plan.
        
        Args:
            plan: List of steps to execute
            context: Execution context
            
        Returns:
            Execution result
        """
        results = {}
        
        for step in plan:
            self.logger.debug(f"Executing step: {step}")
            # In production, each step would have actual implementation
            results[step] = "completed"
        
        return {
            "steps_completed": len(plan),
            "plan": plan,
            "details": results
        }
    
    def get_task_history(self) -> List[Dict[str, Any]]:
        """Get task execution history."""
        return [task.to_dict() for task in self.task_history]
    
    def get_status(self) -> Dict[str, Any]:
        """Get task executor status."""
        return {
            "total_tasks": len(self.task_history),
            "completed": sum(1 for t in self.task_history if t.status == TaskStatus.COMPLETED),
            "failed": sum(1 for t in self.task_history if t.status == TaskStatus.FAILED),
            "recent_tasks": [t.to_dict() for t in self.task_history[-5:]]
        }
