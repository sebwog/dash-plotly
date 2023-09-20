from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
#from dash_bootstrap_templates import load_figure_template
#import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

#load_figure_template('JOURNAL')

df = pd.read_csv('../src/mock-data-v3.csv')

df = df[df.Churn_type != 'No answer']

app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL], assets_folder = 'assets')
server = app.server


# def generate_dropdown():
#     # Dropdown dictionary
#     menu = [
#         {'id': 'market-dropdown',
#          'options':[{'label': market, 'value': market} for market in df['Market'].unique()],
#          'placeholder': 'Market',
#          'width': 1},
#         {'id': 'gender-dropdown',
#          'options':[{'label': gender, 'value': gender} for gender in df['Gender'].unique()],
#          'placeholder': 'Gender',
#          'width': "1"},
#         {'id': 'age-group-dropdown',
#          'options':[{'label': age_group, 'value': age_group} for age_group in df['Age_group_2'].unique()],
#          'placeholder': 'Age',
#          'width': 1},
#         {'id': 'date-dropdown',
#          'options': [{'label': date, 'value': date} for date in df['Date'].unique()],
#          'placeholder': 'Date',
#          'width': 1},
#         {'id': 'churn-type-dropdown',
#          'options': [{'label': churn_type, 'value': churn_type} for churn_type in df['Churn_type'].unique()],
#          'placeholder': 'Churn Type',
#          'width': 4},
#     ]
#
#     return dbc.Row([
#         dbc.Col([
#             dcc.Dropdown(
#                 id=item['id'],
#                 options=item['options'],
#                 multi=True,
#                 placeholder=item['placeholder'],
#                 style={'background-color':'#F3F3F7', 'border-radius':'20px', 'border':'0px'}
#             )
#         ], width=item['width'], className='custom-dropdown')
#         for item in menu
#     ])

