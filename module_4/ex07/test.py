from FileLoader import FileLoader
# from MyPlotLib import MyPlotLib
from Komparator import Komparator
import matplotlib as mp

# Bc boxplot not displayed otherwise, on my macosx
mp.use("QtAgg")

fl = FileLoader()
df = fl.load("./athlete_events.csv")
kmp = Komparator(df)

kmp.compare_box_plots("Sex", "Height")
kmp.compare_box_plots("Medal", "Age")
kmp.compare_histograms("Sex", "Height")
kmp.compare_histograms("Medal", "Height")
kmp.compare_histograms("Medal", "Age")
kmp.density("Medal", "Weight")
kmp.density("Sex", "Height")

# kmp.density("Medal", "Medal")
# kmp.compare_box_plots("Medal", "Medal")
# kmp.compare_histograms("Medal", "Medal")
# kmp.compare_histograms("Height", "Height")
