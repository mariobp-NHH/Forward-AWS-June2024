from dash import Dash, html, dcc
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_defer_js_import as dji
from flask_login import login_required

import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

colors= {
    "c": "rgb(38, 70, 83)", #"charcoal"
    "p-g": "rgb(42, 157, 143)", #"persian-green"
    "o-y-c": "rgb(233, 196, 106)", #"orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)", #"sandy-brown"
    "b-s": "rgb(231, 111, 81)" #"burnt-sienna"
    }

from .layout import html_layout
from .parameters import parameters
from .simulations import quantities, bounds_GO, CDF_GO, bounds_spot, CDF_spot, exp_price, consumer_surplus_spot, consumer_surplus_go, profit, plot_exp_price
from .spot_go_figures import fig_area_function, fig_go_areas_function, fig_strategies, fig_prices, graph_in



def create_dash_spot_go(flask_app):
    dash_app = Dash(server=flask_app, name="Dashboard", url_base_pathname="/spot_go/",
                    external_stylesheets=[
                        "/static/css/se_platform/se_platform_layout_spot_go.css",
                        "/static/dash_spot_go.css",
                        "/static/main.css",
                        "/static/gd_course_chat.css",
                        "https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css",
                        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css",
                        "https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.css",
                        "https://pro.fontawesome.com/releases/v5.10.0/css/all.css",
                        "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css",
                        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/monokai-sublime.min.css"
                    ],
                    external_scripts=external_scripts)
    
    
    # # Method to protect dash views/routes
    # for view_function in dash_app.server.view_functions:
    #         if view_function.startswith(dash_app.config.url_base_pathname):
    #             dash_app.server.view_functions[view_function] = login_required(
    #                 dash_app.server.view_functions[view_function]
    #             )

    mathjax_script = dji.Import(src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS-MML_SVG")

    dash_app.index_string = html_layout

    dash_app.layout = html.Div([

        html.Div([
            html.Div([
                html.Div([

                    html.Div([
                        html.Div([
                            html.Label('Demand node 1, spot ($a_1^s$)'),
                            dcc.Slider(id="ah_s",
                                       min=7,
                                       max=8,
                                       step=None,
                                       marks={
                                           7: '7',
                                           7.2: '7,2',
                                           7.4: '7.4',
                                           7.6: '7.6',
                                           7.8: '7.8',
                                           8: '8',
                                       },
                                       value=7,
                                       ),

                            html.Label('Demand node 2, spot ($a_2^s$)'),
                            dcc.Slider(id="al_s",
                                       min=7,
                                       max=8,
                                       step=None,
                                       marks={
                                           7: '7',
                                           7.2: '7,2',
                                           7.4: '7.4',
                                           7.6: '7.6',
                                           7.8: '7.8',
                                           8: '8',
                                       },
                                       value=7,
                                       ),

                            html.Label('Demand node 1, GO ($a_1^{go}$)'),
                            dcc.Slider(id="ah_go",
                                       min=2,
                                       max=5,
                                       step=None,
                                       marks={
                                           2: '2',
                                           2.6: '2.6',
                                           3: '3',
                                           4.4: '4.4', 
                                           5: '5',                                          
                                       },
                                       value=3,
                                       ),

                            html.Label('Demand node 2, GO ($a_2^{go}$)'),
                            dcc.Slider(id="al_go",
                                       min=2,
                                       max=5,
                                       step=None,
                                       marks={
                                           2: '2',
                                           2.6: '2.6',
                                           3: '3',
                                           4.4: '4.4',
                                           5: '5',
                                       },
                                       value=3,
                                       ),
                        ], className="menu_box"),

                        html.Div([
                            html.Label('Green capacity node 1 ($\\alpha_1$)'),
                            dcc.Slider(id="alpha1",
                                       min=0.5,
                                       max=1,
                                       step=None,
                                       marks={
                                           0.5: '0.5', 
                                           0.6: '0.6',
                                           0.7: '0.7',
                                           0.8: '0.8',
                                           0.9: '0.9',
                                           1: '1',
                                       },
                                       value=1,
                                       ),

                            html.Label('Green capacity node 2 ($\\alpha_2$)'),
                            dcc.Slider(id="alpha2",
                                       min=0.5,
                                       max=1,
                                       step=None,
                                       marks={
                                           0.5: '0.5',
                                           0.6: '0.6',
                                           0.7: '0.7',
                                           0.8: '0.8',
                                           0.9: '0.9',
                                           1: '1',
                                       },
                                       value=1,
                                       ),
                        ], className="menu_box"),

                        html.Div([
                            html.Label('Plot'),
                            dcc.RadioItems(id='plot',
                                           options=[
                                               {'label': 'Strategies', 'value': 'strategies'},
                                               {'label': 'Prices', 'value': 'prices'},
                                               {'label': 'CS', 'value': 'CS'},
                                               {'label': 'Profits', 'value': 'profit'},
                                               {'label': 'Welfare', 'value': 'welfare'}
                                           ],
                                           value='strategies',
                                           labelStyle={'display': 'inline-block'},
                                           className="char-btn1"
                                           ),

                            html.Label('Cases'),
                            dcc.RadioItems(id='cases',
                                           options=[
                                               {'label': 'GO, no-constraint', 'value': 'case1'},
                                               {'label': 'GO, constraint', 'value': 'case2'}
                                           ],
                                           value='case1',
                                           labelStyle={'display': 'inline-block'},
                                           className="char-btn1"
                                           ),
                        ], className="menu_box"),
                    ], className="spot_go_menu_css"),

                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig_area_spot",
                        figure={
                            "layout": {
                                "title": "Spot market"
                            }
                        }
                    ),
                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig_go_areas",
                        figure={
                            "layout": {"title": "GO market"}
                        }
                    ),
                ], className="box"),

            ], className="spot_go_section_developers3_css"),
        ], className="container"),

        html.Div([
            html.Div([
                html.Div([

                    html.Div([

                        html.Div([
                            html.Label('Spot, equilibrium variables'),
                            html.Table([
                                html.Tr([html.Td(['$p_1^s$']), html.Td(['$p_2^s$']), html.Td(['$CS^s$']), html.Td(['$\pi_1^s$']), html.Td(['$\pi_2^s$']), html.Td(['$W^{s}$'])]),
                                html.Tr([html.Td(id='spot_E1'), html.Td(id='spot_E2'), html.Td(id='CSs_tab'), html.Td(id='pi1s_tab'), html.Td(id='pi2s_tab'), html.Td(id='Ws_tab')]),
                            ]),
                        ], className="menu_box"),

                        html.Div([
                            html.Label('Spot + GO, equilibrium variables'),
                            html.Table([
                                html.Tr([html.Td(['$p_1^{sgo}$']), html.Td(['$p_2^{sgo}$']), html.Td(['$CS^{sgo}$']), html.Td(['$\pi_1^{sgo}$']), html.Td(['$\pi_2^{sgo}$']), html.Td(['$W^{sgo}$'])]),
                                html.Tr([html.Td(id='spot_go_E1'), html.Td(id='spot_go_E2'), html.Td(id='CSsgo_tab'), html.Td(id='pi1sgo_tab'), html.Td(id='pi2sgo_tab'), html.Td(id='Wsgo_tab')]),
                            ]),

                        ], className="menu_box"),
                    ], className="spot_go_menu_css"),

                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig_spot_strategies",
                        figure={
                            "layout": {
                                "title": "Spot (strategies)"
                            }
                        }
                    ),
                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig_spot_go_strategies",
                        figure={
                            "layout": {"title": "Spot + GO (strategies)"}
                        }
                    ),
                ], className="box"),

            ], className="spot_go_section_developers3_css"),
        ], className="container"),

        html.Div([
            html.Div([
                html.Div([

                    html.Div([

                        html.Div([
                            html.Label('GO (branch 1), equilibrium variables'),
                            html.Table([
                                html.Tr([html.Td(['$p_1^{go1}$']), html.Td(['$p_2^{go1}$']), html.Td(['$CS^{go1}$']), html.Td(['$\pi_1^{go1}$']), html.Td(['$\pi_2^{go1}$']), html.Td(['$W^{go1}$'])]),
                                html.Tr([html.Td(id='go1_E1'), html.Td(id='go1_E2'), html.Td(id='CSgo1_tab'), html.Td(id='pi1go1_tab'), html.Td(id='pi2go1_tab'), html.Td(id='Wgo1_tab')]),
                            ]),
                        ], className="menu_box"),

                        html.Div([
                            html.Label('GO (branch 2), equilibrium variables'),
                            html.Table([
                                html.Tr([html.Td(['$p_1^{go2}$']), html.Td(['$p_2^{go2}$']), html.Td(['$CS^{go2}$']), html.Td(['$\pi_1^{go2}$']), html.Td(['$\pi_2^{go2}$']), html.Td(['$W^{go2}$'])]),
                                html.Tr([html.Td(id='go2_E1'), html.Td(id='go2_E2'), html.Td(id='CSgo2_tab'), html.Td(id='pi1go2_tab'), html.Td(id='pi2go2_tab'), html.Td(id='Wgo2_tab')]),
                            ]),

                        ], className="menu_box"),
                    ], className="spot_go_menu_css"),

                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig_go1",
                        figure={
                            "layout": {
                                "title": "GO, branch 1 (strategies)"
                            }
                        }
                    ),
                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig_go2",
                        figure={
                            "layout": {"title": "GO, branch 2 (strategies)"}
                        }
                    ),
                ], className="box"),

            ], className="spot_go_section_developers3_css"),
        ], className="container"),

        mathjax_script
    ], className="container")

    # Initialize callbacks after our app is loaded
    # Pass dash_app as a parameter
    init_callbacks(dash_app)

    return dash_app

