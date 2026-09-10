# DSA for Development 🚀

A daily Data Structures & Algorithms practice repository focused on building strong problem-solving skills for software engineering and technical interviews.

The repository is organized by topic, with solutions written in Python and an emphasis on understanding both **brute-force** and **optimized** approaches.

## 📚 Current Progress

### Arrays

The current practice is focused on array-based interview problems.

📁 `Array/`

| File | Problem / Focus | Key Concepts |
|---|---|---|
| `p1.py` | Second Largest Element | Single-pass traversal, two variables, O(n) |
| `p2.py` | Best Time to Buy and Sell Stock | Brute force O(n²), optimized O(n), running minimum |
| `p3.py` | Array Practice | Array traversal and problem solving |
| `p4.py` | Array Practice | Array traversal and problem solving |
| `Duplication.py` | Duplicate-related array problem | Array traversal / duplicate detection |

## 🧠 Problems Completed

### 1. Second Largest Element

The solution keeps track of the largest and second-largest values while traversing the array once.

Core idea:

```python
first = second = float('-inf')

for num in nums:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
```

**Complexity:**
- Time: `O(n)`
- Space: `O(1)`

The implementation also handles arrays with fewer than two elements and cases where a distinct second-largest value does not exist. fileciteturn5file0

---

### 2. Best Time to Buy and Sell Stock

Given daily stock prices, find the maximum profit using exactly one buy and one sell transaction.

Two approaches are implemented.

#### Brute Force — O(n²)

Check every possible buy/sell pair:

```python
for i in range(len(prices) - 1):
    for j in range(i + 1, len(prices)):
        profit = prices[j] - prices[i]
        maximum = max(maximum, profit)
```

#### Optimized — O(n)

Track the lowest price seen so far and calculate the best profit at each step:

```python
lowest = prices[0]
maximum = 0

for i in range(1, len(prices)):
    if prices[i] < lowest:
        lowest = prices[i]

    maximum = max(maximum, prices[i] - lowest)
```

**Complexity:**

| Approach | Time | Space |
|---|---:|---:|
| Brute Force | `O(n²)` | `O(1)` |
| Optimized | `O(n)` | `O(1)` |

The optimized solution reduces the nested-loop approach to a single traversal while preserving constant auxiliary space. fileciteturn6file0

---

## 🎯 Practice Strategy

The goal is to solve DSA problems consistently rather than only memorize solutions.

For each problem:

1. Understand the problem and constraints.
2. Think of a brute-force solution first.
3. Analyze its time and space complexity.
4. Look for a better data structure, traversal, or algorithm.
5. Implement the optimized solution.
6. Test edge cases.
7. Commit the solution to GitHub.

## 📈 Weekly Target

The current DSA practice plan is:

- **4 Easy** problems
- **2 Medium** problems
- **1 Hard** problem
- Focus on **one topic at a time**
- Revise previously solved problems monthly

The difficulty will gradually increase as fundamentals become stronger.

## 🗂️ Planned Topics

Future sections will progressively cover:

- Arrays
- Strings
- Hashing
- Two Pointers
- Sliding Window
- Stack
- Queue
- Linked List
- Binary Search
- Trees
- Binary Search Trees
- Heaps / Priority Queue
- Graphs
- Recursion
- Backtracking
- Dynamic Programming
- Greedy Algorithms

## 💻 Language

Solutions are primarily written in **Python 3**.

## 🔥 Goal

Build strong DSA fundamentals, improve algorithmic thinking, understand complexity, and become interview-ready for software engineering and backend development roles.

---

**Consistency > memorization. Understand the pattern, then solve it yourself. 🚀**
