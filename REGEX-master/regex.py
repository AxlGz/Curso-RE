#!/usr/bin/python

import re#Estamos importanto la libreria para regEx

pattern = re.compile(r'^([\d]{4})\-\d\d\-\d\d,(.*),Friendly,.*$')#Estamos pidiendo que re compile
# nuestra expresion regular, que en este caso va entr comillas simples

#abrir archivo solo para leer 
file = open("./results_6aeb6252-c531-449d-bf29-e11193358b8c.csv" , "r")

for line in file:
	res = re.match(pattern, line)
	if res:
		print ("%s\n" % res.group(2))


file.close()