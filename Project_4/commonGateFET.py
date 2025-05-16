import math

# --- CONSTANTS ---
V_G = 0                      # Gate voltage (for common-gate configuration, usually grounded)
V_TN = 3.85                  # Threshold voltage for NMOS
k_N = 6.5                    # Process transconductance parameter (in mA/V^2)
R_L = # Enter the last two digits of your Net ID (in ohms)
R_G = 10000                 # Gate resistance (often high to avoid loading the circuit)

# --- MAIN FUNCTION ---
def common_gate_fet_amplifier_calculator():
    # --- INPUT PARAMETERS ---
    R_D = # Drain resistor, must be < 500kΩ
    R_S = # Source resistor, must be < 500kΩ
    V_DD = # Supply voltage, must be < 50V

    # --- QUADRATIC FORMULA SETUP FOR CURRENT SOLVING ---
    # The quadratic form solves for I_D using the equation derived from:
    # I_D = (k_N / 2) * (V_GS - V_TN)^2, and V_GS = V_G - V_S = V_G - I_D*R_S
    beta = (k_N * R_S * (V_DD - V_TN) + 1)
    alpha = (R_S**2 * k_N) / 2
    omega = (k_N / 2) * ((V_DD - V_TN) ** 2)

    # Solving the quadratic equation for I_D
    I_D = (beta - math.sqrt(beta**2 - 4 * alpha * omega)) / (2 * alpha)

    # --- VOLTAGE CALCULATIONS ---
    V_S = I_D * R_S - V_DD               # Source voltage (relative to ground)
    V_D = V_DD - I_D * R_D               # Drain voltage
    V_GS = V_G - V_S                     # Gate-Source voltage
    V_DS = V_D - V_S                     # Drain-Source voltage

    # --- PRINT BASIC INFO ---
    print("V_D: ", V_D)

    # --- OPERATING REGION CHECKS ---
    V_DS_SAT = V_GS - V_TN               # Minimum V_DS needed for saturation
    P_D = V_DS * I_D                     # Power dissipated by FET
    g_m = math.sqrt(2 * k_N * I_D)       # Transconductance (small-signal)

    # Check if FET is turned on
    if V_GS < V_TN:
        print("FAILED: V_GS < V_TN: FET not on")
    else:
        print("PASSED: V_GS >= V_TN: FET is on")

    # Check if FET is in saturation region
    if V_DS < V_DS_SAT:
        print("FAILED: V_DS < V_DS_SAT: FET not saturated")
    else:
        print("PASSED: V_DS > V_DS_SAT: FET is saturated")

    # Check power dissipation
    if P_D < 12.5:
        print("PASSED: P_D < 12.5W: power satisfied")
    else:
        print("FAILED: P_D > 12.5W: too much power")

    # --- VOLTAGE GAIN CALCULATION ---
    A_V = g_m * ((R_L * R_D) / (R_L + R_D))  # Voltage gain: g_m * (R_D || R_L)

    # Check if gain is within target range (~10V/V ±10%)
    if 10 * 0.9 <= A_V <= 10 * 1.1:
        print("PASSED: A_V within acceptable range")
        print("A_V = ", A_V)
    else:
        print("FAILED: A_V outside of acceptable range")

    # --- PRINT MARGIN FOR SATURATION (V_OV or overdrive voltage) ---
    print(2 * (V_GS - V_TN))  # Useful for hand-calculations or g_m formula derivation

# --- RUN FUNCTION ---
common_gate_fet_amplifier_calculator()
