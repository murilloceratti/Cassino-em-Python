import random
import os
import time

saldo = 0


def returnToMenu():
    time.sleep(3)
    limpar()
    mainMenu()




def gameMenu():
    print('Escolha algum jogo:\n[1] Roleta 🎲\n[2] Caça-Níquel 🎰\n[3] Dados 🎲')
    op = int(input())
    limpar()
    if op == 1:
        roleta()
    elif op == 2:
        cacaniquel()
    elif op == 3:
        dados()





def mainMenu():
    print('Bem Vindo ao Cassino! 🎰\n[1] Escolher um Jogo 🎲\n[2] Saldo 💲')
    op = int(input())
    limpar()
    if op == 1:
        gameMenu()
    elif op == 2:
        addSaldo()




def dados():

    global saldo

    op = int(input('Seja bem vindo ao jogo de dados!\n[1] Acertas Soma\n[2] Acertar Dado Único\n'))
    limpar()
    aposta = int(input('Insira sua aposta: '))

    if aposta > saldo:
        print('Saldo insuficinete')
        returnToMenu()

    saldo -= aposta
    limpar()
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    if op == 1:
        soma = int(input('Insira o seu palpite de soma: '))
        print(f'Dado 1: {dado1}\nDado 2: {dado2}\nSoma: {dado1+dado2}')
        if soma == (dado1+dado2):
            print(f'Você acertou a soma!\nVocê ganhou: R${aposta*5}')
            saldo += aposta*5
            returnToMenu()

        else:
            print(f'Você errou!\nSaldo atual: R${saldo}')
            returnToMenu()


    elif op == 2:
        dadoUnico = int(input('Insira seu palpite sobre o número de algum dado: '))
        if dadoUnico == dado1 or dadoUnico == dado2:
            print(f'Dado 1: {dado1}\nDado 2: {dado2}\nSeu palpite: {dadoUnico}\nVocê acertou o palpite e seu ganhou foi de: R${aposta*2}')
            saldo += aposta*2
            returnToMenu()
        else:
            print(f'Dado 1: {dado1}\nDado 2: {dado2}\nSeu palpite: {dadoUnico}\nVocê errou o palpite\nSaldo atual: R${saldo}')
            returnToMenu()






def addSaldo():
    global saldo
    print(f'Deseja adicionar mais saldo?\nSeu saldo atual é: R${saldo}\n[1] Sim\n[2] Retornar ao menu principal')
    op = int(input(''))
    limpar()
    if op == 1:
        add = int(input('Quanto você deseja adicionar de saldo?\n'))
        if saldo > 1:
            saldo += add
        elif saldo == 0:
            saldo = add
        print(f'Saldo adicionado com sucesso!\nSeu novo saldo é: R${saldo}')
        returnToMenu()
    elif op == 2:
        mainMenu()







def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')





def cacaniquel():
    global saldo
    emojis = ["🍒", "🍀", "🍉", "💎"]
    numeros = [random.randint(1, 4) for _ in range(3)]

    aposta = int(input(f'Bem vindo ao Caça-Níquel!\nSaldo atual: R${saldo}\nInsira sua aposta: '))
    limpar()
    if aposta > saldo:
        print('Você não possui saldo suficiente, retorne ao menu principal e recarregue')
        returnToMenu()
    else:
        saldo -= aposta

    m = 0

    while m < 20:
        print(f'{random.choice(emojis)} {random.choice(emojis)} {random.choice(emojis)}')
        m = m + 1
        time.sleep(0.1)
        limpar()

    for n in numeros:
        print(emojis[n-1], end=" ")

    if numeros[0] == numeros[1] == numeros[2]:
        saldo += aposta*10
        print(f'\nParabéns, você combinou as 3 figuras, você ganhou: R${aposta*10}\nSaldo atual: R${saldo}')
        returnToMenu()
    elif numeros[0] == numeros[1] or numeros[1] == numeros[2] or numeros[2] == numeros[0]: 
        saldo += aposta*2
        print(f'\nParabéns, você combinou duas figuras, você ganhou: R${aposta*2}\nSaldo atual: R${saldo}')
        returnToMenu()
    else:
        print(f'\nVocê não combinou nenhuma das figuras.\nSaldo atual: R${saldo}')

        returnToMenu()







def saberCor(numero):
    if numero == 0:
        return 'Verde'
    elif numero % 2 == 0:
        return  'Vermelho'
    elif (numero % 2) > 0:
        return('Preto')






def roleta():
    global saldo
    m = 0

    print('Bem vindo a Roleta!\nEscolha uma cor:\n[1] Vermelho (2X) 🔴\n[2] Preto (2X) ⚫\n[3] Verde [10X] 🟢')
    corSelecionada = int(input())
    limpar()
    print(f'Insira o valor da sua aposta (Saldo atual: {saldo}):')
    aposta = int(input())
    if aposta > saldo:
        print('Você não possui saldo suficiente, retorne ao menu principal e recarregue')
        returnToMenu()
    else:
        saldo -= aposta

    while m < 5:
        print('💸 Girando Roleta 💰')
        time.sleep(0.5)
        limpar()
        print('💰 Girando Roleta 💸')
        time.sleep(0.5)
        limpar()
        m = m + 1

    cor = random.randint(0,31)
    corSorteada = saberCor(cor)
    if corSorteada == 'Vermelho' and corSelecionada == 1:
        saldo += aposta*2
        print(f'💲 Você ganhou, o número sorteado foi {cor} e ele é {corSorteada} 🔴!')
        print(f'Você ganhou R${aposta*2}, seu novo saldo é de R${saldo}')
    elif corSorteada == 'Preto' and corSelecionada == 2:
        saldo += aposta*2
        print(f'💲 Você ganhou, o número sorteado foi {cor} e ele é {corSorteada} ⚫!')
        print(f'Você ganhou R${aposta*2}, seu novo saldo é de R${saldo}')
    elif corSorteada == 'Verde' and corSelecionada == 3:
        saldo += aposta*10
        print(f'💲 Você ganhou, o número sorteado foi {cor} e ele é {corSorteada} 🟢!')
        print(f'Você ganhou R${aposta*10}, seu novo saldo é de R${saldo}')
    else:
        print(f'🚫 Você perdeu, o número sorteado foi {cor} e ele é {corSorteada} 🚫')
        print(f'Você perdeu R${aposta}, seu novo saldo é de R${saldo}')
    return returnToMenu()





mainMenu()