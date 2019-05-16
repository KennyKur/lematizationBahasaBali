import BaliLema

sentence = "tiang ngajeng lawar celeng meguling"

for i in sentence.split():
    print(BaliLema.lematization(i))