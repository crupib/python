import plotly.graph_objs as go

fig = (
    go.Figure()
    .add_trace(go.Bar(x=['Apples', 'Oranges', 'Bananas', 'Grapes'], y=[2, 3, 6, 8], name='Fruit Eating'))
    .update_traces(marker_color='royalblue', marker_line_color='black', marker_line_width=1.5)
    .update_layout(title_text='Fruit Eating Bar Chart')
)
fig.show()
