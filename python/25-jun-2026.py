import re

text = """
Hello Kailash
Email: kailash123@gmail.com
Phone: 9876543210
Year: 2026
Python Python Python
"""

# 1. search()
print("SEARCH")
result = re.search(r"\d{10}", text)
print(result.group())

# 2. findall()
print("\nFINDALL")
numbers = re.findall(r"\d+", text)
print(numbers)

# 3. match()
print("\nMATCH")
m = re.match(r"Hello", text.strip())
if m:
    print("Matched:", m.group())

# 4. fullmatch()
print("\nFULLMATCH")
mobile = "9876543210"
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Valid Mobile Number")

# 5. finditer()
print("\nFINDITER")
for i in re.finditer(r"Python", text):
    print("Found at:", i.start())

# 6. sub()
print("\nSUB")
new_text = re.sub("Python", "Data Science", text)
print(new_text)

# 7. split()
print("\nSPLIT")
data = "Apple,Banana,Mango,Grapes"
items = re.split(",", data)
print(items)

# 8. Email Validation
print("\nEMAIL VALIDATION")
email = "kailash123@gmail.com"
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")