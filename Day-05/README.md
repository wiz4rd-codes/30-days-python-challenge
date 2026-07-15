# Day 5 – Water Snake Gun Game & `is` vs `==`

Today I learned the difference between Python's `is` and `==` operators and built a simple **Water Snake Gun** game using conditional statements and the `random` module.

## 📚 What I Learned

### ✅ Difference between `is` and `==`

* `==` checks whether two objects have the **same value**.
* `is` checks whether two variables refer to the **same object in memory**.

### Examples

* Lists with the same values return `True` with `==` but `False` with `is` because they are different objects.
* Tuples may return `True` with both `==` and `is` because Python can reuse immutable objects in some cases.

> **Note:** Don't rely on `is` returning `True` for identical tuples. Use `is` only for identity checks (e.g., `x is None`), not for comparing values.

## 🎮 Project: Water Snake Gun Game

Built a command-line version of the classic Water Snake Gun game.

### Features

* Random computer choice using the `random` module.
* User input validation.
* Win, lose, and draw logic.
* Clean and simple game flow.

## 🛠 Concepts Practiced

* Functions
* Conditional statements (`if`, `elif`, `else`)
* User input
* Random module
* Exception handling (`ValueError`)
* Object identity vs value equality

## 🚀 Day 5 Complete

Another step forward in my **#100DaysOfPython** journey. Looking forward to learning more tomorrow!
