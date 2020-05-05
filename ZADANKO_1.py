import socket
from _thread import *

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("Server Started")

#TODO stwórz dwuelementową listę players i wpisz do niej dwie liczby
# pierwsza będzie zwiększana do 1000 przez pierwszego klienta, a druga zmniejszana do 0 przez drugiego
players = [4, 996]

strPlayers = str(players[0]) + ',' + str(players[1])

def threaded_client(conn, player):
    conn.sendall(str.encode(strPlayers + ',' + str(player)))
    reply = ""
    while True:
        try:
            info = conn.recv(2048).decode()

            #TODO zaktualizuj listę players, pamiętając że otrzymane dane opisują tylko gracza, który je wysłał

            if not info:
                print("Disconnected")
                break
            else:
                if player == 1:
                    players[1] = int(info)
                    reply = str(players[0])
                else:
                    players[0] = int(info)
                    reply = str(players[1])

                print("Received: ", info)
                print("Sending : ", reply)

            #TODO zakoduj wiadomość (podobnie jak po wywołaniu funkcji) i wyślij ją do klienta
            conn.sendall(str.encode(reply))

        except:
            break
        print(players)
    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    #TODO zaakceptuj połączenie z zewnątrz funkcją s.accept(), zwróci ona dwie wartości,
    # połączenie za pomocą którego będziemy wysyłać i odbierać dane oraz adres, zapisz te zmienne jako conn i addr
    (conn, addr) = s.accept()


    print("Connected to:", addr)

    #TODO rozpocznij nowy wątek przy pomocy funkncji
    # start_new_thread(<WYWOŁYWANA FUNKCJA>, <OBIEKT TUPLE ZAWIERAJĄCY POŁĄCZENIE I NUMER GRACZA (ARGUMENTY)>)
    start_new_thread(threaded_client, (conn, currentPlayer))


    currentPlayer += 1