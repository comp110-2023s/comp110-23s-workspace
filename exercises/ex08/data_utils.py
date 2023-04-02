"""EX08 - Data Wrangling."""

__author__ = "730556365"


def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Reads csv file and returns as a list of dicts with header keys."""
    from csv import DictReader

    result: list[dict[str, str]] = list()
    file_handle = open(file_name, "r", encoding='utf8')
    csv_reader = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)

    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Returns a list of the values from an inputed column and table."""
    values: list[str] = list()

    for row in table:
        values.append(row[column_name])
    
    return values


def columnar(table:list[dict[str,str]]) -> dict[str, list[str]]:
    """Changes the orientation of the dictionary so that the column names are the keys."""
    new_table: dict[str, list[str]] = dict()

    column_names_row: dict[str, str] = table[0]

    for column_name in column_names_row:
        new_table[column_name] = column_values(table, column_name)

    return new_table


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns the first 'x' rows from an inputed table."""
    reduced_table: dict[str, list[str]] = dict()

    for column_name in table:
        column_values: list[str] = list()
        for value in range(num_rows):
            column_values.append(table[column_name][value])
        reduced_table[column_name] = column_values

    return reduced_table


def select(table: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    """Function only returns the columns of a table that are inputed as parameters."""
    reduced_table: dict[str, list[str]] = dict()

    for column_name in selected_columns:
        reduced_table[column_name] = table[column_name]

    return reduced_table


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Takes two tables and joins them together into one table."""
    joined_table: dict[str, list[str]] = dict()

    for column_name in table_1:
        joined_table[column_name] = table_1[column_name]
    for column_name in table_2:
        if column_name in joined_table:
            for value in table_2[column_name]:
                joined_table[column_name].append(value)
        else:
            joined_table[column_name] = table_2[column_name]
    
    return joined_table


def count(inp_list: list[str]) -> dict[str, int]:
    """Function counts the instances of an item in a list."""
    counter_dict: dict[str, int] = dict()

    for item in inp_list:
        if item in counter_dict:
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1

    return counter_dict

