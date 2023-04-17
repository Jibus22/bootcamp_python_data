import pandas as pd

def YoungestFellah(df, year):
    if not (isinstance(df, pd.DataFrame) and isinstance(year, int)):
        print("error: wrong arguments")
        return None

    youngest_female_age =\
        df.loc[(df['Sex'] == 'F') & (df['Year'] == year), 'Age'].min()

    youngest_male_age =\
        df.loc[(df['Sex'] == 'M') & (df['Year'] == year), 'Age'].min()

    return {'M': youngest_male_age, 'F': youngest_female_age}
