import json
import re
from statistics import mean


def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n


def filter_even(li):
    k = list(filter(lambda x: x % 2 == 0, li))
    return k


def square(li):
    return list(map(lambda x: x ** 2, li))


def bin_search(li, element):
    try:
        index = li.index(element)
    except ValueError:
        index = -1
    return index


def is_palindrome(string):
    string = "".join(c for c in string if c.isalpha()).lower()
    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


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


def substring_slice(path2file_1, path2file_2):
    list = []
    file1 = open(path2file_1, "r")
    file2 = open(path2file_2, "r")
    text1 = file1.readlines()
    text2 = file2.readlines()
    for i in range(len(text1)):
        line = text2[i].split(" ")
        list.append(text1[i][int(line[0]):int(line[1].replace("\n", "")) + 1])
    return " ".join(list)


def decode_ch(string_of_elements):
    text = ""
    periodic_table = json.load(open("periodic_table.json", encoding='utf-8'))
    list = re.split('(?=[A-Z])', string_of_elements)
    for i in list:
        if i != "":
            text += periodic_table[i]
    return text


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
        if (self.mean_grade() >= 4.5):
            print("YES")
        else:
            print("NO")


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

