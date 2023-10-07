def permutation_3(table1,table2,table3):
    res = []
    for i in table1:
        for j in table2:
            for k in table3:
                res.append(int(i+j+k))
                res.append(int(j+i+k))
                res.append(int(i+k+j))
                res.append(int(j+k+i))
                res.append(int(k+i+j))
                res.append(int(k+j+i))
    return res

def cubes_for_masha():
    cube1 = []
    cube2 = []
    cube3 = []
    number_of_dice = int(input())
    for i in range(number_of_dice):
        if i==0:
            cube1 = input().split(" ")
        if i==1:
            cube2 = input().split(" ")
        if i==2:
            cube3 = input().split(" ")

#cubes_for_masha()
print(len(permutation_3(["0","1","2"],["3","4","5"],["6","7","8"])))