# Sistema de criação de ficha de personagem
nome = input("Digite o nome do personagem: ")
vitalidade_base = 10
forca = int(input("Digite a sua força: "))
agilidade = int(input("Digite a sua agilidade: "))
vigor = int(input("Digite a sua vigor: "))
presenca = int(input("Digite a sua presença: "))
intelecto = int(input("Digite a sua inteligência: "))
n_habilidades_profissao = int(input("Digite o número de habilidades da profissão: "))

vitalidade = vitalidade_base + 2 * vigor
ponto_esforco = forca + vigor + presenca
defesa = 10 + agilidade
num_habilidades = intelecto + n_habilidades_profissao
num_pericias = intelecto + n_habilidades_profissao

print(f"\nVocê pode adicionar {num_pericias} perícias.")
pericias = []
for i in range(num_pericias):
    pericia = input(f"Digite o nome da perícia {i + 1}: ")
    bonus = int(input(f"Digite o bônus da perícia {pericia}: "))
    pericias.append(f"{pericia} +{bonus}")


print(f"\nVocê pode adicionar {num_habilidades} habilidades.")
habilidades = []
for i in range(num_habilidades):
    habilidade = input(f"Digite o nome da habilidade {i + 1}: ")
    descricao = input(f"Descreva o que a habilidade {habilidade} faz: ")
    dano = input(f"Se a habilidade {habilidade} causar dano, informe o valor (ou deixe vazio): ")
    gasto = input(f"Se a habilidade {habilidade} tiver gasto, informe o valor (ou deixe vazio): ")
    habilidades.append({
        "nome": habilidade,
        "descricao": descricao,
        "dano": dano if dano else "Nenhum",
        "gasto": gasto if gasto else "Nenhum"
    })

# Exibição da ficha do personagem
print("\n_________________________________________")
print(f"Nome: {nome}")
print("Ficha do Personagem")
print("_________________________________________")
print(f"Vitalidade: {vitalidade}")
print(f"For: {forca}")
print(f"Agi: {agilidade}")
print(f"Pre: {presenca}")
print(f"Vig: {vigor}")
print(f"Int: {intelecto}")
print(f"Ponto de esforço: {ponto_esforco}")
print(f"Defesa: {defesa} (10 + Agi)")
print("\nItens:")
print("\n_________________________________________")
print("Perícias:")
for pericia in pericias:
    print(f"- {pericia}")
print("_________________________________________")
print("Habilidades:")
for habilidade in habilidades:
    print(f"- {habilidade['nome']}:")
    print(f"  Descrição: {habilidade['descricao']}")
    print(f"  Dano: {habilidade['dano']}")
    print(f"  Gasto: {habilidade['gasto']}")
print("_________________________________________")
