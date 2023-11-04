class Zad3():
    def __init__(self):
        self.number_of_marks = 0
        self.last_mark = 0
        self.table_with_marks = []
        self.women_distance = 0
        self.men_distance = 0

    def load_data(self):
        self.number_of_marks,self.last_mark,self.women_distance,self.men_distance = map(int,input().split())
        self.table_with_marks = list(map(int,input().split()))

