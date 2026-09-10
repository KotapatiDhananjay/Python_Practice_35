import re

s1 = "We are learning regex in Python."
pat = "[a-z]{3}"
match_obj = re.match(pat, s1)
print(match_obj)

phones = "John-8956237845, Carol-7845128956, mark-0123456578"
pat = r"[0-9]{10}"
match_obj = re.search(pat, phones)
print(match_obj)

phones = "John-8956237845, Carol-7845128956, mark-0123456578"
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj)

# findall()
phones = "John-8956237845, Carol-7845128956, mark-0123456578, Rafel-9874150"
pat = r"[0-9]+"
match_obj = re.findall(pat, phones)
print(match_obj)

phones = "John-8956237845, Carol-7845128956, mark-0123456578, Rafel-9874150, Dan-789123045698715623"
# fetch all phone numbers, the phone numbers are exactly 7 digits and should not exceed 15 digit
pat = r"[0-9]{7,15}"
match_obj = re.findall(pat, phones)
print(match_obj)

# fetch all phone numbers, the phone numbers are atleast 7 digits
pat = r"[0-9]{7,}" # 7 or more
match_obj = re.findall(pat, phones)
print(match_obj)

# \b
pat = r"\b[0-9]{7,15}\b"
match_obj = re.findall(pat, phones)
print(match_obj)

# finditer()
pat = r"\b[0-9]{7,15}\b"
match_obj_iter = re.finditer(pat, phones)

for matches in match_obj_iter:
    print(matches)

s2 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
"""
pat = "Sunday"
replacement = "Friday"
"""
pat = r"S[a-z]+"
replacement = "Friday"
result = re.sub(pat, replacement, s2)
print(result)
"""
result = re.sub(pat, replacement, s2, count=1)
print(result)
"""

message = """We are learning re. Using re, we can find a pattern in a given string.
Using the sub(), we can replace the pattern with a given string as well."""
patt = r'\bre\b'
replacement = 'Regular expression'
result = re.sub(patt, replacement, message)
print(result)