# AISC_plotly_intro_presentation
Presentation for machine learning community [AISC](https://aisc.ai.science/about) open-mic night introducing the Plotly visualization package

[Click here for PDF presentation.](https://github.com/anitatea/AISC_plotly_intro_presentation/blob/master/Anita%20Tran%20-%20Accelerator%20June%202020.pdf)

Plotly Express is a terse, consistent, high-level API for creating figures. Data visualization with focus on data exploration through rapid iteration.

More about Plotly Express in Python: https://plotly.com/python/plotly-express/

Example of simple function plotted:
```
import plotly.graph_objects as go

x = [i/10 for i in range(-100, 100)]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
y3 = [i**4 for i in x]

fig = go.Figure(data=go.Scatter(x=x, y=y1))
fig.add_trace(go.Scatter(x=x, y=y2))
fig.add_trace(go.Scatter(x=x, y=y3))

fig.show()
```

<img src="https://github.com/anitatea/AISC_plotly_intro_presentation/blob/master/assets/plotting_simple_functions.gif?raw=true">
