import pandas as pd

def proportion_by_sport(df, year, sport, gender):
    if not (isinstance(df, pd.DataFrame) and isinstance(year, int)
            and isinstance(sport, str) and gender in ["F", "M"]):
        print("error: wrong arguments")
        return None

    participants = df[(df['Sex'] == gender) & (df['Year'] == year)]
    participants = participants.drop_duplicates(subset = "ID")
    participants_by_sport = participants[(participants['Sport'] == sport)]

    return (participants_by_sport.shape[0] / participants.shape[0])
