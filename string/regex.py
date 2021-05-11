import re

# make pattern

pattern = re.compile('([0-9]+)-(?P<first>[0-9]+)-(?P<second>[0-9]+)')

# match Class

match = pattern.match('010-1234-5678')

print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(3))

print(match.groups())
print(match.groupdict())

print(match.start(2))
print(match.end(2))
print(match.span(2))

print(match.string)
print(match.pos)
print(match.endpos)
print(match.lastindex)
print(match.lastgroup)

# match : 처음부터 매칭 시도하여 첫 매칭 반환

print(re.match('[a-z]+', 'python java'))
print(re.match('[a-z]+', 'Python Java'))

# search : 전체에 대해 첫 매칭 찾음

print(re.search('[a-z]+', 'python java'))
print(re.search('[a-z]+', 'Python Java'))

# findall : 모든 매칭에 대한 리스트 반환

print(re.findall('[a-z]+', 'Python Java'))

# finditer : 모든 매칭에 대한 match 객체 iter

for match in re.finditer('[a-z]+', 'Python Java'):
    print(match)

# split : 분할

print(re.split(',\s*', 'red, blue,green'))
print(re.split(',\s*', 'red, blue,green', maxsplit=1))

# sub : 치환

print(re.sub('(\d+)-(\d+)-(\d+)','\g<1>-\g<2>-****', '010-1234-4567'))

def replacement(match):
    return match.group().upper()

print(re.sub(r'\b[a-z]',replacement, 'john doe'))
print(re.sub(r'\b[a-z]',replacement, 'john doe', count=1))

# subn : sub결과와 치환 횟수를 봔환

print(re.subn(r'\b[a-z]',replacement, 'john doe'))