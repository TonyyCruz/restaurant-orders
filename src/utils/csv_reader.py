import csv


def csv_reader(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path}'")
    try:
        with open(path, "r") as file:
            csvreader = csv.reader(file)
            return [data for data in csvreader]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")
