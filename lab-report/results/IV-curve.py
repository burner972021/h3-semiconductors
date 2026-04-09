import numpy as np
import matplotlib.pyplot as plt

# --- Original Diode Parameters ---
m = (0.176 - 0.059) / (1.0 - 0.8)  # 0.585
b = 0.059 - m * 0.8                # -0.409
v_on_intercept = -b / m            # ~0.699

# --- Heated Diode Parameters (Von=0.6, Point=(0.9, 0.150)) ---
m_h = (0.150 - 0) / (0.9 - 0.6)    # 0.5
b_h = 0.150 - m_h * 0.9            # -0.3
v_on_h = 0.6

# Functions
def linear_region(v): return m * v + b
def transition_region(v): return (0.059 / (0.8 - 0.6)**2) * (v - 0.6)**2

def linear_region_h(v): return m_h * v + b_h
def transition_heated(v): return (linear_region_h(0.7) / (0.7 - 0.5)**2) * (v - 0.5)**2

# Generate Plotting Data
v_plot = np.linspace(0, 1.3, 500)
i_plot = np.where(v_plot < 0.6, 0, 
         np.where(v_plot < 0.8, transition_region(v_plot), 
         linear_region(v_plot)))

i_heated = np.where(v_plot < 0.5, 0, 
           np.where(v_plot < 0.7, transition_heated(v_plot), 
           linear_region_h(v_plot)))

# Visualization
plt.figure(figsize=(7, 5))
plt.axhline(0, color='black', lw=1.5)
plt.axvline(0, color='black', lw=1.5)

# Original Plot & Extrapolation
plt.plot(v_plot, i_plot, 'b-', linewidth=1.5, label='Room temperature')
v_extrap = np.linspace(v_on_intercept - 0.05, 1.1, 100)
plt.plot(v_extrap, linear_region(v_extrap), 'b-', alpha=0.3)

# Heated Plot & Extrapolation
plt.plot(v_plot, i_heated, 'm-', linewidth=1.5, label='Heated')
v_extrap_h = np.linspace(v_on_h - 0.05, 1.1, 100)
plt.plot(v_extrap_h, linear_region_h(v_extrap_h), 'm-', alpha=0.3)

# Markers
plt.scatter([0.6, 0.8, 1.0], [0, 0.059, 0.176], marker='x', s=75, color='red', label='Data Points')
plt.scatter([0.5, 0.9], [0, 0.150], marker='x', s=75, color='red')

# Turn-on Voltage lines
plt.axvline(x=v_on_intercept, color='red', linestyle='--', alpha=0.4, label='Turn-on Voltage')
plt.axvline(x=v_on_h, color='magenta', linestyle='--', alpha=0.4)

# Original Annotation
plt.annotate(f'$V_{{on}}$: {v_on_intercept:.3f} V',
             xy=(v_on_intercept, 0),             
             xytext=(v_on_intercept + 0.1, 0.02),
             arrowprops=dict(arrowstyle='->', color='blue'),
             fontsize=11, color='blue', fontweight='bold')

# Heated Annotation
plt.annotate(f'$V_{{heated}}$: {v_on_h:.1f} V',
             xy=(v_on_h, 0),             
             xytext=(v_on_h - 0.3, 0.06),
             arrowprops=dict(arrowstyle='->', color='magenta'),
             fontsize=11, color='magenta', fontweight='bold')

# Formatting
plt.title('I-V curve of diode', fontsize=14)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.xlim(-0.1, 1.4)
plt.ylim(-0.01, 0.25)

plt.tight_layout()
plt.savefig('iv-sketch.pdf', dpi=300)
plt.show()