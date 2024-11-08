import math

def intro():
    print("\nSeja bem-vindo ao Programa de Estudo do Modelo Atômico de Bohr!\n")
    print("Este programa calcula parâmetros do átomo de hidrogênio, incluindo:")
    print("  - Raio da órbita")
    print("  - Velocidade do elétron")
    print("  - Energia cinética")
    print("  - Energia potencial")
    print("  - Energia total")
    print("  - Comprimento de onda de De Broglie")
    print("  - Energia do fóton absorvido ou emitido")
    print("\nO usuário pode fornecer diferentes entradas e obter os parâmetros correspondentes como saída.")
    print("O algoritmo é útil para compreender e calcular características do modelo atômico de Bohr com base em diferentes variáveis de entrada.")
    print("As unidades de medida são rigorosamente aplicadas para garantir precisão nos cálculos.\n")
    print("Autores: Carlos, Tallysson e Cecilia\n")

def exibe_menu():
    print("\n===== Menu de Cálculos de Polarização =====")
    print("1. Calcular intensidade de luz após passar por um filtro polarizador")
    print("2. Calcular intensidade inicial de luz não polarizada com base na intensidade após o filtro")
    print("3. Calcular intensidade de luz após dois filtros polarizadores com ângulo entre eles")
    print("4. Determinar intensidade inicial e após dois filtros com ângulo entre eles")
    print("5. Determinar intensidade inicial e após o primeiro filtro com base na intensidade final do conjunto")
    print("6. Calcular intensidade de luz após três filtros polarizadores")
    print("7. Analisar intensidade com três filtros polarizadores em sequência e ângulos específicos")
    print("8. Estimar intensidade para caso específico envolvendo três filtros polarizadores")
    print("9. Realizar análise de intensidade com dados personalizados do usuário")
    print("10. Sair do programa")

def intensidade_apos_um_filtro():
    intensidade_inicial = float(input("Digite a intensidade da luz não polarizada (em W/cm²): "))
    return intensidade_inicial / 2

def intensidade_inicial_com_base_na_final():
    intensidade_final = float(input("Digite a intensidade da luz após passar pelo filtro (em W/cm²): "))
    return intensidade_final * 2

def intensidade_apos_dois_filtros():
    intensidade_inicial = float(input("Digite a intensidade da luz não polarizada (em W/cm²): "))
    angulo = float(input("Digite o ângulo entre os eixos dos filtros (em graus): "))
    intensidade_apos_primeiro = intensidade_inicial / 2
    intensidade_final = intensidade_apos_primeiro * math.cos(math.radians(angulo))**2
    return intensidade_apos_primeiro, intensidade_final

def intensidade_inicial_e_final_dois_filtros():
    intensidade_apos_primeiro = float(input("Digite a intensidade da luz após o primeiro filtro (em W/cm²): "))
    angulo = float(input("Digite o ângulo entre os eixos dos filtros (em graus): "))
    intensidade_inicial = intensidade_apos_primeiro * 2
    intensidade_final = intensidade_apos_primeiro * math.cos(math.radians(angulo))**2
    return intensidade_inicial, intensidade_final

def intensidade_inicial_apos_conjunto():
    intensidade_apos_conjunto = float(input("Digite a intensidade da luz após o conjunto de filtros (em W/cm²): "))
    angulo = float(input("Digite o ângulo entre os eixos dos filtros (em graus): "))
    intensidade_apos_primeiro = intensidade_apos_conjunto / (math.cos(math.radians(angulo)) ** 2)
    intensidade_inicial = intensidade_apos_primeiro * 2
    return intensidade_inicial, intensidade_apos_primeiro

def intensidade_apos_tres_filtros():
    intensidade_inicial = float(input("Digite a intensidade da luz não polarizada (em W/cm²): "))
    angulo1 = float(input("Digite o ângulo entre o primeiro e o segundo filtro (em graus): "))
    angulo2 = float(input("Digite o ângulo entre o segundo e o terceiro filtro (em graus): "))
    intensidade_apos_primeiro = intensidade_inicial / 2
    intensidade_apos_segundo = intensidade_apos_primeiro * math.cos(math.radians(angulo1))**2
    intensidade_final = intensidade_apos_segundo * math.cos(math.radians(angulo2 - angulo1))**2
    return intensidade_apos_primeiro, intensidade_apos_segundo, intensidade_final

def analisar_tres_filtros():
    intensidade_apos_primeiro = float(input("Digite a intensidade da luz após o primeiro filtro (em W/cm²): "))
    angulo1 = float(input("Digite o ângulo entre o primeiro e o segundo filtro (em graus): "))
    angulo2 = float(input("Digite o ângulo entre o segundo e o terceiro filtro (em graus): "))
    intensidade_inicial = intensidade_apos_primeiro * 2
    intensidade_apos_segundo = intensidade_apos_primeiro * math.cos(math.radians(angulo1))**2
    intensidade_final = intensidade_apos_segundo * math.cos(math.radians(angulo2 - angulo1))**2
    return intensidade_inicial, intensidade_apos_segundo, intensidade_final

