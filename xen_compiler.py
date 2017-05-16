import sys
import os.path

if len(sys.argv) <= 1:
	print "Usage: python xen_compiler.py [xenfile to compile] {-c to gen c var}"
	sys.exit(0)

if not os.path.exists(sys.argv[1]):
	print "Fichier introuvable.";
	sys.exit(0)

if len(sys.argv) >= 2 and sys.argv[2] == "-c":
	tocvar = 1

try:
	with open(sys.argv[1]) as file:
		iline = 1
		bytesbuff = bytearray()
		cbuff = "unsigned char data[] = {\n"
		csize = 1
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
			if split[0] < 0 or split[0] > 7:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Octave incorrect"
				sys.exit(0)
			if split[1] < 1 or split[1] > 12:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Note incorrect"
				sys.exit(0)
			if split[2] < 0 or split[2] > 255:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Duree incorrect"
				sys.exit(0)
			if split[3] < 0 or split[3] > 255:
				print "Fichier " + sys.argv[1] + ", ligne " + str(iline) + '\n' + "Erreur de syntaxe: Attente incorrect"
				sys.exit(0)

			#Ecriture du buffer
			if tocvar:
				csize += 3
				cbuff += "\t" + str((split[0] * 12) + split[1]) + ", " + str(split[2]) + ", " + str(split[3]) + ",\n"
			else:
				bytesbuff.append((split[0] * 12) + split[1])
				bytesbuff.append(split[2])
				bytesbuff.append(split[3])
			iline = iline + 1

		#Ecriture du fichier binaire
		if tocvar:
			cbuff = cbuff[0:len(cbuff) - 2] + "\n};"
			filec = sys.argv[1].split('.')[0] + '.c'
			with open(filec, "w") as file:
				file.write(cbuff)
			print "Compilation terminee.(Size: " + str(csize) + ") " + sys.argv[1] + " -> " + filec
		else:
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
