# -*- coding: utf-8 -*-
"""Heat Sink Thermal Resistance Calculator
This script calculates the thermal resistance requirement for a heat sink
used to dissipate heat from power electronics (voltage regulators, power
amplifiers, power-switching circuits etc.).

Thermal management typically involves passive cooling (conducting the heat to a
heatsink or to the metal case of a device) and active cooling (forced air or 
pumped liquid).

Thermal resistance (Rtheta) = heat rise (C)/power transferred (W)

Example: Power supply linear regulator heat sink
         Power supply (unregulated 8 V, 1 A (full load))
         LM317 linear regulator (4.7 V drop, 1A = 4.7W)
            - Rjc = 4 celcius/W (junction to case)
            - Rcs = 0.5 celcius/W (case to heatsink) T0-220
         Operate up to 50 degree celcius ambient
         Junction temp = 100 degrees C << max. temp 150 degrees C

         Rja = (Tj - Ta)/P = 10.64 degree C/W
         Rsa = Rja - Rjc - Rcs = 6.14 degree C/W

# NOTE: use thermocouple/thermistor or infrared temperature probe to verify
# calculations

"""

print("-- Heat Sink Thermal Resistance Calculator -- ")
temp_junction = float(input("Enter operating junction temperature (\u00b0C): "))
temp_ambient = float(input("Enter max. ambient operating temperature (\u00b0C): "))
voltage_drop = float(input("Enter voltage drop across junction (V): "))
current = float(input("Enter current at full load (A): "))
power_dissipated = voltage_drop * current

R_junction_case = float(input("Enter specified junction to case thermal resistance (\u00b0C/W): "))
R_case_sink = float(input("Enter specified case to heatsink thermal resistance (\u00b0C/W): "))

print("-- Results -- ")
# Calculate required thermal resistance between junction and ambient
# Tj = Ta + (Rjc + Rcs + Rsa)P
# Rja = (Rjc + Rcs + Rsa) = (Tj - Ta)*P
R_junction_ambient = (temp_junction - temp_ambient)/power_dissipated
print("Rja = {0:0.2f}".format(R_junction_ambient), "\u00b0C/W")

# Calculate required heatsink thermal resistance given Rjc and Rcs
R_sink_ambient = R_junction_ambient - R_junction_case - R_case_sink
print("Rsa = {0:0.2f}".format(R_sink_ambient), "\u00b0C/W")


