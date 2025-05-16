# Constants
beta = 150                     # DC current gain of the BJT
V_ce_sat = 0.3                 # Collector-Emitter saturation voltage
R_L = # enter your Net ID value for R_L here

# Main function to perform common-emitter amplifier calculations
def common_source_bjt_amplifier_calculator():
    # --- INPUT SECTION (USER-DEFINED PARAMETERS) ---
    Vdd = # supply voltage; must be between 0 and 50 V
    R1 = # resistor R1 in voltage divider; must be < 500kΩ
    R2 = # resistor R2 in voltage divider; must be < 500kΩ
    R_C = # collector resistor; must be < 500kΩ
    R_E_unbypassed = # emitter resistor not bypassed by a capacitor; < 500kΩ
    R_E_bypassed = # emitter resistor bypassed by a capacitor; < 500kΩ

    # --- BIASING CALCULATIONS ---
    Rth = (R1 * R2) / (R1 + R2)                      # Thevenin equivalent resistance of the bias network
    Vth = Vdd * (R2 / (R1 + R2))                     # Thevenin equivalent voltage of the bias network
    print("Vth = ", Vth, "Rth = ", Rth)

    # Calculate base current (I_B), emitter current (I_E), and collector current (I_C)
    I_B = (Vth - 0.7) / (Rth + (R_E_bypassed + R_E_unbypassed) * (beta + 1))  # Assuming V_BE = 0.7V
    I_E = (beta + 1) * I_B
    I_C = beta * I_B
    print("I_C = ", I_C, "I_E = ", I_E, "I_B = ", I_B)

    # --- CHECK FOR FORWARD ACTIVE REGION ---
    V_ce = (-Vdd + R_C * I_C + (R_E_unbypassed + R_E_bypassed) * I_E) * -1  # V_CE calculation
    print("V_ce = ", V_ce, "V_ce_sat = ", V_ce_sat)

    if V_ce < V_ce_sat:
        print("FAILED: V_ce < V_ce_sat: BJT not forward active")
    else:
        print("PASSED: V_ce > V_ce_sat: BJT is forward active")

    # --- POWER DISSIPATION CHECK ---
    P_D = V_ce * I_C  # Power dissipated by the transistor
    print("P_D = ", P_D)
    if P_D > 0.2:
        print("FAILED: P_D > 0.2W: too much power")
    else:
        print("PASSED: P_D < 0.2W: power satisfied")

    # --- STABILITY CHECKS ---
    r_pi = beta * (0.026) / I_C  # Small signal input resistance of the base
    # DC stability check: base bias network must dominate emitter resistance
    if (1 + beta) * (R_E_unbypassed + R_E_bypassed) >= Rth * 10 and Vth >= 3:
        print("PASSED: DC Stability achieved")
    else:
        print("FAILED: DC Stability not achieved")

    # AC stability check: r_pi << beta * R_E_unbypassed
    if r_pi * 10 <= beta * R_E_unbypassed:
        print("PASSED: AC Stability achieved")
        print("r_pi =", r_pi, "beta*(R_E_unbypassed) =", beta * R_E_unbypassed)
    else:
        print("FAILED: AC Stability not achieved")
        print("r_pi =", r_pi, "beta*(R_E_unbypassed) =", beta * R_E_unbypassed)

    # --- VOLTAGE GAIN CALCULATION ---
    V_out = -1 * ((R_L * R_C) / (R_L + R_C)) * beta  # Output voltage swing (approximate)
    V_in_prime = r_pi + R_E_unbypassed * (beta + 1)  # Effective input resistance
    V_in = V_in_prime * ((Rth + 50) / Rth)           # Input voltage considering signal source resistance
    print("V_in_prime: ", V_in_prime)

    A_v = V_out / V_in  # Voltage gain
    print("V_out = ", V_out, "V_in = ", V_in, "A_v = ", A_v)

    # --- GAIN VERIFICATION ---
    if abs(A_v) >= 15 * 0.95 and abs(A_v) <= 15 * 1.05:
        print("PASSED: A_v within acceptable range")
        print("A_V = ", A_v)
    else:
        print("FAILED: A_v outside of acceptable range")
        print("A_V = ", A_v)

# Run the function
common_source_bjt_amplifier_calculator()
