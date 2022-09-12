print('BANCO DIGITAL')
print('''[ 1 ] - Depositar
[ 2 ] - Sacar
[ 3 ] - Ver saldo
[ 4 ] - Sair''')
saldo = 0
while True:
    try:
        opcao = int(input('Escola uma opção: '))
        if opcao == 1:
            deposito = float(input('Valor do deposito: '))
            saldo = saldo + deposito
            print(f'Saldo atual: R${saldo:.2f}')
        elif opcao == 2:
            saque = float(input('Valor do saque: '))
            saldo = saldo - saque
            print(f'Saldo atual: R${saldo:.2f}')
        elif opcao == 3:
            print(f'Saldo atual: R${saldo:.2f}')
        elif opcao == 4:
            break
        else:
            print('Digite apenas uma das opção acima')
    except:
        print('Só aceitamos apenas números!!')
