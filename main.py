import math

# Função para exibir o menu de opções
def exibeMenu():
    print("\n===== Menu de Cálculos de Polarização =====")
    print("1. Calcular a intensidade de luz após atravessar um filtro polarizador")
    print("2. Calcular a intensidade de luz não polarizada a partir da intensidade após o filtro")
    print("3. Calcular a intensidade após atravessar dois filtros polarizadores com ângulo entre eles")
    print("4. Calcular a intensidade da luz incidente e após o conjunto de filtros com ângulo entre eles")
    print("5. Calcular a intensidade da luz incidente e após o primeiro filtro com base na intensidade após o conjunto")
    print("6. Calcular a intensidade após três filtros polarizadores")
    print("7. Resolver questão de polarização com três filtros")
    print("8. Resolver questão específica com três filtros")
    print("9. Resolver questão específica com entradas do usuário")
    print("10. Sair do programa")

# Função para calcular a intensidade após atravessar um filtro polarizador
def calcular_intensidade_apos_filtro(intensidade_inicial):
    intensidade_final = intensidade_inicial / 2
    return intensidade_final

# Função para calcular a intensidade inicial de luz não polarizada
def calcular_intensidade_inicial(intensidade_final):
    intensidade_inicial = intensidade_final * 2
    return intensidade_inicial

# Função para calcular a intensidade após dois filtros polarizadores com ângulo entre eles
def calcular_intensidade_dois_filtros(intensidade_inicial, angulo):
    intensidade_apos_primeiro = calcular_intensidade_apos_filtro(intensidade_inicial)
    intensidade_final = intensidade_apos_primeiro * math.cos(math.radians(angulo))**2
    return intensidade_apos_primeiro, intensidade_final

# Função para calcular a intensidade incidente e a intensidade após o conjunto de dois filtros polarizadores
def calcular_intensidade_incidente_e_apos_conjunto(intensidade_apos_primeiro, angulo):
    intensidade_inicial = intensidade_apos_primeiro * 2
    intensidade_final = intensidade_apos_primeiro * math.cos(math.radians(angulo))**2
    return intensidade_inicial, intensidade_final

# Função para calcular a intensidade incidente e após o primeiro filtro com base na intensidade após o conjunto
def calcular_intensidade_incidente_com_base_no_conjunto(intensidade_apos_conjunto, angulo):
    intensidade_apos_primeiro = intensidade_apos_conjunto / (math.cos(math.radians(angulo)) ** 2)
    intensidade_inicial = intensidade_apos_primeiro * 2
    return intensidade_inicial, intensidade_apos_primeiro

# Função para calcular a intensidade após o conjunto de três filtros polarizadores
def calcular_intensidade_tres_filtros(intensidade_inicial, angulo1, angulo2):
    intensidade_apos_primeiro = calcular_intensidade_apos_filtro(intensidade_inicial)
    intensidade_apos_segundo = intensidade_apos_primeiro * math.cos(math.radians(angulo1))**2
    intensidade_final = intensidade_apos_segundo * math.cos(math.radians(angulo2 - angulo1))**2
    return intensidade_apos_primeiro, intensidade_apos_segundo, intensidade_final

