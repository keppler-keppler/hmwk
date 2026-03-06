import sympy as sp

t = sp.Symbol('t')

m1, m2, l, g, x0, w0 = sp.symbols('m1 m2 l g x0 w0', real=True, positive=True)

phi = sp.Function('phi')(t)
x = sp.Function('x')(t)

phi_dot = sp.diff(phi, t)
x_dot = sp.diff(x, t)

T = 0.5 * (m1 + m2) * x_dot**2 + 0.5 * m2 * (l**2 * phi_dot**2 + 2 * x_dot * l * phi_dot * sp.cos(phi))
V = -m2 * g * l * sp.cos(phi)

L = T - V

# d/dt( dL/d(phi_dot) ) - dL/d(phi) = 0

dL_dphidot = sp.diff(L, phi_dot)

d_dt_dL_dphidot = sp.diff(dL_dphidot, t)

dL_dphi = sp.diff(L, phi)

eom_phi = sp.simplify(d_dt_dL_dphidot - dL_dphi)

# Print the result
print("The exact equation of motion (equal to 0) is:")
sp.pprint(eom_phi)