# Using Dash Bootstrap Components to render the app, divided in Rows and Columns in the Rows
app.layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H2(style={'textAlign': 'center', 'height': '50px'}),  # whitespace
            html.H3('Churn Analysis Dashboard',
                    style={'textAlign': 'center', 'height': '100px', "font-weight": "bold", 'font-family':'Arial'}
                    ),
        ], width=12
        )
    ]),

    dbc.Row([
        dbc.Col([html.H4()], width=2),
        dbc.Col([html.H4('Churn type distribution')], width=7),
        dbc.Col([html.H4('Churn reasons')], width=3),
    ]),

    dbc.Row([
        dbc.Col([
            html.H2(style={'textAlign': 'center', 'height': '5px'})  # whitespace
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Row([
                dcc.Dropdown(
                    id='market-dropdown',
                    options=[{'label': market, 'value': market} for market in df['Market'].unique()],
                    multi=True,
                    placeholder='Market',
                    style={'background-color':'#F3F3F7', 'border-radius':'20px', 'border':'0px'})
            ]),
            dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})), #whitespace
            dbc.Row([
                dcc.Dropdown(
                    id='gender-dropdown',
                    options=[{'label': gender, 'value': gender} for gender in df['Gender'].unique()],
                    multi=True,
                    placeholder='Gender',
                    style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            ]),
            dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})), #whitespace
            dbc.Row([
                dcc.Dropdown(
                    id='age-group-dropdown',
                    options=[{'label': age_group, 'value': age_group} for age_group in
                             df.sort_values(by=['Age_group_2'])['Age_group_2'].unique()],
                    multi=True,
                    placeholder='Age',
                    style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            ]),
            # dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})), #whitespace
            # dbc.Row([
            #     dcc.Dropdown(
            #         id='date-dropdown',
            #         options=[{'label': date, 'value': date} for date in df['Date'].unique()],
            #         multi=True,
            #         placeholder='Date',
            #         style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            # ]),
            dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})),  # whitespace
            dbc.Row([
                dcc.Dropdown(
                    id='app-use-dropdown',
                    options=[{'label': 'No', 'value': 0}, {'label': 'Yes', 'value': 1}],
                    multi=True,
                    placeholder='App use',
                    style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            ]),
            dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})),  # whitespace
            dbc.Row([
                dcc.Dropdown(
                    id='card-use-dropdown',
                    options=[{'label': 'No', 'value': 0}, {'label': 'Yes', 'value': 1}],
                    multi=True,
                    placeholder='Card use',
                    style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            ]),
            dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})),  # whitespace
            dbc.Row([
                dcc.Dropdown(
                    id='cs-contact-dropdown',
                    options=[{'label': 'No', 'value': 0}, {'label': 'Yes', 'value': 1}],
                    multi=True,
                    placeholder='CS contact',
                    style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            ]),
            dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})),  # whitespace
            dbc.Row([
                dcc.Dropdown(
                    id='shopping-search-dropdown',
                    options=[{'label': 'No', 'value': 0}, {'label': 'Yes', 'value': 1}],
                    multi=True,
                    placeholder='Shopping search',
                    style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            ])
        ], width=2, className='custom-dropdown'),

        dbc.Col([
            dbc.Row([
                dcc.Graph(id='churn-bar')
            ]),
            dbc.Row([html.H4('Number of orders & AOV insights')]),
            dbc.Row([
                dcc.Graph(id='graph')
            ])

        ], width=7),

        dbc.Col([
            dbc.Row([
                dcc.Dropdown(id='churn-type-dropdown',
                             options=[{'label': churn_type, 'value': churn_type} for churn_type in
                                      df['Churn_type'].unique()],
                             multi=True, placeholder='Filter by churn type',
                             style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
            ]),
            dbc.Row(html.H2(style={'textAlign': 'center', 'height': '2px'})), #whitespace
            dbc.Row([
                html.Div(id='selected-churn-reasons',
                         style={'overflowY': 'scroll', 'height': '600px', 'textAlign': 'left'})
            ])

        ], width=3, className='custom-dropdown')
    ]),

    #generate_dropdown(),

    # dbc.Row([
    #     dbc.Col([
    #         dcc.Dropdown(id='market-dropdown', options=[{'label': market, 'value': market} for market in df['Market'].unique()],
    #                      multi=True, placeholder='Market',
    #                      style={'background-color':'#F3F3F7', 'border-radius':'20px', 'border':'0px'})
    #     ], width=1, className='custom-dropdown'),
    #     dbc.Col([
    #         dcc.Dropdown(id='gender-dropdown',
    #                      options=[{'label': gender, 'value': gender} for gender in df['Gender'].unique()],
    #                      multi=True, placeholder='Gender',
    #                      style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
    #     ], width=1, className='custom-dropdown'),
    #     dbc.Col([
    #         dcc.Dropdown(id='age-group-dropdown',
    #                      options=[{'label': age_group, 'value': age_group} for age_group in df['Age_group_2'].unique()],
    #                      multi=True, placeholder='Age',
    #                      style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
    #     ], width=1, className='custom-dropdown'),
    #     dbc.Col([
    #         dcc.Dropdown(id='date-dropdown',
    #                      options=[{'label': date, 'value': date} for date in df['Date'].unique()],
    #                      multi=True, placeholder='Date',
    #                      style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
    #     ], width=1, className='custom-dropdown'),
    #     dbc.Col([html.H4()], width=4),
    #     dbc.Col([
    #         dcc.Dropdown(id='churn-type-dropdown',
    #                      options=[{'label': churn_type, 'value': churn_type} for churn_type in df['Churn_type'].unique()],
    #                      multi=True, placeholder='Filter by churn type',
    #                      style={'background-color': '#F3F3F7', 'border-radius': '20px', 'border': '0px'})
    #     ], width=4, className='custom-dropdown'),
    # ]),
    #
    # dbc.Row([
    #     dbc.Col([
    #         html.H2(style={'textAlign': 'center', 'height': '10px'})  # whitespace
    #     ], width=12)
    # ]),
    #
    # dbc.Row([
    #     dbc.Col([
    #         dbc.Row([
    #             dcc.Graph(id='churn-bar')
    #         ])#,
    #         # dbc.Row([
    #         #     html.H4('AOV vs number of orders last 5 years'),
    #         #     dcc.Graph(id='graph')
    #         # ])
    #     ], width=7),
    #     dbc.Col([html.H4()], width=1),
    #     dbc.Col([
    #         html.Div(id='selected-churn-reasons',
    #                  style={'overflowY': 'scroll', 'height': '400px', 'textAlign': 'left'})
    #     ], width=4)
    # ]),

    # dbc.Row([
    #     dbc.Col([
    #         html.H4('Churn Reasons', style={'font-family':'Arial'}),
    #         html.Div(id='selected-churn-reasons',
    #                  style={'overflowY': 'scroll', 'height': '800px', 'textAlign': 'left'})
    #     ], width=4),
    #     dbc.Col([
    #         dbc.Row([
    #             html.H4('Churn type distribution'),
    #             dcc.Graph(id='churn-bar')
    #         ]),
    #         dbc.Row([
    #             html.H4('AOV vs number of orders last 5 years'),
    #             dcc.Graph(id='graph')
    #         ])
    #     ], width=8)
    # ])

])


