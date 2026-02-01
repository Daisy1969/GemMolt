"""
Example: Basic GemMolt Usage

Demonstrates basic usage of GemMolt system.
"""

import logging
from gemmolt import GemMolt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """Run basic GemMolt example."""
    print("=== GemMolt Basic Example ===\n")
    
    # Configuration
    config = {
        'security': {
            'gcp_project_id': 'gemmolt-demo-project',
            'use_gcp': False  # Set to True in production with actual GCP setup
        },
        'tasks': {
            'max_history': 50
        },
        'monitoring': {
            'max_history': 500
        },
        'integration': {}
    }
    
    # Initialize GemMolt
    print("1. Initializing GemMolt...")
    gemmolt = GemMolt(config)
    
    # Start GemMolt
    print("2. Starting GemMolt system...")
    gemmolt.start()
    
    # Check status
    print("\n3. Checking system status...")
    status = gemmolt.get_status()
    print(f"   - Running: {status['running']}")
    print(f"   - Security authenticated: {status['security']['authenticated']}")
    print(f"   - Monitoring active: {status['monitoring']['active']}")
    
    # Execute tasks
    print("\n4. Executing autonomous tasks...")
    
    # Task 1: System health check
    print("   a) Task: Check system health")
    result1 = gemmolt.execute_task(
        "Check system health and report status",
        context={"priority": "high"}
    )
    print(f"      Result: {result1['success']}, Task ID: {result1['task_id']}")
    
    # Task 2: Monitor resources
    print("   b) Task: Monitor system resources")
    result2 = gemmolt.execute_task(
        "Monitor system resources and alert if needed",
        context={"threshold": "80%"}
    )
    print(f"      Result: {result2['success']}, Task ID: {result2['task_id']}")
    
    # Task 3: Custom analysis
    print("   c) Task: Analyze workspace")
    result3 = gemmolt.execute_task(
        "Analyze digital workspace and provide recommendations",
        context={"depth": "detailed"}
    )
    print(f"      Result: {result3['success']}, Task ID: {result3['task_id']}")
    
    # Get updated status
    print("\n5. Final system status...")
    final_status = gemmolt.get_status()
    print(f"   - Total tasks executed: {final_status['tasks']['total_tasks']}")
    print(f"   - Tasks completed: {final_status['tasks']['completed']}")
    print(f"   - Tasks failed: {final_status['tasks']['failed']}")
    print(f"   - Uptime: {final_status['uptime_seconds']:.2f} seconds")
    
    # Stop GemMolt
    print("\n6. Stopping GemMolt...")
    gemmolt.stop()
    
    print("\n=== Example Complete ===")

if __name__ == "__main__":
    main()
