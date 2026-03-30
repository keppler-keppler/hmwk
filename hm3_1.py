import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

m1 = 1.0           
m2 = 4.0           
l = 1.5           
g = 9.81          
w0_vals = [1.3, 2.3]  

x0 = (m1 * l) / (m1 + m2)

t_span = (0, 60)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

def pendulum_ode(t, y, w0, x0, l, g):
    phi = y[0]
    dphi_dt = y[1]
    
    d2phi_dt2 = (x0 * w0**2 / l) * np.cos(w0 * t) - (g / l) * phi
    
    return [dphi_dt, d2phi_dt2]

y0 = [0.0, 0.0]

plt.figure(figsize=(12, 5))

for i, w0 in enumerate(w0_vals):

    sol = solve_ivp(pendulum_ode, t_span, y0, args=(w0, x0, l, g), t_eval=t_eval)
    
    t = sol.t
    phi_t = sol.y[0] 
    
    x_t = x0 * np.cos(w0 * t)
    
    # Plotting
    plt.subplot(1, 2, i + 1)
    plt.plot(t, x_t, 'b-', linewidth=1.5, label='Fulcrum x(t) [m]')
    plt.plot(t, phi_t, 'r--', linewidth=1.5, label='Pendulum $\\phi$(t) [rad]')
    
    plt.title(f'System Motion for $\\omega_0$ = {w0} rad/s')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()
