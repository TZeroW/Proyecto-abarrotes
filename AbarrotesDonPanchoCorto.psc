Algoritmo AbarrotesDonPanchoCorto
	Escribir 'Este programa ayuda a que los dueños de abarrotes'
	Escribir 'A poder gestionar los productos que venden de una manera mas facil'
	Definir opcion Como Entero
	Definir continuar Como Lógico
	continuar <- Verdadero
	Mientras continuar Hacer
		Escribir 'Elige una opcion: 1. Frutas 2. Salir'
		Leer opcion
		Si opcion=1 Entonces
			Escribir 'Frutas'
			Escribir '¿Deseas agregar una fruta? (s/n)'
			Leer agregar
			Si agregar='s' Entonces
				Escribir 'Fruta agregada.'
			FinSi
		FinSi
		Si opcion=5 Entonces
			Escribir 'Gracias. ¡Hasta luego!'
			continuar <- Falso
		FinSi
	FinMientras
FinAlgoritmo
