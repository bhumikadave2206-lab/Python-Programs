# (13) Frequency of Characters
text = "Python is easy language"
freq = {}
for char in text:
 freq[char] = freq.get(char, 0) + 1
print(freq)
