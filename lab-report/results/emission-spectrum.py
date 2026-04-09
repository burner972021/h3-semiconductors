import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit

# Data
wavelength = np.array([600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700])  # in nm
intensity = np.array([0.00, 0.01, 0.2, 3.8, 7.6, 7.0, 1.9, 0.1, 0.01, 0.0, 0.0])  # in Volts

# 1. Define the Gaussian (Bell Curve) function
def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu)**2 / (2 * sigma**2))

# 2. Perform the fit
# Initial guesses: [peak value, center wavelength, width guess]
p0 = [max(intensity), wavelength[np.argmax(intensity)], 20]
popt, pcov = curve_fit(gaussian, wavelength, intensity, p0=p0)
a_fit, mu_fit, sigma_fit = popt

# Calculate FWHM (Full Width at Half Maximum)
fwhm = 2 * np.sqrt(2 * np.log(2)) * sigma_fit

# 3. Create a smooth x-axis for plotting the fit curve
w_smooth = np.linspace(min(wavelength), max(wavelength), 200)
i_smooth = gaussian(w_smooth, *popt)

plt.figure(figsize=(7, 5))

# Plot raw data as points
plt.scatter(wavelength, intensity, color='red', marker='x', label='Measured Data', zorder=5)

# Plot the best fit line
plt.plot(w_smooth, i_smooth, 'b-', linewidth=1.5)

# Label the peak wavelength
plt.axvline(mu_fit, color='gray', linestyle='--', alpha=0.6)

# plt.text(mu_fit + 10, a_fit * 0.9, f'Peak: {mu_fit:.1f} nm', fontsize=10, color='blue', fontweight='bold')
plt.annotate(f'Peak: {mu_fit:.1f} nm',
             xy=(mu_fit, a_fit),
             xytext=(mu_fit + 10, a_fit * 0.9),
             arrowprops=dict(arrowstyle='->', color='blue'),
             fontsize=11, color='blue', fontweight='bold')

fwhm = 2 * np.sqrt(2 * np.log(2)) * sigma_fit
half_max = a_fit / 2
x1 = mu_fit - (fwhm / 2)
x2 = mu_fit + (fwhm / 2)

plt.hlines(y=half_max, xmin=x1, xmax=x2, color='blue', linestyle='-', linewidth=2, alpha=0.4)
# Add label for FWHM
plt.text(mu_fit, half_max - 0.5, f'FWHM: {fwhm:.1f} nm', 
         color='red', fontsize=10, fontweight='bold', ha='center', va='top')

plt.title('Emission Spectrum of LED')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (mV)')
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig('emission_spectrum.pdf', dpi=300)  # Uncomment to save the image
plt.show()