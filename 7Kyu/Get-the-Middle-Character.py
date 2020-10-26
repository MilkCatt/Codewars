def get_middle(s):
    half=int(len(s)/2)
    #Set the half length. Rounds down.
    if len(s)%2==0:
    #Test if the length of the string is even
        return (s[half-1]+s[half])
        #Returns concatenated middle two characters of string
    else:
    #If the string is not even, it is odd
        return (s[half])
        #Returns middle character of string (Index rounded down)