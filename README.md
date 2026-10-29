# Unified Multi-Physics Cross-Domain Simulation Suite

**Automated Verification and Cross-Parameter Sweep Pipeline for Tokamak Reactor Archiving**  
*Targeted for publication in **Fusion Engineering and Design** (Elsevier) under the Traditional No-Fee Subscription Publishing Model*

**Author:** Jacob James Rasmussen (ORCID: 0009-0009-7084-6523)  
**Affiliation:** Independent Researcher, Shell Lake, WI / Incoming CVTC STEM Scholar  

---

## Executive Overview

The **Master Cross-Domain Fusion Simulation Suite** delivers an open-science, production-ready computational verification pipeline coupling five primary physical domains across high-field tokamak fusion power plants (B0 >= 10 T, Ip >= 8 MA):

1. **Phase 1: Core Equilibrium Magnetics & Transport** — Grad-Shafranov equilibrium solvers and 1D transport codes outputting magnetic flux surfaces and parallel heat flux q_parallel.
2. **Phase 2: PFC Hydrodynamics & Liquid CPS (Paper I)** — Taylor-Couette stability (Ta <= 45.8), Young-Laplace capillary retention Delta P_cap, Carman-Kozeny hydraulic permeability collapse K(dpa), and critical dryout heat flux q''_dryout.
3. **Phase 3: Liquid Metal Blanket MHD (Paper IV)** — 3D Navier-Stokes-Maxwell liquid lead-lithium (Pb-17Li) flows at Ha ~ 10^4 (benchmark Ha = 500), Hartmann boundary layer thinning delta_H = 0.20 mm, MHD pressure drop dP/dz = 0.45 MPa/m, and Shercliff side-wall jets U_jet = 15 U0.
4. **Phase 4: Transient Disruptions & REBCO Magnet Protection (Paper II)** — Unmitigated halo current quenches (I_halo = 1.8 MA) coupled to non-insulated (NI) REBCO tape stacks with turn-to-turn contact resistivity rho_ct = 15.0 uOhm.cm2, characteristic time constant tau_L/R = 1.0-3.0 s, and peak hotspot T_max <= 200 K.
5. **Phase 5: Vacuum Vessel Structural Yield & Reserves (Paper III)** — Inconel 718 keyway shear pins under asymmetric n=1 halo forces (DAF = 1.85) evaluated via the 3D anisotropic Tsai-Wu failure criterion f_TW = 0.244 <= 1.0, establishing a Strength Reserve Ratio SRR = 1.61.

---

## Repository Directory Structure

```
fusion-cross-domain-simulation-suite/
├── LICENSE                        # MIT License
├── README.md                      # Comprehensive landing page & quickstart
├── CITATION.cff                   # Citation File Format (ORCID: 0009-0009-7084-6523)
├── requirements.txt               # Python dependencies
├── docs/
│   ├── Master_Verification_Manual.pdf   # Technical manual detailing cross-domain coupling
│   ├── Validation_Protocol.pdf          # Out-of-distribution stability & grid convergence
│   └── Highlights.pdf                   # Core research submission highlights
├── src/
│   ├── __init__.py
│   ├── cross_domain_orchestrator.py     # Master execution script running 5-phase handshakes
│   ├── thermal_cps_validator.py         # Validates Paper I Taylor-Couette & CPS dryout
│   ├── rebco_magnet_validator.py        # Validates Paper II REBCO strain Jc & NI coil L/R
│   ├── structural_tsaiwu_validator.py   # Validates Paper III 3D Tsai-Wu yield f_TW <= 1.0
│   └── mhd_channel_validator.py         # Validates Paper IV Hartmann Ha=500 & dP/dz=0.45 MPa/m
├── data/
│   ├── cross_domain_sweep_matrix.csv    # Unified multi-parameter verification dataset
│   └── master_system_verification.json  # Global convergence status & residual tolerances (< 0.1%)
├── figures/
│   ├── cross_domain_pipeline_300dpi.png # Master flowchart (300 DPI)
│   └── cross_domain_pipeline_vector.svg # Scalable vector graphic flowchart
└── .github/workflows/
    └── python-test.yml            # CI/CD test runner executing verification on push
```

---

## Quickstart Execution Guide

### 1. Environment Setup
```bash
cd fusion-cross-domain-simulation-suite
pip install -r requirements.txt
```

### 2. Running the Full Cross-Domain Verification Pipeline
```bash
python -m src.cross_domain_orchestrator
```

**Expected Verification Output:**
```
================================================================================
MASTER CROSS-DOMAIN FUSION SIMULATION SUITE - VERIFICATION ORCHESTRATOR
Target Journal: Fusion Engineering and Design (Elsevier)
Author: Jacob James Rasmussen (ORCID: 0009-0009-7084-6523)
================================================================================
Global Convergence Status : CONVERGED
Max Residual Error        : 0.0150% (< 0.1% target)
Roache GCI Index          : 0.42% (<= 0.50% target)
================================================================================
```

---

## Cross-Domain Verification Sweep Matrix

| Operational State | Fluence (dpa) | Pore Radius r_p (um) | Capillary Press Delta P_cap (kPa) | Permeability K (10^-11 m^2) | Critical Dryout q''_dryout (MW/m^2) | Safety Factor (SF) | REBCO J_c/J_c0 | Tsai-Wu f_TW | Reserve Ratio SRR | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Pristine State** | `0.0` | `25.00` | `27.05` | `1.25` | `41.50` | **`2.77`** | `1.0000` | `0.244` | `1.61` | Baseline Optimal |
| **Replacement Limit** | `9.8` | `17.54` | `38.55` | `0.60` | `22.50` | **`1.50`** | `0.9996` | `0.244` | `1.61` | Mandatory Replacement |
| **Dryout Parity** | `13.0` | `16.49` | `41.00` | `0.50` | `15.00` | **`1.00`** | `0.9995` | `0.244` | `1.61` | Thermal Dryout Limit |
| **Extreme Damage** | `20.0` | `15.20` | `44.48` | `0.38` | `8.69` | **`0.58`** | `0.9838` | `0.244` | `1.61` | Sub-critical Failure |

---

## Academic Citation & Licensing

This suite is published under the **MIT License**. If you utilize these computational tools or verification matrices in academic work, please cite:

```bibtex
@article{rasmussen2026fusion,
  author    = {Jacob James Rasmussen},
  title     = {Unified Multi-Physics Cross-Domain Simulation Suite: Automated Verification and Cross-Parameter Sweep Pipeline for Tokamak Reactor Archiving},
  journal   = {Fusion Engineering and Design},
  publisher = {Elsevier},
  year      = {2026},
  note      = {Traditional No-Fee Subscription Publishing Model}
}
```
