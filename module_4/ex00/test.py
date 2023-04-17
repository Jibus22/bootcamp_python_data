from FileLoader import FileLoader

fl = FileLoader()
ds = fl.load("./athlete_events.csv")

fl.display(ds, 2)
fl.display(ds, -2)
fl.display(ds, 12)
