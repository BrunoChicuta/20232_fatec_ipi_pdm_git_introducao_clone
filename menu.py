import teste_calculadora

print('1 - Soma')
print('2 - Subtracao')
print('3 - Multiplicacao')
print('4 - Divisao')
print('0 - Sair')
opcao = input('Selecione a opcao desejada:')

if (opcao == 1):
    print(teste_calculadora.somar())
