# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:51:20 2021

@author: s14761
"""
import plotly.graph_objects as go
colors= {
    "c": "rgb(38, 70, 83)", #"charcoal"
    "p-g": "rgb(42, 157, 143)", #"persian-green"
    "o-y-c": "rgb(233, 196, 106)", #"orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)", #"sandy-brown"
    "b-s": "rgb(231, 111, 81)" #"burnt-sienna"
    }


def fig_area_function(al, ah):
    fig_area = go.Figure()
    fig_area.update_layout(title={
                    'text': "Equilibrium areas",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='demand low-node (al)',
                    yaxis_title='demand high-node (ah)')
    fig_area.update_yaxes(range=[40, 100])  
    fig_area.update_xaxes(range=[0, 20])
    fig_area.update_yaxes(tickvals=[41.1, 45.1, 50.1, 55.1, 59.1, 65, 70, 75, 80, 85, 90, 95, 99])
    fig_area.update_xaxes(tickangle=0, tickvals=[1, 5, 10, 15, 19, 60, 100])
    fig_area.update_yaxes(showgrid=False)
    fig_area.update_xaxes(showgrid=False)
        
    fig_area.add_trace(go.Scatter(
    x=[0, 20], y=[40, 40],
    showlegend=False,
    fill=None,
    mode='lines',
    line=dict(width=0.5, color=colors["c"]),))
    fig_area.add_trace(go.Scatter(
    x=[0, 20], y=[60, 40],
    showlegend=False,
    fill='tonexty',
    mode='lines',
    line=dict(width=0.5, color=colors["c"]),))
    fig_area.add_trace(go.Scatter(
    x=[0, 20], y=[100, 100],
    showlegend=False,
    fill='tonexty',
    mode='lines',
    line=dict(width=0.5, color=colors["p-g"]),))
    
    fig_area.add_trace(go.Scatter(x=[0, al], y=[ah, ah], mode= 'lines', showlegend=False,
                    line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_area.add_trace(go.Scatter(x=[al, al], y=[0, ah], mode= 'lines', showlegend=False,
                    line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_area.add_scatter(x=[al],y=[ah], mode="markers", showlegend=False,
                marker=dict(size=10, color=colors["s-b"]))
    
    return fig_area

def fig_strategies(p_dis_ex_ante, Fh_dis_ex_ante, Fl_dis_ex_ante, Eh_dis_ex_ante, El_dis_ex_ante, E_dis_ex_ante, p_dis_ex_post, Fh_dis_ex_post, Fl_dis_ex_post, Eh_dis_ex_post, El_dis_ex_post, E_dis_ex_post):
    #Fig 1: Discriminatory, ex-ante (strategies)
    color1='blue'
    color2='red'
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=p_dis_ex_ante, y=Fh_dis_ex_ante,
                        mode='lines',
                        name='Fh (ex-ante)',
                        line = dict(color=colors["c"], width=1.5)))
    fig1.add_trace(go.Scatter(x=p_dis_ex_ante, y=Fl_dis_ex_ante,
                        mode='lines',
                        name='Fl (ex-ante)',
                        line = dict(color=colors["p-g"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[Eh_dis_ex_ante,Eh_dis_ex_ante], y=[0,1],
                        mode='lines',
                        name='Eh (ex-ante)',
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[El_dis_ex_ante,El_dis_ex_ante], y=[0,1],
                        mode='lines',
                        name='El (ex-ante)',
                        line = dict(color=colors["s-b"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[E_dis_ex_ante,E_dis_ex_ante], y=[0,1],
                        mode='lines',
                        name='E (ex-ante)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig1.update_layout(title={
                    'text': "Discriminatory, ex-ante (strategies)",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='Price',
                    yaxis_title='CDF')
    fig1.update_yaxes(range=[0, 1.1])  
    fig1.update_xaxes(range=[0, 7.1]) 
    fig1.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])
    
    #Fig 2: Discriminatory, ex-ante \ ex-post (strategies)
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=p_dis_ex_ante, y=Fh_dis_ex_ante,
                        mode='lines',
                        name='Fh (ex-ante)',
                        opacity=.2,
                        line = dict(color=colors["c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=p_dis_ex_ante, y=Fl_dis_ex_ante,
                        mode='lines',
                        name='Fl (ex-ante)',
                        opacity=.2,
                        line = dict(color=colors["p-g"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[Eh_dis_ex_ante,Eh_dis_ex_ante], y=[0,1],
                        mode='lines',
                        name='Eh (ex-ante)',
                        opacity=.2,
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[El_dis_ex_ante,El_dis_ex_ante], y=[0,1],
                        mode='lines',
                        name='El (ex-ante)',
                        opacity=.2,
                        line = dict(color=colors["s-b"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E_dis_ex_ante,E_dis_ex_ante], y=[0,1],
                        mode='lines',
                        opacity=.2,
                        name='E (ex-ante)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig2.add_trace(go.Scatter(x=p_dis_ex_post, y=Fh_dis_ex_post,
                        mode='lines',
                        name='Fh (ex-post)',
                        line = dict(color=colors["c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=p_dis_ex_post, y=Fl_dis_ex_post,
                        mode='lines',
                        name='Fl (ex-post)',
                        line = dict(color=colors["p-g"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[Eh_dis_ex_post,Eh_dis_ex_post], y=[0,1],
                        mode='lines',
                        name='Eh (ex-post)',
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[El_dis_ex_post,El_dis_ex_post], y=[0,1],
                        mode='lines',
                        name='El (ex-post)',
                        line = dict(color=colors["s-b"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E_dis_ex_post,E_dis_ex_post], y=[0,1],
                        mode='lines',
                        name='E (ex-post)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig2.update_layout(title={
                    'text': "Discriminatory, ex-ante \ ex-post (strategies)",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='Price',
                    yaxis_title='CDF')
    fig2.update_yaxes(range=[0, 1.1])  
    fig2.update_xaxes(range=[0, 7.1]) 
    fig2.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])
    
    #Fig 3: Discriminatory, ex-post (strategies)
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=p_dis_ex_post, y=Fh_dis_ex_post,
                        mode='lines',
                        name='Fh (ex-post)',
                        line = dict(color=colors["c"], width=1.5)))
    fig3.add_trace(go.Scatter(x=p_dis_ex_post, y=Fl_dis_ex_post,
                        mode='lines',
                        name='Fl (ex-post)',
                        line = dict(color=colors["p-g"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[Eh_dis_ex_post,Eh_dis_ex_post], y=[0,1],
                        mode='lines',
                        name='Eh (ex-post)',
                        line = dict(color=colors["o-y-c"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[El_dis_ex_post,El_dis_ex_post], y=[0,1],
                        mode='lines',
                        name='El (ex-post)',
                        line = dict(color=colors["s-b"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[E_dis_ex_post,E_dis_ex_post], y=[0,1],
                        mode='lines',
                        name='E (ex-post)',
                        line = dict(color=colors["b-s"], width=1.5)))
    fig3.update_layout(title={
                    'text': "Discriminatory, ex-post (strategies)",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    xaxis_title='Price',
                    yaxis_title='CDF')
    fig3.update_yaxes(range=[0, 1.1])  
    fig3.update_xaxes(range=[0, 7.1]) 
    fig3.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])
    
    return fig1, fig2, fig3
    

def fig_prices(ah, ah_lst_dis_ex_ante, Eh_lst_dis_ex_ante, El_lst_dis_ex_ante, E_lst_dis_ex_ante, ah_lst_dis_ex_post, Eh_lst_dis_ex_post, El_lst_dis_ex_post, E_lst_dis_ex_post):
        #Fig 1: Discriminatory, ex-ante (prices)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=Eh_lst_dis_ex_ante,
                            mode='lines',
                            name='Eh (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=El_lst_dis_ex_ante,
                            mode='lines',
                            name='El (ex-ante)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=E_lst_dis_ex_ante,
                            mode='lines',
                            name='El (ex-ante)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.update_layout(title={
                        'text': "Discriminatory, ex-ante (prices)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Price')
        fig1.update_yaxes(range=[0, 7])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (prices)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=Eh_lst_dis_ex_ante,
                            mode='lines',
                            name='Eh (ex-ante)',
                            opacity=.2,
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=El_lst_dis_ex_ante,
                            mode='lines',
                            name='El (ex-ante)',
                            opacity=.2,
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=E_lst_dis_ex_ante,
                            mode='lines',
                            opacity=.2,
                            name='El (ex-ante)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=Eh_lst_dis_ex_post,
                            mode='lines',
                            name='Eh (ex-post)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=El_lst_dis_ex_post,
                            mode='lines',
                            name='El (ex-post)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=E_lst_dis_ex_post,
                            mode='lines',
                            name='E (ex-post)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.update_layout(title={
                        'text': "Discriminatory, ex-ante \ ex-post (prices)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Price')
        fig2.update_yaxes(range=[0, 7])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: : Discriminatory, ex-post (prices)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=Eh_lst_dis_ex_post,
                            mode='lines',
                            name='Eh (ex-post)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=El_lst_dis_ex_post,
                            mode='lines',
                            name='El (ex-post)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=E_lst_dis_ex_post,
                            mode='lines',
                            name='E (ex-post)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.update_layout(title={
                        'text': "Discriminatory, ex-post (prices)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Price')
        fig3.update_yaxes(range=[0, 7])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        return fig1, fig2, fig3
    
def fig_cs_capita(ah, ah_lst_dis_ex_ante, CS_capita_lst_dis_ex_ante, ah_lst_dis_ex_post, CS_capita_lst_dis_ex_post, CS_capita_adjusted_lst_dis_ex_post):
        #Fig 1: Discriminatory, ex-ante (CS capita)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=CS_capita_lst_dis_ex_ante,
                            mode='lines',
                            name='CS (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.update_layout(title={
                        'text': "Discriminatory, ex-ante (CS (capita))",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='CS (capita)')
        fig1.update_yaxes(range=[0, 7])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (CS capita)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=CS_capita_lst_dis_ex_ante,
                            mode='lines',
                            opacity=.2,
                            name='CS (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_capita_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS (ex-post)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_capita_adjusted_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS ad (ex-post)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.update_layout(title={
                        'text': "Discriminatory, ex-ante \ ex-post (CS capita)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='CS (capita)')
        fig2.update_yaxes(range=[0, 7])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: : Discriminatory, ex-post (CS capita)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_capita_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS (ex-post)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_capita_adjusted_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS ad (ex-post)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,7],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.update_layout(title={
                        'text': "Discriminatory, ex-post (CS capita)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='CS (capita)')
        fig3.update_yaxes(range=[0, 7])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        return fig1, fig2, fig3

def fig_profits(ah, ah_lst_dis_ex_ante, pil_lst_dis_ex_ante, pih_lst_dis_ex_ante, pi_aggregate_lst_dis_ex_ante, ah_lst_dis_ex_post, pil_lst_dis_ex_post, pih_lst_dis_ex_post, pi_aggregate_lst_dis_ex_post):
    #Fig 1: Discriminatory, ex-ante (profits)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pil_lst_dis_ex_ante,
                            mode='lines',
                            name='pil (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pih_lst_dis_ex_ante,
                            mode='lines',
                            name='pih (ex-ante)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pi_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            name='pi (ex-ante)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,500],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.update_layout(title={
                        'text': "Discriminatory, ex-ante (profits)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Profit')
        fig1.update_yaxes(range=[0, 500])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (profits)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pil_lst_dis_ex_ante,
                            mode='lines',
                            opacity=0.2,
                            name='pil (ex-ante)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pih_lst_dis_ex_ante,
                            mode='lines',
                            opacity=0.2,
                            name='pih (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pi_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            opacity=0.2,
                            name='pi (ex-ante)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pil_lst_dis_ex_post,
                            mode='lines',
                            name='pil (ex-post)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pih_lst_dis_ex_post,
                            mode='lines',
                            name='pih (ex-post)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pi_aggregate_lst_dis_ex_post,
                            mode='lines',
                            name='pi (ex-post)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,500],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.update_layout(title={
                        'text': "Discriminatory, ex-ante \ ex-post (profits)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Profit')
        fig2.update_yaxes(range=[0, 500])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: : Discriminatory, ex-post (profits)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pil_lst_dis_ex_post,
                            mode='lines',
                            name='pil (ex-post)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pih_lst_dis_ex_post,
                            mode='lines',
                            name='pih (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pi_aggregate_lst_dis_ex_post,
                            mode='lines',
                            name='pi (ex-ante)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,500],
                            mode='lines',
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.update_layout(title={
                        'text': "Discriminatory, ex-post (profits)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Profit')
        fig3.update_yaxes(range=[0, 500])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        return fig1, fig2, fig3
    
def fig_welfare(ah, ah_lst_dis_ex_ante, CS_aggregate_lst_dis_ex_ante, pi_aggregate_lst_dis_ex_ante, welfare_aggregate_lst_dis_ex_ante, ah_lst_dis_ex_post, CS_aggregate_lst_dis_ex_post, CS_aggregate_adjusted_lst_dis_ex_post, pi_aggregate_lst_dis_ex_post, welfare_aggregate_lst_dis_ex_post, welfare_aggregate_adjusted_lst_dis_ex_post):
        #Fig 1: Discriminatory, ex-ante (welfare)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=CS_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            name='CS (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pi_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            name='pi (ex-ante)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig1.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=welfare_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            name='W (ex-ante)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig1.add_trace(go.Scatter(x=[ah,ah], y=[0,800],
                            mode='lines',
                            name='ah',
                            opacity=1,
                            line = dict(color=colors["s-b"], width=1.5, dash='dash')))
        fig1.update_layout(title={
                        'text': "Discriminatory, ex-ante (welfare)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Welfate')
        fig1.update_yaxes(range=[0, 800])  
        fig1.update_xaxes(range=[40, 101]) 
        fig1.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 2: Discriminatory, ex-ante \ ex-post (welfare)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=CS_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            opacity=0.2,
                            name='CS (ex-ante)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=pi_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            opacity=0.2,
                            name='pi (ex-ante)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_ante, y=welfare_aggregate_lst_dis_ex_ante,
                            mode='lines',
                            opacity=0.2,
                            name='W (ex-ante)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_aggregate_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS (ex-post)',
                            line = dict(color=colors["c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_aggregate_adjusted_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS ad (ex-post)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pi_aggregate_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='pi (ex-post)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=welfare_aggregate_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='W (ex-post)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig2.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=welfare_aggregate_adjusted_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='W ad (ex-post)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig2.add_trace(go.Scatter(x=[ah,ah], y=[0,800],
                            mode='lines',
                            opacity=1,
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5, dash='dash')))
        fig2.update_layout(title={
                        'text': "Discriminatory, ex-ante / ex-post (welfare)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Welfate')
        fig2.update_yaxes(range=[0, 800])  
        fig2.update_xaxes(range=[40, 101]) 
        fig2.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
        
        #Fig 3: Discriminatory, ex-post (strategies)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_aggregate_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS (ex-post)',
                            line = dict(color=colors["c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=CS_aggregate_adjusted_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='CS ad (ex-post)',
                            line = dict(color=colors["p-g"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=pi_aggregate_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='pi (ex-post)',
                            line = dict(color=colors["o-y-c"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=welfare_aggregate_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='W (ex-post)',
                            line = dict(color=colors["s-b"], width=1.5)))
        fig3.add_trace(go.Scatter(x=ah_lst_dis_ex_post, y=welfare_aggregate_adjusted_lst_dis_ex_post,
                            mode='lines',
                            opacity=1,
                            name='W ad (ex-post)',
                            line = dict(color=colors["b-s"], width=1.5)))
        fig3.add_trace(go.Scatter(x=[ah,ah], y=[0,800],
                            mode='lines',
                            opacity=1,
                            name='ah',
                            line = dict(color=colors["s-b"], width=1.5, dash='dash')))
        fig3.update_layout(title={
                        'text': "Discriminatory, ex-post (welfare)",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                        xaxis_title='Demand high-node (ah)',
                        yaxis_title='Welfate')
        fig3.update_yaxes(range=[0, 800])  
        fig3.update_xaxes(range=[40, 101]) 
        fig3.update_xaxes(tickangle=0, tickvals=[41, 45, 50, 55, 50, 60, 65, 70, 75, 80, 85, 90, 95, 99])
       
        return fig1, fig2, fig3