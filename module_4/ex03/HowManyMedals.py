import pandas as pd
import numpy as np

def how_many_medals(df, name):
    if not (isinstance(df, pd.DataFrame) and isinstance(name, str)):
        print("error: wrong arguments")
        return None

    athlete = df[(df['Name'] == name)]
    if athlete.empty:
        return None
    # Group data by year and medal type
    grp = athlete.groupby(["Year", "Medal"], dropna=False).size()
    # Convert the resulting Series to a DataFrame
    medal_counts = grp.to_frame(name="Count").reset_index()
    # Pivot the data to get a separate column for each medal type
    medal_counts = medal_counts.pivot(index="Year", columns="Medal", values="Count")

    # add medals colors columns if they doesn't exist (meaning no medals were
    # won in the corresponding year)
    if 'Bronze' not in medal_counts.columns:
        medal_counts.loc[:, 'Bronze'] = 0
    if 'Silver' not in medal_counts.columns:
        medal_counts.loc[:, 'Silver'] = 0
    if 'Gold' not in medal_counts.columns:
        medal_counts.loc[:, 'Gold'] = 0

    # Replace any missing values with 0
    medal_counts.fillna(0, inplace=True)
    # Delete the NaN column (auto created for slots where no medals were won)
    if np.nan in medal_counts.columns:
        medal_counts = medal_counts.drop(np.nan, axis=1)
    # Select only the columns that are numeric
    m = medal_counts.select_dtypes(np.number)
    # Then round them to the nearest integer using the round method
    # Convert values from float to int
    medal_counts[m.columns] = m.round().astype('Int64')

    # rename columns
    medal_counts = medal_counts.rename(columns={'Bronze': 'B'})
    medal_counts = medal_counts.rename(columns={'Silver': 'S'})
    medal_counts = medal_counts.rename(columns={'Gold': 'G'})
    # reorder columns
    medal_counts = medal_counts[['G', 'S', 'B']]

    return medal_counts.to_dict(orient="index")
