combo_list = []
for num in range(100):
    stringed_num = "{:0>2}".format(num)
    if num != 99:
        if stringed_num.split("") not in combo_list:
            combo_list.append(stringed_num.split(""))
        print(int(stringed_num), end=", ")