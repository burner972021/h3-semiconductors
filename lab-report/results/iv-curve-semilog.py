import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import numpy as np

voltage_log = np.array([0.45, 0.50, 0.55, 0.60, 0.63, 0.65, 0.68])
current_log = np.array([0.01, 0.05, 0.2, 1.0, 3.0, 5.0, 10.0])

# Perform linear regression: ln(I) = slope * V + intercept
slope, intercept = np.polyfit(voltage_log, np.log(current_log), 1)
I_0 = np.exp(intercept)

# Define ranges for the lines
v_fit_range = np.linspace(min(voltage_log), max(voltage_log), 100)
i_fit_range = np.exp(slope * v_fit_range + intercept)

v_extrapolate = np.linspace(0, min(voltage_log), 100)
i_extrapolate = np.exp(slope * v_extrapolate + intercept)

plt.figure(figsize=(7, 5))
plt.semilogy(voltage_log, current_log, 'rs', label='Measured Data', markersize=6)
plt.semilogy(v_fit_range, i_fit_range, 'b-', label='Best Fit Line')
plt.semilogy(v_extrapolate, i_extrapolate, 'b--', alpha=0.7)

plt.plot(0, I_0, 'ro', markersize=8) # Blue dot at the intercept
plt.annotate(f'$I_0 = {I_0:.2e}$ mA', 
             xy=(0, I_0), 
             xytext=(0.1, I_0 * 5),
             arrowprops=dict(arrowstyle='->', color='blue'),
             fontsize=11, color='blue', fontweight='bold')

plt.title('I-V Characteristic of Diode')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.xlim(0, max(voltage_log) + 0.05) # Ensure x-axis starts at 0

ax = plt.gca() # Get current axis
# Set the locator for the minor ticks on the y-axis
ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs='auto', numticks=12))

plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig('iv-curve-semilog.pdf', dpi=300)
plt.show()

print(f"Calculated y-intercept (I_0): {I_0:.4e} mA")