import sys
x1, y1, x2, y2 = map(int, sys.stdin.read().split()[:4])
print("YES" if (x1 + y1) % 2 == (x2 + y2) % 2 else "NO")