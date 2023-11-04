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

    def wich_distances_possible_to_create(self):
        result = [None,None]
        current_length = 0
        for start_index in range(len(self.table_with_marks) -1):
            if result[0] != None and result[1] != None:
                break
            current_index = start_index + 1
            while self.table_with_marks[current_index] - self.table_with_marks[start_index] <= self.men_distance and current_index < len(self.table_with_marks) - 1:
                current_length = self.table_with_marks[current_index] - self.table_with_marks[start_index]
                if current_length == self.men_distance and result[0] == None:
                    result[0] = self.men_distance
                if current_length == self.women_distance and result[1] == None:
                    result[1] = self.women_distance
                current_index += 1

        if result[0] == None and result[1] == None:
            return []
        elif result[0] == None:
            return [result[1]]
        elif result[1] == None:
            return [result[0]]
        else:
            return result

    def None_possible_to_create_case(self):
        for start_index in range(len(self.table_with_marks) - 1):
            current_index = start_index + 1
            current_length = self.table_with_marks[current_index] - self.table_with_marks[start_index]
            while current_length < self.women_distance:
                current_index = current_index + 1
                current_length = self.table_with_marks[current_index] - self.table_with_marks[start_index]
            current_length = 0
            new_mark = self.table_with_marks[start_index] + self.women_distance
            while current_length < self.men_distance:
                current_index = current_index + 1
                current_length = self.table_with_marks[current_index] - new_mark
            if current_length == self.men_distance:
                return [new_mark]
        return [self.women_distance,self.men_distance]












