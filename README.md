# Python Regular Expressions - `re` Module 🔎

A beginner-friendly Python program demonstrating different functions and patterns from the built-in **`re` (Regular Expression)** module.

## 📌 Description

This example covers the most commonly used Regex functions in Python:

* `re.match()`
* `re.search()`
* `re.findall()`
* `re.finditer()`
* `re.sub()`

It also demonstrates Regex patterns for matching numbers, word boundaries, repetitions, and replacing text.

## 💻 Code

```python
import re

# match()
s1 = "We are learning regex in Python."

pat = "[a-z]{3}"
match_obj = re.match(pat, s1)
print(match_obj)


# search()
phones = "John-8956237845, Carol-7845128956, mark-0123456578"

pat = r"[0-9]{10}"
match_obj = re.search(pat, phones)
print(match_obj)


# findall()
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj)


# Find all groups of digits
phones = "John-8956237845, Carol-7845128956, mark-0123456578, Rafel-9874150"

pat = r"[0-9]+"
match_obj = re.findall(pat, phones)
print(match_obj)


# Phone numbers between 7 and 15 digits
phones = "John-8956237845, Carol-7845128956, mark-0123456578, Rafel-9874150, Dan-789123045698715623"

pat = r"[0-9]{7,15}"
match_obj = re.findall(pat, phones)
print(match_obj)


# Phone numbers with at least 7 digits
pat = r"[0-9]{7,}"
match_obj = re.findall(pat, phones)
print(match_obj)


# Using word boundaries
pat = r"\b[0-9]{7,15}\b"
match_obj = re.findall(pat, phones)
print(match_obj)


# finditer()
pat = r"\b[0-9]{7,15}\b"
match_obj_iter = re.finditer(pat, phones)

for matches in match_obj_iter:
    print(matches)


# sub()
s2 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"

pat = r"S[a-z]+"
replacement = "Friday"

result = re.sub(pat, replacement, s2)
print(result)


# Replacing the word "re"
message = """We are learning re. Using re, we can find a pattern in a given string.
Using the sub(), we can replace the pattern with a given string as well."""

patt = r'\bre\b'
replacement = 'Regular expression'

result = re.sub(patt, replacement, message)
print(result)
```

## 🧠 Regex Functions

### 1. `re.match()`

```python
re.match(pattern, string)
```

Checks for a match **only at the beginning** of the string.

```python
pat = "[a-z]{3}"
re.match(pat, s1)
```

Since the string starts with `"We "` and not three lowercase letters, it returns `None`.

---

### 2. `re.search()`

```python
re.search(pattern, string)
```

Searches for the **first matching pattern anywhere** in the string.

Example:

```python
pat = r"[0-9]{10}"
```

It finds the first 10-digit phone number.

---

### 3. `re.findall()`

```python
re.findall(pattern, string)
```

Returns **all matching values as a list**.

Example:

```text
['8956237845', '7845128956', '0123456578']
```

---

### 4. `re.finditer()`

```python
re.finditer(pattern, string)
```

Returns an iterator containing **match objects**.

You can get the matched value using:

```python
matches.group()
```

and its position using:

```python
matches.span()
```

---

### 5. `re.sub()`

```python
re.sub(pattern, replacement, string)
```

Used to **replace matching text**.

Example:

```python
pat = r"S[a-z]+"
replacement = "Friday"

result = re.sub(pat, replacement, s2)
```

This replaces:

```text
Sunday
```

with:

```text
Friday
```

## 🔢 Important Regex Patterns

| Pattern   | Meaning                                        |
| --------- | ---------------------------------------------- |
| `[0-9]`   | Any digit from 0 to 9                          |
| `[a-z]`   | Any lowercase letter                           |
| `[A-Z]`   | Any uppercase letter                           |
| `{3}`     | Exactly 3 repetitions                          |
| `{7,15}`  | Between 7 and 15 repetitions                   |
| `{7,}`    | 7 or more repetitions                          |
| `+`       | One or more repetitions                        |
| `\b`      | Word boundary                                  |
| `S[a-z]+` | Starts with `S`, followed by lowercase letters |

## 📱 Phone Number Examples

### Exactly 10 digits

```python
r"[0-9]{10}"
```

Matches:

```text
8956237845
```

### 7 to 15 digits

```python
r"\b[0-9]{7,15}\b"
```

Matches complete numbers containing between **7 and 15 digits**.

The `\b` prevents a 7–15 digit portion from being extracted from a longer number.

For example, a 16-digit number will not be treated as a valid 7–15 digit phone number.

## 🔄 `match()` vs `search()` vs `findall()`

| Function     | Purpose                            |
| ------------ | ---------------------------------- |
| `match()`    | Checks only at the beginning       |
| `search()`   | Finds the first match anywhere     |
| `findall()`  | Finds all matches as a list        |
| `finditer()` | Finds all matches as match objects |
| `sub()`      | Replaces matching text             |

## 🛠️ Technologies Used

* Python 3
* `re` module

## ▶️ How to Run

Save the program as:

```text
regex_functions.py
```

Run:

```bash
python regex_functions.py
```

## 📚 Learning Outcome

This project helps understand:

* Regular Expressions
* `re.match()`
* `re.search()`
* `re.findall()`
* `re.finditer()`
* `re.sub()`
* Regex quantifiers
* Word boundaries
* Pattern matching
* Text replacement

## 👨‍💻 Author

**Kotapati Dhananjay**
