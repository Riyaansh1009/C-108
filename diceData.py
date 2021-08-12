import random
import plotly.express as pl
import plotly.figure_factory as ff

count = []
diceResult = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    count.append(i)
    diceResult.append(dice1+dice2)
print(diceResult)

# graph = pl.bar(x=diceResult,y=count)
graph = ff.create_distplot([diceResult],["result"],show_hist=False)
graph.show()