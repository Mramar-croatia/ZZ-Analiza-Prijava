import pandas as pd

from . import simplifier as sp

# Will read the excel file and return the DataFrame
def read_xls(file_path: str, sheet_name: str) -> pd.DataFrame:
    return pd.read_excel(file_path, sheet_name=sheet_name)

# Will ensure that only the necessary columns are present in the DataFrame
def ensure_columns(df: pd.DataFrame, column_dict: dict[str:str]) -> pd.DataFrame:
    df.rename(columns=column_dict, inplace=True)
    return df.filter(items=column_dict.values())

# Will simplify the values in the DataFrame
def simplify(df: pd.DataFrame, locations: list[str], school_tuples: list[tuple[str, ...]], subjects: list[str], availabilities: list[str]) -> pd.DataFrame:
    
    # Simplify the values using the simplifier functions
    df['LOKACIJA'] = df['LOKACIJA'].apply(lambda x: sp.simplify_location(x, locations))
    df['IME'] = df['IME'].apply(lambda x: sp.simplify_name(x))
    df['SKOLA'] = df['SKOLA'].apply(lambda x: sp.simplify_school(x, school_tuples))
    df['PREDMET'] = df['PREDMET'].apply(lambda x: sp.simplify_subjects(x, subjects))
    df['TERMIN'] = df['TERMIN'].apply(lambda x: sp.simplify_availability(x, availabilities))
    df['BROJ'] = df['BROJ'].apply(lambda x: sp.simplify_number(x))
    df['RAZRED'] = df['RAZRED'].apply(lambda x: sp.simplify_grade(x))
    
    # Drop duplicates and set the index
    df = df.drop_duplicates(subset='BROJ')
    df = df.set_index('IME')
    df = df.reset_index()
    
    return df

# Will process the excel file
def process_xls(file_path: str, sheet_name: str, column_dict: dict[str:str], locations: list[str], school_tuples: list[tuple[str, ...]], subjects: list[str], availabilities: list[str]) -> pd.DataFrame:
    # Reads the file
    df = read_xls(file_path, sheet_name)
    
    # Ensures that only the necessary columns are present
    df = ensure_columns(df, column_dict)
    
    # Simplifies the values in the DataFrame
    df = simplify(df, locations, school_tuples, subjects, availabilities)
    
    return df