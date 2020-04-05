count = int(input())
for case in range(count):
    n = int(input())
    arr = [[int(a) for a in input().split()] for _ in range(n)]
    k = sum([arr[i][i] for i in range(n)])
    r = sum([len(set(arr[i])) != n for i in range(n)])
    c = sum([len(set([arr[j][i] for j in range(n)])) != n for i in range(n)])
    print('Case #' + str(case + 1) + ': ' + str(k) + ' ' + str(r) + ' ' + str(c))
