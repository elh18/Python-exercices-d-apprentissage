import os

def input_numbers(nb_elements):
    """ Fonction pour saisir des nombres entiers depuis l'entrée utilisateur """
    numbers = []
    for i in range(nb_elements):
        number_str = input("Entrez le nombre {}: ".format(i+1))
        number = int(number_str)
        numbers.append(number)
    return numbers

def save_to_file(numbers, filename):
    """ Fonction pour enregistrer les nombres dans un fichier texte """
    with open(filename, 'w') as file:
        for number in numbers:
            file.write("{}\n".format(number))

