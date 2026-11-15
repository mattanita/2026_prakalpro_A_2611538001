# Part A
print("=== PART A ===")

text = "Infomatika"
print(text[-1])
print(text.upper())
print(text[0:20])

print()

# Part B
print("=== PART B ===")

text = "Algoritma dan Pemrograman"
count = 0

for char in text:
    if char in "aiueoAIUEO":
     count += 1

print("Vowels:", count)

print()

print("=== MY FULL NAME ====")
text = "Matt Anita"
count = 0

for char in text:
   if char in "aiueoAIUEO":
        count += 1

print("Vowels:", count)

