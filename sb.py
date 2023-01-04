
words = open("words.txt")

special = input("Input the special character: ")
regular = input("Input the regular 6 characters: ")
goodWords = []

for w in words:
    ws = w.strip()
    if ((ws not in goodWords) and (special in ws)):
        flag = True
        for c in ws:
            if (c not in regular and c not in special):
                flag = False
                break
        if flag:
            goodWords.append(ws)
        
print("THE FOLLOWING GOOD WORDS WERE FOUND:")
for g in goodWords:
    print(f"    {g}")

