import pyfiglet


while True:
	text = input("veuillez entrer le texte à convertir en ascii art : ")
	ascii_art = pyfiglet.figlet_format(text)
	print(ascii_art)
	cont = input("continuer ? oui ou non: ")
	if cont == 'oui':
		print("ok")
	elif cont == 'non':
		break
	elif cont == 'nn':
		break
	else:
		print("pas compris, donc c'est oui")
