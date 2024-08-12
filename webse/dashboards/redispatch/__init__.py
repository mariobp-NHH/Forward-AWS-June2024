# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:07:31 2021

@author: s14761
"""


#import numpy as np
#import plotly.graph_objects as go
from dash import Dash, html, dcc
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash_defer_js_import as dji
from .module_discriminatory import CDF_dis_ex_ante, CDF_dis_ex_post, welfare_ex_ante, welfare_ex_post, plot_welfare_ex_ante, plot_welfare_ex_post
from .module_plot_figures import fig_area_function, fig_strategies, fig_prices, fig_cs_capita, fig_profits, fig_welfare
from .layout import html_layout

colors= {
    "c": "rgb(38, 70, 83)", #"charcoal"
    "p-g": "rgb(42, 157, 143)", #"persian-green"
    "o-y-c": "rgb(233, 196, 106)", #"orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)", #"sandy-brown"
    "b-s": "rgb(231, 111, 81)" #"burnt-sienna"
    }

external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

#Define the parameters
def parameters(a, b, c):
    al = a
    ah = b
    plot = c
    kl = 60
    kh = 60
    T = 40
    P = 7
    N = 100
    N2 = 400 #Points to work out the expected price for a given al
    return al, ah, plot, kl, kh, T, P, N, N2

# Define the graph function
def graph_in(al, ah, plot,
             Fh_dis_ex_ante, Fl_dis_ex_ante, p_dis_ex_ante, b_dis_ex_ante,
             Fh_dis_ex_post, Fl_dis_ex_post, p_dis_ex_post, b_dis_ex_post,
             Eh_dis_ex_ante, El_dis_ex_ante, E_dis_ex_ante, CS_capita_dis_ex_ante, CS_aggregate_dis_ex_ante, pil_dis_ex_ante, pih_dis_ex_ante, pi_aggregate_dis_ex_ante, welfare_aggregate_dis_ex_ante,
             Eh_dis_ex_post, El_dis_ex_post, E_dis_ex_post, CS_capita_dis_ex_post, CS_capita_adjusted_dis_ex_post, CS_aggregate_dis_ex_post, CS_aggregate_adjusted_dis_ex_post, pil_dis_ex_post, pih_dis_ex_post, pi_aggregate_dis_ex_post, welfare_aggregate_dis_ex_post, welfare_aggregate_adjusted_dis_ex_post,
             ah_lst_dis_ex_ante, Eh_lst_dis_ex_ante, El_lst_dis_ex_ante, E_lst_dis_ex_ante, CS_capita_lst_dis_ex_ante, CS_aggregate_lst_dis_ex_ante, pil_lst_dis_ex_ante, pih_lst_dis_ex_ante, pi_aggregate_lst_dis_ex_ante, welfare_aggregate_lst_dis_ex_ante,
             ah_lst_dis_ex_post, Eh_lst_dis_ex_post, El_lst_dis_ex_post, E_lst_dis_ex_post, CS_capita_lst_dis_ex_post, CS_capita_adjusted_lst_dis_ex_post, CS_aggregate_lst_dis_ex_post, CS_aggregate_adjusted_lst_dis_ex_post, pil_lst_dis_ex_post, pih_lst_dis_ex_post, pi_aggregate_lst_dis_ex_post, welfare_aggregate_lst_dis_ex_post, welfare_aggregate_adjusted_lst_dis_ex_post):
    #Fig area:
    fig_area = fig_area_function(al, ah)
        
    if plot == 'strategies':
        fig1, fig2, fig3 = fig_strategies(p_dis_ex_ante, Fh_dis_ex_ante, Fl_dis_ex_ante, Eh_dis_ex_ante, El_dis_ex_ante, E_dis_ex_ante, p_dis_ex_post, Fh_dis_ex_post, Fl_dis_ex_post, Eh_dis_ex_post, El_dis_ex_post, E_dis_ex_post)
    elif plot == 'prices':
        fig1, fig2, fig3 = fig_prices(ah, ah_lst_dis_ex_ante, Eh_lst_dis_ex_ante, El_lst_dis_ex_ante, E_lst_dis_ex_ante, ah_lst_dis_ex_post, Eh_lst_dis_ex_post, El_lst_dis_ex_post, E_lst_dis_ex_post)
    elif plot == 'cs_capita':
        fig1, fig2, fig3 = fig_cs_capita(ah, ah_lst_dis_ex_ante, CS_capita_lst_dis_ex_ante, ah_lst_dis_ex_post, CS_capita_lst_dis_ex_post, CS_capita_adjusted_lst_dis_ex_post)
    elif plot == 'profits':
        fig1, fig2, fig3 = fig_profits(ah, ah_lst_dis_ex_ante, pil_lst_dis_ex_ante, pih_lst_dis_ex_ante, pi_aggregate_lst_dis_ex_ante, ah_lst_dis_ex_post, pil_lst_dis_ex_post, pih_lst_dis_ex_post, pi_aggregate_lst_dis_ex_post)
    else:
        fig1, fig2, fig3 = fig_welfare(ah, ah_lst_dis_ex_ante, CS_aggregate_lst_dis_ex_ante, pi_aggregate_lst_dis_ex_ante, welfare_aggregate_lst_dis_ex_ante, ah_lst_dis_ex_post, CS_aggregate_lst_dis_ex_post, CS_aggregate_adjusted_lst_dis_ex_post, pi_aggregate_lst_dis_ex_post, welfare_aggregate_lst_dis_ex_post, welfare_aggregate_adjusted_lst_dis_ex_post)  
    
    return fig_area, fig1, fig2, fig3

# Create the app
def create_dash_redispatch(flask_app):
    dash_app = Dash(server=flask_app, name="Dashboard", url_base_pathname="/redispatch/",
                    external_stylesheets=[
                        "/static/css/se_platform/se_platform_layout_spot_go.css",
                        #"/static/dash_spot_go.css",
                        "/static/main.css",
                        "/static/gd_course_chat.css",
                        "/static/css/se_platform/redispatch/codepen.css",
                        "/static/css/se_platform/redispatch/radio.css",
                        "/static/css/se_platform/redispatch/slider.css",
                        "/static/css/se_platform/redispatch/stylesheet.css",
                        "/static/css/se_platform/redispatch/wraper_style1.css",
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
            html.H2("Redispatch - Zonal Market App"),
            #html.Img(src="/assets/stock-icon.png")
            ],className = "banner"),
    
        html.Div([
            html.Div([
                
                html.Label('Demand low-node (al)'),
                dcc.Slider(id="al",
                    min=1,
                    max=19,
                    step=None,
                    marks={
                        1: '1',
                        5: '5',
                        10: '10',
                        15: '15',
                        19: '19',
                    },
                    value=5,
                ),
                
                
                html.Label('Demand high-node (ah)'),
                dcc.Slider(id="ah",
                    min=41,
                    max=99,
                    step=None,
                    marks={
                        41.1: '41.1',
                        45.1: '45.1',
                        50.1: '50.1',
                        55.1: '55.1',
                        59.1: '59.1',
                        65: '65',
                        70: '70',
                        75: '75',
                        80: '80',
                        85: '85',
                        90: '90',
                        95: '95',
                        99: '99',
                    },
                    value=41,
                ),
                
                html.Label('Plot'),
                dcc.RadioItems(id='plot',
                    options=[
                        {'label': 'Strategies', 'value': 'strategies'},
                        {'label': 'Prices', 'value': 'prices'},
                        {'label': 'Consumer Surplus (per capita)', 'value': 'cs_capita'},
                        {'label': 'Profits', 'value': 'profits'},
                        {'label': 'Welfare (aggregate)', 'value': 'aggregate'}
                    ],
                    value='strategies',
                    labelStyle={'display': 'inline-block'},
                    className = "char-btn"
                ),
                
                
            ],className = "box_menu"),
            
            html.Div([   
                
                dcc.Graph(
                    id="fig_area",
                    figure = {}
                ),            
                
            ]),
            
        ],className = "wrapper"),    
        
        html.Div([
            html.Div([
            dcc.Graph(
                    id="fig1",
                    figure = {
                        "layout": {
                            "title": "Discriminatory, ex-ante (strategies)"                        
                        }                
                    }
                ),
            ],className="four columns"),
            
            html.Div([
                dcc.Graph(
                    id="fig2",
                    figure = {
                        "layout": {
                            "title": "Discriminatory, ex-ante \ ex-post (strategies)"                        
                        }                
                    }
                ),
            ],className="four columns"),
            
            html.Div([ 
                dcc.Graph(
                    id="fig3",
                    figure = {
                        "layout": {
                            "title": "Discriminatory, ex-post (strategies)"                        
                        }                
                    }
                ),
            ],className="four columns"),
        ],className="row"),
            
        ])

    # Initialize callbacks after our app is loaded
    # Pass dash_app as a parameter
    init_callbacks(dash_app)
    return dash_app

# Define the callbacks
def init_callbacks(dash_app):
    @dash_app.callback(
        [
            Output('fig_area', 'figure'),
            Output("fig1", "figure"),   
            Output("fig2", "figure"),
            Output("fig3", "figure") 
        ],
        [
            Input('al', 'value'),
            Input('ah', 'value'),
            Input('plot', 'value')
        ]
    )
    def update_graph(a_input, b_input, c_input):
        #Get parameters
        al, ah, plot, kl, kh, T, P, N, N2 = parameters(a_input, b_input, c_input)
        #CDF discriminatory (ex-ante)
        Fh_dis_ex_ante, Fl_dis_ex_ante, p_dis_ex_ante, b_dis_ex_ante = CDF_dis_ex_ante(
            al, ah, kl, kh, T, P, N)
        #CDF discriminatory (ex-post)
        Fh_dis_ex_post, Fl_dis_ex_post, p_dis_ex_post, b_dis_ex_post = CDF_dis_ex_post(
            al, ah, kl, kh, T, P, N)
        #Welfare (ex-ante)
        Eh_dis_ex_ante, El_dis_ex_ante, E_dis_ex_ante, CS_capita_dis_ex_ante, CS_aggregate_dis_ex_ante, pil_dis_ex_ante, pih_dis_ex_ante, pi_aggregate_dis_ex_ante, welfare_aggregate_dis_ex_ante = welfare_ex_ante(
            Fh_dis_ex_ante, Fl_dis_ex_ante, p_dis_ex_ante, al, ah, T, kl, kh, P)
        #Welfare (ex-post)
        Eh_dis_ex_post, El_dis_ex_post, E_dis_ex_post, CS_capita_dis_ex_post, CS_capita_adjusted_dis_ex_post, CS_aggregate_dis_ex_post, CS_aggregate_adjusted_dis_ex_post, pil_dis_ex_post, pih_dis_ex_post, pi_aggregate_dis_ex_post, welfare_aggregate_dis_ex_post, welfare_aggregate_adjusted_dis_ex_post = welfare_ex_post(
            Fh_dis_ex_post, Fl_dis_ex_post, p_dis_ex_post, al, ah, T, kl, kh, P)
        #Plot welfare (ex-ante)
        ah_lst_dis_ex_ante, Eh_lst_dis_ex_ante, El_lst_dis_ex_ante, E_lst_dis_ex_ante, CS_capita_lst_dis_ex_ante, CS_aggregate_lst_dis_ex_ante, pil_lst_dis_ex_ante, pih_lst_dis_ex_ante, pi_aggregate_lst_dis_ex_ante, welfare_aggregate_lst_dis_ex_ante = plot_welfare_ex_ante(
            al, kl, kh, T, P, N, N2)
        #Plot welfare (ex-post)
        ah_lst_dis_ex_post, Eh_lst_dis_ex_post, El_lst_dis_ex_post, E_lst_dis_ex_post, CS_capita_lst_dis_ex_post, CS_capita_adjusted_lst_dis_ex_post, CS_aggregate_lst_dis_ex_post, CS_aggregate_adjusted_lst_dis_ex_post, pil_lst_dis_ex_post, pih_lst_dis_ex_post, pi_aggregate_lst_dis_ex_post, welfare_aggregate_lst_dis_ex_post, welfare_aggregate_adjusted_lst_dis_ex_post = plot_welfare_ex_post(
            al, kl, kh, T, P, N, N2)
        ##Update the graphs
        fig_area, fig1, fig2, fig3 = graph_in(al, ah, plot,
                                    Fh_dis_ex_ante, Fl_dis_ex_ante, p_dis_ex_ante, b_dis_ex_ante,
                                    Fh_dis_ex_post, Fl_dis_ex_post, p_dis_ex_post, b_dis_ex_post,
                                    Eh_dis_ex_ante, El_dis_ex_ante, E_dis_ex_ante, CS_capita_dis_ex_ante, CS_aggregate_dis_ex_ante, pil_dis_ex_ante, pih_dis_ex_ante, pi_aggregate_dis_ex_ante, welfare_aggregate_dis_ex_ante,
                                    Eh_dis_ex_post, El_dis_ex_post, E_dis_ex_post, CS_capita_dis_ex_post, CS_capita_adjusted_dis_ex_post, CS_aggregate_dis_ex_post, CS_aggregate_adjusted_dis_ex_post, pil_dis_ex_post, pih_dis_ex_post, pi_aggregate_dis_ex_post, welfare_aggregate_dis_ex_post, welfare_aggregate_adjusted_dis_ex_post,
                                    ah_lst_dis_ex_ante, Eh_lst_dis_ex_ante, El_lst_dis_ex_ante, E_lst_dis_ex_ante, CS_capita_lst_dis_ex_ante, CS_aggregate_lst_dis_ex_ante, pil_lst_dis_ex_ante, pih_lst_dis_ex_ante, pi_aggregate_lst_dis_ex_ante, welfare_aggregate_lst_dis_ex_ante,
                                    ah_lst_dis_ex_post, Eh_lst_dis_ex_post, El_lst_dis_ex_post, E_lst_dis_ex_post, CS_capita_lst_dis_ex_post, CS_capita_adjusted_lst_dis_ex_post, CS_aggregate_lst_dis_ex_post, CS_aggregate_adjusted_lst_dis_ex_post, pil_lst_dis_ex_post, pih_lst_dis_ex_post, pi_aggregate_lst_dis_ex_post, welfare_aggregate_lst_dis_ex_post, welfare_aggregate_adjusted_lst_dis_ex_post)
        return fig_area,  fig1, fig2, fig3


