f = open("sample.txt","r")
freq = dict()
for line in f :
  words = line.split()
  for word in words :
    if word in freq :
      freq[word] = freq[word] + 1
    else :
      freq[word] = 1
for k,v in freq.items() :
  print(k + ":" + str(v))
