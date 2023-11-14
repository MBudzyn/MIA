
def has_divisor(number):
    for i in range(2,int(number**(1/2)) + 1):
        if number % i == 0:
            return number//i
    return False
def is_prime(number):
    if number == 1:
        return False
    for i in range(2,int(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True
def is_T_prime(number):
    divisor = has_divisor(number)
    if divisor:
        if is_prime(divisor) and (number%divisor != 0 or number == divisor**2):
            return True
    return False

class Zad2:

    def __init__(self):
        self.number_of_data = 0
        self.table_with_data = []
        self.table_with_results = []
    def load_data(self):
        self.number_of_data = int(input())
        self.table_with_data = list(map(int,input().split()))
    def fill_result(self):
        for i in self.table_with_data:
            if is_T_prime(i):
                self.table_with_results.append("YES")
            else:
                self.table_with_results.append("NO")
    def print_result(self):
        for i in self.table_with_results[:-1]:
            print(i)
        print(self.table_with_results[-1],end="")
    def run(self):
        self.load_data()
        self.fill_result()
        self.print_result()

zad2 = Zad2()
zad2.run()

