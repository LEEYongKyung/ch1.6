# print() 연습

import sys

print(1)
print('hello', 'world')

x = 0.2
s = "hello World"

# sep, end 키워드 파라미터 지정하기
print(x, s, sep=',')
print(str(x) + ',' + s)

print(x, s, sep=',', end='')

# 기본적인 print() 호출은
print(sep=' ', end='\n')

# file 파라미터를 지정할 수 있다.
print('Hello World', file=sys.stdout)
print('error: Hello World', file=sys.stderr)

# file 출력
f = open('hello.txt', 'w')
print('Hello World', file=f)

# 참고
sys.stdout.write('Hello World')
