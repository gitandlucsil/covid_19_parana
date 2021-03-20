import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go

trace = go.Bar(x = ['Banana', 'Maçã', 'Uva'], y = [10, 20, 30])
data = [trace]
py.iplot(data)