# 📖 Python for Everybody — Chapter 8: Lists

| Key idea | One-sentence takeaway |
|----------|-----------------------|
| **Lists are mutable sequences** | You can change, grow, or shrink them in place. |
| **Zero-based indexing & slicing** | Same slice rules as strings, but writable. |
| **`append()` vs `extend()`** | `append(x)` adds one item; `extend(iter)` concatenates another iterable. |
| **Aliasing vs. copying** | `b = a` links to the same list; use `a[:]` or `list(a)` for a copy. |
| **`in` operator** | Fast membership test: `if item in list:`. |
| **List comprehension** | Concise way to create lists from iterables: `[x**2 for x in nums if x%2]`. |
| **`split()` produces lists** | Powerful when combined with `for` loops and aggregate functions. |

---

## 🔑 Syntax Cheatsheet
```python
nums = [10, 20, 30]

# indexing / slicing
nums[0]         # 10
nums[-1]        # 30
nums[1:3]       # [20, 30]

# mutating
nums[1] = 25    # [10, 25, 30]
nums.append(40) # [10, 25, 30, 40]
nums.extend([50, 60])

# insert / remove
nums.insert(2, 99)     # index, value
nums.remove(25)        # by value
popped = nums.pop()    # by index (default last)

# list comprehension
squares = [x*x for x in range(1, 6)]   # [1, 4, 9, 16, 25]

# sorting
nums.sort()            # in place
sorted_nums = sorted(nums, reverse=True)  # returns new list
```

### Common functions:
| Function | Purpose |
| ----------- | ----------- |
| `len(L)` | length |
| `max(L)`/`min(L)` | largest/smallest |
| `sum(L)` | numeric total |
| `list(iter)` | convert iterable to list |

---
## 🧐 Common Pitfalls
| Mistake                                             | Fix                                                      |
| --------------------------------------------------- | -------------------------------------------------------- |
| Using `append(list2)` when you meant to concatenate | Use `extend(list2)` **or** `list1 += list2`.             |
| Accidentally aliasing (`b = a`) then modifying `b`  | Copy with `a[:]` or `a.copy()`.                          |
| Sorting mixed types (`['1', 2]`)                    | Keep lists homogeneous or supply `key=` for custom sort. |
| Modifying a list while looping over it              | Iterate over a copy: `for x in list(L): ...`             |

---
## 💡 Reading Tips
* Use `enumerate(L)` when you need both index and value.
* `",".join(list_of_strings)` is the inverse of `split()`
* Slicing a list (`L[:]`) creates a *shallow* copy.