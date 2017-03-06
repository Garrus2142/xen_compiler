import sys
import os.path

if len(sys.argv) <= 1:
	print "Usage: python3 xen_compiler.py [file to compile]"
	sys.exit(0)

if not os.path.exists(sys.argv[1]):
	print "Fichier introuvable.";
	sys.exit(0)

try:
	with open(sys.argv[1]) as file:
		iline = 1
		bytesbuff = bytearray()
		for line in file:
			line = line.replace('\n', '').replace('\r', '')
			split = line.split(';')
			if len(split) != 4:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: ';' indefini"
				sys.exit(0)
			
			split[0] = int(split[0])
			split[1] = int(split[1])
			split[2] = int(split[2])
			split[3] = int(split[3])
		
			# Verification des valeurs
			if split[0] < 0 or split[0] > 5:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Octave incorrect"
				sys.exit(0)
			if split[1] < 1 or split[1] > 7:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Note incorrect"
				sys.exit(0)
			if split[2] < 0 or split[2] > 255:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Duree incorrect"
				sys.exit(0)
			if split[3] < 0 or split[3] > 255:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Attente incorrect"
				sys.exit(0)

			#Ecriture du buffer
			bytesbuff.append(split[0])
			bytesbuff.append(split[1])
			bytesbuff.append(split[2])
			bytesbuff.append(split[3])
			iline = iline + 1

		#Ecriture du fichier binaire
		filebin = sys.argv[1].split('.')[0] + '.bin'
		with open(filebin, "wb") as file:
			file.write(bytesbuff)
		print "Compilation terminee. " + sys.argv[1] + " -> " + filebin
except IOError as err:
	print "Erreur fichier: " + err.strerror
	sys.exit(0)
except ValueError:
	print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntax: Caractere incorrect"
	sys.exit(0)
