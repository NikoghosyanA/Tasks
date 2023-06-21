n, a, b = int(input()), int(input()), int(input())
t1, t2, t3, t4 = 0, 0, 0, 0
z1, z2, z3, z4 = n, 0, 0, 0
sm = 1
s1, s2, s3, s4 = n * a, n * b, n * a, n * b
st1, st2, st3, st4 = True, False, False, False
while True:
    if st1 and z1 > 0:
        t1 += 1
        sm += 1
        if t1 == a:
            st2 = True
            t1 = 0
            z1 -= 1
            z2 += 1
    elif z1 == 0:
        st1 = False
    if st2 and z2 > 0:
        t2 += 1
        if not st1:
            sm += 1
        if t2 == b:
            st3 = True
            t2 = 0
            z2 -= 1
            z3 += 1
    elif z2 == 0:
        st2 = False
    if not st1 and st3 and z3 > 0:
        t3 += 1
        if not st2:
            sm += 1
        if t3 == a:
            st4 = True
            t3 = 0
            z3 -= 1
            z4 += 1
    elif z3 == 0:
        st3 = False
    if not st2 and st4 and z4 > 0:
        t4 += 1
        if t4 == b:
            t4 = 0
            z4 -= 1
        if not st3:
            sm += 1
    elif z4 == 0:
        st4 = False
    if z1 + z2 + z3 + z4 == 0:
        print(sm)
        break
