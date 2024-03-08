#include <stdio.h>

//Prende due numeri in entrata e ne restituisce la somma
int somma(int num1, int num2){
	return num1+num2;
}


//Prende due numeri in entrata e ne restituisce la sottrazione
int sottrazione(int num1, int num2){
	return num1-num2;
}


//Prende due numeri in entrata e ne restituisce la moltiplicazione
int moltiplicazione(int num1, int num2){
	return num1*num2;
}

//Prende due numeri in entrata li trasforma a float e ne restituisce la divisione
float divisione(float num1, float num2){
	return num1/num2;
}


//Prende due numeri in entrata e ne restituisce la media
float media(int num1, int num2){
	//richiama la funzione somma e casta il risultato a un float
	return ((float) somma(num1,num2))/2;
}

int main()
{
	int num1, num2, scelta;
	
	//Chiede il primo numero in input
	printf("Inserici il primo numero: ");
	scanf("%d",&num1);
	
	//Chiede il secondo numero in input
	printf("Inserisci il secondo numero: ");
	scanf("%d",&num2);

	printf(" \n1) Somma \n2) Sottrazione \n3) Moltiplicazione \n4) Divisione \n5) Media \n0) Esci\n");
	//Continua a chiedere input dall'utente finchè non inserisce un numero valido
	do {	
		printf("Che operazione vuoi svolgere? ");
		scanf("%d",&scelta); 
	}while(scelta<0 || scelta>5);
	
	//un switch case che rimanda alla funzione scelta dall'utente
	switch(scelta){
		case 1:
			printf("Risultato: %d",somma(num1,num2));
			break;
		case 2:
			printf("Risultato: %d",sottrazione(num1,num2));
			break;
		case 3:
			printf("Risultato: %d",moltiplicazione(num1,num2));
			break;
		case 4:
			//controlla che il secondo numero non sia 0
			if(num2!=0)
				printf("Risultato: %.2f",divisione(num1,num2));
			else{
				printf("Impossibile dividere per 0");
				return 0;
			}
			break;
		case 5:
			
			printf("Risultato: %.2f",media(num1,num2));
			
			break;
		default:
			break;
	}

	return 0;	
}

