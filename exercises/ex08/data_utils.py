"""EX08 - Data Wrangling"""

__author__ = "730556365"



def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys"""
    from csv import DictReader

    result: list[dict[str, str]] = []
    file_handle = open(file_name, "r", encoding='utf8')
    csv_reader = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)

    return result