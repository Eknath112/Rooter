import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.sympify import SympifyError
import io, base64

plt.style.use('ggplot')

def solve_iteration(equation_str, x0, tol=1e-6, max_iterations=100, plot=False):
    """
    Fixed Point Iteration method.
    equation_str: iteration function g(x) as a string
    x0: initial guess
    tol: tolerance
    max_iterations: maximum iterations
    plot: whether to return plot as base64
    """

    x = sp.symbols('x')
    try:
        g_sympy = sp.sympify(equation_str)
    except SympifyError:
        return {"text": "Invalid equation input. Please enter a valid mathematical expression in terms of x.", "plot": None}

    if x not in g_sympy.free_symbols:
        return {"text": "Equation must contain variable 'x'.", "plot": None}

    g = sp.lambdify(x, g_sympy, 'numpy')

    # Iteration loop
    iteration = 0
    try:
        while iteration < max_iterations:
            x1 = g(x0)
            if abs(x1 - x0) < tol:
                root = x1
                break
            x0 = x1
            iteration += 1
        else:
            root = x1
    except Exception as e:
        return {"text": f"Error during iteration: {e}", "plot": None}

    result_text = f"Root found: {root:.6f}\nNumber of iterations: {iteration}"

    img_data = None
    if plot:
        x_vals = np.linspace(root - 2, root + 2, 400)
        y_vals = g(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f'g(x) = {equation_str}')
        plt.plot(x_vals, x_vals, color='black', linestyle='--', label='y = x')
        plt.axvline(root, color='blue', linestyle='--', label=f'Root ≈ {root:.6f}')
        plt.scatter([root], [g(root)], color='red', zorder=5)
        plt.title('Fixed Point Iteration Method')
        plt.xlabel('x')
        plt.ylabel('g(x)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        img_data = base64.b64encode(buf.read()).decode("utf-8")
        plt.close()

    return {"text": result_text, "plot": img_data}
