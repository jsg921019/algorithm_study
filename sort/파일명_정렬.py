# https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3#

# solution 1

def solution(files):

    def key(file):

        head, number = '', ''

        for char in file:
            if not char.isdigit():
                head += char
            else:
                break

        for char in file[len(head):]:
            if char.isdigit() and len(number) < 5:
                number += char
            else:
                break
            
        return (head.lower(), int(number))

    return sorted(files, key=key)

# solution 2

import re

def solution(files):

    def key(file):
        head, number = re.match('(\D+)(\d{1,5})', file).groups()
        return (head.lower(), int(number))

    return sorted(files, key=key)