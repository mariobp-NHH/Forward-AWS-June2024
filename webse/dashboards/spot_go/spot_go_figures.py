# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:51:20 2021

@author: s14761
"""
import plotly.graph_objects as go

colors = {
    "c": "rgb(38, 70, 83)",  # "charcoal"
    "p-g": "rgb(42, 157, 143)",  # "persian-green"
    "o-y-c": "rgb(233, 196, 106)",  # "orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)",  # "sandy-brown"
    "b-s": "rgb(231, 111, 81)"  # "burnt-sienna"
}


def graph_in(plot, ah, al, ah_go, al_go,
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
             Wgo1_lst, Wgo2_lst, Wsgo_lst, Ws_lst):

    # Fig area:
    fig_demand = fig_area_function(ah, al)
    # Fig kapital:
    fig_go_areas = fig_go_areas_function(T, q11, q12, q21, q22, alpha1, alpha2, ah_go, al_go)
    # Figures 1-3:
    if plot == 'strategies':
        fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2 = fig_strategies(pgo1, F1go1, F1go2, E1go1, E1go2,
                                          pgo2, F2go1, F2go2, E2go1, E2go2,
                                          psgo, F1sgo, F2sgo, E1sgo, E2sgo,
                                          ps, F1s, F2s, E1s, E2s)
    elif plot == 'prices':
        fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2 = fig_prices(ah, al, pmaxgo, pmaxs, a2_lst, E1go1_lst, E2go1_lst,
                                      Esgo1_lst, Esgo2_lst,
                                      Es1_lst, Es2_lst,
                                      E1go2_lst, E2go2_lst)

    elif plot == 'CS':
        fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2 = fig_CS(al, a2_lst, CSgo1_lst, CSgo2_lst, CSsgo_lst, CSs_lst)

    elif plot == 'profit':
        fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2 = fig_pi(al, a2_lst, pi1go1_lst, pi2go1_lst, pi1go2_lst, pi2go2_lst, pi1sgo_lst, pi2sgo_lst, pi1s_lst, pi2s_lst)
    else:
        fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2 = fig_W(al, a2_lst, Wgo1_lst, Wgo2_lst, Wsgo_lst, Ws_lst)

    return fig_demand, fig_go_areas, fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2

def fig_area_function(ah, al):
    T=2
    fig_area_spot = go.Figure()
    fig_area_spot.update_layout(title={
        'text': "Equilibrium areas (spot)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title=r'a2-s',
        yaxis_title=r'a1-s')
    fig_area_spot.update_yaxes(range=[0, 15])
    fig_area_spot.update_xaxes(range=[0, 15])
    fig_area_spot.update_yaxes(tickvals=[0, 2, 12, 14])
    fig_area_spot.update_xaxes(tickangle=0, tickvals=[0, 2, 12, 14])
    fig_area_spot.update_yaxes(showgrid=False)
    fig_area_spot.update_xaxes(showgrid=False)

    fig_area_spot.add_trace(go.Scatter(
        x=[0, 10, 14, 14], y=[0, 0, 0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color='rgb(0, 0, 0)'), ))
    fig_area_spot.add_trace(go.Scatter(
        x=[0, 10, 14, 14], y=[14, 14, 10, 0],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color='rgb(0, 0, 0)'), ))

    fig_area_spot.add_trace(go.Scatter(
        x=[7, 8], y=[7, 7],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))
    fig_area_spot.add_trace(go.Scatter(
        x=[7, 8], y=[8, 8],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))

    fig_area_spot.add_trace(go.Scatter(x=[0, T], y=[12, 12 - T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_area_spot.add_trace(go.Scatter(x=[T, T], y=[0, 12 - T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_area_spot.add_trace(go.Scatter(x=[T, 12 + T], y=[12 - T, 12 - T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_area_spot.add_trace(go.Scatter(x=[0, 12 - T], y=[T, T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_area_spot.add_trace(go.Scatter(x=[12 - T, 12 - T], y=[T, 12 + T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_area_spot.add_trace(go.Scatter(x=[12 - T, 12 + T], y=[T, 0], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))


    fig_area_spot.add_trace(go.Scatter(x=[0, al], y=[ah, ah], mode='lines', showlegend=False,
                                  line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_area_spot.add_trace(go.Scatter(x=[al, al], y=[0, ah], mode='lines', showlegend=False,
                                  line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_area_spot.add_scatter(x=[al], y=[ah], mode="markers", showlegend=False,
                         marker=dict(size=10, color=colors["s-b"]))

    return fig_area_spot

def fig_go_areas_function(T, q11, q12, q21, q22, alpha1, alpha2, ah_go, al_go):
    k1go1 = alpha1*q11
    k2go1 = alpha2*q12
    k1go2 = alpha1*q21
    k2go2 = alpha2*q22
    fig_go_areas = go.Figure()
    fig_go_areas.update_layout(title={
        'text': "Equilibrium areas (GO)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title=r'a2-go',
        yaxis_title=r'a1-go')
    fig_go_areas.update_yaxes(range=[0, 12])
    fig_go_areas.update_xaxes(range=[0, 12])
    fig_go_areas.update_yaxes(tickvals=[T, k1go2, k1go1-T, k1go1, k1go1+T])
    fig_go_areas.update_xaxes(tickangle=0, tickvals=[T, k2go1, k2go2-T, k2go2, k2go2+T])
    fig_go_areas.update_yaxes(showgrid=False)
    fig_go_areas.update_xaxes(showgrid=False)


    fig_go_areas.add_trace(go.Scatter(
        x=[0, k2go1-T, k2go1+T, k2go1+T], y=[0, 0, 0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color='rgb(0, 0, 0)'), ))
    fig_go_areas.add_trace(go.Scatter(
        x=[0, k2go1-T, k2go1+T, k2go1+T], y=[k1go1+T, k1go1+T, k1go1-T, 0],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color='rgb(0, 0, 0)'), ))


    fig_go_areas.add_trace(go.Scatter(
        x=[0, k2go2 - T, k2go2 + T, k2go2 + T], y=[0, 0, 0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color='rgb(0, 0, 0)'), ))
    fig_go_areas.add_trace(go.Scatter(
        x=[0, k2go2 - T, k2go2 + T, k2go2 + T], y=[k1go2 + T, k1go2 + T, k1go2 - T, 0],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color='rgb(0, 0, 0)'), ))

    fig_go_areas.add_trace(go.Scatter(
        x=[2, 3], y=[2, 2],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))
    fig_go_areas.add_trace(go.Scatter(
        x=[2, 3], y=[3, 3],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))

    fig_go_areas.add_trace(go.Scatter(x=[0, T], y=[k1go1, k1go1-T], mode='lines', showlegend=False,
                                       line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_go_areas.add_trace(go.Scatter(x=[T, T], y=[0, k1go1-T], mode='lines', showlegend=False,
                                       line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_go_areas.add_trace(go.Scatter(x=[T, k2go1+T], y=[k1go1 - T, k1go1 - T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_go_areas.add_trace(go.Scatter(x=[0, k2go1-T], y=[T, T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_go_areas.add_trace(go.Scatter(x=[k2go1-T, k2go1-T], y=[T, k1go1 + T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))
    fig_go_areas.add_trace(go.Scatter(x=[k2go1-T, k2go1], y=[T, 0], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(233, 196, 106)')))

    fig_go_areas.add_trace(go.Scatter(x=[0, k2go2-T], y=[T, T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(231, 111, 81)')))
    fig_go_areas.add_trace(go.Scatter(x=[k2go2-T, k2go2], y=[T, 0], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(231, 111, 81)')))
    fig_go_areas.add_trace(go.Scatter(x=[k2go2-T, k2go2-T], y=[T, k1go2+T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(231, 111, 81)')))
    fig_go_areas.add_trace(go.Scatter(x=[0, T], y=[k1go2, k1go2-T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(231, 111, 81)')))
    fig_go_areas.add_trace(go.Scatter(x=[T, T], y=[k1go2-T, 0], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(231, 111, 81)')))
    fig_go_areas.add_trace(go.Scatter(x=[T, k2go2 + T], y=[k1go2 - T, k1go2-T], mode='lines', showlegend=False,
                                      line=dict(width=0.5, color='rgb(231, 111, 81)')))

    fig_go_areas.add_trace(go.Scatter(x=[0, al_go], y=[ah_go, ah_go], mode='lines', showlegend=False,
                                       line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_go_areas.add_trace(go.Scatter(x=[al_go, al_go], y=[0, ah_go], mode='lines', showlegend=False,
                                       line=dict(width=1, color='rgb(0, 0, 0)', dash='dash')))
    fig_go_areas.add_scatter(x=[al_go], y=[ah_go], mode="markers", showlegend=False,
                              marker=dict(size=10, color=colors["s-b"]))

    return fig_go_areas


def fig_strategies(pgo1, F1go1, F1go2, E1go1, E1go2,
                   pgo2, F2go1, F2go2, E2go1, E2go2,
                   psgo, F1sgo, F2sgo, E1sgo, E2sgo,
                   ps, F1s, F2s, E1s, E2s):

    fig_spot_strategies = go.Figure()
    fig_spot_strategies.add_trace(go.Scatter(x=ps, y=F1s,
                              mode='lines',
                              opacity=1,
                              name='F1',
                              line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=ps, y=F2s,
                              mode='lines',
                              opacity=1,
                              name='F2',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=[E1s, E1s], y=[0, 1],
                              mode='lines',
                              opacity=1,
                              name='E1',
                              line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=[E2s, E2s], y=[0, 1],
                              mode='lines',
                              opacity=1,
                              name='E2',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.update_layout(title={
        'text': "Spot (strategies)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='Price',
        yaxis_title='CDF')
    fig_spot_strategies.update_yaxes(range=[0, 1.1])
    fig_spot_strategies.update_xaxes(range=[3.5, 7.1])
    fig_spot_strategies.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])

    fig_spot_go_strategies = go.Figure()
    fig_spot_go_strategies.add_trace(go.Scatter(x=psgo, y=F1sgo,
                                             mode='lines',
                                             name='F1',
                                             line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=psgo, y=F2sgo,
                                             mode='lines',
                                             name='F2',
                                             line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=[E1sgo, E1sgo], y=[0, 1],
                                             mode='lines',
                                             name='E1',
                                             line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=[E2sgo, E2sgo], y=[0, 1],
                                             mode='lines',
                                             name='E2',
                                             line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.update_layout(title={
        'text': "Spot-GO (strategies)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='Price',
        yaxis_title='CDF')
    fig_spot_go_strategies.update_yaxes(range=[0, 1.1])
    fig_spot_go_strategies.update_xaxes(range=[3.5, 7.1])
    fig_spot_strategies.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])

    fig_go1 = go.Figure()
    fig_go1.add_trace(go.Scatter(x=pgo1, y=F1go1,
                              mode='lines',
                              name='F1',
                              line=dict(color=colors["c"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=pgo1, y=F2go1,
                              mode='lines',
                              name='F2',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=[E1go1, E1go1], y=[0, 1],
                              mode='lines',
                              name='E1',
                              line=dict(color=colors["c"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=[E2go1, E2go1], y=[0, 1],
                              mode='lines',
                              name='E2',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig_go1.update_layout(title={
        'text': "GO1 (strategies)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='Price',
        yaxis_title='CDF')
    fig_go1.update_yaxes(range=[0, 1.1])
    fig_go1.update_xaxes(range=[0, 2.1])
    fig_go1.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])

    fig_go2 = go.Figure()
    fig_go2.add_trace(go.Scatter(x=pgo1, y=F1go2,
                                 mode='lines',
                                 name='F1',
                                 line=dict(color=colors["c"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=pgo1, y=F2go2,
                                 mode='lines',
                                 name='F2',
                                 line=dict(color=colors["s-b"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=[E1go2, E1go2], y=[0, 1],
                                 mode='lines',
                                 name='E1',
                                 line=dict(color=colors["c"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=[E2go2, E2go2], y=[0, 1],
                                 mode='lines',
                                 name='E2',
                                 line=dict(color=colors["s-b"], width=1.5)))
    fig_go2.update_layout(title={
        'text': "GO2 (strategies)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='Price',
        yaxis_title='CDF')
    fig_go2.update_yaxes(range=[0, 1.1])
    fig_go2.update_xaxes(range=[0, 2.1])
    fig_go2.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])

    return fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2


def fig_prices(ah, al, pmaxgo, pmaxs, a2_lst, E1go1_lst, E2go1_lst,
                                      Esgo1_lst, Esgo2_lst,
                                      Es1_lst, Es2_lst,
                                      E1go2_lst, E2go2_lst):
    fig_go1 = go.Figure()
    fig_go1.add_trace(go.Scatter(x=a2_lst, y=E1go1_lst,
                              mode='lines',
                              name='p1',
                              line=dict(color=colors["c"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=a2_lst, y=E2go1_lst,
                              mode='lines',
                              name='p2',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=[al, al], y=[0, pmaxgo],
                              mode='lines',
                              name='a2',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go1.update_layout(title={
        'text': "GO1 (prices)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Price')
    fig_go1.update_yaxes(range=[0, pmaxgo])
    fig_go1.update_xaxes(range=[7, 8])
    fig_go1.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_go2 = go.Figure()
    fig_go2.add_trace(go.Scatter(x=a2_lst, y=E1go2_lst,
                                 mode='lines',
                                 name='p1',
                                 line=dict(color=colors["c"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=a2_lst, y=E2go2_lst,
                                 mode='lines',
                                 name='p2',
                                 line=dict(color=colors["s-b"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=[al, al], y=[0, pmaxgo],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go2.update_layout(title={
        'text': "GO2 (prices)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Price')
    fig_go2.update_yaxes(range=[0, pmaxgo])
    fig_go2.update_xaxes(range=[7, 8])
    fig_go2.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_strategies = go.Figure()
    fig_spot_strategies.add_trace(go.Scatter(x=a2_lst, y=Es1_lst,
                                 mode='lines',
                                 opacity=1,
                                 name='p1',
                                 line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=a2_lst, y=Es2_lst,
                                 mode='lines',
                                 opacity=1,
                                 name='p2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=[al, al], y=[3, pmaxs],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.update_layout(title={
        'text': "Spot (prices)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Price')
    fig_spot_strategies.update_yaxes(range=[5, 6])
    fig_spot_strategies.update_xaxes(range=[7, 8])
    fig_spot_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_go_strategies = go.Figure()
    fig_spot_go_strategies.add_trace(go.Scatter(x=a2_lst, y=Esgo1_lst,
                              mode='lines',
                              name='p1',
                              line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=a2_lst, y=Esgo2_lst,
                              mode='lines',
                              name='p2',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=[al, al], y=[3, pmaxs],
                              mode='lines',
                              name='a2',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.update_layout(title={
        'text': "Spot-GO (prices)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Price')
    fig_spot_go_strategies.update_yaxes(range=[5, 6])
    fig_spot_go_strategies.update_xaxes(range=[7, 8])
    fig_spot_go_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    return fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2

def fig_CS(al, a2_lst, CSgo1_lst, CSgo2_lst, CSsgo_lst, CSs_lst):
    fig_go1 = go.Figure()
    fig_go1.add_trace(go.Scatter(x=a2_lst, y=CSgo1_lst,
                              mode='lines',
                              name='CS',
                              line=dict(color=colors["b-s"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(CSgo1_lst),min(CSgo2_lst)),1.05*max(max(CSgo1_lst),max(CSgo2_lst))],
                              mode='lines',
                              name='a2',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go1.update_layout(title={
        'text': "GO1 (consumer surplus)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='CS')
    fig_go1.update_yaxes(range=[0.95*min(min(CSgo1_lst),min(CSgo2_lst)),1.05*max(max(CSgo1_lst),max(CSgo2_lst))])
    fig_go1.update_xaxes(range=[7, 8])
    fig_go1.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_go2 = go.Figure()
    fig_go2.add_trace(go.Scatter(x=a2_lst, y=CSgo2_lst,
                                 mode='lines',
                                 name='CS',
                                 line=dict(color=colors["b-s"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(CSgo1_lst),min(CSgo2_lst)),1.05*max(max(CSgo1_lst),max(CSgo2_lst))],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go2.update_layout(title={
        'text': "GO2 (consumer surplus)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='CS')
    fig_go2.update_yaxes(range=[0.95*min(min(CSgo1_lst),min(CSgo2_lst)),1.05*max(max(CSgo1_lst),max(CSgo2_lst))])
    fig_go2.update_xaxes(range=[7, 8])
    fig_go2.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_strategies = go.Figure()
    fig_spot_strategies.add_trace(go.Scatter(x=a2_lst, y=CSs_lst,
                                 mode='lines',
                                 opacity=1,
                                 name='CS',
                                 line=dict(color=colors["b-s"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(CSsgo_lst),min(CSs_lst)),1.05*max(max(CSsgo_lst),max(CSs_lst))],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.update_layout(title={
        'text': "Spot (consumer surplus)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='CS')
    fig_spot_strategies.update_yaxes(range=[0.95*min(min(CSsgo_lst),min(CSs_lst)),1.05*max(max(CSsgo_lst),max(CSs_lst))])
    fig_spot_strategies.update_xaxes(range=[7, 8])
    fig_spot_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_go_strategies = go.Figure()
    fig_spot_go_strategies.add_trace(go.Scatter(x=a2_lst, y=CSsgo_lst,
                              mode='lines',
                              name='CS',
                              line=dict(color=colors["b-s"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(CSsgo_lst),min(CSs_lst)),1.05*max(max(CSsgo_lst),max(CSs_lst))],
                              mode='lines',
                              name='a2',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.update_layout(title={
        'text': "Spot-GO (consumer surplus)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='CS')
    fig_spot_go_strategies.update_yaxes(range=[0.95*min(min(CSsgo_lst),min(CSs_lst)),1.05*max(max(CSsgo_lst),max(CSs_lst))])
    fig_spot_go_strategies.update_xaxes(range=[7, 8])
    fig_spot_go_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    return fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2

def fig_pi(al, a2_lst, pi1go1_lst, pi2go1_lst, pi1go2_lst, pi2go2_lst, pi1sgo_lst, pi2sgo_lst, pi1s_lst, pi2s_lst):
    fig_go1 = go.Figure()
    fig_go1.add_trace(go.Scatter(x=a2_lst, y=pi1go1_lst,
                                 mode='lines',
                                 name='pi1',
                                 line=dict(color=colors["c"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=a2_lst, y=pi2go1_lst,
                                 mode='lines',
                                 name='pi2',
                                 line=dict(color=colors["s-b"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(pi1go1_lst),min(pi2go1_lst),min(pi1go2_lst),min(pi2go2_lst)),1.05*max(max(pi1go1_lst),max(pi2go1_lst),max(pi1go2_lst),max(pi2go2_lst))],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go1.update_layout(title={
        'text': "GO1 (profits)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Profit')
    fig_go1.update_yaxes(range=[0.95*min(min(pi1go1_lst),min(pi2go1_lst),min(pi1go2_lst),min(pi2go2_lst)),1.05*max(max(pi1go1_lst),max(pi2go1_lst),max(pi1go2_lst),max(pi2go2_lst))])
    fig_go1.update_xaxes(range=[7, 8])
    fig_go1.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_go2 = go.Figure()
    fig_go2.add_trace(go.Scatter(x=a2_lst, y=pi1go2_lst,
                                 mode='lines',
                                 name='pi1',
                                 line=dict(color=colors["c"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=a2_lst, y=pi2go2_lst,
                                 mode='lines',
                                 name='pi2',
                                 line=dict(color=colors["s-b"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(pi1go1_lst),min(pi2go1_lst),min(pi1go2_lst),min(pi2go2_lst)),1.05*max(max(pi1go1_lst),max(pi2go1_lst),max(pi1go2_lst),max(pi2go2_lst))],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go2.update_layout(title={
        'text': "GO2 (profits)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Profit')
    fig_go2.update_yaxes(range=[0.95*min(min(pi1go1_lst),min(pi2go1_lst),min(pi1go2_lst),min(pi2go2_lst)),1.05*max(max(pi1go1_lst),max(pi2go1_lst),max(pi1go2_lst),max(pi2go2_lst))])
    fig_go2.update_xaxes(range=[7, 8])
    fig_go2.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_strategies = go.Figure()
    fig_spot_strategies.add_trace(go.Scatter(x=a2_lst, y=pi1s_lst,
                                             mode='lines',
                                             opacity=1,
                                             name='pi1',
                                             line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=a2_lst, y=pi2s_lst,
                                             mode='lines',
                                             opacity=1,
                                             name='pi2',
                                             line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(pi1sgo_lst),min(pi2sgo_lst),min(pi1s_lst),min(pi2s_lst)),1.05*max(max(pi1sgo_lst),max(pi2sgo_lst),max(pi1s_lst),max(pi2s_lst))],
                                             mode='lines',
                                             name='a2',
                                             line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.update_layout(title={
        'text': "Spot (profits)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Profit')
    fig_spot_strategies.update_yaxes(range=[0.95*min(min(pi1sgo_lst),min(pi2sgo_lst),min(pi1s_lst),min(pi2s_lst)),1.05*max(max(pi1sgo_lst),max(pi2sgo_lst),max(pi1s_lst),max(pi2s_lst))])
    fig_spot_strategies.update_xaxes(range=[7, 8])
    fig_spot_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_go_strategies = go.Figure()
    fig_spot_go_strategies.add_trace(go.Scatter(x=a2_lst, y=pi1sgo_lst,
                                                mode='lines',
                                                name='pi1',
                                                line=dict(color=colors["p-g"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=a2_lst, y=pi2sgo_lst,
                                                mode='lines',
                                                name='pi2',
                                                line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.add_trace(go.Scatter(x=[al, al], y=[0.95*min(min(pi1sgo_lst),min(pi2sgo_lst),min(pi1s_lst),min(pi2s_lst)),1.05*max(max(pi1sgo_lst),max(pi2sgo_lst),max(pi1s_lst),max(pi2s_lst))],
                                                mode='lines',
                                                name='a2',
                                                line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.update_layout(title={
        'text': "Spot-GO (profits)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='Profit')
    fig_spot_go_strategies.update_yaxes(range=[0.95*min(min(pi1sgo_lst),min(pi2sgo_lst),min(pi1s_lst),min(pi2s_lst)),1.05*max(max(pi1sgo_lst),max(pi2sgo_lst),max(pi1s_lst),max(pi2s_lst))])
    fig_spot_go_strategies.update_xaxes(range=[7, 8])
    fig_spot_go_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    return fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2

def fig_W(al, a2_lst, Wgo1_lst, Wgo2_lst, Wsgo_lst, Ws_lst):
    fig_go1 = go.Figure()
    fig_go1.add_trace(go.Scatter(x=a2_lst, y=Wgo1_lst,
                                 mode='lines',
                                 name='W',
                                 line=dict(color=colors["b-s"], width=1.5)))
    fig_go1.add_trace(go.Scatter(x=[al, al], y=[0.95 * min(min(Wgo1_lst), min(Wgo2_lst)),
                                                1.05 * max(max(Wgo1_lst), max(Wgo2_lst))],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go1.update_layout(title={
        'text': "GO1 (welfare)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='W')
    fig_go1.update_yaxes(range=[0.95 * min(min(Wgo1_lst), min(Wgo2_lst)), 1.05 * max(max(Wgo1_lst), max(Wgo2_lst))])
    fig_go1.update_xaxes(range=[7, 8])
    fig_go1.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_go2 = go.Figure()
    fig_go2.add_trace(go.Scatter(x=a2_lst, y=Wgo2_lst,
                                 mode='lines',
                                 name='W',
                                 line=dict(color=colors["b-s"], width=1.5)))
    fig_go2.add_trace(go.Scatter(x=[al, al], y=[0.95 * min(min(Wgo1_lst), min(Wgo2_lst)),
                                                1.05 * max(max(Wgo1_lst), max(Wgo2_lst))],
                                 mode='lines',
                                 name='a2',
                                 line=dict(color=colors["o-y-c"], width=1.5)))
    fig_go2.update_layout(title={
        'text': "GO2 (welfare)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='W')
    fig_go2.update_yaxes(range=[0.95 * min(min(Wgo1_lst), min(Wgo2_lst)), 1.05 * max(max(Wgo1_lst), max(Wgo2_lst))])
    fig_go2.update_xaxes(range=[7, 8])
    fig_go2.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_strategies = go.Figure()
    fig_spot_strategies.add_trace(go.Scatter(x=a2_lst, y=Ws_lst,
                                             mode='lines',
                                             opacity=1,
                                             name='W',
                                             line=dict(color=colors["b-s"], width=1.5)))
    fig_spot_strategies.add_trace(
        go.Scatter(x=[al, al], y=[0.95 * min(min(Wsgo_lst), min(Ws_lst)), 1.05 * max(max(Wsgo_lst), max(Ws_lst))],
                   mode='lines',
                   name='a2',
                   line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_strategies.update_layout(title={
        'text': "Spot (welfare)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='W')
    fig_spot_strategies.update_yaxes(
        range=[0.95 * min(min(Wsgo_lst), min(Ws_lst)), 1.05 * max(max(Wsgo_lst), max(Ws_lst))])
    fig_spot_strategies.update_xaxes(range=[7, 8])
    fig_spot_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    fig_spot_go_strategies = go.Figure()
    fig_spot_go_strategies.add_trace(go.Scatter(x=a2_lst, y=Wsgo_lst,
                                                mode='lines',
                                                name='W',
                                                line=dict(color=colors["b-s"], width=1.5)))
    fig_spot_go_strategies.add_trace(
        go.Scatter(x=[al, al], y=[0.95 * min(min(Wsgo_lst), min(Ws_lst)), 1.05 * max(max(Wsgo_lst), max(Ws_lst))],
                   mode='lines',
                   name='a2',
                   line=dict(color=colors["o-y-c"], width=1.5)))
    fig_spot_go_strategies.update_layout(title={
        'text': "Spot-GO (welfare)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='a2 (spot)',
        yaxis_title='W')
    fig_spot_go_strategies.update_yaxes(
        range=[0.95 * min(min(Wsgo_lst), min(Ws_lst)), 1.05 * max(max(Wsgo_lst), max(Ws_lst))])
    fig_spot_go_strategies.update_xaxes(range=[7, 8])
    fig_spot_go_strategies.update_xaxes(tickangle=0, tickvals=[7, 7.2, 7.4, 7.6, 7.8, 8])

    return fig_spot_strategies, fig_spot_go_strategies, fig_go1, fig_go2

