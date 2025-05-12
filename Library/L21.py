from typing import List, Tuple

def binomial(n: int, k: int) -> int:
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]

def cut_rod(p: List[int], n: int) -> Tuple[List[int], List[int]]:
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s

def lcs(x: str, y: str) -> str:
    m, n = len(x), len(y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
            else:
                c[i + 1][j + 1] = max(c[i + 1][j], c[i][j + 1])
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs_str.append(x[i - 1])
            i -= 1
            j -= 1
        elif c[i - 1][j] >= c[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs_str))

if __name__ == "__main__":
    print(binomial(10, 5))
    r, s = cut_rod([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10)
    print(r)
    print(s)
    print(lcs("ABCBDAB", "BDCABA"))
