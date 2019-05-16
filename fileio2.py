# 다양한 파일 입출력 함수

f = open('text.txt', 'r+t', encoding='utf-8')
text = f.read()
print(text)

# position은 바이트 단위다.
pos = f.tell()
print(pos)

# position을 이동
f.seek(17)

# 다시 읽기
text = f.read()
print("----" + text + "----")
f.close()


# 라인단위로 읽기
line_num = 0
f2 = open('fileio2.py', 'rt', encoding='utf-8')
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break

    line_num += 1
    print('{0}: {1}'.format(line_num, line), end='')


f3 = open('fileio2.py', 'rt', encoding='utf-8')
for line_num, line in enumerate(f3.readlines()):
    print('{0}: {1}'.format(line_num, line), end='')
f3.close()

# with ~ as 문을 사용하면 자동으로 파일이 닫힌다.
with open('fileio2.py', 'rt', encoding='utf-8') as f4:
    for line_num, line in enumerate(f4.readlines()):
        print('{0}: {1}'.format(line_num, line), end='')

print('\n', f4.closed)