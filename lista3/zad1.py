class Zad1:
    def __init__(self):
        self.length_of_ribbon = 0
        self.a_length = 0
        self.b_length = 0
        self.c_length = 0
        self.table = []
        self.smallest = 0
        self.biggest = 0
    def load_data(self):
        tmp_table = input().split()
        self.length_of_ribbon = int(tmp_table[0])
        self.a_length = int(tmp_table[0])
        self.b_length = int(tmp_table[0])
        self.c_length = int(tmp_table[0])
        self.table = [-1] * self.length_of_ribbon
        self.smallest = min(self.c_length, self.b_length, self.a_length)
        self.biggest = max(self.c_length, self.b_length, self.a_length)


