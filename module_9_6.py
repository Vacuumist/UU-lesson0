def all_variants(text):
    l = 1
    while l <= len(text):
        i = 0
        while i + l <= len(text):
            yield text[i : i + l]
            i += 1
        l += 1


a = all_variants("abcd")
for i in a:
    print(i)