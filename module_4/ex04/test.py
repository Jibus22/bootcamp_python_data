from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

fl = FileLoader()
df = fl.load("./athlete_events.csv")

sp = SpatioTemporalData(df)

def print_when(location):
    print(f"{location}:\n  {sp.when(location)}")

def print_where(date):
    print(f"{date}:\n  {sp.where(date)}")

print("--- WHERE ---")
print_when('Athina')
# Output [2004, 1906, 1896]
print_when('Paris')
# Output [1900, 1924]
print_when('bla')
print_when('Beijing')
print_when('Rio de Janeiro')

print("\n--- WHEN ---")
print_where(1896)
# Output ['Athina']
print_where(2016)
# Output ['Rio de Janeiro']
print_where(2015)
print_where(-324)
print_where(1948)
print_where(2012)
