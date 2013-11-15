#!/usr/bin/env python
# -*- coding: iso-8859-15
#	Scrabble.py: Programa que dado el diccionario SOWPODS de Scrabble, determina que letras nunca aparecen repetidas
#				 de forma consecutiva.
#	Autor: Fernando Zerpa
#	Fecha: 14/11/2013
#
#	Corrida: python Scrabble.py sowpods.txt
#
import sys

#lista de palabras a buscar en el diccionario
l=['AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','VV','WW','XX','YY','ZZ'];


if len(sys.argv) >= 2:

	#iterador sobre la lista de palabras
	for buscar in l:	

		#abrimos el archivo pasado como argumento por la linea de comandos
		entrada=sys.argv[1];
		f = open(entrada,"r");
		while True:

			#leemos el diccionario linea por linea y buscamos si se encuentra la palabra, si la encuentra cierra el archivo 
			#y procede a buscar la proxima palabra, si el archivo finaliza y no lo encuentra, imprime la letra que nunca se repite consecutivamente
			linea = f.readline();
			esta=linea.count(buscar);
			if esta > 0:
				f.close();
				break;
			if not linea: 
				print "la letra '"+ buscar[0] +"' nunca aparece de manera consecutiva"; 
				break;  
else:
        print "Este programa necesita sowpods.txt como parámetro";