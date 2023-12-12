#Sistema bancário com depósito, saque, e extrato


usuarios = []
contas = []
extrato = list()

opcao = -1
saldo = 0
saques_realizados = 0
LIMITE_SAQUES_DIARIOS = 3
LIMITE_DE_SAQUE = 500
AGENCIA_BANCARIA = "0001"


#USUÁRIOS
def verifica_cpf(cpf, lista):
    if lista:
        for usuario in lista:
            if usuario["CPF"] == cpf:
                return usuario["Nome"]
        
        return False

    else:
        return False


def criar_usuario(lista):
    cpf = int(input("Digite seu CPF :"))
    if verifica_cpf(cpf, usuarios)==False:
        nome = str(input("Digite o nome do usuário: "))
        data_nascimento = str("Data de nascimento: ")
        logradouro = str(input("Seu logradouro: "))
        numero = int(input("Número:"))
        bairro = str(input("Seu bairro: "))
        cidade = str(input("Cidade: "))
        sigla = str(input("Sigla: "))
        endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla}"

        lista.append({"CPF":cpf,"Nome":nome, "Data de Nascimento": data_nascimento, "Endereço":endereco})
        print("Usuário cadastrado com sucesso!")

    else:
        print("Este CPF já está cadastrado")


def criar_conta(lista, contas, agencia, numero_conta):
    print(lista)
    cpf = int(input("Informe o CPF do titular da conta: "))
    usuario = verifica_cpf(cpf, usuarios)
    if usuario:
        contas.append({"Agência": agencia, "Numero_Conta": numero_conta, "Usuário":usuario})
        print(contas)
    else:
        print("Este CPF não foi cadastrado em nosso banco")


def sacar(*,saldo, valor, extrato, saques_realizados):

    valor_negativo = valor <=0

    extrapolou_saldo = valor > saldo

    extrapolou_saques_diarios = saques_realizados >= LIMITE_SAQUES_DIARIOS

    extrapolou_limite_de_saque = valor > LIMITE_DE_SAQUE


    if extrapolou_saldo:
        print("Saldo insuficiente para realizar operação")


    elif extrapolou_saques_diarios:
        print("Você já realizou 3 saques hoje. Volte amanhã")

    
    elif extrapolou_limite_de_saque:
        print("O saque máximo é de R$500,00")

    elif valor_negativo:
        print("Os saques devem ser superior a R$0,00")

    else:
        saldo-=valor
        operacao = {f"Saque: -R${valor}"}
        extrato += operacao
        saques_realizados +=1
        print(f"Saque de R${valor} realizado com sucesso!")
        return(saldo, extrato, saques_realizados)


def depositar(saldo, valor, extrato,/):

    valor_negativo = valor <=0

    if valor_negativo:
        print("Valor para depósito deve ser maior que R$0,00")
    else:
        saldo += valor
        operacao = {f"Depósito : +R${valor}"}
        extrato +=operacao
        print(f"Depósito de R${valor} realizado com sucesso!")
        return(saldo, extrato)


def fextrato(saldo,*,extratoP):
    print("EXTRATO".center(30,"="))
    if extratoP:
        for operacao in extratoP:
            print(operacao)
        print("="*30)
        print(f"Saldo atual -> R${saldo}")
    else:
        print("Nenhuma operação registrada")
        print("="*30)
        print(f"Saldo atual -> R${saldo}")



while opcao != 0:

    print(''' 
    ********** Banco Invest **********

    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Criar usuário
    5 - Criar Conta
    0 - Sair
    ''')

    opcao = int(input('Operação:'))

    while opcao != 1 and 2 and 3 and 4 and 5 and 0:
        print("Opção inválida!")
        opcao = int(input('Operação:'))

    ####SACAR####

    if opcao == 1:
        valor = float(input("Valor do saque -> R$"))

        saque = sacar(saldo=saldo, valor=valor, extrato=extrato, saques_realizados=saques_realizados)
        if saque:
            saldo = saque[0]
            extrato = saque[1]  
            saques_realizados = saque[2]


    ####DEPOSITAR####

    elif opcao == 2:
        quantia = float(input("Valor que deseja DEPOSITAR:"))

        deposito = depositar(saldo, quantia, extrato)

        saldo = deposito[0]
        extrato = deposito[1]


    ####EXTRATO####


    elif opcao == 3:
        fextrato(saldo, extratoP=extrato)
    
    elif opcao == 4:
        criar_usuario(usuarios)

    elif opcao == 5:
        criar_conta(usuarios,contas,AGENCIA_BANCARIA,len(contas)+1)


print('Obrigado por utilizar nosso sistema. Volte sempre :)')