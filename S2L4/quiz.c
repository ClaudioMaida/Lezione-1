#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

//Ho usato due constanti per rendere più accessibili future modifiche

const int nDomande = 7;

//Le domande le ho raccolte in una matrice di stringhe
const char *quiz[7][3] = {
    {
        "Qual'e' la console piu' venduta al mondo?",
        "\nA)Playstation 2\nB)Nintendo DS\nC)Playstation 4\nD)Nintendo Switch",
        "A"
    },
    {
        "Final Fantasy VI in Nord America e' stato rilasciato con il nome di?",
        "\nA)Secret of Mana\nB)Final Fantasy Legends\nC)Final Fantasy III\nD)Final Fantasy VI",
        "C"
    },
    {
        "A quanti Bit era il NES?",
        "\nA)4 Bit\nB)8 Bit\nC)16 Bit\nD)32 Bit",
        "B"
    },
    {
        "Chi e' stato il creatore della serie di giochi Metal Gear?",
        "\nA)Hideo Kojima\nB)Shigeru Miyamoto\nC)Hironobu Sakaguchi\nD)Yu Suzuki",
        "A"
    },
    {
        "Quale videogioco e' stato il primo a utilizzare la tecnologia di motion capture per animare i personaggi?",
        "\nA)Mortal Kombat\nB)Resident Evil\nC)Final Fantasy VII\nD)Prince of Persia: Sands of Time",
        "D"
    },
    {
        "Qual e' stato il primo videogioco ad essere inserito nella collezione permanente del Museum of Modern Art di New York?",
        "\nA)Pong\nB)Tetris\nC)Super Mario Bros\nD)Myst",
        "A"
    },
    {
        "Qual e' stato il primo videogioco a introdurre la modalita' multiplayer online su console?",
        "\nA)Counter-Strike\nB)Quake III Arena\nC)Diablo III\nD)Halo 2",
        "D"
    }

};

//chiede al giocatore se vuole giocare
int menu(){
    printf("A) Iniziare una nuova partita\nB) Uscire dal gioco\n");
    char scelta;
    do{
        printf("Cosa vuoi fare? ");
        scanf("%c",&scelta);
        while(getchar()!='\n'); //ho dovuto usare questa riga per pulire l'input buffer
        scelta=toupper(scelta);
    }while(scelta!='B'&&scelta!='A');

    //Usato l'operatore ternario perchè non ne so vivere senza
    return (scelta=='A' ? 1 : 0 );
}

void playQuiz(){
    char risp;
    int score=0;
    
    //un ciclo for cicla tutte le domande e risposte
    for(int i=0;i<nDomande;i++){
        printf("\n----------------------------------------------\n");
        printf("%s",quiz[i][0]);
        printf("%s",quiz[i][1]);
    
        do{
            printf("\nRisposta: ");
            scanf("%c",&risp);
            while(getchar()!='\n');
            risp=toupper(risp);
        }while(risp!='A'&&risp!='B'&&risp!='C'&&risp!='D');
        
        //Controlla che la risposta corrisponda
        if(risp==quiz[i][2][0]){
            printf("Risposta Esatta ^^");
            score++;
        }else{
            printf("\nRisposta Sbagliata :(\nLa risposta giusta era: %c",quiz[i][2][0]);
        }

        printf("\nPremi invio per continuare...");
        getchar();
    }


    //controlla il risultato ottenuto e si complimenta in base alla media 
    if((score/nDomande)==1){
        printf("\nWOW hai totalizzato %d/%d punti, le sapevi tutte!\nO hai imbrogliato...",score,nDomande);
    }else if(score==0){
        printf("\nFai sul serio?\nHai totalizzato %d/%d punti",score,nDomande);
    }else if(((float)score/(float)nDomande)<0.5){
        printf("\nInsomma potevi impegnarti di piu'...\nHai totalizzato %d/%d punti",score,nDomande);
    }else{
        printf("\nComplimenti!\nHai totalizzato %d/%d punti",score,nDomande);
    }
};

int main(){
    
    //se la funzione riporta esito positivo il gioco comincia
    if(menu()){
        playQuiz();
    }
    return 0;
}