import plotly.graph_objects as go


x = [i for i in range(-10, 10)]
y = [2*i**3 + 3*i + 3 for i in x]

fig = go.Figure(data=[go.Scatter(x=x, y=y)])
fig.show()



import plotly.graph_objects as go

x = [i/10 for i in range(-100, 100)]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
y3 = [i**4 for i in x]

fig = go.Figure(data=go.Scatter(x=x, y=y1))
fig.add_trace(go.Scatter(x=x, y=y2))
fig.add_trace(go.Scatter(x=x, y=y3))

fig.show()
