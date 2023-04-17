from FileLoader import FileLoader
from HowManyMedals import how_many_medals

fl = FileLoader()
df = fl.load("./athlete_events.csv")

def get_athlete_medals(name):
    print(f"{name}:\n  {how_many_medals(df, name)}\n")

get_athlete_medals("Per Knut Aaland")
get_athlete_medals("Kjetil Andr Aamodt")
get_athlete_medals("John Aalberg")
get_athlete_medals("Paavo Johannes Aaltonen")
get_athlete_medals("Pirjo Hannele Aalto (Mattila-)")
get_athlete_medals("Juhamatti Tapio Aaltonen")
get_athlete_medals("Meelis Aasme")
get_athlete_medals("Mohamed Ibrahim Abd El-Fatah Mohamed")
get_athlete_medals("Reem Wa'il Abdalazem Abdalazem El-Bossaty")
get_athlete_medals("Robert Daniel Marie Alfred Franois Dagallier")
get_athlete_medals("pouet")
get_athlete_medals("Gustave Lonard Daghelinckx")
get_athlete_medals("Mustafa Dastanl")
get_athlete_medals("Stephen Daglish")
get_athlete_medals("tienne Dagon")
get_athlete_medals("Nikola Dimitrov Dagorov")
get_athlete_medals("Jennifer ""Jenny"" Dahlgren Fitzner")
get_athlete_medals("Anders Fredrik Dahlin")
get_athlete_medals("Kenza Tifahi Dahmani")
