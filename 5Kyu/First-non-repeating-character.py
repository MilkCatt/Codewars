def first_non_repeating_letter(string):
    char_order = []
    ctr = {}
    lstring = string.lower()
    for c in lstring:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1 
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return string[lstring.index(c)]
    return ""