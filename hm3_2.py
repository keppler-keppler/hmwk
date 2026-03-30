import numpy as np
import matplotlib.pyplot as plt

m = 1.0        # Mass in kg
R = 0.05       # Radius in m
l = 1.0        # Length in m
g = 9.81       # Gravity in m/s^2

mu1 = 0.560    # Pa-s
mu2 = 0.200    # Pa-s

omega_n = np.sqrt(g / l)

gamma1 = (3 * np.pi * mu1 * R) / m
gamma2 = (3 * np.pi * mu2 * R) / m

omega_d1 = np.sqrt(omega_n**2 - gamma1**2)
omega_d2 = np.sqrt(omega_n**2 - gamma2**2)

t = np.linspace(0, 25, 1000)

v0 = 1.0 / (m * l)

phi1 = (v0 / omega_d1) * np.exp(-gamma1 * t) * np.sin(omega_d1 * t)
phi2 = (v0 / omega_d2) * np.exp(-gamma2 * t) * np.sin(omega_d2 * t)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(t, phi1, 'b-', linewidth=2, label=r'$\mu = 560$ mPa-s')
axes[0].set_title(r'Pendulum Motion ($\mu = 560$ mPa-s)', fontsize=14)
axes[0].set_xlabel('Time (s)', fontsize=12)
axes[0].set_ylabel(r'Angle $\phi$ (rad)', fontsize=12)
axes[0].grid(True)
axes[0].legend(fontsize=12)
axes[0].set_ylim(-0.25, 0.35) # Fixed y-axis scale for direct visual comparison

axes[1].plot(t, phi2, 'r-', linewidth=2, label=r'$\mu = 200$ mPa-s')
axes[1].set_title(r'Pendulum Motion ($\mu = 200$ mPa-s)', fontsize=14)
axes[1].set_xlabel('Time (s)', fontsize=12)
axes[1].set_ylabel(r'Angle $\phi$ (rad)', fontsize=12)
axes[1].grid(True)
axes[1].legend(fontsize=12)
axes[1].set_ylim(-0.25, 0.35) # Fixed y-axis scale for direct visual comparison

plt.tight_layout()
plt.savefig('damped_pendulum.png', dpi=300)
