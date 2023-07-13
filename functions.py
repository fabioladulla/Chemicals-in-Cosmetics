import pandas as pd

def change_dtype(df, col_list, dtype):
    """
    Change the data type of the given columns.

    Parameters:
    df (pd.DataFrame): The DataFrame whose columns' data types are to be changed.
    col_list (list of str): The names of the columns to change.
    dtype (str or type): The new data type.
    
    Returns:
    pd.DataFrame: The DataFrame with changed data types.
    """
    
    for col in col_list:
        df[col] = df[col].astype(dtype)
    return df


def check_id_counts(data, subcategory_col, id_col):
    """
    Print the number of unique IDs for each unique subcategory.

    Parameters:
    df (pd.DataFrame): The DataFrame to operate on.
    subcategory_col (str): The name of the column containing the subcategories.
    id_col (str): The name of the column containing the IDs.
    """
    id_counts = {subcat: len(df.loc[df[subcategory_col] == subcat, id_col].unique())
                 for subcat in df[subcategory_col].unique()}
    for subcat, count in id_counts.items():
        print(f'{subcat}: {count}')