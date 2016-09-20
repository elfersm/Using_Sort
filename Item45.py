def bubSort(my_list):
    for numb in range(len(my_list)-1, 0, -1):
        for i in range(numb):
            if my_list[i] > my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp

my_list = [1, 2, 13, 45, 67, 998]
bubSort(my_list)
print my_list

list_two = [89, 23, 33, 45, 10, 12, 45, 45, 45]
bubSort(list_two)
print list_two
