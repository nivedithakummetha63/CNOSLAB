def scan():
    tracks = list(map(int, input("Enter the track positions: ").split()))
    h = int(input("Enter the starting position: "))
    tot = max(tracks)
    tracks.insert(0, 0)
    tracks.append(tot)
    tracks.sort()
    if h not in tracks:
        tracks.append(h)
        tracks.sort()
    j = tracks.index(h)
    atr = []
    p = 0
    while tracks[j] != tot:
        atr.append(tracks[j])
        j += 1
        p += 1
    atr.append(tracks[j])
    p += 1
    i = 0
    while p != len(tracks) and tracks[i] != h:
        atr.append(tracks[i])
        i += 1
        p += 1
    total_seek_time = 0
    print("Tracks traversed Difference Between tracks")
    for j in range(len(atr) - 1):
        diff = abs(atr[j] - atr[j + 1])
        print(f"{atr[j]} {diff}")
        total_seek_time += diff
    avg_seek_time = total_seek_time / (len(tracks) - 2)
    print(f"\nAverage seek time: {avg_seek_time:.7f}")
scan()
