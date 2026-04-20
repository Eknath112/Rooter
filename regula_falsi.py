import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.sympify import SympifyError
import io, base64

plt.style.use('ggplot')

def solve_regula_falsi(equation_str, a, b, tol=1e-6, max_iterations=100, plot=False):
    x = sp.symbols('x')
    try:
        f_sympy = sp.sympify(equation_str)
    except SympifyError:
        return {"text": "Invalid equation input. Please enter a valid mathematical expression in terms of x.", "plot": None}

    if x not in f_sympy.free_symbols:
        return {"text": "Equation must contain variable 'x'.", "plot": None}

    f = sp.lambdify(x, f_sympy, 'numpy')

    # Test evaluation at endpoints
    try:
        fa, fb = f(a), f(b)
    except Exception as e:
        return {"text": f"Equation cannot be evaluated numerically: {e}", "plot": None}

    if fa * fb >= 0:
        return {"text": "Function has same signs at the ends of interval [a, b]. Regula Falsi cannot proceed.", "plot": None}

    # Regula Falsi loop
    iteration = 0
    c = a
    root = None
    while iteration < max_iterations:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)

        if abs(fc) < tol:
            root = c
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iteration += 1
        root = c

    result_text = f"Root found: {root:.6f}\nNumber of iterations: {iteration}"

    img_data = None
    if plot:
        x_vals = np.linspace(a - 1, b + 1, 400)
        y_vals = f(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f'f(x) = {equation_str}')
        plt.axhline(0, color='black', linewidth=0.8)
        plt.axvline(root, color='blue', linestyle='--', label=f'Root ≈ {root:.6f}')
        plt.scatter([root], [f(root)], color='red', zorder=5)
        plt.title('Regula Falsi Method Root Finding')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        img_data = base64.b64encode(buf.read()).decode("utf-8")
        plt.close()

    return {"text": result_text, "plot": img_data}
