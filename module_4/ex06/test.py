from FileLoader import FileLoader
from MyPlotLib import MyPlotLib
import matplotlib as mp

# Bc boxplot not displayed otherwise, on my macosx
mp.use("QtAgg")

fl = FileLoader()
df = fl.load("./athlete_events.csv")
mpl = MyPlotLib()

mpl.histogram(df, ["Height", "Weight", "Age", "Year"])
mpl.histogram(df, ["Height"])

mpl.density(df, ["Height"])
mpl.density(df, ["Height", "Weight"])

mpl.pair_plot(df, ["Height", "Weight"])

mpl.box_plot(df, ["Height", "Weight"])
mpl.box_plot(df, ["Height"])
