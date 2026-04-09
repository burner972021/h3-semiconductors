import numpy as np
import matplotlib.pyplot as plt


I0 = 1.01e-8   # Reverse saturation current
n = 1.82     # Ideality factor
Vt = 0.0252 # Thermal voltage at room temp

def shockley(V, I0, n):
    return I0 * (np.exp(V / (n * Vt)) - 1)

v_shift = 0.062 

v_plot = np.linspace(0, 1.2, 500)
i_curve_rtp = shockley(v_plot, I0, n)

# --- Original Diode Parameters ---
m = (0.176 - 0.059) / (1.0 - 0.8)  # 0.585
b = 0.059 - m * 0.8                # -0.409
v_on_intercept = -b / m            # ~0.699

# Functions
def linear_region(v): return m * v + b
def transition_region(v): return (0.059 / (0.8 - 0.6)**2) * (v - 0.6)**2

# Generate Plotting Data
v_plot = np.linspace(0, 1.4, 500)
i_plot = np.where(v_plot < 0.6, 0, 
         np.where(v_plot < 0.8, transition_region(v_plot), 
         linear_region(v_plot)))

# Visualization
plt.figure(figsize=(7, 5))
plt.axhline(0, color='black', lw=1.5)
plt.axvline(0, color='black', lw=1.5)

plt.plot(v_plot, i_curve_rtp, 'r-', lw=1.5, label=f'Ideal diode curve')
plt.axhline(0, color='black', lw=1.5)
plt.axvline(0, color='black', lw=1.5)

# Original Plot & Extrapolation
plt.plot(v_plot, i_plot, 'b-', linewidth=1.5, label='Room temperature')
# v_extrap = np.linspace(v_on_intercept - 0.05, 1.1, 100)
# plt.plot(v_extrap, linear_region(v_extrap), 'b-', alpha=0.3)

plt.scatter([0.6, 0.8, 1.0], [0, 0.059, 0.176], marker='x', s=75, color='red', label='Data Points')

# Turn-on Voltage lines
# plt.axvline(x=v_on_intercept, color='red', linestyle='--', alpha=0.4, label='Turn-on Voltage')
# # Original Annotation
# plt.annotate(f'$V_{{on}}$: {v_on_intercept:.3f} V',
#              xy=(v_on_intercept, 0),             
#              xytext=(v_on_intercept + 0.1, 0.02),
#              arrowprops=dict(arrowstyle='->', color='blue'),
#              fontsize=11, color='blue', fontweight='bold')

plt.title('Ideal diode versus measured diode', fontsize=14)
plt.xlabel('Voltage $V$ (V)', fontsize=12)
plt.ylabel('Current $I$ (mA)', fontsize=12)
plt.xlim(0.2, 1.4)
plt.ylim(-0.01, 0.25)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('ideal-iv.pdf', dpi=300)
plt.show()