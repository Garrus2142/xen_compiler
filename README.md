# Xen Compiler
Compilateur de fichiers xen en binaire pour être lu par le PIC32
## Requirement
* Python 2
* Xen file

## Usage
python xen_compiler [xenfile to compile]

## Xen format
[octave 0:5];[note 1:7];[durée (centième de secondes 0:255];[attente (centième de secondes 0:255)]

## Bin format
Une instruction est contenu dans 4 octets.
Ex:
L'octet 6 est la note de la 2eme instruction.
