def expanded_form(num):
    result = ""
    n_list = []
    for i in str(num):
        n_list.append(i)
    x = len(n_list)-1
    for j in n_list:
        if j == "0":
            x -= 1
        else:
            result += " " + j + "0"*x + " +"
            x -= 1
    return result[1:-2]