import pandas
import plotly.figure_factory as pf

df = pandas.read_csv("data.csv")
fig = pf.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"]. show_hist= False)

fig.show()

