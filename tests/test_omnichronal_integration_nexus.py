# tests/test_omnichronal_integration_nexus.py

import pytest
from datetime import datetime
from omnichronal_integration_nexus import OmnichronalIntegrator

def test_init_with_string():
    integrator = OmnichronalIntegrator("2025-07-20T12:00:00")
    assert integrator.start_time == datetime(2025, 7, 20, 12, 0, 0)

def test_init_with_datetime():
    dt = datetime(2025, 7, 20, 12, 0, 0)
    integrator = OmnichronalIntegrator(dt)
    assert integrator.start_time == dt

def test_integrate_forward():
    integrator = OmnichronalIntegrator("2025-07-20T12:00:00")
    result = integrator.integrate_forward(3600)  # 1 hour
    assert result == datetime(2025, 7, 20, 13, 0, 0)

def test_integrate_backward():
    integrator = OmnichronalIntegrator("2025-07-20T12:00:00")
    result = integrator.integrate_backward(1800)  # 30 minutes
    assert result == datetime(2025, 7, 20, 11, 30, 0)

def test_time_difference():
    integrator = OmnichronalIntegrator("2025-07-20T12:00:00")
    diff = integrator.time_difference("2025-07-20T13:00:00")
    assert diff == 3600.0

def test_invalid_init():
    with pytest.raises(ValueError):
        OmnichronalIntegrator(12345)  # Invalid input
