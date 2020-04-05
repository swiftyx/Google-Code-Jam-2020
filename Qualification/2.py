"""
8
0000
101
111000
1
021
312
4
221

"""

count = int(input())
for case in range(count):
    s = input()
    ans = ''
    nest = 0
    for c in s:
        n = int(c)
        diff = n - nest
        if diff > 0:
            ans += '(' * diff + c
            nest = n
        elif diff < 0:
            ans += ')' * -diff + c
            nest = n
        else:
            ans += c
    ans += ')' * nest
    print('Case #%d: %s' % (case + 1, ans))
