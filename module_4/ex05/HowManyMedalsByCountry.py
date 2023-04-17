import pandas as pd
import numpy as np

def how_many_medals_by_country(df, country_name):
    """ returns a dictionary of dictionaries giving the number and type of
        medal for each competition where the country delegation earned medals.
    """

    if not (isinstance(df, pd.DataFrame) and isinstance(country_name, str)):
        print("error: wrong arguments")
        return None

    # Filter all rows with Team column corresponding to country_name
    delegation = df[(df['Team'] == country_name)]
    if delegation.empty:
        return None

    team_sports =\
        ['Basketball', 'Football', 'Tug-Of-War', 'Handball', 'Water Polo',
         'Hockey', 'Rowing', 'Volleyball', 'Synchronized Swimming', 'Baseball',
         'Rugby Sevens', 'Beach Volleyball', 'Rugby', 'Lacrosse', 'Polo']

    # create a mask which selects all team sports
    team_sports_mask = delegation['Sport'].isin(team_sports)
    # get a dataframe without team_sports
    delegation_no_ts = delegation[~team_sports_mask]
    # get a dataframe with only team_sports
    delegation_only_ts = delegation[team_sports_mask]

    if not delegation_only_ts.empty:
        # Group data by event, year and medal type
        delegation_only_ts =\
            delegation_only_ts.groupby(["Event", "Year", "Medal"]).size()
        # Convert the resulting Series to a DataFrame, adding 'Count' column
        delegation_only_ts =\
            delegation_only_ts .to_frame(name="Count").reset_index()
        # All medal counters set to 1 bc team sport medals must be counted 1 time
        delegation_only_ts["Count"] = 1
        delegation_only_ts = delegation_only_ts.drop("Event", axis=1)

    if not delegation_no_ts.empty:
        # Group data by year and medal type
        delegation_no_ts = delegation_no_ts.groupby(["Year", "Medal"]).size()
        # Convert the resulting Series to a DataFrame
        delegation_no_ts = delegation_no_ts.to_frame(name="Count").reset_index()

    if delegation_no_ts.empty and not delegation_only_ts.empty:
        delegation_merged = delegation_only_ts
    elif not delegation_no_ts.empty and delegation_only_ts.empty:
        delegation_merged = delegation_no_ts
    elif delegation_no_ts.empty and delegation_only_ts.empty:
        return {}

    # Concat dataframe without team_sports and dataframe with only team_sports
    delegation_merged = pd.concat([delegation_no_ts, delegation_only_ts])

    # Group data by year and medal type to remove duplicates entries
    # but by doing a sum of medals per years into "Count"
    delegation_merged =\
        delegation_merged.groupby(['Year', 'Medal']).sum().reset_index()

    # Pivot the data to get a separate column for each medal type, indexed by
    # years and filled with values into "Count" column
    delegation_merged =\
        delegation_merged.pivot(index="Year", columns="Medal", values="Count")

    # add medals colors columns if they doesn't exist (meaning no medals were
    # won in the corresponding year)
    if 'Bronze' not in delegation_merged.columns:
        delegation_merged.loc[:, 'Bronze'] = 0
    if 'Silver' not in delegation_merged.columns:
        delegation_merged.loc[:, 'Silver'] = 0
    if 'Gold' not in delegation_merged.columns:
        delegation_merged.loc[:, 'Gold'] = 0

    # Replace any missing values with 0
    delegation_merged.fillna(0, inplace=True)
    # Delete the NaN column (auto created for slots where no medals were won)
    if np.nan in delegation_merged.columns:
        delegation_merged = delegation_merged.drop(np.nan, axis=1)
    # Convert floats to int
    m = delegation_merged.select_dtypes(np.number)
    delegation_merged[m.columns] = m.round().astype('Int64')

    # rename columns
    delegation_merged = delegation_merged.rename(columns={'Bronze': 'B'})
    delegation_merged = delegation_merged.rename(columns={'Silver': 'S'})
    delegation_merged = delegation_merged.rename(columns={'Gold': 'G'})
    # reorder columns
    delegation_merged = delegation_merged[['G', 'S', 'B']]

    return delegation_merged.to_dict(orient="index")
