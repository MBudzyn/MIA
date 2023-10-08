def permutation_3(table1,table2,table3,number_of_perm):
    res = []
    if number_of_perm == 3:
        for i in table1:
            for j in table2:
                for k in table3:
                    res.append(int(i+j+k))
                    res.append(int(j+i+k))
                    res.append(int(i+k+j))
                    res.append(int(j+k+i))
                    res.append(int(k+i+j))
                    res.append(int(k+j+i))

    for i in range(6):
        for j in range(6):
            res.append(int(table1[i] + table2[j]))
            res.append(int(table1[i] + table3[j]))
            res.append(int(table2[i] + table3[j]))
            res.append(int(table2[i] + table1[j]))
            res.append(int(table3[i] + table2[j]))
            res.append(int(table3[i] + table1[j]))

    for i in range(6):
        if table1[i] != "":
            res.append(int(table1[i]))
        if table2[i] != "":
            res.append(int(table2[i]))
        if table3[i] != "":
            res.append(int(table3[i]))

    return list(set(res))


def cubes_for_masha():
    cube1 = []
    cube2 = []
    cube3 = []
    number_of_dice = int(input())
    if number_of_dice == 2:
        cube3 = ["","","","","",""]

    for i in range(number_of_dice):
        if i==0:
            cube1 = input().split(" ")
        if i==1:
            cube2 = input().split(" ")
        if i==2:
            cube3 = input().split(" ")
    if number_of_dice ==1:
        for i in range(1,8):
            if str(i) not in cube1:
                return i-1

    res = (permutation_3(cube1,cube2,cube3,number_of_dice))
    res.sort()
    print(res)
    if res[0] == 0:
        res = res[1:]
    for i in range(1,1000):
        if i != res[i-1]:
            return i-1

cubes_for_masha()
