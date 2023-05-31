# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

def solution(phone_book):
    phone_book.sort()
    for str1, str2 in zip(phone_book[:-1], phone_book[1:]):
        if str2.startswith(str1):
            return False
    return True