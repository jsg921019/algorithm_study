# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3

import math
def solution(w,h):
    a = math.gcd(w, h)
    return w*h - (w + h - a)