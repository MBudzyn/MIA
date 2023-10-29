
def smallest_number_of_slices(table_of_hairs,max_length):
    result = 0
    during_cut = False
    for hair in table_of_hairs:
        if hair <= max_length and during_cut:
            during_cut = False
            result += 1
        if hair > max_length:
            during_cut = True
    if during_cut:
        return result + 1
    else:
        return result

class Zad2():
    def __init__(self):
        self.table_with_hairs = []
        self.number_of_hairs = 0
        self.number_of_command = 0
        self.favorite_number = 0
    def load_data(self):
        self.number_of_hairs,self.number_of_command,self.favorite_number = map(int,input().split())
        self.table_with_hairs = list(map(int, input().split()))
    def execute_0_command(self):
        print(smallest_number_of_slices(self.table_with_hairs,self.favorite_number))
    def execute_1_command(self,index_to_grow,grow_by):
        self.table_with_hairs[index_to_grow-1] += grow_by
    def execute_command(self):
        pom_list = list(map(int, input().split()))
        if len(pom_list) == 1:
            self.execute_0_command()
        else:
            self.execute_1_command(pom_list[1],pom_list[2])

    def run(self):
        self.load_data()
        for command in range(self.number_of_command):
            self.execute_command()

zad2 = Zad2()
zad2.run()