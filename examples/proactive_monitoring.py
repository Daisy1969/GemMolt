"""
Example: Proactive Monitoring

Demonstrates proactive monitoring capabilities of GemMolt.
"""

import logging
import time
from gemmolt import GemMolt
from gemmolt.monitoring import MonitoringEvent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def custom_event_handler(event: MonitoringEvent):
    """Custom handler for monitoring events."""
    print(f"   [EVENT] {event.level.value.upper()}: {event.message}")

def main():
    """Run proactive monitoring example."""
    print("=== GemMolt Proactive Monitoring Example ===\n")
    
    # Configuration
    config = {
        'security': {
            'use_gcp': False
        },
        'monitoring': {
            'max_history': 100
        }
    }
    
    # Initialize and start GemMolt
    print("1. Starting GemMolt...")
    gemmolt = GemMolt(config)
    gemmolt.start()
    
    # Register custom event handler
    print("\n2. Registering custom event handler...")
    gemmolt.proactive_monitor.register_handler(custom_event_handler)
    
    # Demonstrate proactive monitoring
    print("\n3. Monitoring system health...")
    for i in range(3):
        print(f"\n   Check #{i+1}:")
        health = gemmolt.proactive_monitor.check_system_health()
        print(f"   Overall health: {health['overall']}")
        time.sleep(1)
    
    # Get monitoring status
    print("\n4. Monitoring status...")
    mon_status = gemmolt.proactive_monitor.get_status()
    print(f"   - Active: {mon_status['active']}")
    print(f"   - Total events: {mon_status['total_events']}")
    print(f"   - Handlers registered: {mon_status['handlers_registered']}")
    
    # Show event history
    print("\n5. Recent monitoring events:")
    events = gemmolt.proactive_monitor.get_event_history()
    for event in events[-5:]:
        print(f"   - [{event['level']}] {event['message']} at {event['timestamp']}")
    
    # Stop GemMolt
    print("\n6. Stopping GemMolt...")
    gemmolt.stop()
    
    print("\n=== Example Complete ===")

if __name__ == "__main__":
    main()
