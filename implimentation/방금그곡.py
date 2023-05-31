# https://programmers.co.kr/learn/courses/30/lessons/17683

def translate(m):
    for note in 'ABCDEFG':
        m = m.replace(note + '#', note.lower())
    return m

def solution(m, musicinfos):

    m = translate(m)
    answer, answer_t = "", 0

    for musicinfo in musicinfos:
        s, e, n, m_ = musicinfo.split(',')
        m_ = translate(m_)
        s_h, s_m = map(int, s.split(':'))
        e_h, e_m = map(int, e.split(':'))
        t = (e_h-s_h)*60 + (e_m-s_m)
        td, tr = divmod(t, len(m_))
        m_ = m_*td + m_[:tr]
        if m in m_ and t > answer_t:
            answer, answer_t = n, t

    return answer if answer else '(None)'