def count(str) :
    c = dict()
    words = str.split()

    for word in words :
        if word in c :
            c[word] = c[word] + 1
        else :
            c[word] = 1
    return c
s = input("Enter the sentance: ")
c = count(s)
for k,v in c.items() :
    print(k + " : " + str(v))
