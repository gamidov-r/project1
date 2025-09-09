import csv

import pandas as pd


def read_transactions_csv(path_to_csv: str) -> list:
    with open(path_to_csv, encoding="UTF-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        trans_list = []
        for row in reader:
            trans_list.append(row)
        return trans_list


def read_transactions_excel(path_to_excel: str) -> list:
    df = pd.read_excel(path_to_excel)
    return df.to_dict(orient="records")
