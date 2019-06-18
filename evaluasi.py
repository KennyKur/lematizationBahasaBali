def floatToSting(data):
    hasil = str(float(data))
    return hasil.replace('.',',')
def printAccuracy(mode):
    file = open('evaluasi2.txt','r')
    content = file.read()
    content = content.split('\n')
    row = 4
    length = len(content)
    loop = int(length/4)
    myIndex = 0
    komulatif_akurasi = 0
    tot_length = 0
    tot_wrong = 0
    tot_right = 0
    for i in range(0,loop):
        myIndex = (i * row)

        # print(i,'. ',content[myIndex])

        if mode == 1:
            # Per kalimat
            kalimat = content[myIndex+1]
            length_kalimat = len(kalimat.split())
            wrong = int(content[myIndex+2].split(':')[1])
            right = length_kalimat-wrong
            akurasi = (right/length_kalimat)*100
            # print(kalimat,'\npanjang:',length_kalimat,'\nwrong:',wrong,'\nright:',right,'\nakurasi:',akurasi,'\n')
            print(floatToSting(akurasi),end='\t')

        elif mode == 2:
            #continue
            kalimat = content[myIndex + 1]
            length_kalimat = len(kalimat.split())
            wrong = int(content[myIndex + 2].split(':')[1])
            right = length_kalimat - wrong
            akurasi = (right / length_kalimat) * 100
            komulatif_akurasi+=akurasi
            # print(kalimat,'\npanjang:',length_kalimat,'\nwrong:',wrong,'\nright:',right,'\nakurasi:',akurasi,'\n')
            print(floatToSting(komulatif_akurasi/(i+1)), end='\t')

        elif mode == 3:
            # continue v 2
            kalimat = content[myIndex + 1]
            length_kalimat = len(kalimat.split())
            wrong = int(content[myIndex + 2].split(':')[1])
            right = length_kalimat - wrong
            akurasi = (right / length_kalimat) * 100
            if i == 0:
                komulatif_akurasi += akurasi
            else:
                komulatif_akurasi = (komulatif_akurasi+akurasi)/2

            # print(kalimat,'\npanjang:',length_kalimat,'\nwrong:',wrong,'\nright:',right,'\nakurasi:',akurasi,'\n')
            print(floatToSting(komulatif_akurasi), end='\t')
        elif mode == 4:
            #per kata
            kalimat = content[myIndex + 1]
            length_kalimat = len(kalimat.split())
            tot_length+=length_kalimat
            wrong = int(content[myIndex + 2].split(':')[1])
            tot_wrong+=wrong
            right = length_kalimat - wrong
            tot_right+=right
            akurasi = (tot_right / tot_length) * 100
            # print(kalimat,'\npanjang:',length_kalimat,'\nwrong:',wrong,'\nright:',right,'\nakurasi:',akurasi,'\n')
            print(floatToSting(akurasi), end='\t')
        elif mode == 5:
            kalimat = content[myIndex + 1]
            length_kalimat = len(kalimat.split())
            # print(length_kalimat)
            tot_length+=length_kalimat
    # print(tot_length/250)
    print('')

# printAccuracy(1)
# printAccuracy(2)
# printAccuracy(3)
printAccuracy(4)
# printAccuracy(5)
