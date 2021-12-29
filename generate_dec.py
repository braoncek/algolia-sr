import classla
#classla.download('sr')
nlp = classla.Pipeline('sr')
from deklinacije import deklinacije

with open("lista.txt",'r',encoding='utf8') as lista_reci:
    with open("nova_lista.txt", 'w',encoding='utf8') as nova_lista_reci:
        for rec in lista_reci:
            print(rec)
            doc=nlp(rec.rstrip())
            doc_dict=doc.to_dict()[0][0][0]
            #print(doc_dict[0][0][0])
            nova_lista_reci.write(" ".join(deklinacije(lemma=doc_dict['lemma'], pos=doc_dict['xpos'])+"\n"))

