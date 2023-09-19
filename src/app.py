from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
#from dash_bootstrap_templates import load_figure_template
#import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

#load_figure_template('JOURNAL')

df = pd.read_csv('../src/mock-data.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
server = app.server


def generate_dropdown():
    # Dropdown dictionary
    menu = [
        {'id': 'market-dropdown',
         'options':[{'label': market, 'value': market} for market in df['Market'].unique()],
         'placeholder': 'Market',
         'width': 2},
        {'id': 'gender-dropdown',
         'options':[{'label': gender, 'value': gender} for gender in df['Gender'].unique()],
         'placeholder': 'Gender',
         'width': 2},
        {'id': 'age-group-dropdown',
         'options':[{'label': age_group, 'value': age_group} for age_group in df['Age_group'].unique()],
         'placeholder': 'Age group',
         'width': 2},
        {'id': 'date-dropdown',
         'options': [{'label': date, 'value': date} for date in df['Date'].unique()],
         'placeholder': 'Date',
         'width': 2},
        {'id': 'churn-type-dropdown',
         'options': [{'label': churn_type, 'value': churn_type} for churn_type in df['Churn_type'].unique()],
         'placeholder': 'Churn Type',
         'width': 4},
    ]

    return dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id=item['id'],
                options=item['options'],
                multi=True,
                placeholder=item['placeholder'],
                style={'background-color':'#e5ecf6', 'border-radius':'20px', 'border':'0px'}
            )
        ], width=item['width'], className='custom-dropdown')
        for item in menu
    ])

# Using Dash Bootstrap Components to render the app, divided in Rows and Columns in the Rows
app.layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H2(style={'textAlign': 'center', 'height': '50px'}),  # whitespace
            html.H3('Churn Analysis Dashboard',
                    style={'textAlign': 'center', 'height': '1500px', "font-weight": "bold"}),
        ], width=12
        )
    ]),

    generate_dropdown(),

    dbc.Row([
        dbc.Col([
            html.H4('Churn Reasons'),
            html.Div(id='selected-churn-reasons',
                     style={'overflowY': 'scroll', 'height': '800px', 'textAlign': 'left'})
        ], width=4),
        dbc.Col([
            dbc.Row([
                html.H4('Churn type distribution'),
                dcc.Graph(id='churn-bar')
            ]),
            dbc.Row([
                html.H4('Churn type distribution'),
                dcc.Graph(id='graph')
            ])
        ], width=8)
    ])

])


@app.callback(
    Output('churn-bar', 'figure'),
    Output('selected-churn-reasons', 'children'),
    Output('graph', 'figure'),
    Input('market-dropdown', 'value'),
    Input('age-group-dropdown', 'value'),
    Input('gender-dropdown', 'value'),
    Input('date-dropdown', 'value'),
    Input('churn-type-dropdown', 'value')
)
def update_df(selected_markets, selected_age_groups, selected_genders, selected_dates, selected_churn_types):
    if not (selected_markets or selected_age_groups or selected_genders or selected_dates or selected_churn_types):
        filtered_df = df

        churn_type_counts = df['Churn_type'].value_counts()
        churn_type_aov_mean = df.groupby('Churn_type')['AOV'].mean()
        churn_type_app_use_mean = df.groupby('Churn_type')['App_use'].mean()

        selected_churn_reasons = df['Churn_reason']

    else:
        filtered_df = df[
            (df['Market'].isin(selected_markets) if selected_markets else True) &
            (df['Age_group'].isin(selected_age_groups) if selected_age_groups else True) &
            (df['Gender'].isin(selected_genders) if selected_genders else True) &
            (df['Date'].isin(selected_dates) if selected_dates else True) &
            (df['Churn_type'].isin(selected_churn_types) if selected_churn_types else True)
        ]

        churn_type_counts = filtered_df['Churn_type'].value_counts()
        churn_type_aov_mean = filtered_df.groupby('Churn_type')['AOV'].mean()
        churn_type_app_use_mean = filtered_df.groupby('Churn_type')['App_use'].mean()

        selected_churn_reasons = filtered_df['Churn_reason']  # Show Churn_reasons based on selected filters

    # Churn type distribution bar plot
    data = {
        'Churn_type': churn_type_counts.index,
        'Count': churn_type_counts.values,
        'Mean_AOV': churn_type_aov_mean.reindex(churn_type_counts.index).values,
        'Mean_App_Use': churn_type_app_use_mean.reindex(churn_type_counts.index).values
    }
    new_df = pd.DataFrame(data)

    new_df['Mean_AOV'] = new_df['Mean_AOV'].apply(lambda x: f"${int(x):,}")
    new_df['Mean_App_Use'] = new_df['Mean_App_Use'].apply(lambda x: f"{x:.2%}")

    bar_fig = px.bar(new_df, x='Churn_type', y='Count',
                 hover_data=['Count', 'Mean_AOV', 'Mean_App_Use'],
                 labels={'Churn_type': 'Churn Type', 'Mean_AOV': 'Avg. Order Value',
                         'Mean_App_Use': 'Avg. App Use'}#,
                 #template='simple_white',# https://plotly.com/python/templates/
                 #color='Gender', barmode='group'
                 )

    # Scatter plot
    scatter_fig = px.scatter(filtered_df, x="Orders_5y", y="AOV")

    if not selected_churn_types:
        selected_churn_reasons_html = [html.P(reason) for reason in selected_churn_reasons]
    else:
        selected_churn_reasons_html = [html.P(reason) for reason in selected_churn_reasons[
            selected_churn_reasons.isin(df[df['Churn_type'].isin(selected_churn_types)]['Churn_reason'])]]

    return bar_fig, selected_churn_reasons_html, scatter_fig


if __name__ == '__main__':
    app.run_server(debug=True)


## tod  do:
# try write a function for filtering the data frame, then call that function in the callback function displaying the graphs

