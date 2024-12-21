# https://oij.edu.pl/oij16/etap3/zadania/zag/zagzad.pdf

s = input()
suma = 0
for i in range(len(s)):
    suma += ord(s[i])
print(chr(2015 - suma)) # 2015 to suma kodów ASCII wielkich liter (A-Z)