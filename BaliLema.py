import re

# vocab
with open('BaliVocab.txt') as f:
    vocabs = f.read().splitlines()
#rules
rules = [0,1,2,3,4,5]
# Komibinasi affix
rules[0] = [
    {'rule' : '^n[a-z]*in$',
     'type' : 'wrap',
     'action' : [
         {'from' : '^n', 'to' : ['t']},
        {'from' : 'in$', 'to' : ''},
     ]
    },
    # sendiri
    {'rule' : '^ny[a-z]*in$',
     'type' : 'wrap',
     'action' : [
         {'from' : '^ny', 'to' : ['c','j','s']},
        {'from' : 'in$', 'to' : ''},
     ]
    },
    # sendiri end
    {'rule' : '^man[a-z]*in$',
     'type' : 'wrap',
     'action' : [
         {'from' : '^man', 'to' : ['t','d']},
        {'from' : 'in$', 'to' : ''},
     ]
    },
    {'rule' : '^ma[a-z]*an$',
    'type' : 'wrap',
     'action' : [
         {'from' : '^ma', 'to' : ''},
        {'from' : 'an$', 'to' : ''},
     ]
    },
    {'rule' : '^mang[a-z]*ang$',
    'type' : 'wrap',
     'action' : [
         {'from' : '^mang', 'to' : ''},
        {'from' : 'ang$', 'to' : ''},
     ]
    },

#     Tamvbah sendiri
{'rule': '^ng[a-z]*in$',
     'type': 'wrap',
     'action': [

         {'from': '^ng', 'to': ['','k','g']},
         {'from': 'in$', 'to': ''}
     ],
     },

]
# Somulfiks
rules[1] = [
    {'rule': '^mam[a-z]*',
     'type':'non-wrap',
     'action': [

         {'from': '^mam', 'to': ['b' , 'p']}
     ],
     },
    {'rule': '^pang[a-z]*',
     'type':'non-wrap',
     'action': [

         {'from': '^pang', 'to': ['k','g']}
     ],
     },
]
# konfix
rules[2] = [
    # Tambah sendiri
    {'rule': '^ka[a-z]*ang$',
     'type':'non-wrap',
     'action': [

         {'from': '^ka', 'to': ''},
        {'from': 'ang$', 'to': ''}
     ],
     },
    {'rule': '^ny[a-z]*[aiueo]yang$',
     'type':'non-wrap',
     'action': [

         {'from': '^ny', 'to': ['c','j','s']},
        {'from': 'yang$', 'to': ''}
     ],
     },

    {'rule': '^ka[a-z]*e$',
     'type': 'non-wrap',
     'action': [

         {'from': '^ka', 'to': ''},
         {'from': 'e$', 'to': ''}
     ],
     },

    {'rule': '^ng[aiueo]*[a-z]*in$',
     'type': 'non-wrap',
     'action': [

         {'from': '^ng', 'to': ['','k','g']},
         {'from': 'in$', 'to': ''}
     ],
     },


    {'rule': '^peng[aiueo][a-z]*ne$',
     'type':'non-wrap',
     'action': [

         {'from': '^peng', 'to': ''},
        {'from': 'ne$', 'to': ''}
     ],
     },
    #end tambah sendiri
    {'rule': '^pa[a-z]*an$',
     'type':'non-wrap',
     'action': [

         {'from': '^pa', 'to': ''},
        {'from': 'an$', 'to': ''}
     ],
     },
{'rule': '^ny[aiueo][a-z]*[^aiueo]in$',
     'type':'non-wrap',
     'action': [

         {'from': '^ny', 'to': ['c','j','s']},
        {'from': 'in$', 'to': ''}
     ],
     },


    {'rule': '^ka[a-z]*an$',
     'type':'non-wrap',
     'action': [

         {'from': '^ka', 'to': ''},
         {'from': 'an$', 'to': ''}
     ],
     },
    {'rule': '^ma[a-z]*an$',
     'type':'non-wrap',
     'action': [

         {'from': '^ma', 'to': ''},
         {'from': 'an$', 'to': ''}
     ],
     },
    {'rule': '^bra[a-z]*an$',
     'type':'non-wrap',
     'action': [

         {'from': '^bra', 'to': 'a'},
         {'from': 'an$', 'to': ''}
     ],
     },
]
rules[3] = [
    # Prefix
    {'rule': '^ng[aiueo]',
     'type': 'non-wrap',
     'action': [

         {'from': '^ng', 'to': ['k', 'g']}
     ],
     },

    {'rule' : '^ng[aiueo]',
     'type':'non-wrap',
     'action': [

        {'from' : '^ng' , 'to' : ''}
        ],
     },

    {'rule': '^ng[w]',
     'type':'non-wrap',
     'action': [

         {'from': '^ng', 'to': ''}
     ],
     },

    {'rule': '^n[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^n', 'to': ['t','d']}
     ],
     },

    {'rule': '^ny[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^ny', 'to': ['c','j','s']}
     ],
     },


    {'rule': '^m[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^m', 'to': ['b', 'p']}
     ],
     },

    {'rule': '^nga[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^nga', 'to': ''}
     ],
     },
    #ma
    {'rule': '^ma[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^ma', 'to': ''}
     ],
     },
    {'rule': '^ma[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^ma', 'to': ''}
     ],
     },
    {'rule': '^me[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^me', 'to': ''}
     ],
     },
    {'rule': '^me[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^me', 'to': ''}
     ],
     },
    {'rule': '^ma[wy]',
     'type':'non-wrap',
     'action': [

         {'from': '^ma', 'to': ''}
     ],
     },
    # {'rule': '^m[aiueo]',
    #  'type':'non-wrap',
    #  'action': [
    #
    #      {'from': '^m', 'to': ''}
    #  ],
    #  },
    #pa
    {'rule': '^p[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^p', 'to': ''}
     ],
     },
    #ka
    {'rule': '^k[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^k', 'to': ''}
     ],
     },
    #
    {'rule': '^sa[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^sa', 'to': ''}
     ],
     },
    {'rule': '^sa[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^sa', 'to': ''}
     ],
     },
    #a
    {'rule': '^a[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^a', 'to': ''}
     ],
     },
    {'rule': '^a[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^a', 'to': ''}
     ],
     },
    #pra
    {'rule': '^pra[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^pra', 'to': ''}
     ],
     },
    #pari
    {'rule': '^pari[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^pari', 'to': ''}
     ],
     },
    {'rule': '^pari[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^pari', 'to': ''}
     ],
     },
    #pati
    {'rule': '^pati[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^pati', 'to': ''}
     ],
     },
    #maka
    {'rule': '^maka[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^maka', 'to': ''}
     ],
     },
    {'rule': '^maka[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^maka', 'to': ''}
     ],
     },
    {'rule': '^saka[aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^saka', 'to': ''}
     ],
     },
    {'rule': '^saka[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^saka', 'to': ''}
     ],
     },
    {'rule': '^kuma[^aiueo]',
     'type':'non-wrap',
     'action': [

         {'from': '^kuma', 'to': ''}
     ],
     },
    # tambah sendiri
    {'rule': '^n[^aiueo]',
     'type': 'non-wrap',
     'action': [

         {'from': '^n', 'to': ''}
     ],
     },
    # end tambah sendiri
]
rules[4] = [
    # Suffix
    {'rule' : '[a-z]*a$',
     'type':'non-wrap',
     'action': [

        {'from' : 'a$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo]na$',
     'type':'non-wrap',
     'action': [

        {'from' : 'na$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[^aiueo]ang$',
     'type':'non-wrap',
     'action': [

        {'from' : 'ang$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo][ny]ang$',
     'type':'non-wrap',
     'action': [

        {'from' : '[ny]ang$' , 'to' : ''}
        ],
     },

    {'rule' : '[a-z]*[^aiueo]an$',
     'type':'non-wrap',
     'action': [
        {'from' : 'an$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo]nan$',
     'type':'non-wrap',
     'action': [

        {'from' : 'nan$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[^aiueo]in$',
     'type':'non-wrap',
     'action': [

        {'from' : 'in$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo]nin$',
     'type':'non-wrap',
     'action': [

        {'from' : 'nin$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[^aiueo]e$',
     'type':'non-wrap',
     'action': [

        {'from' : 'e$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo]ne$',
     'type':'non-wrap',
     'action': [

        {'from' : 'ne$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[^aiueo]ne$',
     'type':'non-wrap',
     'action': [

        {'from' : 'ne$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo]nne$',
     'type':'non-wrap',
     'action': [

        {'from' : 'nne$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo]n$',
     'type':'non-wrap',
     'action': [

        {'from' : 'n$' , 'to' : ''}
        ],
     },
    {'rule' : '[a-z]*[aiueo]ning$',
    'type':'non-wrap',
     'action': [
        {'from' : 'ning$' , 'to' : ''}
        ],
     },
]
# Infiks
rules[5] = [

    #
{'rule' : '[^aiueo]*in[aiueo][a-z]*an$',
     'type':'wrap',
     'action': [

        {'from' : 'in' , 'to' : ''},
        {'from' : 'an' , 'to' : ''}
        ],
     },
    # Inffix
    {'rule' : '[^aiueo]*in[aiueo][a-z]*',
     'type':'non-wrap',
     'action': [

        {'from' : 'in' , 'to' : ''}
        ],
     },
    {'rule' : '^in[aiueo][a-z]*',
     'type':'non-wrap',
     'action': [

        {'from' : '^in' , 'to' : ''}
        ],
     },
    {'rule' : '[^aiueo]*um[aiueo][a-z]*',
     'type':'non-wrap',
     'action': [

        {'from' : 'um' , 'to' : ''}
        ],
     },
    {'rule': '^um[aiueo][a-z]*',
     'type':'non-wrap',
     'action': [

         {'from': '^um', 'to': ''}
     ],
     },
    {'rule': '[^aiueo]*el[aiueo][a-z]*',
     'type':'non-wrap',
     'action': [

         {'from': 'el', 'to': ''}
     ],
     },
    {'rule': '[^aiueo]*er[aiueo][a-z]*',
     'type':'non-wrap',
     'action': [

         {'from': 'er', 'to': ''}
     ],
     },
]

# Simulfiks


# cek database
def cekVocab(word):
    if(word in vocabs):
        return True;
    else:
        return False;
# Cek Regex
def cekRegex(regex,word):
    result = re.match(regex, word)
    if result:
        return True
    else:
        return False

def stemming(kata):
    #cek dulu di db
    listStem = []
    listStem.append(kata)
    if(cekVocab(kata)):
        returnWord = kata
        matchRule = False
        message = False
        listStem = False
    else:
        for z in rules:
            for i in z:
                returnWord = False
                matchRule = False
                message = False
                wrap = False
                if (cekRegex(i['rule'], kata)):
                    matchRule = i['rule']
                    tempWord = kata
                    # print(matchRule)
                    if (i['type'] == 'wrap'):
                        wrap = True

                    for j in i['action']:
                        if (isinstance(j['to'], list)):
                            for x in j['to']:
                                tempWord2 = (re.sub(j['from'], x, tempWord))
                                listStem.append(tempWord2)
                                # print(tempWord2)
                                # Jika wrap lakukan ini
                                if(wrap):
                                    tempWord = tempWord2

                                if (cekVocab(tempWord2)):
                                    returnWord = tempWord2
                                    message = False
                                    break;
                                else:
                                    message = 'not found on vocab'
                        else:
                            tempWord2 = re.sub(j['from'], j['to'], tempWord)
                            listStem.append(tempWord2)
                            # print(tempWord2)
                            tempWord = tempWord2
                            if (cekVocab(tempWord2)):
                                returnWord = tempWord2
                if returnWord is not False:
                    break
            if returnWord is not False:
                break
    r = {'word' : kata, 'matchRule' : matchRule , 'stemWord' : returnWord,'message' : message , 'listStem' : listStem}
    return r

def lavenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def lematization(input):
    input = input.lower()
    output = False
    hasil = stemming(input)
    output = hasil['stemWord']

    if(hasil['stemWord'] == False):
        longest = len(input)
        recommend = input

        for recWord in hasil['listStem']:
            for word in vocabs:
                distance = lavenshteinDistance(recWord,word)
                if(distance < longest):
                    longest = distance
                    recommend = word
            # print(word,' ',distance)
        # print('---')
        # print(recommend)
        output = recommend
    return output

def lematizationNoLD(input):
    input = input.lower()
    output = False
    hasil = stemming(input)
    output = hasil['stemWord']

    if(hasil['stemWord'] == False):
        longest = len(input)
        recommend = input
    #
    #     for recWord in hasil['listStem']:
    #         for word in vocabs:
    #             distance = lavenshteinDistance(recWord,word)
    #             if(distance < longest):
    #                 longest = distance
    #                 recommend = word
    #         # print(word,' ',distance)
    #     # print('---')
    #     # print(recommend)
        output = recommend
    return output

def lematizationDetail(input):
    input = input.lower()
    output = False
    hasil = stemming(input)
    output = hasil['stemWord']

    if(hasil['stemWord'] == False):
        longest = len(input)
        recommend = input

        for recWord in hasil['listStem']:
            for word in vocabs:
                distance = lavenshteinDistance(recWord,word)
                if(distance < longest):
                    longest = distance
                    recommend = word
            # print(word,' ',distance)
        # print('---')
        # print(recommend)
        output = recommend
    print(hasil)
    print(output)

def lematizationOld(input):
    output = False
    hasil = stemming(input)
    output = hasil['stemWord']

    if(hasil['stemWord'] == False):
        longest = len(input)
        recommend = input

        for word in vocabs:
            distance = lavenshteinDistance(input,word)
            if(distance < longest):
                longest = distance
                recommend = word
            # print(word,' ',distance)
        # print('---')
        # print(recommend)
        output = recommend
    return output


testWord = [
# "ngidih"
# ,"ngwangun"
# ,'negul'
# ,'nundun'
# ,'nyacad'
# ,'nyaring'
# ,'nyampat'
# ,'ngutang'
# ,'ngambar'
# ,'mapag'
# ,'matek'
# ,'ngamaling'
# ,'nganengneng'
# ,'maling'
# ,'daara'
# ,'anggona'
# ,'jemakang'
# ,'gedenang'
# ,'gedeyang'
# ,'cenikan'
# ,'dawanan'
# ,'jagurin'
# ,'jumunin'
# ,'payuke'
# ,'bajune'
# ,'baasne'
# ,'giginne'
# ,'bukun'
# ,'rikalaning'
# ,'sinurat'
# ,'inucap'
# ,'rumaksa'
# ,'umawak'
# ,'telapak'
# ,'gerudug'
# ,'pasirepan'
# ,'kasengsaraan'
# ,'majemakan'
# ,'bramahan'
# ,'mamuduh'
# ,'pangalung'
# ,'makurenan'
# ,'manuturin'
# ,'mangorahang'
#     'makesiab',
#     'mayasa',
#     'mikut',
#     'mubad',
#     'pileh',
#     'kicen',
#     'sajagat',
#     'sausan',
#     'adiri',
#     'aukud',
#     'prajani',
#     'paribasa',
#     'pariindik',
#     'patigrepe',
#     'makasami',
#     'makaukud',
#     'sakabesik',
#     'sakaukud',
#     'kumajaum'

]
# print(testWord)
# for ij in testWord:
#     print(ij,' => ',lematization(ij))

# print(lematization('ngajeng'))

# sentence = "tiang ngajeng lawar celeng meguling"

# for i in sentence.split():
#     print(lematization(i))








