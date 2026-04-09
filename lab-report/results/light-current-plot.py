import matplotlib.pyplot as plt
import numpy as np

# Per instructions: Current goes from 0 to 35 mA in steps of 5 mA
led_current = np.array([0, 5, 10, 15, 20, 25, 30, 35])  # in mA
luxmeter_reading = np.array([10, 23, 44, 61, 78, 94, 108, 124]) 

slope, intercept = np.polyfit(led_current, luxmeter_reading, 1)
lux_fit = slope * led_current + intercept

plt.figure(figsize=(8, 6))
plt.plot(led_current, luxmeter_reading, 'rx', label='Measured Data', markersize=8)
plt.plot(led_current, lux_fit, ls='--', color='blue', label='Best Fit Line')
plt.title('Light-Current Characteristic of LED')
plt.xlabel('LED Current (mA)')
plt.ylabel('Luxmeter Reading (Lux)')
plt.grid(True, alpha=0.5)
plt.legend()

plt.tight_layout()
plt.savefig('light_current_curve.pdf', dpi=300)  # Uncomment to save the image
plt.show()