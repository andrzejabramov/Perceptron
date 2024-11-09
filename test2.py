import pandas as pd
import matplotlib.pyplot as plot
from matplotlib.pyplot import xticks
from setuptools.command.rotate import rotate

_data=[["2017-01-01",28, 30, 33, 39],
      ["2017-01-02",40, 40, 35, 29],
      ["2017-01-03",28, 25, 16, 27],
      ["2017-01-04",33, 35, 37, 39],
      ["2017-01-05", 38, 35, 36, 37]
     ]

_df = pd.DataFrame(_data, columns=["Дата", 27, 2, 20, 6])
_df.plot(x="Дата", y=[27, 2, 20, 6], kind="bar",figsize=(8,4))
plot.xticks(rotation=30)
plot.title('billing')
plot.xlabel('Дата')
plot.ylabel('Траффик')
plot.show()