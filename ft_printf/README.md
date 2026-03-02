*This project has been created as part of the 42 curriculum by mboubaza.*

# ft_printf

## Description
The `ft_printf` project is a recoding of the standard C library function `printf`. The primary goal is to learn how to manage variadic arguments (`va_list`) and understand how different data types are stored and formatted in memory.

This static library (`libftprintf.a`) mimics the behavior of the original `printf`, supporting the following conversions:
* `%c` - Prints a single character.
* `%s` - Prints a string.
* `%p` - Prints a `void *` pointer argument in hexadecimal format.
* `%d` / `%i` - Prints a decimal (base 10) number.
* `%u` - Prints an unsigned decimal (base 10) number.
* `%x` - Prints a number in hexadecimal (base 16) lowercase format.
* `%X` - Prints a number in hexadecimal (base 16) uppercase format.
* `%%` - Prints a percent sign.

## Instructions

### Compilation
The project is compiled using a `Makefile` which generates the static library `libftprintf.a`.

To compile the library:
`make`

To remove object files:
`make clean`

To remove object files and the library:
`make fclean`

To recompile everything:
`make re`

### Usage
To use `ft_printf` in your own C project:

1.  Include the header file in your source code:
    #include "ft_printf.h"

2.  Compile your code and link it with the library:
    cc main.c libftprintf.a -o my_program

**Example (`main.c`):**

#include "ft_printf.h"### AI Usage
Artificial Intelligence was used as a peer reviewer and debugging tool during the development of this project:
* **Code Review:** AI was used to analyze source code for logical errors, specifically checking for correct return values in recursive functions (`print_int` and `print_uint`).
* **Debugging:** AI assisted in identifying bugs related to pointer casting (`unsigned long` vs `unsigned int`) and format string parsing.
* **Documentation:** AI generated the initial structure of this README file to ensure compliance with the project submission guidelines.

int main(void)
{
ft_printf("Char: %c, String: %s, Int: %d\n", 'A', "42 Network", 1337);
ft_printf("Hex: %x, Pointer: %p\n", 255, &main);
return (0);
}

## Algorithm and Data Structure Justification

### Data Structure: `va_list`
The project relies on `va_list` from `<stdarg.h>` to handle the undefined number of arguments. This structure allows the function to traverse the memory stack (or registers) to retrieve arguments sequentially using the `va_start`, `va_arg`, and `va_end` macros.

### Algorithm: Dispatcher & Recursion
The implementation uses a **Parsing and Dispatch** approach:
1.  **Parsing:** The main loop iterates through the format string. When a `%` is found, it inspects the next character.
2.  **Dispatching:** A dedicated function (`which_to_pr`) routes the argument to the correct helper function based on the specifier (e.g., `print_int` for `%d`, `print_hex` for `%x`).
3.  **Recursive Printing:**
    * For numeric conversions (`%d`, `%u`, `%x`), a recursive algorithm is used.
    * **Justification:** Recursion simplifies the logic for printing numbers in different bases (10 or 16) without needing `malloc` or external buffers. It allows the function to print digits in the correct order (most significant to least significant) while calculating the length on the fly.
4.  **Return Value:** Each helper function tracks and returns the exact number of bytes written. These are summed in the main loop to ensure the final return value matches the standard `printf`.

## Resources

### References
* **Man Pages:** `man 3 printf`, `man 3 stdarg`.
* **General Research:** Various online articles and forums were used to verify behavior and implementation details of variadic functions and type promotion.

### AI Usage
Artificial Intelligence was used as a peer reviewer and debugging tool during the development of this project:
* **Code Review:** AI was used to analyze source code for logical errors, specifically checking for correct return values in recursive functions (`print_int` and `print_uint`).
* **Debugging:** AI assisted in identifying bugs related to pointer casting (`unsigned long` vs `unsigned int`) and format string parsing.
* **Documentation:** AI generated the initial structure of this README file to ensure compliance with the project submission guidelines.