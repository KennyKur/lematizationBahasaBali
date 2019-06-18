file = open ('mentah.txt','r')
content = file.read()
content = content.split('.')
jadi = open('hasil_split.txt','w')
for i in content:
    jadi.write(i+'\n')
jadi.close()


