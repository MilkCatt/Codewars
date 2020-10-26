def persistence(n):
    count=0
    #count the number times the while loop is carried out
    while len(str(n))>1:
        j=1
        #set a variable to store the multiplied number
        for i in str(n):
        #iterate through each digit in the number
            j*=int(i)
            #multiply all variables with each digit in the number
        n=j
        count+=1
        #add to the counter
    return count