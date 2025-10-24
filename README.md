# Find me as the Prime Number (Subtraction)

A program to find and perform sequential subtraction on all prime numbers from a series of user inputs.

## 📝 Description

This program repeatedly asks the user if they want to enter a number. If the user agrees (by entering 'y'), they provide an integer. The program must check if this integer is a prime number. When the user decides to stop (by entering 'n'), the program calculates the final result.

The **first** prime number found is used as the starting value. Every **subsequent** prime number found is subtracted from this running total.

-----

## 🎯 Problem Statement

### Input:

  * A sequence of 'y' (yes) or 'n' (no) prompts to control the loop.
  * An integer input from the user following each 'y' prompt.

### Output:

  * The final result of the sequential subtraction.
  * "NoProceed" if an invalid input (like a negative number) is entered.

### Rules:

1.  The program runs in a loop, asking for input. 'y' continues the loop, 'n' stops it.
2.  A **prime number** is a natural number **greater than 1** (e.g., 2, 3, 5, 7...).
3.  **Subtraction Logic:** The *first* prime number entered is the initial value. Every *subsequent* prime number is subtracted from this total.
4.  If no prime numbers are found, the result is 0.
5.  If only one prime number is found, the result is that number itself.
6.  Non-prime positive numbers (like 1, 4, 8, 10) are ignored.
7.  Entering a **negative number** is invalid and should output "NoProceed".

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
y
2
y
10
n
```

**Output:**

```
2
```

**Explanation:** `2` is the first prime. `10` is not prime and is ignored. Only one prime was found, so the result is **2**.

### Example 2 (Sample 2)

**Input:**

```
y
5
y
3
y
2
n
```

**Output:**

```
0
```

**Explanation:** `5` is the first prime. `3` is the next prime (5 - 3 = 2). `2` is the next prime (2 - 2 = 0). The final result is **0**.

### Example 3 (Sample 3)

**Input:**

```
y
4
y
8
n
```

**Output:**

```
0
```

**Explanation:** Neither `4` nor `8` is a prime number. No primes were found, so the result is **0**.

### Example 4 (Sample 4)

**Input:**

```
n
```

**Output:**

```
0
```

**Explanation:** No numbers were entered, so the result is **0**.

### Example 5 (Sample 5)

**Input:**

```
y
3
y
-5
```

**Output:**

```
NoProceed
```

**Explanation:** The input `-5` is a negative number, which is not a valid input.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/subtract-primes.git
    cd subtract-primes
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Follow the 'y/n' prompts to enter numbers and see the result.
