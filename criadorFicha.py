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
num_habilidades = intelecto
num_pericias = intelecto + n_habilidades_profissao
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
print(f"Perícias: ({num_pericias} disponíveis)")
print("_________________________________________")
print(f"Habs: ({num_habilidades} disponíveis)")
print("_________________________________________")
