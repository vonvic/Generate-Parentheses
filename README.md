# Generate-Parentheses
Leetcode Problem 22. Generate Parentheses

A dynamic programming solution that generates all possible valid combinations of parenthes.

## How I solved it
I discovered the solution by generalizing the problem after noticing a pattern of the valid combinations. Easily, the solution is dynamic programming as there are multiple recursive calls of the same arguments in a top down fashion.

### Actual Answers
```
n = 0

n = 1
()

n = 2
()()
(())

n = 3
()()()
()(())
(())()
(()())
((()))
```

### Generalized Answer
n
(n-1)
(n-2)1
(n-3)2
...
(1)n-2
()n-1
```