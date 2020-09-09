import pandas as pd

data = "cities.csv"

cities = pd.read_csv(data)

cities.to_html("table.html", index=False)


