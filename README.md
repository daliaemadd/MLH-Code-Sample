# Knights and Knaves Logic Puzzle Solver

This project is a Python program that solves a set of classic **Knights and Knaves** logic puzzles using the [`z3-solver`](https://pypi.org/project/z3-solver/) constraint-solving library.

In these puzzles, every character is either a **knight**, who always tells the truth, or a **knave**, who always lies. The program translates each character's statement into Boolean logic and uses the Z3 theorem prover to determine whether a consistent solution exists.

## Project Overview

The goal of this project was to practice representing natural-language logic problems as formal Boolean constraints. Each puzzle is modeled using:

- Boolean variables for each character
- Logical operators such as `And`, `Or`, `Not`, and `Implies`
- Biconditional relationships to represent the rule that a knight's statement is true and a knave's statement is false
- The Z3 `Solver` to check whether the constraints are satisfiable

The program currently solves four puzzles:

1. A two-character Ted and Zippy puzzle
2. A five-character puzzle involving Betty, Marge, Homer, Carl, and Sue
3. A larger eight-character puzzle involving nested statements
4. A challenge puzzle involving implication and same-type reasoning

## Technologies Used

- Python 3
- Z3 Solver / `z3-solver`
- Boolean logic
- Constraint satisfaction modeling

## How It Works

Each character is represented as a Boolean variable:

- `True` means the character is a knight
- `False` means the character is a knave

For each statement, the program adds a constraint of the form:

```python
Character == Statement
```

This means:

- If the character is a knight, their statement must be true.
- If the character is a knave, their statement must be false.

For example, in Puzzle 1:

```python
T, Z = Bools('Ted Zippy')
t_s.add(T == Or(And(T, Not(Z)), And(Not(T), Z)))
t_s.add(Z == Not(T))
```

Ted's statement says exactly one of Ted and Zippy is a knight, and Zippy's statement says Ted is a knave. Z3 evaluates these constraints and returns a model showing which characters are knights and which are knaves.

## Installation

Install the Z3 solver package:

```bash
pip install z3-solver
```

## How to Run

Save the program in a Python file, for example:

```bash
knights_knaves_solver.py
```

Then run:

```bash
python knights_knaves_solver.py
```

The program will print each puzzle name and either display a valid model or report that no solution exists.

## Sample Output Format

The output is printed in the following format:

```text
--- Puzzle 1 ---
[Ted = False, Zippy = True]

--- Puzzle 2 ---
No solution exists
```

The exact model may be displayed in a different order depending on Z3.

## Key Concepts Demonstrated

This project demonstrates:

- Translating English statements into formal logic
- Modeling truth-tellers and liars with Boolean variables
- Using satisfiability solving to test logical consistency
- Building and checking constraints with Z3
- Debugging nested logical statements

## Files

```text
knights_knaves_solver.py   # Main Python program
README.md                  # Project description and setup instructions
```

## Future Improvements

Possible improvements include:

- Formatting the output to clearly label each person as "Knight" or "Knave"
- Adding automated tests for each puzzle
- Allowing puzzles to be entered through a text or JSON input file
- Detecting and displaying multiple possible solutions
- Creating a small command-line interface for selecting puzzles

## Why This Project Is Useful

This project shows how symbolic reasoning tools can solve problems that are difficult to brute-force manually. It also demonstrates how AI and formal methods can be used to convert real-world logic into constraints that a solver can analyze automatically.
