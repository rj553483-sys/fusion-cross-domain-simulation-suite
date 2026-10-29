"""
Unified Cross-Domain Fusion Simulation Suite
Automated Verification and Cross-Parameter Sweep Pipeline for Tokamak Reactor Archiving
Targeted for Fusion Engineering and Design
Author: Jacob James Rasmussen (ORCID: 0009-0009-7084-6523)
"""

__version__ = "1.0.0"
__author__ = "Jacob James Rasmussen"
__email__ = "jrasmussen38@student.cvtc.edu"

from .thermal_cps_validator import validate_thermal_cps
from .rebco_magnet_validator import validate_rebco_magnet
from .structural_tsaiwu_validator import validate_structural_tsaiwu
from .mhd_channel_validator import validate_mhd_channel
from .cross_domain_orchestrator import run_master_orchestrator

__all__ = [
    "validate_thermal_cps",
    "validate_rebco_magnet",
    "validate_structural_tsaiwu",
    "validate_mhd_channel",
    "run_master_orchestrator",
]
