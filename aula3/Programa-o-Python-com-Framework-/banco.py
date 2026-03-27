saldo = [1500.0]


extrato = []


extrato.append(sum(saldo))


saque =  float(input('Digite o saque: '))


transacao =  sum(saldo) - saque


extrato.append(saque)


saldo = [transacao]


print('Saldo R$', saldo)


deposito =  float(input('Digite o Deposito R$: '))


extrato.append(deposito)


transacao =  sum(saldo) + deposito


saldo = [transacao]


print('Saldo R$', saldo)


print(extrato)

