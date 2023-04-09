"""Data Utils - EX08!"""

__author__ = "730575328"

from csv import DictReader
from tabulate import tabulate

def read_csv_rows(filename:str) -> list[dict[str,str]]:
    """Returns an organized and readible version of the inputed csv"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        result.append(row[header])
        #save every value under key "header"
    return result 

def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table 
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(data: dict[str, list [str]], rows: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    n: int = 0
    n_key: list[str] = []
    first_column: list[str] = []
    for row in data:
        n_key.append(row)
    while n <= rows:
        result[n_key[n]] = data[n_key[n]]
    return result

def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
   result: dict[str, list[str]] = {}
