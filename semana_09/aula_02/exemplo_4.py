st = input("Frase: ")

# A: 65
# a: 97
# ----- 32

# N: 78
# n: 110
# ----- 32

#print(st.upper())
#print(st)

# min -> mai
for s in st:
    if (s >= 'a') and (s <= 'z'):
        print(chr(ord(s) - 32))
    else:
        print(s)
