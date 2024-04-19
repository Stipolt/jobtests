# 1

def unique_elements(input_list):
    return list(set(input_list))


# 2

def prime_numbers(minimum, maximum):
    prime_list = []
    for num in range(minimum, maximum + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list
    
# 3

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        
# 4

def sort_strings_by_length(strings):
    # Сортировка списка строк по длине, сначала по возрастанию
    sorted_asc = sorted(strings, key=len)
    print("Сортировка по длине, по возрастанию:", sorted_asc)

    # Сортировка списка строк по длине, затем по убыванию
    sorted_desc = sorted(strings, key=len, reverse=True)
    print("Сортировка по длине, по убыванию:", sorted_desc)
    
    