import csv

def load_values(file):
    """Charge les valeurs à partir d'un fichier texte"""
    with open(file) as f:
        reader = csv.reader(f, delimiter=';')
        values = [list(map(int, row)) for row in reader]
    return values

def build_lists(values):
    """Construit deux listes à partir des valeurs chargées"""
    x_values = [row[0] for row in values]
    y_values = [row[1] for row in values]
    return x_values, y_values

def cross_products_sum(x_values, y_values):
    """Calcule la somme des produits croisés entre les deux listes"""
    products = [x_values[i] * y_values[i] for i in range(len(x_values))]
    sum_products = sum(products)
    return sum_products
