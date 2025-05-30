# 📖 Python for Everybody — Chapter 6: Strings

| Key idea | One-sentence takeaway |
|----------|-----------------------|
| **Strings are sequences** | You can index, slice, and iterate over them just like lists. |
| **Immutability** | You can’t change a string in place—always create a new one. |
| **Built-in functions** | `len()`, `min()`, `max()`, `sum()` (on `map(ord, s)`) work on strings. |
| **`in` / `not in` operator** | Fast way to test substring membership. |
| **Looping idioms** | `for ch in s:` or `for i in range(len(s)):` for index-based access. |
| **String methods** | `lower()`, `upper()`, `startswith()`, `find()`, `strip()`, `split()`, `join()`, `replace()`, etc. |
| **String comparison** | Uses alphabetical (lexicographical) ordering, case-sensitive unless normalized. |
| **Parsing patterns** | Combine `find()` and slicing or use `split()` to extract pieces from text. |
| **Formatting** | f-strings (`f"Hi {name}"`) or `str.format()` replace old `%` operator. |

---


## 🔑 Syntax Cheatsheet

```python
s = "Monty Python"

# indexing / slicing
s[0]        # 'M'
s[-1]       # 'n'
s[6:12]     # 'Python'
s[:5]       # 'Monty'
s[::-1]     # 'nohtyP ytnoM'  (reverse)

# immutability
new = s[:5] + "!"             # concatenate to make a new string

# searching
"Py" in s                     # True
s.find("Py")                  # 6  (-1 if not found)

# case handling
s.lower()                     # 'monty python'
s.upper().startswith("MONT")  # True

# splitting / joining
words = s.split()             # ['Monty', 'Python']
":".join(words)               # 'Monty:Python'

# stripping whitespace
line = "  hello \n"
line = line.strip()           # 'hello'

# f-string formatting
name = "Michelle"
print(f"Hello, {name}!")


## 🧐 Common Pitfalls

| Mistake | Fix |
| ----------- | ----------- |
| **Off-by-one in slicing** (`s[0:len(s)]` excludes last char) | Remember slices stop *before* the end index. |
| **Using `replace()` without reassignment** | `s.replace("x","y")` returns a new string; assign it back. |
| **Case-sensitive comparisons** | Normalize with `.lower()` before comparing. |
| **Trying to mutate `s[0] = 'h'` | Build a new string: `s = 'h' + s[1:]`. |


## 🧩 Mini-Exercises

1. **Vowel counter**  
   Count vowels in a user-supplied word (case-insensitive).

2. **Find the domain**  
   Given `"From user@example.com Sat 2025"` extract `"example.com"`.

3. **Palindrome test**  
   Ask for a phrase, ignore spaces/punctuation/case, report if it’s a palindrome.

4. **CSV to list**  
   Prompt for a comma-separated line, split into a clean list (use `.strip()` on each item).

5. **First & last swap**  
   Write a function `swap_ends(s)` that returns a new string with first and last characters exchanged.

*(Put solutions in `playground/Chapter6_sandbox.py`.)*


## 🛠 Handy Method Table

| Method | Purpose | Example |
|--------|---------|---------|
| `s.lower()` / `s.upper()` | case normalization | `"Hi".lower() → 'hi'` |
| `s.startswith("pre")` | prefix test | `"prefix".startswith("pre")` |
| `s.strip()` / `lstrip()` / `rstrip()` | remove whitespace | `"  x \n".strip()` |
| `s.find(sub)` | first index of `sub` or `-1` | |
| `s.count(sub)` | occurrences of `sub` | `"aaa".count("a") → 3` |
| `s.replace(old, new)` | global substitution | |
| `s.split(delim)` | split into list | `"a,b".split(',')` |
| `'delim'.join(list)` | join list → string | |






