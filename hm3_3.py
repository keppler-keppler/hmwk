import sympy as sp
from sympy.physics.mechanics import dynamicsymbols, Lagrangian, LagrangesMethod

t = sp.symbols('t')
m1, m2 = sp.symbols('m1 m2')           
l1, l2 = sp.symbols('l1 l2')           
lc1, lc2 = sp.symbols('lc1 lc2')       
g = sp.symbols('g')                   

q1, q2 = dynamicsymbols('q1 q2')
dq1, dq2 = dynamicsymbols('q1 q2', 1)
ddq1, ddq2 = dynamicsymbols('q1 q2', 2)

x1 = lc1 * sp.cos(q1)
y1 = lc1 * sp.sin(q1)

x2 = l1 * sp.cos(q1) + lc2 * sp.cos(q1 + q2)
y2 = l1 * sp.sin(q1) + lc2 * sp.sin(q1 + q2)

v1_sq = sp.diff(x1, t)**2 + sp.diff(y1, t)**2
v2_sq = sp.diff(x2, t)**2 + sp.diff(y2, t)**2

I1 = m1 * lc1**2
I2 = m2 * lc2**2

T1 = 0.5 * m1 * v1_sq + 0.5 * I1 * dq1**2
T2 = 0.5 * m2 * v2_sq + 0.5 * I2 * (dq1 + dq2)**2
T = T1 + T2

V = m1 * g * y1 + m2 * g * y2

L = T - V
LM = LagrangesMethod(L, [q1, q2])
equations = LM.form_lagranges_equations()

params = {
    m1: 9, m2: 15,
    l1: 0.25, l2: 0.35,
    lc1: 0.2, lc2: 0.3,
    g: 9.81,
    q1: sp.rad(25), q2: sp.rad(65),
    dq1: 0.75, dq2: 1.0,
    ddq1: 0.5, ddq2: 1.2
}

tau = equations.subs(params)

print(f"Torque 1 (tau1): {float(tau[0]):.2f} N-m")
print(f"Torque 2 (tau2): {float(tau[1]):.2f} N-m")