@app.callback(
    Output('churn-bar', 'figure'),
    Output('selected-churn-reasons', 'children'),
    Output('graph', 'figure'),
    Input('market-dropdown', 'value'),
    Input('age-group-dropdown', 'value'),
    Input('gender-dropdown', 'value'),
    #Input('date-dropdown', 'value'),
    Input('churn-type-dropdown', 'value'),
    Input('app-use-dropdown', 'value'),
    Input('card-use-dropdown', 'value'),
    Input('cs-contact-dropdown', 'value'),
    Input('shopping-search-dropdown', 'value')
)
def update_df(selected_markets, selected_age_groups, selected_genders, #selected_dates,
              selected_churn_types, selected_app_use, selected_card_use, selected_cs_contact, selected_shopping_search):
    if not (selected_markets or selected_age_groups or selected_genders #or selected_dates
            or selected_churn_types or selected_app_use or selected_card_use or selected_cs_contact or selected_shopping_search):

        filtered_df = df

        churn_type_counts = df['Churn_type'].value_counts()
        churn_type_aov_mean = df.groupby('Churn_type')['AOV'].mean()
        churn_type_app_use_mean = df.groupby('Churn_type')['App_use'].mean()
        churn_type_card_use_mean = df.groupby('Churn_type')['Card_use'].mean()

        selected_churn_reasons = df['Churn_reason']

    else:
        filtered_df = df[
            (df['Market'].isin(selected_markets) if selected_markets else True) &
            (df['Age_group_2'].isin(selected_age_groups) if selected_age_groups else True) &
            (df['Gender'].isin(selected_genders) if selected_genders else True) &
            #(df['Date'].isin(selected_dates) if selected_dates else True) &
            (df['Churn_type'].isin(selected_churn_types) if selected_churn_types else True) &
            (df['App_use'].isin(selected_app_use) if selected_app_use else True) &
            (df['Card_use'].isin(selected_card_use) if selected_card_use else True) &
            (df['CS_contact'].isin(selected_cs_contact) if selected_cs_contact else True) &
            (df['Shopping_search'].isin(selected_shopping_search) if selected_shopping_search else True)
        ]

        churn_type_counts = filtered_df['Churn_type'].value_counts()
        churn_type_aov_mean = filtered_df.groupby('Churn_type')['AOV'].mean()
        churn_type_app_use_mean = filtered_df.groupby('Churn_type')['App_use'].mean()
        churn_type_card_use_mean = filtered_df.groupby('Churn_type')['Card_use'].mean()

        selected_churn_reasons = filtered_df['Churn_reason']  # Show Churn_reasons based on selected filters

    # Churn type distribution bar plot
    data = {
        'Churn_type': churn_type_counts.index,
        'Count': churn_type_counts.values,
        'Mean_AOV': churn_type_aov_mean.reindex(churn_type_counts.index).values,
        'Mean_App_Use': churn_type_app_use_mean.reindex(churn_type_counts.index).values,
        'Mean_Card_Use': churn_type_card_use_mean.reindex(churn_type_counts.index).values
    }
    new_df = pd.DataFrame(data)

    new_df['Mean_AOV'] = new_df['Mean_AOV'].apply(lambda x: f"${int(x):,}")
    new_df['Mean_App_Use'] = new_df['Mean_App_Use'].apply(lambda x: f"{x:.2%}")
    new_df['Mean_Card_Use'] = new_df['Mean_Card_Use'].apply(lambda x: f"{x:.2%}")

    bar_fig = px.bar(new_df, x='Churn_type', y='Count',#title='Churn type distribution',
                 hover_data=['Count', 'Mean_AOV', 'Mean_App_Use', 'Mean_Card_Use'],
                 labels={'Churn_type': 'Churn Type', 'Mean_AOV': 'Avg. Order Value',
                         'Mean_App_Use': 'Avg. App Use', 'Mean_Card_Use': 'Avg. Card Use'}#,
                 #template='simple_white',# https://plotly.com/python/templates/
                 #color='Gender', barmode='group'
                 )
    bar_fig.update_traces(marker_color='#FFB3C7')
    bar_fig.update_layout(plot_bgcolor="#F3F3F7", margin=dict(l=30, r=30, t=0, b=0))

    # Scatter plot
    scatter_fig = px.scatter(filtered_df, x="Orders_5y", y="Orders_1y",
                             log_x=True, log_y=True, color='Gender', size='AOV',
                             labels={
                                 'Orders_5y': '# of orders in the past 5 years',
                                 'Orders_1y': '# of orders in the past year'
                             })
    #scatter_fig.update_traces(marker_color='#FFB3C7')
    scatter_fig.update_layout(plot_bgcolor="#F3F3F7", margin=dict(l=30, r=30, t=40, b=0))

    # histogram_fig = px.histogram(filtered_df, x='Orders_1y')
    # histogram_fig.update_traces(marker_color='#FFB3C7')
    # histogram_fig.update_layout(plot_bgcolor="#F3F3F7", margin=dict(l=30, r=30, t=0, b=0))

    # Selected churn reasons
    if not selected_churn_types:
        selected_churn_reasons_html = [html.P(reason) for reason in selected_churn_reasons]
    else:
        selected_churn_reasons_html = [html.P(reason) for reason in selected_churn_reasons[
            selected_churn_reasons.isin(df[df['Churn_type'].isin(selected_churn_types)]['Churn_reason'])]]

    return bar_fig, selected_churn_reasons_html, scatter_fig


if __name__ == '__main__':
    #app.run(debug=True)
    app.run_server(debug=True)


