*This project has been created as part of the 42 curriculum by mboubaza.*

> *Because Swap_push doesn't feel as natural*

## Description

**Push_swap** is an algorithmic project that involves sorting a stack of integers using a limited set of operations, with the goal of achieving the minimum number of moves possible. This project is part of the 42 school curriculum, focusing on algorithm optimization and complexity management.

### Rules

- You have **two stacks**: `a` and `b`
- Stack `a` contains a random set of unique integers
- Stack `b` is initially empty
- The goal is to sort stack `a` in ascending order using the available operations

### Algorithm

This implementation uses the **Turk Algorithm**, a cost-based approach that:

1. Pushes elements from stack A to B while maintaining relative order
2. Calculates the optimal "push cost" for each element
3. Always moves the element with the lowest push cost
4. Pushes everything back to A in sorted order

### Operations

| Operation | Description |
| --------- | ----------- |
| `sa` | Swap the first 2 elements of stack A |
| `sb` | Swap the first 2 elements of stack B |
| `ss` | Execute `sa` and `sb` simultaneously |
| `pa` | Push the top element from B to A |
| `pb` | Push the top element from A to B |
| `ra` | Rotate stack A (first element becomes last) |
| `rb` | Rotate stack B (first element becomes last) |
| `rr` | Execute `ra` and `rb` simultaneously |
| `rra` | Reverse rotate stack A (last element becomes first) |
| `rrb` | Reverse rotate stack B (last element becomes first) |
| `rrr` | Execute `rra` and `rrb` simultaneously |

## Instructions

### Compilation

```bash
# Compile
make

# Clean object files
make clean

# Full clean (including executable)
make fclean

# Recompile
make re
```

### Usage

```bash
# Basic usage with space-separated arguments
./push_swap 4 67 3 87 23

# Usage with quoted string
./push_swap "4 67 3 87 23"

# Count the number of operations
./push_swap 4 67 3 87 23 | wc -l

# Verify the result with checker
ARG="4 67 3 87 23"; ./push_swap $ARG | ./checker_linux $ARG
```

### Error Handling

The program handles the following errors:

- Non-integer arguments
- Integer overflow/underflow
- Duplicate values
- Empty arguments

```bash
./push_swap 1 2 2        # Error (duplicate)
./push_swap 1 2 abc      # Error (non-integer)
./push_swap              # No output (no arguments)
```

### Performance

| Stack Size | Operations | Benchmark Target |
| ---------- | ---------- | ---------------- |
| 3 | ≤ 3 | ≤ 3 |
| 5 | ≤ 12 | ≤ 12 |
| 100 | ~550 | < 700 (5 pts) |
| 500 | ~1500 | < 5500 (5 pts) |

## Resources

### References

- [Push_swap Tutorial - Medium](https://medium.com/@jamierobertdawson/push-swap-the-least-amount-of-moves-with-two-stacks-d1e76a71789a)
- [Turk Algorithm Explanation](https://github.com/o-reo/push_swap_visualizer)

### AI Usage

AI tools were used to simplify complex concepts, provide clearer explanations of algorithms, and assist with debugging during development.

## Project Structure

```text
push_swap/
├── Makefile
├── push_swap.h
├── main.c
├── init.c
├── init_utils.c
├── init_target.c
├── turk.c
├── list_utils.c
├── safe_atoi.c
├── moves/
│   ├── push.c
│   ├── swap.c
│   ├── rotate.c
│   └── rev_rotate.c
└── libft/
```

---

Made with ❤️ at 42
