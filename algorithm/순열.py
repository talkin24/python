# 중복순열
for i1 in range(1,4):
    for i2 in range(1,4):
        for i3 in range(1,4):
            print(i1, i2, i3)

# 중복 허용하지 않는 순열
for i1 in range(1,4):
    for i2 in range(1,4):
        if i1 != i2:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
