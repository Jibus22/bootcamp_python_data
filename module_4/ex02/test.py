from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

fl = FileLoader()
df = fl.load("./athlete_events.csv")

print(proportion_by_sport(df, 2004, "Basketball", "F"))
print(proportion_by_sport(df, 2004, "Basketball", "M"))
print(proportion_by_sport(df, 2004, 'Tennis', 'F'))
