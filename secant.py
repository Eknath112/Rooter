import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.sympify import SympifyError
import io, base64

plt.style.use('ggplot')

def solve_secant(equation_str, x0, x1, tol=1e-6, max_iterations=100, plot=False):
    x = sp.symbols('x')
    try:
        f_sympy = sp.sympify(equation_str)
    except SympifyError:
        return {"text": "Invalid equation input. Please enter a valid mathematical expression in terms of x.", "plot": None}

    if x not in f_sympy.free_symbols:
        return {"text": "Equation must contain variable 'x'.", "plot": None}

    f = sp.lambdify(x, f_sympy, 'numpy')

    # Test evaluation at initial guesses
    try:
        f0, f1 = f(x0), f(x1)
    except Exception as e:
        return {"text": f"Equation cannot be evaluated numerically: {e}", "plot": None}

    # Secant method loop
    iteration = 0
    root = None
    while iteration < max_iterations:
        if f(x1) - f(x0) == 0:
            return {"text": "Division by zero encountered in Secant method.", "plot": None}

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        if abs(x2 - x1) < tol:
            root = x2
            break

        x0, x1 = x1, x2
        iteration += 1
        root = x2

    result_text = f"Root found: {root:.6f}\nNumber of iterations: {iteration}"

    img_data = None
    if plot:
        x_vals = np.linspace(min(x0, x1) - 1, max(x0, x1) + 1, 400)
        y_vals = f(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f'f(x) = {equation_str}')
        plt.axhline(0, color='black', linewidth=0.8)
        plt.axvline(root, color='blue', linestyle='--', label=f'Root ≈ {root:.6f}')
        plt.scatter([root], [f(root)], color='red', zorder=5)
        plt.title('Secant Method Root Finding')
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
