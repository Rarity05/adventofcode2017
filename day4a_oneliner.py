filepath = 'input.txt'

i = 0
#with open(filepath) as fp:
fp = ["aa bb cc dd aa bb cc"]
res = 0
i += i+1
for line in fp:
 print(line)
 words = line.split()
 res += 1 if len([1 for indx1, elem in enumerate(words) for indx2, duplicate in enumerate(words) if (indx2!=indx1 and elem==duplicate)]) > 0 else 0

#print(i)
print(res)
