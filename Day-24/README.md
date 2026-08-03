# Day 24 - 30 Days Python Challenge 🐍

## What I Learned Today
- Multiprocessing (`multiprocessing` module)
- Completed CodeWithHarry's 100-day Python playlist! 🎉

## Programs Written

### 1. Car Race Simulation
A multiprocess race simulation where each car runs its race independently in
its own process using `multiprocessing.Process()`. Random events (crash/nitro)
affect race progress, and results are collected using a `multiprocessing.Queue()`
to build a final leaderboard.

### 2. File Copier
A program that copies all `.txt` files from a source folder to a destination
folder concurrently, using a separate process for each file via
`multiprocessing.Process()`.

## Concepts Covered
- Multiprocessing with `multiprocessing.Process()`
- Inter-process communication using `multiprocessing.Queue()`
- `process.start()` and `process.join()`
- Sorting with `lambda` as a custom key

---
Part of my #30DaysPythonChallenge 🚀
