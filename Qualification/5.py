"""
2
3 6
2 3

"""

# TLE On the Hidden Verdict (Test Set 2)


def fill(i, j, c_r, c_c, result):
    n = len(result)
    if j == n:
        if i == n - 1:
            return result
        i += 1
        j = 0
    if i == j:
        return fill(i, j + 1, c_r, c_c, result)
    for v in range(1, n + 1):
        if v not in c_r[i] and v not in c_c[j]:
            c_r[i].add(v)
            c_c[j].add(v)
            result[i][j] = v
            possible = fill(i, j + 1, c_r, c_c, result)
            if possible:
                return possible
            c_r[i].remove(v)
            c_c[j].remove(v)
    return None


def helper(i, k, result):
    n = len(result)
    if i == n:
        if k == 0:
            c_r = [{result[i][i]} for i in range(n)]
            c_c = [{result[i][i]} for i in range(n)]
            possible = fill(0, 0, c_r, c_c, result)
            if possible:
                return possible
        return None
    for k_i in range(1, min(n, k) + 1):
        result[i][i] = k_i
        possible = helper(i + 1, k - k_i, result)
        if possible:
            return possible
        else:
            result[i][i] = 0
    return None


count = int(input())
for case in range(count):
    n, k = [int(a) for a in input().split()]
    result = [[0] * n for _ in range(n)]
    result = helper(0, k, result)
    if result:
        print('Case #%d: POSSIBLE' % (case + 1))
        for line in result:
            print(*line)
    else:
        print('Case #%d: IMPOSSIBLE' % (case + 1))

