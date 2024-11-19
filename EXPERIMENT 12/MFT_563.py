def main():
    ms = int(input("Enter total memory (Bytes): "))
    bs = int(input("Enter block size (Bytes): "))
    n = int(input("Enter number of processes: "))
    
    mp = [int(input(f"Memory for process {i+1} (Bytes): ")) for i in range(n)]
    nob, ef, tif, p = ms // bs, ms % bs, 0, 0

    print(f"\nBlocks available: {nob}\n\nPROCESS\tREQUIRED\tALLOCATED\tINTERNAL FRAG.")
    for i in range(n):
        print(f"\n{i+1}\t{mp[i]}", end='')
        if mp[i] > bs:
            print("\tNO\t---")
        else:
            print(f"\tYES\t{bs - mp[i]}")
            tif += bs - mp[i]
            p += 1
        if p == nob:
            print("\nMemory Full, remaining processes can't be accommodated.")
            break

    print(f"\n\nTotal Internal Fragmentation: {tif}")
    print(f"Total External Fragmentation: {ef}")

if __name__ == "__main__":
    main()
