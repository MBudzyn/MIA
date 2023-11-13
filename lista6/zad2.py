

class Zad2:
    def __init__(self):
        self.number_of_data = 0
        self.table_with_data = []
        self.table_with_results = []
    def load_data(self):
        self.number_of_data = int(input())
        self.table_with_data = list(map(int,input().split()))
    def fill_result(self):
        pass
    def print_result(self):
        for i in self.table_with_results[:-1]:
            print(i)
        print(self.table_with_results[-1],end="")
    def run(self):
        self.load_data()
        self.fill_result()
        self.print_result()

