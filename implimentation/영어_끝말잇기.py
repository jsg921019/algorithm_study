# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3

def solution(n, words):
    vocab = set([words[0]])
    for i in range(1, len(words)):
        prev_word, curr_word = words[i-1], words[i]
        if curr_word in vocab or prev_word[-1] != curr_word[0]:
            d, r = divmod(i, n)
            return [r+1, d+1]
        vocab.add(curr_word)
    return [0, 0]