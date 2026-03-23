#1. Create a Series (1D data)
import pandas as pd
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)

#. Create a DataFrame (table format)
import pandas as pd

data = {
    "Name": ["Kailash", "Rahul", "Aman"],
    "Age": [22, 25, 21],
    "City": ["Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print(df)