"""Data Utils - EX08!"""

__author__ = "730575328"

from csv import DictReader
from tabulate import tabulate

def read_csv_rows(filename:str) -> list[dict[str,str]]:
    """Returns an organized and readible version of the inputed csv."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        result.append(row[header])
        #save every value under key "header"
    return result 

def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table 
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(data: dict[str, list [str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column tabke with the first N rows."""
    result: dict[str, list[str]] = {}
    n: int = 0
    if rows >= len(data):
        return data
    for row in data:
        val_list: list[str] = []
        val_list = data[row]
        temp_list: list[str] = []
        n = 0
        while n <= rows - 1:
            temp_list.append(val_list[n])
            n += 1
        result[row] = temp_list
    return result

def select(data: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Produces a new column table with a specific subet of the original columns."""
    result: dict[str, list[str]] = {}
    for index in column_name:
        result[index] = data[index]
    return result

def concat(table_one: dict[str, list[str]],table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column table by combining two tables."""
    result: dict[str, list[str]] = {}
    for row in table_one:
        list_one: list[str] = []
        list_one = table_one[row]
        temp_list: list[str] = []
        n = 0
        for x in table_one[row]:
            temp_list.append(list_one[n])
            n += 1
        result[row] = temp_list
    for row in table_two:
        list_two: list[str] = []
        list_two = table_two[row]
        temp_list: list[str] = []
        n = 0
        for x in table_two[row]:
            temp_list.append(list_two[n])
            n += 1
        if row in result:
            result[row] += temp_list
        else: 
            result[row] = temp_list
    return result

def count(given: list[str]) -> dict[str, int]:
    """Counts the number of times that a value appeared in the input."""
    result: dict[str, int] = {}
    for key in given:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result