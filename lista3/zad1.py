
def mid_el(a,b,c):
    if (a >= b and b >=c) or (a <= b and b <=c):
        return b
    if (b >= a and a >= c) or (b <= a and a <= c):
        return a
    else:
        return c

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
        self.table = [-1] * (self.length_of_ribbon + 1)
        self.smallest = min(self.c_length, self.b_length, self.a_length)
        self.biggest = max(self.c_length, self.b_length, self.a_length)
        self.mid = mid_el(self.a_length,self.b_length,self.c_length)

    def table_filling(self):
        self.table[self.smallest] = 1
        self.table[self.mid] = 1
        self.table[self.biggest] = 1
        for i in range(self.smallest + 1,self.mid):
            if self.table[i - self.smallest] != -1:
                self.table[i] = self.table[i - self.smallest] + 1

        for i in range(self.mid + 1,self.biggest):
            if self.table[i - self.smallest] != -1:
                self.table[i] = self.table[i - self.smallest] + 1
            if self.table[i - self.mid] != -1:
                self.table[i] = self.table[i - self.mid] + 1

        for i in range(self.biggest,self.length_of_ribbon + 1):
            if self.table[i - self.smallest] != -1:
                self.table[i] = self.table[i - self.smallest] + 1
            if self.table[i - self.mid] != -1:
                self.table[i] = self.table[i - self.mid] + 1
            if self.table[i - self.biggest] != -1:
                self.table[i] = self.table[i - self.biggest] + 1



