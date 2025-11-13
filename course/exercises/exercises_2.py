import numpy as np


# Given a data frame 'df' and a column name 'column'
# return the mean of the specified column.
def column_mean(df, column):
    x = np.mean(df[column])
    return x


# Given a data frame 'df' and an integer 'x'
# return the xth row of the DataFrame
def select_row(df, x):
    row = df.iloc[x]
    return row


# Given a dataframe 'df' and the name of a categorical variable column 'cat_col'
# return frequency counts of that categorical column
def frequencies_by_group(df, cat_col):
    freq = df[cat_col].value_counts()
    return freq


# return rows where the column value is greater than the threshold
def filter_rows(df, column, threshold):
    rows = df[df[column] > threshold]
    return rows


# 'numerator' and 'denominator', the name of a new column 'new_col'
# return a dataframe with this named new column that is the ratio of two existing columns
def add_ratio_column(df, numerator, denominator, new_col):
    df[new_col] = df[numerator] / df[denominator]
    return df


# Given a dataframe 'df# and a dictionary that maps
# existing column names to new names, return a dataframe with the new names
def rename_columns(df, columns_dict):
    df_new = df.rename(columns=columns_dict)
    return df_new


# return a dataframe having dropped rows with any  missing values
def drop_missing(df):
    df_new = df.dropna()
    return df_new


# Given a dataframe 'df' and a marker for missing values 'value' which could be NA
# return a data frame where the missing values with this specified value
def fill_missing(df, value):
    filled = df.fillna(value)
    return filled


# Given the dataframe 'df' and the name of a column 'column'
# return a DataFrame sorted by that specified column
def sort_by_column(df, column, ascending=True):
    sorted_df = df.sort_values(column)
    return sorted_df


# Given a dataframe 'df' and a named column 'column'
# return unique values from that specified column.
def unique_values(df, column):
    return df[column].unique()
