"""
5
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440
5
0 1
1 3
3 4
0 2
2 4

"""


def helper(tasks):
    c_next = 0
    j_next = 0
    ans = ''
    for (start, end) in tasks:
        if start >= c_next:
            ans += 'C'
            c_next = end
        elif start >= j_next:
            ans += 'J'
            j_next = end
        else:
            return None
    return ans


count = int(input())
for case in range(count):
    n = int(input())
    tasks = [[int(a) for a in input().split()] for _ in range(n)]
    indices, tasks = zip(*sorted(enumerate(tasks), key=lambda x: x[1]))
    ans = helper(tasks)
    if ans:
        ans = ''.join([a[1] for a in sorted(zip(indices, ans))])
    else:
        ans = 'IMPOSSIBLE'
    print('Case #%d: %s' % (case + 1, ans))
