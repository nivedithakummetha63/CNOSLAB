def scan():
    n = int(input("Enter the number of tracks to be traversed: "))
    h = int(input("Enter the position of head: "))
    tracks = [0] * (n + 2)
    tracks[0] = 0
    tracks[1] = h

    print("Enter the tracks:")
    for i in range(2, n + 2):
        tracks[i] = int(input())

    tracks.sort()

    for i in range(n + 2):
        if tracks[i] == h:
            j = i
            k = i

    order = []

    p = 0
    while tracks[j] != 0:
        order.append(tracks[j])
        j -= 1
        p += 1

    order.append(tracks[j])

    for p in range(k + 1, n + 2):
        order.append(tracks[p])

    total_seek_time = 0
    print("\nTracks traversed Difference between tracks")
    for i in range(len(order) - 1):
        diff = abs(order[i] - order[i + 1])
        print(f"{order[i]} {diff}")
        total_seek_time += diff

    avg_seek_time = total_seek_time / n
    print(f"\nAverage header movements: {avg_seek_time:.2f}")

scan()