def estimar_intensidade_especifica_tres_filtros():
    intensidade_apos_segundo = float(input("Digite a intensidade da luz após o segundo polarizador (em W/cm²): "))
    angulo1 = float(input("Digite o ângulo entre o primeiro e o segundo filtro (em graus): "))
    angulo2 = float(input("Digite o ângulo entre o segundo e o terceiro filtro (em graus): "))
    intensidade_apos_primeiro = intensidade_apos_segundo / (math.cos(math.radians(angulo1))**2)
    intensidade_inicial = intensidade_apos_primeiro * 2
    intensidade_final = intensidade_apos_segundo * math.cos(math.radians(angulo2 - angulo1))**2
    return intensidade_inicial, intensidade_apos_primeiro, intensidade_final

def analise_com_entrada_usuario():
    intensidade_final = float(input("Digite a intensidade após o conjunto dos três filtros (em W/cm²): "))
    angulo1 = float(input("Digite o ângulo do segundo filtro em relação ao primeiro (em graus): "))
    angulo2 = float(input("Digite o ângulo do terceiro filtro em relação ao primeiro (em graus): "))
    intensidade_apos_primeiro = intensidade_final / (math.cos(math.radians(angulo2 - angulo1))**2)
    intensidade_apos_segundo = intensidade_apos_primeiro / (math.cos(math.radians(angulo1))**2)
    intensidade_inicial = intensidade_apos_segundo * 2
    return intensidade_inicial, intensidade_apos_primeiro, intensidade_apos_segundo

def menu():
    while True:
        exibe_menu()
        escolha = input("\nDigite o número correspondente à opção desejada: ")

        if escolha == "1":
            intensidade_final = intensidade_apos_um_filtro()
            print(f"\nA intensidade da luz após atravessar o filtro é: {intensidade_final:.2f} W/cm²")

        elif escolha == "2":
            intensidade_inicial = intensidade_inicial_com_base_na_final()
            print(f"\nA intensidade da luz não polarizada é: {intensidade_inicial:.2f} W/cm²")

        elif escolha == "3":
            intensidade_apos_primeiro, intensidade_final = intensidade_apos_dois_filtros()
            print(f"\nA intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")
            print(f"A intensidade da luz após atravessar os dois filtros é: {intensidade_final:.2f} W/cm²")

        elif escolha == "4":
            intensidade_inicial, intensidade_final = intensidade_inicial_e_final_dois_filtros()
            print(f"\nA intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
            print(f"A intensidade da luz após atravessar o conjunto de filtros é: {intensidade_final:.2f} W/cm²")

        elif escolha == "5":
            intensidade_inicial, intensidade_apos_primeiro = intensidade_inicial_apos_conjunto()
            print(f"\nA intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
            print(f"A intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")

        elif escolha == "6":
            intensidade_apos_primeiro, intensidade_apos_segundo, intensidade_final = intensidade_apos_tres_filtros()
            print(f"\nA intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")
            print(f"A intensidade da luz após o segundo filtro é: {intensidade_apos_segundo:.2f} W/cm²")
            print(f"A intensidade da luz após o terceiro filtro é: {intensidade_final:.2f} W/cm²")

        elif escolha == "7":
            intensidade_inicial, intensidade_apos_segundo, intensidade_final = analisar_tres_filtros()
            print(f"\nA intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
            print(f"A intensidade da luz após o segundo filtro é: {intensidade_apos_segundo:.2f} W/cm²")
            print(f"A intensidade da luz após o terceiro filtro é: {intensidade_final:.2f} W/cm²")

        elif escolha == "8":
            intensidade_inicial, intensidade_apos_primeiro, intensidade_final = estimar_intensidade_especifica_tres_filtros()
            print(f"\nA intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
            print(f"A intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")
            print(f"A intensidade da luz após o conjunto dos três filtros é: {intensidade_final:.2f} W/cm²")

        elif escolha == "9":
            intensidade_inicial, intensidade_apos_primeiro, intensidade_apos_segundo = analise_com_entrada_usuario()
            print(f"\nA intensidade inicial da luz é: {intensidade_inicial:.2f} W/cm²")
            print(f"A intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")
            print(f"A intensidade da luz após o segundo filtro é: {intensidade_apos_segundo:.2f} W/cm²")

        elif escolha == "10":
            print("Encerrando o programa...")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida.")

def main():
    intro()
    
    while True:
        acessa = input("Deseja acessar o programa? 1 (Sim) e 2 (Não): ")
        
        if acessa == "1":
            menu()
            break
        elif acessa == "2":
            print("Saindo do programa...")
            break
        else:
            print("\nOpção inválida!\n")

if __name__ == "__main__":
    main()
