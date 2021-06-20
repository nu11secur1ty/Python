#!/usr/bin/python3
# Coded by Carlos/cardangi
# Debug nu11secur1ty
#Full port scanner in simple way! :D


import socket
import os
import sys
from datetime import datetime


try:
    tempoinicial = datetime.now()
    if sys.argv[1] == "-ip":
        os.system("cls")
        ipvitima = sys.argv[2]
        print ("Ip escolhido: ", sys.argv[2], "\n")
        if sys.argv[3] == "-todasportas":
            print ("Opção escolhida: Todas portas.")
            print ("Deseja porta UDP ou TCP?")
            udptcp = (input(">"))
        if sys.argv[3] == "-1024":
            print ("Portas bem conhecidas escolhida")
            print ("Deseja porta UDP ou TCP?")
            udptcp = (input(">"))
        if sys.argv[3] == "-portafixa":
            print ("Porta fixa escolhida")
            print ("Deseja porta UDP ou TCP?")
            udptcp = (input(">"))


        if udptcp == "TCP" or udptcp == "tcp":
            os.system("cls")
            print ("TCP escolhida!")
            print ("Começando o scan...")
            try:
                if sys.argv[3] == "-1024":
                    for porta in range (1,1025):
                        print ("Escaneando... aguarde!")
                        print ("...")
                        socket.setdefaulttimeout(0.5)
                        serverremoto = socket.gethostbyname(sys.argv[2])
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        resultado = s.connect_ex((serverremoto, porta))
                        if resultado == 0:
                            print ("Porta {}       Aberta [:)]".format(porta))
                        
                if sys.argv[3] == "-todasportas":
                    for porta in range (1,65535):
                        print ("Escaneando... aguarde!")
                        print ("...")
                        socket.setdefaulttimeout(0.5)
                        serverremoto = socket.gethostbyname(sys.argv[2])
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        resultado = s.connect_ex((serverremoto, porta))
                        if resultado == 0:
                            print ("Porta {}       Aberta [:)]".format(porta))
                if sys.argv[3] == "-portafixa":
                    
                    print ("Escaneando... aguarde!")
                    print ("...")
                    socket.setdefaulttimeout(0.5)
                    serverremoto = socket.gethostbyname(sys.argv[2])
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    resultado = s.connect_ex((serverremoto, int(sys.argv[4])))
                    if resultado == 0:
                            print ("Porta {}       Aberta [:)]".format(sys.argv[4]))
                    else:
                        print ("Porta {}          Fechada! [X]".format(sys.argv[4]))
                    s.close()
                    tempoatual = datetime.now()
                    tempototal = tempoinicial - tempoatual
            except socket.gaierror:
                    print ("Ip / host nao encontrado!")
            except socket.error:
                    print ("Não foi possivel conectar ao server. Cheque a conexao com a net!")


        else:
            print ("UDP Escolhida!")
            try:
                if sys.argv[3] == "-1024":
                    for porta in range (1,1025):
                        print ("Escaneando... aguarde!")
                        print ("...")
                        serverremoto = socket.gethostbyname(sys.argv[2])
                        mensagem = "Ola"
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.sendto(mensagem.encode(),(serverremoto,porta))
                        s.settimeout(12)
                        print ((s.recvfrom(1024).decode))
                        
                        
                if sys.argv[3] == "-todasportas":
                    for porta in range (1,65535):
                        print ("Escaneando... aguarde!")
                        print ("...")
                        serverremoto = socket.gethostbyname(sys.argv[2])
                        mensagem = "Ola"
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.sendto(mensagem.encode(),(serverremoto,porta))
                        s.settimeout(12)
                        print ((s.recvfrom(1024).decode))
                if sys.argv[3] == "-portafixa":
                    
                    print ("Escaneando... aguarde!")
                    print ("...")
                    serverremoto = socket.gethostbyname(sys.argv[2])
                    mensagem = "Ola"
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.sendto(mensagem.encode(),(serverremoto,int(sys.argv[4])))
                    s.settimeout(12)
                    print ((s.recvfrom(1024).decode))
                    print ("Scan terminado, tempo demorado: ", tempototal)
            except socket.gaierror:
                    print ("Ip / host nao encontrado!")
            except socket.error:
                    print ("Não foi possivel conectar ao server. Cheque a conexao com a net!")
                    print ("Obs: Pode também ser um bug da opção UDP.")
    if sys.argv[1] == "-cardangibuffer":
        os.system("python cardangibuffer")

        os.system("cls")
        print ("Opção buffer overflow ainda não acrescentada.")
                
            
except IndexError:
    os.system("cls")
    os.system("color c")
    print ("\n")
    print ("Sem argumentos digitados! Maneira de uso: \n")
    print ("escaneador.py -ip ip_alvo -todasportas \n")
    print ("\n\n Lista de argumentos:\n -todasportas : Escaneia todas portas de 1 a 65535")
    print (" -1024 : Escaneia as portas conhecidas, 1 a 1024.")
    print (" -portafixa : Escaneia a porta que você quiser.")
    print ("Uso final: escaneador.py -ip www.google.com -portafixa 30")
    print ("Ou: escaneador.py -ip www.google.com -1024")
    print ("\n\n")
    print ("Também é possivel usar esse script pra enviar um Buffer Overflow remoto para a porta.")
    print ("escaneador.py -cardangibuffer : Usar bufferoverflow.")
