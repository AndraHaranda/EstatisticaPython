import itertools

num, num1, num2, num3 = map(int, sys.stdin.readline().split())

a = [num, num1, num2, num3]

for i in xrange(1,len(a)+1)
   print list(itertools.combinations(a, i))

print(sorted(a, i))