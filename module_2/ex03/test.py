from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader("bla.csv", header=True, skip_bottom=1, skip_top=19) as file:
        if file == None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()

            print(f"DATA: len: {len(data)}\n{data}\n")
            print(f"----\nHEADER: {header}\n")

    print(80 * "-")

    with CsvReader("bad.csv") as file:
        if file == None:
            print("File is corrupted")
