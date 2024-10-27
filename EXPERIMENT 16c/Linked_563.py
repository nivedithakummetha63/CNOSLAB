def allocate_blocks():
    f = [0] * 50
    p = int(input("Enter how many blocks that are already allocated: "))
    print("Enter the blocks no.s that are already allocated: ")
    for _ in range(p):
        a = int(input())
        f[a] = 1

    while True:
        st, length = map(int, input("Enter the starting index block & length: ").split())
        k = length
        for j in range(st, k + st):
            if f[j] == 0:
                f[j] = 1
                print(f"{j} -> {f[j]}")
            else:
                print(f"{j} -> file is already allocated")
                k += 1

        c = int(input("If you want to enter one more file? (yes-1/no-0): "))
        if c != 1:
            break

allocate_blocks()
