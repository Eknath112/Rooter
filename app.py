from flask import Flask, render_template, request
from bisection import solve_bisection
from regula_falsi import solve_regula_falsi
from secant import solve_secant
from newton_raphson import solve_newton_raphson
from iteration import solve_iteration

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    outputs = {}

    if request.method == "POST":
        # Bisection
        eq = request.form.get("equation_Bisection")
        a = request.form.get("a_Bisection")
        b = request.form.get("b_Bisection")
        if eq and a and b:
            outputs["Bisection"] = solve_bisection(eq, float(a), float(b), plot=True)

        # Regula Falsi
        eq = request.form.get("equation_Regula Falsi")
        a = request.form.get("a_Regula Falsi")
        b = request.form.get("b_Regula Falsi")
        if eq and a and b:
            outputs["Regula Falsi"] = solve_regula_falsi(eq, float(a), float(b), plot=True)

        # Secant
        eq = request.form.get("equation_Secant")
        x0 = request.form.get("x0_Secant")
        x1 = request.form.get("x1_Secant")
        if eq and x0 and x1:
            outputs["Secant"] = solve_secant(eq, float(x0), float(x1), plot=True)

        # Newton-Raphson
        eq = request.form.get("equation_Newton-Raphson")
        x0 = request.form.get("x0_Newton-Raphson")
        if eq and x0:
            outputs["Newton-Raphson"] = solve_newton_raphson(eq, float(x0), plot=True)

        # Iteration (Fixed Point)
        eq = request.form.get("equation_Iteration")
        x0 = request.form.get("x0_Iteration")
        if eq and x0:
            outputs["Iteration"] = solve_iteration(eq, float(x0), plot=True)

    return render_template("dashboard.html", outputs=outputs)

if __name__ == "__main__":
    app.run(debug=True)
