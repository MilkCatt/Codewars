def square_digits(num):
    squarelist=[int(integer)**2 for integer in str(num)]
    #square each integer in the list
    stringlist=[str(integer)for integer in squarelist]
    #convert list of integers into list of strings for concatenation
    squared_strings="".join(stringlist)
    #concatenate strings
    return(int(squared_strings))
    #return the string as an integer