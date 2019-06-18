import BaliLema
import string

# sentence = "Ada katuturan satua I Siap Selem ngelah pianak pepitu. Ane paling cerika tusing ngelah bulu madan I Doglagan. Sawai-wai I Siap Selem ngalih amah nganti ke dauh pangkunge. Sedek dina anu ritatkala I Siap Selem teken panak - panakne ngalih amah dauh pangkunge, lantas langite megerudug nyihnayang lakar ujan."
# sentence = " “ Me, lan jani mulih. Ento guleme gede gati ” keto pianakne kelihan ngomong. “ Ao me yang takut nyanan iraga ujanan dini ” pianakne lianan milu masaut “ Cening jak mekejang, lan jani ditu di umahe ento malu maembon. Yen jani iraga mulih pedas iraga ujanan. Tolih ento adine, I Doglagan. Ia tusing ngelah bulu. Yen ia ujanan pepes bisa mati ” keto I Siap Selem maorahan teken pianak - pianakne. Lantas I Siap selem teken pianakne makapitu ngungsi kaumahe ane ada di sisin pangkunge ento."
# sentence = " pekenne adanina “ Jero jero sane madue pondok niki, dados ke tiang milu maembon? ”   keto I Siap Selem metakon. Lantas pesu ane ngelah umahe ento boya ja sios wantah meong lua madan Meng Kuuk. “ Ngeong ngeong.. ih cai Siap Selem ngudiang cai mai? ”   “ Jero Meong, tiang mriki jagi maembon mawinan tiang madue pianak - pianak kari alit. Tusing melah keneh tiange ngajakin ngrobok ujan ”  . “ Nah lamun buka keto, lan mai macelep ka tengah ”   ditu lantas Meng Kuuk ngajakin I Siap Selem tekening pianakne mulihan. Sajaan lantas tuun ujan bales pesan ngaenang pangkunge blabar. Meng Kuuk nanjenin I Siap Selem apanga nginep di umahne. I Siap Selem nyak nginep kerana ia pedalem teken pianakne. Petengne I Siap Selem tusing ngidayang pules. Ditu lantas ia ningeh Meng Kuuk mererembug ajaka pianak - pianakne. “ Cening ajak mekejang, petenge ene iraga lakar pesta besar. Ne meme ngelah siap pengina ngajak pianak makapitu ”   keto munyine Meng Kuuk. "

# text = "metakon"
# print(BaliLema.lematization('metakon'))
# BaliLema.lematizationDetail('metakon')

def cleaning(sentence,removeChar):
    for i in removeChar:
        sentence = sentence.replace(i,'')
    return  sentence

file = open('kalimat.txt','r')
sentence = file.read()
sentence = sentence.translate(str.maketrans('','',string.punctuation))
removeChar = ['"','“','”']
sentence = cleaning(sentence,removeChar)
sentence = sentence.lower()

hasil = open('evaluasi2.txt','w')
for j in sentence.split('\n'):
    print(j)
    hasil.write(j+'\n')
    for i in j.split():
        # print(i,' = ',BaliLema.lematization(i))
        print(BaliLema.lematizationNoLD(i),end=' ')
        hasil.write(BaliLema.lematizationNoLD(i)+' ')
    hasil.write('\nSALAH:0\n\n')
    print('\n')
hasil.close()