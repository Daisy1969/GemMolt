"""
Command Line Interface for GemMolt

Provides CLI access to GemMolt functionality.
"""

import sys
import argparse
import logging
from typing import Dict, Any

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

from gemmolt import GemMolt


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    if not HAS_YAML:
        print("Warning: PyYAML not installed, using default config")
        return {}
    
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
        return {}
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}


def setup_logging(level: str = "INFO") -> None:
    """
    Setup logging configuration.
    
    Args:
        level: Logging level
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def cmd_start(args) -> int:
    """Start GemMolt in interactive mode."""
    setup_logging(getattr(args, 'log_level', 'INFO'))
    
    config = {'security': {'use_gcp': False}}  # Default to no GCP for CLI
    if args.config:
        config = load_config(args.config)
    
    print("Starting GemMolt...")
    gemmolt = GemMolt(config)
    
    try:
        gemmolt.start()
        print("GemMolt started successfully!")
        print("Press Ctrl+C to stop")
        
        # Keep running until interrupted
        import time
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping GemMolt...")
        gemmolt.stop()
        print("GemMolt stopped.")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


def cmd_status(args) -> int:
    """Get GemMolt status."""
    setup_logging(getattr(args, 'log_level', 'INFO'))
    
    config = {'security': {'use_gcp': False}}  # Default to no GCP for CLI
    if args.config:
        config = load_config(args.config)
    
    gemmolt = GemMolt(config)
    gemmolt.start()
    
    try:
        status = gemmolt.get_status()
        
        print("\n=== GemMolt Status ===")
        print(f"Running: {status['running']}")
        print(f"Uptime: {status['uptime_seconds']:.2f} seconds")
        print(f"\nSecurity:")
        print(f"  - Authenticated: {status['security']['authenticated']}")
        print(f"  - GCP Enabled: {status['security']['gcp_enabled']}")
        print(f"\nTasks:")
        print(f"  - Total: {status['tasks']['total_tasks']}")
        print(f"  - Completed: {status['tasks']['completed']}")
        print(f"  - Failed: {status['tasks']['failed']}")
        print(f"\nMonitoring:")
        print(f"  - Active: {status['monitoring']['active']}")
        print(f"  - Events: {status['monitoring']['total_events']}")
        
        gemmolt.stop()
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


def cmd_task(args) -> int:
    """Execute a task."""
    setup_logging(getattr(args, 'log_level', 'INFO'))
    
    config = {'security': {'use_gcp': False}}  # Default to no GCP for CLI
    if args.config:
        config = load_config(args.config)
    
    gemmolt = GemMolt(config)
    gemmolt.start()
    
    try:
        print(f"Executing task: {args.description}")
        result = gemmolt.execute_task(args.description)
        
        if result['success']:
            print(f"\n✓ Task completed successfully")
            print(f"Task ID: {result['task_id']}")
        else:
            print(f"\n✗ Task failed")
            print(f"Error: {result.get('error', 'Unknown error')}")
        
        gemmolt.stop()
        return 0 if result['success'] else 1
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


def cmd_version(args) -> int:
    """Show version information."""
    from gemmolt import __version__
    print(f"GemMolt version {__version__}")
    return 0


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='GemMolt - Master Coding and Manager Assistant',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--config', '-c',
        help='Path to configuration file'
    )
    parser.add_argument(
        '--log-level', '-l',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO',
        help='Logging level (default: INFO)'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Start command
    parser_start = subparsers.add_parser('start', help='Start GemMolt')
    parser_start.set_defaults(func=cmd_start)
    
    # Status command
    parser_status = subparsers.add_parser('status', help='Get system status')
    parser_status.set_defaults(func=cmd_status)
    
    # Task command
    parser_task = subparsers.add_parser('task', help='Execute a task')
    parser_task.add_argument('description', help='Task description')
    parser_task.set_defaults(func=cmd_task)
    
    # Version command
    parser_version = subparsers.add_parser('version', help='Show version')
    parser_version.set_defaults(func=cmd_version)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
