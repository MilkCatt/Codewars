def rgb(r, g, b):
    colour_list = [r,g,b]
    for i in colour_list:
        if i >255:
            colour_list[colour_list.index(i)]=255
        elif i<0:
            colour_list[colour_list.index(i)]=0
    print(colour_list)
    a = colour_list[0]
    b = colour_list[1]
    c = colour_list[2]
    ans = '%02x%02x%02x' % (a, b, c)
    return ans.upper()