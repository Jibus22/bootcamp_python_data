import pandas as pd

class SpatioTemporalData:
    def __init__(self, df):
        if not (isinstance(df, pd.DataFrame)):
            print("error: wrong arguments")
            return None
        self.df = df

    # returns a list containing the years where games were held in the given
    # location
    def when(self, location):
        if not (isinstance(location, str)):
            print("error: wrong arguments")
            return None
        df_location = self.df[self.df['City'] == location]
        if df_location.empty:
            return []
        # Group data by year
        grp = df_location.groupby(["Year"], dropna=False).size()
        return list(grp.index)

    # returns the location where the Olympics took place in the given year
    def where(self, date):
        if not (isinstance(date, int)):
            print("error: wrong arguments")
            return None
        df_date = self.df[self.df['Year'] == date]
        if df_date.empty:
            return []
        # Group data by location
        grp = df_date.groupby(["City"], dropna=False).size()
        return list(grp.index)
