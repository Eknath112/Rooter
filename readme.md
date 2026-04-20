# Rooter – Numerical Methods Root Finder

## Project Overview

Rooter is a Python-based mini project designed to compute the **roots of mathematical equations** using multiple classical numerical methods. It integrates backend computation with a simple frontend interface to provide both **numerical results and graphical visualization**.

## Main Objective

The purpose of this project is to:

* Demonstrate how different numerical root-finding methods work
* Compare their convergence behavior
* Provide an interactive and visual learning tool for students

---

## Methods Implemented

Each method is implemented in a separate Python file and integrated through `app.py`.

---

### 1. Bisection Method

**Concept:**
A bracketing method that repeatedly halves an interval where a root lies.

**Condition:**
If `f(a) * f(b) < 0`, then at least one root exists in `[a, b]`.

**Formula:**
[
c = \frac{a + b}{2}
]

**Example:**
Solve `f(x) = x^3 - x - 2` in the interval `[1, 2]`.

---

### 2. Secant Method

**Concept:**
An open method that approximates the root using a secant line between two points.

**Formula:**
[
x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}
]

**Example:**
Solve `f(x) = x^2 - 4` with initial guesses `x₀ = 1`, `x₁ = 3`.

---

### 3. Regula Falsi Method

**Concept:**
A bracketing method similar to bisection but uses a weighted approximation.

**Formula:**
[
c = b - \frac{f(b)(b - a)}{f(b) - f(a)}
]

**Example:**
Solve `f(x) = x^3 - x - 2` in `[1, 2]`.

---

### 4. Iteration Method (Fixed Point Iteration)

**Concept:**
Transforms the equation into the form `x = g(x)` and iteratively computes values.

**Formula:**
[
x_{n+1} = g(x_n)
]

**Condition for Convergence:**
[
|g'(x)| < 1
]

**Example:**
Solve `x^2 - 3 = 0` by rewriting as `x = sqrt(3)`.

---

### 5. Newton-Raphson Method

**Concept:**
Uses the tangent at a point to approximate the root.

**Formula:**
[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
]

**Advantages:**

* Fast convergence
* High accuracy

**Limitation:**

* Requires derivative

**Example:**
Solve `f(x) = x^2 - 2` with initial guess `x₀ = 1`.

---

## Project Structure

```id="n5k1b2"
rooter/
│
├── bisection.py
├── secant.py
├── regula_falsi.py
├── iteration.py
├── newton_raphson.py
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    └── dashboard.html
```

---

## How It Works

* Each method file contains a function that computes the root and returns:

  * Final root value
  * Data required for plotting
  * Number of iterations taken

* `app.py`:

  * Handles user input
  * Calls selected numerical method
  * Generates graphs using plotting libraries
  * Displays the **number of iterations on the graph**
  * Provides functionality to download graph images

---

## Iteration Policy

* The **maximum number of allowed iterations is 100**
* If a method reaches 100 iterations:

  * It is assumed that the method **did not converge**
  * If the plotted curves do not intersect, it indicates **no real root found in the given domain**

---

## Features

* Multiple numerical root-finding methods
* Graphical visualization of functions
* Iteration count displayed on graph
* Downloadable plot images
* Modular and organized code structure
* Built-in convergence safeguard (100 iteration cap)

---

## How to Run the Project

### 1. Clone the Repository

```bash id="7c3vxp"
git clone https://github.com/your-username/rooter.git
cd rooter
```

### 2. Install Dependencies

```bash id="2x0yqf"
pip install -r requirements.txt
```

### 3. Run the Application

```bash id="c9v1g8"
python app.py
```

### 4. Open in Browser

```id="6yk8q2"
http://localhost:5000
```

---

## Example Usage

* Input function: `x^3 - x - 2`
* Select method: Bisection
* Interval: `[1, 2]`

Output:

* Root ≈ 1.521
* Iterations displayed on graph
* Graph visualization
* Option to download the graph

---

## Possible Improvements

* Add iteration-by-iteration tables
* Compare convergence speed across methods visually
* Include error tolerance input
* Support symbolic expressions using libraries like SymPy
* Enhance frontend design and responsiveness

---

## Contributing

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Submit a pull request

---

## Learning Outcomes

* Understanding numerical root-finding techniques
* Observing convergence behavior
* Applying mathematical concepts in programming
* Building modular Python applications

---

## License

This project is open-source and available under the MIT License.
