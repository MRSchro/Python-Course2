# 📖 Python for Everybody — Chapter 7: Files

| Key idea | One-sentence takeaway |
|----------|-----------------------|
| **File handles** | `open()` returns a handle you read or write through. |
| **Text mode vs. binary** | Default `'r'` / `'w'` operate on *str*; use `'rb'` / `'wb'` for bytes. |
| **Iteration** | `for line in fh:` streams the file line-by-line (memory-efficient). |
| **Whitespace stripping** | `line.rstrip()` removes `\n`; combine with `.lower()` for case-free parsing. |
| **Error handling** | Always `try/except` around `open()` to catch `FileNotFoundError`. |
| **`with` statement** | Context manager closes files automatically—preferred modern style. |

---

## 🔑 Syntax Cheatsheet
```python
# open for reading (UTF-8 default)
fh = open("mbox.txt", "r")

# safer:
with open("mbox.txt") as fh:        # closes on exit
    for line in fh:                 # iterate lazily
        line = line.rstrip()        # strip newline
        ...

# read whole file at once (small files only)
data = open("small.txt").read()

# write
with open("output.txt", "w") as out:
    out.write("Hello\n")

| Mode | Meaning |
| ----------- | ----------- |
| 'r' | read (default) |
| 'w' | truncate or create |
| 'a' | append |
| 'rb' | read binary |
| 'x' | create, fail if exists |


## 💡 Reading Tips

* Combine `line = line.strip()` with `if not line: continue` to skip blank lines.  
* Use `enumerate(fh, start=1)` to iterate with line numbers.  
* Remember: `readlines()` loads *all* lines into a list—handy for small files, dangerous for large ones.


## 🧐 Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Reading huge files with `.read()` | Use `for line in fh:` instead. |
| Forgetting to close the file | Use `with open(...) as fh:`. |
| Extra blank lines on Windows | Open with `newline=''` **or** write `\n` exactly once. |
| Treating binary data as text | Open with `'rb'` / `'wb'` and handle bytes. |




