import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("overs.csv")
data.plot.bar(x = 'over', y = 'runs_scored',title = "Test",fontsize = '9',xticks=(0,10,20,30,40,50),grid=True)
plt.show()
