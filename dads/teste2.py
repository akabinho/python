O código exibido foi escrito na linguagem de progamação C.
você deve ler o código, identificar as funcionalidades existentes e reescrevê-lo na linguagem de progamação Python.

Usa as seguintes práticas de progamação:
- Tipagem estática:
- Bons nomes para variáveis e funções:
- Funções:
-Comentários.


#include
#include
#include
#include
#define TAM 3

float calcularMedia(float notas[]){
	int i;
	float soma = 0;
	for(i = 0; i < TAM; i++){
		soma += notas[i];
	}
	return soma / TAM;
}

char* verificarSituacao(float media){
	char* resultado[200];
	media >= 7 ? strcpy(resultado, "Aprovado!") : strcpy(resultado, "Reprovado!");
	return resultado;
}

void mostrarResultado(float notas[]){
	printf("\nMédia: %.1f \n", calcularMedia(notas));
	printf("Resultado: %s \n", verificarSituacao(calcularMedia(notas)));
}

int main(){
	setlocale(LC_ALL, "");
	float notam[TAM];
	int i;

	for(i = 0; i < TAM; i++){
		printf("Digite o %d nota: ", i + 1);
		scanf("%f", -as[i]);
	} 
	
	mostrarResultado(notas);
	return 0;
}