def char_at(mina, i):
    if i < 0 or i >= len(mina):
        return None
    return mina[i]

def pos_ouro(mina, i=0):
    # Caso base: fim da string
    if i >= len(mina):
        return -1

    c = char_at(mina, i)
    if c == 'T':  # tremor → parar
        return -1
    if c == 'G':  # ouro encontrado
        return i

    # passo recursivo → avança
    return pos_ouro(mina, i + 1)
def contar_ouro(mina, i=0):
    # Caso base: fim da string
    if i >= len(mina):
        return 0

    c = char_at(mina, i)
    if c == 'T':  # parar contagem
        return 0

    # soma 1 se for 'G', senão soma 0
    return (1 if c == 'G' else 0) + contar_ouro(mina, i + 1)

def indices_de_ouro(mina, i=0):
    # Caso base: fim da string
    if i >= len(mina):
        return []

    c = char_at(mina, i)
    if c == 'T':  # parar ao encontrar tremor
        return []

    # se for 'G', adiciona este índice + os próximos
    if c == 'G':
        return [i] + indices_de_ouro(mina, i + 1)
    else:
        return indices_de_ouro(mina, i + 1)


# Menú para realizar a atividade recursiva
def menu():
    print("\n=== 🪓 Minerador na Mina ===")
    mina = input("Digite a string da min (Apenas R, G, T e .): ").strip()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver caractere em uma posição (char_at)")
        print("2 - Procurar o primeiro ouro (pos_ouro)")
        print("3 - Contar ouros (contar_ouro)")
        print("4 - Listar índices dos ouros (indices_de_ouro)")
        print("5 - Mostrar mina")
        print("0 - Sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            pos = int(input("Digite a posição: "))
            print("Resultado:", char_at(mina, pos))

        elif opcao == "2":
            print("Posição do primeiro ouro:", pos_ouro(mina))

        elif opcao == "3":
            print("Quantidade de ouro:", contar_ouro(mina))

        elif opcao == "4":
            print("Índices dos ouros:", indices_de_ouro(mina))

        elif opcao == "5":
            print("Mina atual:", mina)

        elif opcao == "0":
            print("Encerrando o jogo. Até a próxima!")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()