import sys
t, pres, pulse = map(float, sys.stdin.read().split()[:3])

doctor = t < 35 or t > 38 or pres < 105 or pres > 140 or pulse < 55 or pulse > 110
normal = 36 <= t <= 37 and 110 <= pres <= 130 and 60 <= pulse <= 100

if doctor:
    print("Требуется врач")
elif normal:
    print("Нормальное состояние")
else:
    print("Легкое недомогание")
