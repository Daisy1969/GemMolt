"""
Example: GemMolt with GCP Integration

Demonstrates GemMolt with actual GCP integration for production use.
"""

import logging
from gemmolt import GemMolt, SecurityManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """Run GemMolt with GCP integration example."""
    print("=== GemMolt GCP Integration Example ===\n")
    
    # Configuration with GCP enabled
    config = {
        'security': {
            'gcp_project_id': 'your-actual-gcp-project-id',  # Replace with your GCP project ID
            'use_gcp': True
        },
        'tasks': {
            'max_history': 100
        },
        'monitoring': {
            'max_history': 1000
        }
    }
    
    print("Note: This example requires actual GCP credentials and project setup.")
    print("Please ensure you have:")
    print("  - Created a GCP project")
    print("  - Enabled Secret Manager and IAM APIs")
    print("  - Set up authentication (gcloud auth application-default login)")
    print()
    
    try:
        # Initialize GemMolt
        print("1. Initializing GemMolt with GCP...")
        gemmolt = GemMolt(config)
        
        # Start GemMolt (will authenticate with GCP)
        print("2. Starting GemMolt and authenticating with GCP...")
        gemmolt.start()
        
        # Demonstrate secret management
        print("\n3. Testing GCP Secret Manager integration...")
        security_manager = gemmolt.security_manager
        
        # Store a secret
        print("   a) Storing a secret...")
        success = security_manager.store_secret("api_key", "secret_api_key_value_12345")
        print(f"      Secret stored: {success}")
        
        # Retrieve the secret
        print("   b) Retrieving the secret...")
        secret_value = security_manager.get_secret("api_key")
        print(f"      Secret retrieved: {secret_value is not None}")
        
        # Execute secure task
        print("\n4. Executing secure task with GCP authentication...")
        result = gemmolt.execute_task(
            "Process sensitive data with encryption",
            context={"security_level": "high"}
        )
        print(f"   Task result: {result['success']}")
        
        # Get status
        print("\n5. System status...")
        status = gemmolt.get_status()
        print(f"   - GCP Authenticated: {status['security']['authenticated']}")
        print(f"   - GCP Project: {status['security']['project_id']}")
        
        # Stop GemMolt
        print("\n6. Stopping GemMolt...")
        gemmolt.stop()
        
        print("\n=== Example Complete ===")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nPlease ensure GCP is properly configured:")
        print("  1. Set GEMMOLT_GCP_PROJECT_ID environment variable")
        print("  2. Run: gcloud auth application-default login")
        print("  3. Enable required APIs in your GCP project")

if __name__ == "__main__":
    main()
