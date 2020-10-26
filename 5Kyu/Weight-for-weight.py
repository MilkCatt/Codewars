def new_weight(n):
    nw = 0
    for i in str(n):
        nw += int(i)
    return nw

def order_weight(strng):
    weight_list = strng.split(" ")
    weight_val = []
    for i in weight_list:
            weight_val.append(new_weight(i))
    modified_tpl = list(zip(weight_list,weight_val))
    modified_tpl.sort(key = lambda x: x[0])
    modified_tpl.sort(key = lambda x: x[1])
    new_string = ""
    for i in modified_tpl:
        new_string += (i[0] + " ")
    return new_string.strip()
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))