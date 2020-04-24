import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

# Read Tesla (TSLA) shock from Yahoo
df = web.DataReader('TSLA', 'yahoo', start, end)

# Save the data frame to a .csv file
# df.to_csv('tsla.csv')
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)

# Read a .csv file
# df = pd.read_csv("tsla.csv", parse_dates=True, index_col=0)

df.plot()
plt.show()