# Xen Compiler
Compilateur de fichiers xen en binaire pour être lu par le PIC32
## Requirement
* Python 2
* Xen file

## Usage
python xen_compiler [xenfile to compile] {-c to gen c file}

## Xen format
[octave 0:7];[note 1:12];[durée (centième de secondes 0:255];[attente (centième de secondes 0:255)]
Ex:
0;1;100;50 = Do (32Hz) pendant 1s et attend 0.5s avant de jouer la prochaine note.

## Bin format
Une instruction est contenu dans 3 octets.
Ex:
L'octet 5 est la note de la 2eme instruction.
