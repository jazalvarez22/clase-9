import numpy as np

# ============================================================
# CAMBIA AQUÍ TU FUNCIÓN f(x)
# ============================================================
def f(x):
    # Ejemplo (cámbialo): sin(x) + x^2
    return np.sin(x) + x**2


# ============================================================
# Métodos de integración
# ============================================================
def rectangulo_izq(f, a, b, n):
    h = (b - a) / n
    x = a + h * np.arange(0, n)          # x0 ... x_{n-1}
    return h * np.sum(f(x))

def rectangulo_der(f, a, b, n):
    h = (b - a) / n
    x = a + h * np.arange(1, n + 1)      # x1 ... x_n
    return h * np.sum(f(x))

def punto_medio(f, a, b, n):
    h = (b - a) / n
    x = a + h * (np.arange(0, n) + 0.5)  # midpoints
    return h * np.sum(f(x))

def trapecio(f, a, b, n):
    h = (b - a) / n
    x = a + h * np.arange(0, n + 1)      # x0 ... x_n
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])


# ============================================================
# Referencia (opcional): SymPy si se puede, si no trapecio fino
# ============================================================
def integral_referencia(a, b):
    try:
        import sympy as sp
        x = sp.Symbol("x")

        # IMPORTANTE: define la misma función aquí en SymPy si cambias f(x)
        f_sym = sp.sin(x) + x**2

        val = sp.integrate(f_sym, (x, a, b))
        return float(val.evalf()), "sympy"
    except Exception:
        # fallback: trapecio muy fino
        n_ref = 1_000_000
        f_np = np.vectorize(f)
        val = trapecio(f_np, a, b, n_ref)
        return float(val), f"trapecio_fino(n={n_ref})"


if __name__ == "__main__":
    # ============================================================
    # CAMBIA AQUÍ TUS LÍMITES Y PARTICIONES
    # ============================================================
    a = 0.0
    b = 2.0
    n = 50

    f_np = np.vectorize(f)

    ref, ref_src = integral_referencia(a, b)

    r_izq = rectangulo_izq(f_np, a, b, n)
    r_der = rectangulo_der(f_np, a, b, n)
    pm    = punto_medio(f_np, a, b, n)
    tr    = trapecio(f_np, a, b, n)

    def err(aprx):
        return abs(aprx - ref)

    print("==============================================")
    print(f"Integral en [{a}, {b}] con n={n}")
    print(f"Referencia ({ref_src}) = {ref:.10f}")
    print("==============================================")
    print(f"Rectángulo Izq   = {r_izq:.10f} | error = {err(r_izq):.3e}")
    print(f"Rectángulo Der   = {r_der:.10f} | error = {err(r_der):.3e}")
    print(f"Punto Medio      = {pm:.10f} | error = {err(pm):.3e}")
    print(f"Trapecio         = {tr:.10f} | error = {err(tr):.3e}")
    print("==============================================")
