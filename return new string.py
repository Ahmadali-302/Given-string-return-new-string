def stringBits(str_):
    my_list = ''
    for i in range(len(str_)):
        if i % 2 != 0:
            my_list += (str_[i])
    return my_list


s = stringBits(" Heeololeo")
print(s)