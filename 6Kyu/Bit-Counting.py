def countBits(n):
    ans = 0
    print(bin(int(n)))
    for i in str(bin(int(n))):
        if i == "1":
            ans += 1
    return ans