#
# write test
#

# text 모드가 default : wt
f = open('text.txt', 'w', encoding='utf-8')
write_size = f.write('안녕하세요\n둘리입니다.')
f.close()
print(write_size)

# binary mode : wb
f = open('test2.txt', 'wb')
write_size = f.write(bytes('안녕하세요\n둘리입니다.', encoding='utf-8'))
f.close()
print(write_size)


#
# read test
#
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
f.close()
print(text)

#
# copy binary file
#

f_src = open('python.png', 'rb')
data = f_src.read()
f_src.close()

print(type(data))

f_dest = open('python2.png', 'wb')
f_dest.write(data)
f_dest.close()







