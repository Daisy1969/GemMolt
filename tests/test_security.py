"""
Tests for Security Manager
"""

import pytest
from gemmolt.security import SecurityManager


def test_security_manager_initialization():
    """Test SecurityManager initialization."""
    config = {
        'gcp_project_id': 'test-project',
        'use_gcp': False
    }
    
    manager = SecurityManager(config)
    
    assert manager is not None
    assert manager.gcp_project_id == 'test-project'
    assert manager.use_gcp is False
    assert manager.authenticated is False


def test_security_manager_authenticate_no_gcp():
    """Test authentication with GCP disabled."""
    config = {'use_gcp': False}
    manager = SecurityManager(config)
    
    result = manager.authenticate()
    
    assert result is True
    assert manager.authenticated is True


def test_security_manager_authenticate_with_gcp():
    """Test authentication with GCP enabled (simulated)."""
    config = {
        'gcp_project_id': 'test-project',
        'use_gcp': True
    }
    manager = SecurityManager(config)
    
    result = manager.authenticate()
    
    assert result is True
    assert manager.authenticated is True


def test_security_manager_verify_permissions():
    """Test permission verification."""
    config = {'use_gcp': False}
    manager = SecurityManager(config)
    
    # Should fail when not authenticated
    result = manager.verify_permissions("test task")
    assert result is False
    
    # Should succeed after authentication
    manager.authenticate()
    result = manager.verify_permissions("test task")
    assert result is True


def test_security_manager_get_secret():
    """Test secret retrieval."""
    config = {'use_gcp': False}
    manager = SecurityManager(config)
    manager.authenticate()
    
    secret = manager.get_secret("test_secret")
    
    assert secret is not None
    assert "secret_value_for_test_secret" in secret


def test_security_manager_store_secret():
    """Test secret storage."""
    config = {'use_gcp': False}
    manager = SecurityManager(config)
    manager.authenticate()
    
    result = manager.store_secret("test_secret", "test_value")
    
    assert result is True


def test_security_manager_get_status():
    """Test getting security manager status."""
    config = {
        'gcp_project_id': 'test-project',
        'use_gcp': False
    }
    manager = SecurityManager(config)
    manager.authenticate()
    
    status = manager.get_status()
    
    assert status is not None
    assert 'authenticated' in status
    assert 'gcp_enabled' in status
    assert 'project_id' in status
    assert status['authenticated'] is True
