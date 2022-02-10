import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/Neil/PycharmProjects/amazon stocks/tokyo weather latest.csv")
print(data)
close = data['M']


# for e in range (0,5841):
# print (close[e])


plt.plot(close,label= "hum")
plt.show()