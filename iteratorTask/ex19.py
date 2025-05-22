words = ["apple", "banana", "grape", "mountain", "cat", "dog", "tree", "house", "sky", "book"]

for word in words:
    for ind,itm in enumerate(word):
        if itm == "a":
            print(ind)
            break