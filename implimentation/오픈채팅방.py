# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):

    result = []
    uid_dict = {}

    for r in record:
        cmd = r.split()
        if cmd[0] == 'Leave':
            result.append([cmd[1], '님이 나갔습니다.'])
        else:
            if cmd[0] == 'Enter':
                result.append([cmd[1], '님이 들어왔습니다.'])
            uid_dict[cmd[1]] = cmd[2]
    
    result = [uid_dict[uid] + text for uid, text in result]
        
    return result