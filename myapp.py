from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load dataset
df = px.data.gapminder()

# Create a Series of unique countries for the dropdown
countries = df['country'].unique()

# Initialize Dash app
app = Dash(__name__)


server = app.server

# Define layout
app.layout = html.Div([
    html.H1("Global GDP Per Capita Dashboard", style={'textAlign': 'center'}),
    
    html.Label("Select a Country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in countries],
        value='Canada', # Initial value
        clearable=False
    ),
    
    dcc.Graph(id='gdp-growth')
])

# Decorator for callback
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    # Filter dataset
    filtered_df = df[df['country'] == selected_country]
    
    # line plot
    fig = px.line(
        filtered_df, 
        x='year', 
        y='gdpPercap', 
        title=f'GDP Per Capita Growth: {selected_country}',
        markers=True
    )
    
    # Format layout
    fig.update_layout(xaxis_title="Year", yaxis_title="GDP per Capita")
    return fig

# Run app local
if __name__ == '__main__':
    app.run_server(debug=True)