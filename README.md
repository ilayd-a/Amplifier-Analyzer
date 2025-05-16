# Amplifier-Analyzer

## 🔍 Overview

This repository contains Python scripts and supplemental documents for analyzing and verifying the design of **BJT** and **FET** single-stage amplifiers. These projects were developed as part of NYU Tandon's *ECE3114 Fundamentals of Electronics I* course, covering both theoretical hand calculations and automated validation of design parameters.

## 📁 Directory Structure

<pre>
Amplifier-Analyzer/
├── Project_3/                         # BJT Common-Emitter Amplifier
│   ├── bjt_amplifier.py            # Python script for amplifier analysis
│   └── ECE3114 Project 3 BJT Amplifier Spring 2025.pdf   # Official project description and specs
│
├── Project_4/                         # FET Common-Gate Amplifier
│   ├── commonGateFET.py            # Python script for amplifier analysis
│   └── ECE3114 Extra Credit Design Project 4 FET Common Gate Amplifier Spring 2025.pdf   # Official project description and specs
│
├── LICENSE
└── README.md
</pre>

## 🧪 What These Scripts Do

Each Python script:
- Calculates bias points: \( I_C, V_{CE}, I_D, V_{DS}, etc. \)
- Computes and validates small-signal gain
- Checks for:
  - **Forward-active region** (for BJT)
  - **Saturation region** (for FET)
  - DC & AC stability
  - Power dissipation limits
- Reports whether each key specification is **passed** or **failed**

## ⚙️ Specifications
### 🔧 Project 3 – BJT Amplifier
- Transistor: 2N3904 (β = 150, V<sub>CE,sat</sub> = 0.3 V)
- Single +V<sub>CC</sub> power supply ≤ 50 V
- Resistor-only DC biasing
- Capacitors = large (1 F for PSpice)
- Load resistor: RL = 800 Ω + last two digits of student ID
- Target gain: 15 ± 5%
- Max transistor power dissipation: 200 mW

### 🔧 Project 4 – FET Amplifier
- Transistor: IRF840 NMOS (k<sub>n</sub> = 6.5 A/V², V<sub>TN</sub> = 3.85 V)
- Dual ±V<sub>DD</sub> supply (≤ 50 V)
- Load resistor: RL = last two digits of student ID (min 20 Ω)
- Target gain: 10 ± 10%
- Max transistor power dissipation: 12.5 W
- All resistors ≤ 500 kΩ
- Capacitors = large

## 🚀 How to Run

1. Open either `bjt_amplifier.py` or `commonGateFET.py` in your preferred IDE.
2. Fill in the appropriate values for resistors, supply voltages, and student ID–based RL.
3. Run the script:
   ```bash
   python bjt_amplifier.py
   # or
   python commonGateFET.py
Read the printed output to verify if your design meets course requirements.

✅ Example Output (BJT Script)
```
      Vth = 3.29 Rth = 4935.48
      I_C = 0.0095 A, I_E = 0.00957 A, I_B = 6.33e-05 A
      V_ce = 2.59 V, V_ce_sat = 0.3 V
      PASSED: V_ce > V_ce_sat: BJT is forward active
      P_D = 0.0246 W
      PASSED: P_D < 0.2W: power satisfied
      PASSED: DC Stability achieved
      PASSED: AC Stability achieved
      r_pi = 410.77, beta*(R_E_unbypassed) = 4500.0
      V_in_prime: 4880.77
      V_out = -10341.17, V_in = 5375.25, A_v = -1.92
      FAILED: A_v outside of acceptable range
      A_V = -1.92
```