# Função para resolver a questão de polarização com três filtros
def resolver_questao_tres_filtros():
    intensidade_apos_primeiro = float(input("Digite a intensidade da luz após o primeiro filtro (em W/cm²): "))
    angulo1 = float(input("Digite o ângulo entre o primeiro e o segundo filtro (em graus): "))
    angulo2 = float(input("Digite o ângulo entre o segundo e o terceiro filtro (em graus): "))

    intensidade_inicial = intensidade_apos_primeiro * 2
    intensidade_apos_segundo = intensidade_apos_primeiro * math.cos(math.radians(angulo1))**2
    intensidade_final = intensidade_apos_segundo * math.cos(math.radians(angulo2 - angulo1))**2

    print(f"\n1. A intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
    print(f"2. A intensidade da luz após o segundo filtro é: {intensidade_apos_segundo:.2f} W/cm²")
    print(f"3. A intensidade da luz após o terceiro filtro é: {intensidade_final:.2f} W/cm²")

# Função para resolver a questão específica com três filtros polarizadores
def resolver_questao_especifica_tres_filtros():
    intensidade_apos_segundo = float(input("Digite a intensidade da luz após o segundo polarizador (em W/cm²): "))
    angulo1 = float(input("Digite o ângulo entre o primeiro e o segundo filtro (em graus): "))
    angulo2 = float(input("Digite o ângulo entre o segundo e o terceiro filtro (em graus): "))

    intensidade_apos_primeiro = intensidade_apos_segundo / (math.cos(math.radians(angulo1))**2)
    intensidade_inicial = intensidade_apos_primeiro * 2
    intensidade_final = intensidade_apos_segundo * math.cos(math.radians(angulo2 - angulo1))**2

    print(f"\n1. A intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
    print(f"2. A intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")
    print(f"3. A intensidade da luz após o conjunto dos três filtros é: {intensidade_final:.2f} W/cm²")

# Função para resolver questão específica com entradas do usuário
def resolver_questao_especifica_com_entradas_usuario():
    intensidade_final = float(input("Digite a intensidade após o conjunto dos três filtros (em W/cm²): "))
    angulo1 = float(input("Digite o ângulo do segundo filtro em relação ao primeiro (em graus): "))
    angulo2 = float(input("Digite o ângulo do terceiro filtro em relação ao primeiro (em graus): "))

    intensidade_apos_primeiro = intensidade_final / (math.cos(math.radians(angulo2 - angulo1))**2)
    intensidade_apos_segundo = intensidade_apos_primeiro / (math.cos(math.radians(angulo1))**2)
    intensidade_inicial = intensidade_apos_segundo * 2

    print(f"\n1. A intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
    print(f"3. A intensidade da luz após o segundo filtro é: {intensidade_apos_segundo:.2f} W/cm²")
    print(f"2. A intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")

# Função do menu principal para chamar as funções de cálculo
def menu():
    while True:
        exibeMenu()
        escolha = input("\nDigite o número correspondente à opção desejada: ")

        if escolha == "1":
            intensidade_inicial = float(input("Digite a intensidade da luz não polarizada (em W/cm²): "))
            intensidade_final = calcular_intensidade_apos_filtro(intensidade_inicial)
            print(f"\nA intensidade da luz após atravessar o filtro é: {intensidade_final:.2f} W/cm²")

        elif escolha == "2":
            intensidade_final = float(input("Digite a intensidade da luz após passar pelo filtro (em W/cm²): "))
            intensidade_inicial = calcular_intensidade_inicial(intensidade_final)
            print(f"\nA intensidade da luz não polarizada é: {intensidade_inicial:.2f} W/cm²")

        elif escolha == "3":
            intensidade_inicial = float(input("Digite a intensidade da luz não polarizada (em W/cm²): "))
            angulo = float(input("Digite o ângulo entre os eixos dos filtros (em graus): "))
            intensidade_apos_primeiro, intensidade_final = calcular_intensidade_dois_filtros(intensidade_inicial, angulo)
            print(f"\nA intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")
            print(f"A intensidade da luz após atravessar os dois filtros é: {intensidade_final:.2f} W/cm²")

        elif escolha == "4":
            intensidade_apos_primeiro = float(input("Digite a intensidade da luz após o primeiro filtro (em W/cm²): "))
            angulo = float(input("Digite o ângulo entre os eixos dos filtros (em graus): "))
            intensidade_inicial, intensidade_final = calcular_intensidade_incidente_e_apos_conjunto(intensidade_apos_primeiro, angulo)
            print(f"\nA intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
            print(f"A intensidade da luz após atravessar o conjunto de filtros é: {intensidade_final:.2f} W/cm²")

        elif escolha == "5":
            intensidade_apos_conjunto = float(input("Digite a intensidade da luz após o conjunto de filtros (em W/cm²): "))
            angulo = float(input("Digite o ângulo entre os eixos dos filtros (em graus): "))
            intensidade_inicial, intensidade_apos_primeiro = calcular_intensidade_incidente_com_base_no_conjunto(intensidade_apos_conjunto, angulo)
            print(f"\nA intensidade da luz incidente é: {intensidade_inicial:.2f} W/cm²")
            print(f"A intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")

        elif escolha == "6":
            intensidade_inicial = float(input("Digite a intensidade da luz não polarizada (em W/cm²): "))
            angulo1 = float(input("Digite o ângulo entre o primeiro e o segundo filtro (em graus): "))
            angulo2 = float(input("Digite o ângulo entre o segundo e o terceiro filtro (em graus): "))
            intensidade_apos_primeiro, intensidade_apos_segundo, intensidade_final = calcular_intensidade_tres_filtros(intensidade_inicial, angulo1, angulo2)
            print(f"\nA intensidade da luz após o primeiro filtro é: {intensidade_apos_primeiro:.2f} W/cm²")
            print(f"A intensidade da luz após o segundo filtro é: {intensidade_apos_segundo:.2f} W/cm²")
            print(f"A intensidade da luz após o terceiro filtro é: {intensidade_final:.2f} W/cm²")

        elif escolha == "7":
            resolver_questao_tres_filtros()

        elif escolha == "8":
            resolver_questao_especifica_tres_filtros()

        elif escolha == "9":
            resolver_questao_especifica_com_entradas_usuario()

        elif escolha == "10":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
menu()
