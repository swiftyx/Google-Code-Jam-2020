def ask(pos):
    print(pos + 1)
    i = input()
    if i == 'N':
        exit()
    return int(i)


def naive(pos, bits):
    ask(pos)  # I don't care
    now_pos = ask(pos)
    if now_pos != bits[pos]:
        flip(bits)


# Swap 0 with 1
def flip(bits):
    B = len(bits)
    for i in range(B):
        bits[i] = 1 - bits[i]

# Reverse and swap 0 & 1
def rev_flip(bits):
    B = len(bits)
    for i in range(B // 2):
        bits[B - 1 - i], bits[i] = 1 - bits[i], 1 - bits[B - 1 - i]


T, B = [int(a) for a in input().split()]
for case in range(T):
    bits = [-1] * B
    start = 0
    end = B - 1
    same_P = None
    oppo_P = None

    for j in range(5):
        bits[start] = ask(start)
        bits[end] = ask(end)
        if same_P is None and bits[start] == bits[end]:
            same_P = start
        if oppo_P is None and bits[start] != bits[end]:
            oppo_P = end
        start += 1
        end -= 1

    for i in range(1, 15):
        # Checking
        if same_P is None:
            naive(oppo_P, bits)
        elif oppo_P is None:
            naive(same_P, bits)
        else:
            now_same_start = ask(same_P) == bits[same_P]
            now_oppo_start = ask(oppo_P) == bits[oppo_P]
            if now_same_start:
                if now_oppo_start:
                    pass  # identity
                else:  # Reverse
                    bits = bits[::-1]
            else:
                if now_oppo_start:
                    rev_flip(bits)
                else:
                    flip(bits)
        # Normal Reading Bits
        for j in range(4):
            if start == B:
                ask(0)
                ask(0)
            else:
                bits[start] = ask(start)
                bits[end] = ask(end)
                if same_P is None and bits[start] == bits[end]:
                    same_P = start
                if oppo_P is None and bits[start] != bits[end]:
                    oppo_P = end
                start += 1
                end -= 1
    print(''.join(map(str, bits)))
    if input() == 'N':
        exit()
