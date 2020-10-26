def solution(n):
    num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    ans = ""
    counter = 0
    while int(n)>0:
        for i in range(n//num[counter]):
            ans+=rom[counter]
            n-=num[counter]
        counter+=1
    return ans