def init_callbacks(dash_app):


    @dash_app.callback(
        [
            Output('fig_area_spot', 'figure'),
            Output('fig_go_areas', 'figure'),
            Output('fig_spot_strategies', 'figure'),
            Output('fig_spot_go_strategies', 'figure'),
            Output("fig_go1", "figure"),
            Output("fig_go2", "figure"),
            Output('spot_E1', 'children'),
            Output('spot_E2', 'children'),
            Output('spot_go_E1', 'children'),
            Output('spot_go_E2', 'children'),
            Output('go1_E1', 'children'),
            Output('go1_E2', 'children'),
            Output('go2_E1', 'children'),
            Output('go2_E2', 'children'),
            Output('CSs_tab', 'children'),
            Output('CSsgo_tab', 'children'),
            Output('CSgo1_tab', 'children'),
            Output('CSgo2_tab', 'children'),
            Output('pi1s_tab', 'children'),
            Output('pi2s_tab', 'children'),
            Output('pi1sgo_tab', 'children'),
            Output('pi2sgo_tab', 'children'),
            Output('pi1go1_tab', 'children'),
            Output('pi2go1_tab', 'children'),
            Output('pi1go2_tab', 'children'),
            Output('pi2go2_tab', 'children'),
            Output('Ws_tab', 'children'),
            Output('Wsgo_tab', 'children'),
            Output('Wgo1_tab', 'children'),
            Output('Wgo2_tab', 'children'),
        ],
        [
            Input('ah_s', 'value'),
            Input('al_s', 'value'),
            Input('ah_go', 'value'),
            Input('al_go', 'value'),
            Input('alpha1', 'value'),
            Input('alpha2', 'value'),
            Input('plot', 'value'),
            Input('cases', 'value'),
        ]
    )
    def update_graph(a_input, b_input, c_input, d_input, e_input, f_input, g_input, h_input):
        # Get parameters
        ah, al, ah_go, al_go, alpha1, alpha2, plot, cases, T, pmaxs, pmaxgo, N, N2 = parameters(
            a_input, b_input, c_input, d_input, e_input, f_input, g_input, h_input)

        # Quantities
        q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, cases)
        # GO1:
        b11go, b12go, b1go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch=1)
        F1go1, F2go1, pgo1 = CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, b1go, pmaxgo, branch=1)
        E1go1, E2go1 = exp_price(F1go1, F2go1, pgo1)
        CSgo1 = consumer_surplus_go(al_go, ah_go, E2go1, E1go1, pmaxgo)
        pi1go1, pi2go1 = profit(b1go, q1go11, q1go22)
        Wgo1 = CSgo1 + pi1go1 + pi2go1
        # GO2:
        b21go, b22go, b2go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch=2)
        F1go2, F2go2, pgo2 = CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, b2go, pmaxgo, branch=2)
        E1go2, E2go2 = exp_price(F1go2, F2go2, pgo2)
        CSgo2 = consumer_surplus_go(al_go, ah_go, E2go2, E1go2, pmaxgo)
        pi1go2, pi2go2 = profit(b2go, q2go11, q2go22)
        Wgo2 = CSgo2 + pi1go2 + pi2go2
        # Spot
        b1sgo, b2sgo, bsgo = bounds_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, b1go, b2go, pmaxs)
        F1sgo, F2sgo, psgo = CDF_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, N, bsgo, b1go, b2go, pmaxs)
        E1sgo, E2sgo = exp_price(F1sgo, F2sgo, psgo)
        CSsgo = consumer_surplus_spot(al, ah, E2sgo, E1sgo, pmaxs)
        pi1sgo, pi2sgo = profit(bsgo, q11, q22)
        Wsgo = CSsgo + pi1sgo + pi2sgo
        b1s, b2s, bs = bounds_spot(q11, q12, q21, q22, 0, 0, 0, 0, 0, 0, pmaxs)
        F1s, F2s, ps = CDF_spot(q11, q12, q21, q22, 0, 0, 0, 0, N, bs, 0, 0, pmaxs)
        E1s, E2s = exp_price(F1s, F2s, ps)
        CSs = consumer_surplus_spot(al, ah, E2s, E1s, pmaxs)
        pi1s, pi2s = profit(bs, q11, q22)
        Ws = CSs + pi1s + pi2s

        # GO2 Price
        E1go2_lst, E2go2_lst, a2_lst, CSgo2_lst, pi1go2_lst, pi2go2_lst, Wgo2_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, alpha1, alpha2, cases, branch=2)
        # GO1 Price
        E1go1_lst, E2go1_lst, a2_lst, CSgo1_lst, pi1go1_lst, pi2go1_lst, Wgo1_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, alpha1, alpha2, cases, branch=1)
        # Spot Price
        Esgo1_lst, Esgo2_lst, a2_lst, CSsgo_lst, pi1sgo_lst, pi2sgo_lst, Wsgo_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, alpha1, alpha2, cases, branch=0)
        Es1_lst, Es2_lst, a2_lst, CSs_lst, pi1s_lst, pi2s_lst, Ws_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, alpha1, alpha2, cases, branch=-1)


        #Table Spot
        spot_E1 = round(E1s,3)
        spot_E2 = round(E2s,3)
        spot_go_E1 = round(E1sgo,3)
        spot_go_E2 = round(E2sgo,3)
        CSs_tab = round(CSs, 2)
        CSsgo_tab = round(CSsgo, 2)
        pi1s_tab = round(pi1s,2)
        pi2s_tab = round(pi2s,2)
        pi1sgo_tab = round(pi1sgo, 2)
        pi2sgo_tab = round(pi2sgo, 2)
        Ws_tab = round(Ws,2)
        Wsgo_tab = round(Wsgo, 2)

        #Table GO
        go1_E1 = round(E1go1,2)
        go1_E2 = round(E2go1,2)
        go2_E1 = round(E1go2,2)
        go2_E2 = round(E2go2,2)
        CSgo1_tab = round(CSgo1,2)
        CSgo2_tab = round(CSgo2,2)
        pi1go1_tab = round(pi1go1, 2)
        pi2go1_tab = round(pi2go1, 2)
        pi1go2_tab = round(pi1go2, 2)
        pi2go2_tab = round(pi2go2, 2)
        Wgo1_tab = round(Wgo1, 2)
        Wgo2_tab = round(Wgo2, 2)

        fig_area_spot, fig_go_areas, fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2 = graph_in(plot, ah, al, ah_go, al_go,
                                                             T, q11, q12, q21, q22, alpha1, alpha2,
                                                             pgo1, F1go1, F1go2, E1go1, E1go2,
                                                             pgo2, F2go1, F2go2, E2go1, E2go2,
                                                             psgo, F1sgo, F2sgo, E1sgo, E2sgo,
                                                             ps, F1s, F2s, E1s, E2s,
                                                             pmaxgo, pmaxs, a2_lst, E1go1_lst, E2go1_lst,
                                                             Esgo1_lst, Esgo2_lst,
                                                             Es1_lst, Es2_lst,
                                                             E1go2_lst, E2go2_lst,
                                                             CSgo1_lst, CSgo2_lst, CSsgo_lst, CSs_lst,
                                                             pi1go1_lst, pi2go1_lst, pi1go2_lst, pi2go2_lst, pi1sgo_lst, pi2sgo_lst, pi1s_lst, pi2s_lst,
                                                             Wgo1_lst, Wgo2_lst, Wsgo_lst, Ws_lst)

        return fig_area_spot, fig_go_areas, fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2, spot_E1, spot_E2, spot_go_E1, spot_go_E2, go1_E1, go1_E2, go2_E1, go2_E2, CSs_tab, CSsgo_tab, CSgo1_tab, CSgo2_tab, pi1s_tab, pi2s_tab, pi1sgo_tab, pi2sgo_tab, pi1go1_tab, pi2go1_tab, pi1go2_tab, pi2go2_tab, Ws_tab, Wsgo_tab, Wgo1_tab, Wgo2_tab
