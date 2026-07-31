# Day 20 - 30 Days Python Challenge 🐍

## What I Learned Today
- Generators (`yield`)
- Function Caching (`@lru_cache`)

## Programs Written

### 1. RPG Battle Game
A turn-based RPG battle game between a Hero and a Monster, featuring moves like
Slash, Heavy Strike, Heal, Blood Rage, and an Ultimate Move. Uses a generator
function with `yield` to pause and resume turns without re-running the whole
function each time.

### 2. Movie Rating Fetcher
A program that demonstrates function caching using `@lru_cache` — the first
call to fetch a movie's rating takes 5 seconds (simulating an API call), but
the second call for the same movie returns instantly since the result is cached.

## Concepts Covered
- Generators and the `yield` keyword
- Turn-based logic using generator state
- Function caching with `functools.lru_cache`
- Random number generation (`random.randint`)

---
Part of my #30DaysPythonChallenge 🚀
