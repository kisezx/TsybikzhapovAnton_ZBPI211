def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n




def filter_even(li):
  k = list(filter(lambda x: x % 2 == 0, li))
  return k

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = filter_even(l)


def square(li):
  return list(map(lambda x: x ** 2, li))


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = square(l)




def bin_search(li, element):
    try:
        index = li.index(element)
    except ValueError:
        index = -1
    return index
sortedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 7




def is_palindrome(str):
    str="".join(c for c in str if c.isalpha()).lower()
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

s = "Рђ СЂРѕР·Р° СѓРїР°Р»Р° РЅР° Р»Р°РїСѓ РђР·РѕСЂР°"
ans = is_palindrome(s)
if (ans):
    print("Yes")
else:
    print("No")



def calculate(path2file):
    list = []
    file1 = open(path2file, "r")
    text = file1.readlines()
    for i in text:
        line = i.split("    ")
        if (line[0] == "+"):
            sum = int(line[1]) + int(line[2].replace("\n", ""))
            list.append(sum)
        if (line[0] == "-"):
            sum = int(line[1]) - int(line[2].replace("\n", ""))
            list.append(sum)
        if (line[0] == "*"):
            sum = int(line[1]) * int(line[2].replace("\n", ""))
            list.append(sum)
        if (line[0] == "//"):
            sum = int(line[1]) // int(line[2].replace("\n", ""))
            list.append(sum)
        if (line[0] == "%"):
            sum = int(line[1]) % int(line[2].replace("\n", ""))
            list.append(sum)
        if (line[0] == "**"):
            sum = int(line[1]) ** int(line[2].replace("\n", ""))
            list.append(sum)
    return ','.join([str(i) for i in list])

path = "test_input_file_1.txt"
string = calculate(path)




def substring_slice(path1, path2):
    list = []
    file1 = open(path1, "r")
    file2 = open(path2, "r")
    text1 = file1.readlines()
    text2 = file2.readlines()
    for i in range(len(text1)):
        line = text2[i].split(" ")
        list.append(text1[i][int(line[0]):int(line[1].replace("\n", "")) + 1])
    return " ".join(list)

path1 = "test_import_file_2_1.txt"
path2 = "test_import_file_2_2.txt"
text = substring_slice(path1, path2)



import json
import re


def decode_ch(string):
    text = ""
    periodic_table = json.load(open("periodic_table.json", encoding='utf-8'))
    list = re.split('(?=[A-Z])', string)
    for i in list:
        if i != "":
            text += periodic_table[i]
    return text


line = "NOTiFICaTiON"




from statistics import mean


class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.grades = grades

    def __add__(self, other):
       return "{} is friends with {}".format(self.name, other.name)

    def __str__(self):
       return self.fullname

    def greeting(self):
       print("Hello, i am Student")

    def mean_grade(self):
       return mean(self.grades)

    def is_otlichnik(self):
       if(self.mean_grade() >= 4.5):
           print("YES")
       else: print("NO")

student1 = Student("school", "boy", [5, 4, 5, 5])




class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    raise MyError("TEST ERROR")
except MyError as ex:
    
