from FileLoader import FileLoader
from YoungestFellah import YoungestFellah

fl = FileLoader()
df = fl.load("./athlete_events.csv")

print(YoungestFellah(df, 1980))
print(YoungestFellah(df, 2004))
print(YoungestFellah(df, 2014))
print(YoungestFellah(df, 1991))
print(YoungestFellah(df, 2003))
