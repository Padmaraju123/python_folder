"""
Given a string, we need to write a Python program that counts and displays all the vowels present in the string.
Let’s explore different ways of counting and displaying vowels in a string.

We need to identify all the vowels in the string both uppercase and lowercase.
We should display each vowel found.
We should also count how many total vowels are in the string.
"""

word = input("Enter the word: ")
lis_vowels = "aeiou"
dik = dict()
for v in word:
    if v.lower() in lis_vowels and v not in dik:
        dik[v] = 1
    elif v in dik:
        dik[v]= dik[v]+1
print(dik)


