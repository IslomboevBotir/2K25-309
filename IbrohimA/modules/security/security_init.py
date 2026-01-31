"""
Security Module Package
"""

from modules.security.security_devices import SecurityCamera

try:
    from modules.security.security_system import SecuritySystem
except:
    # SecuritySystem is defined in __init__.py
    pass

__all__ = ['SecurityCamera']
