import json
import pprint

with open ('professor\\base_de_autorização_professor.json', "r") as arquivo:
    base = json.load(arquivo)


# pprint.pprint(base)

base[0]['permissoes'][0]["escrita"] = True
base[0]['permissoes'][0]["excecucao"] = False

pprint.pprint(base)

with open ('base_de_autorização.json', 'w') as arquivo:
    arquivo = json.dump(base, arquivo , ensure_ascii=False)