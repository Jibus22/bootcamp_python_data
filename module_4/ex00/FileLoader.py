import pandas as pd

class FileLoader:
    def __init__(self):
        pass

    def load(self, path):
        try:
            data = pd.read_csv(path)
            print(f"Loading dataset of dimensions {data.shape[0]}x{data.shape[1]}")
        except FileNotFoundError:
            print("error: File not found")
            return None
        except ValueError:
            print("error: Value error")
            return None
        return data

    def display(self, df, n):
        if not (isinstance(df, pd.DataFrame) and isinstance(n, int)):
            print("error: wrong arguments")
            return None
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
