# -*- coding: utf-8 -*-
"""
File: Echem_tutorial_app.py
Created: 2025-JUN-12
@author: RebeccaFrederick
Last Updated: 2025-NOV-24 by Rebecca A. Frederick
"""
#-----------------------------------------------------------------------------
# !!!  IN PROGRESS LIST  !!!
#-----------------------------------------------------------------------------
# [1] add .csv files with example data
#     columns = ocp time, ocp voltage, eis frequency, eis |Z|, eis phase, 
#         {cv scan rate, cv time, cv voltage, cv current} x all scan rates
#     data_PEDOT.csv
#     data_GOLDmilli.csv
#     data_GOLDmicro.csv
#     data_GOLDultra.csv
#     data_SIROF.csv
#     data_AIROF.csv
#     data_EIROF.csv
#     data_SRUOF.csv
# [2] Pull data into dataframes
# [3] Create static charts of data in 3x2 grid
# [4] Allow user to select what electrode to view
# [5] Allow user to overlay data from mutliple electrodes
# [6] Add animations connecting OCP <> CV (V vs I) <> CV (V vs Time + I vs Time) <> VT
# [7] Add hover features
#     [ ] Highlight data point relationships to other/all graphs
#     [ ] Hightlight and explain |Z| and Phase (reference note (!) for 1kHz rationale)
#     [ ] Shade in and explain CSC
#     [ ] Shade in and explain Q/ph
#     [ ] Shade in and explain Q inj capacity (+ link to CSC)
#     [ ] Highlight and explain Emc
#     [ ] Highlight and explain Overpotentials
# [8] Add measurement explainations
#     [ ] OCP half cell rxns, Fermi Level
#     [ ] CV scan direction, step size (10mV), range, rate
#     [ ] EIS sinusoid V & I, Lissajous Plots
#     [ ] VT Vacc, Vdrive, Vp, Emc, IP delay, freq., waveform


#-----------------------------------------------------------------------------
#                               SECTION 1
#-----------------------------------------------------------------------------
# Import Required Packages
#-----------------------------------------------------------------------------
# Include packages required for data analysis:
import pandas as pd   # used to read raw data csv files
import plotly.express as px
from plotly.subplots import make_subplots
#import plotly.graph_objects as go
import dash
from dash import Dash, dcc, Input, Output, html, callback
import dash_bootstrap_components as dbc
#import numpy as np
#import matplotlib.pyplot as plt  # used to make plots
#import matplotlib.mlab as mlab
#import matplotlib.ticker as ticker # used to setup minor ticks in plots


#-----------------------------------------------------------------------------
#                               SECTION 2
#-----------------------------------------------------------------------------
# Define Functions
#-----------------------------------------------------------------------------
# def load_data():
#     PEDOT = pd.read_csv('assets/data_PEDOT.csv')
# #    GOLD = pd.read_csv('assets/data_GOLD.csv')
#     return all_data


#-----------------------------------------------------------------------------
#                               SECTION 3
#-----------------------------------------------------------------------------
# Load Example Data
#-----------------------------------------------------------------------------
# load PEDOT data
PEDOT = pd.read_csv('assets/data_PEDOT.csv')
# shift CV time values to start at zero...
PEDOT['Time(s)_CV00050'] = PEDOT['Time(s)_CV00050'] - PEDOT['Time(s)_CV00050'].iloc[0]  # 0.05 V/s
PEDOT['Time(s)_CV00100'] = PEDOT['Time(s)_CV00100'] - PEDOT['Time(s)_CV00100'].iloc[0]  # 0.10 V/s
PEDOT['Time(s)_CV00500'] = PEDOT['Time(s)_CV00500'] - PEDOT['Time(s)_CV00500'].iloc[0]  # 0.50 V/s
PEDOT['Time(s)_CV01000'] = PEDOT['Time(s)_CV01000'] - PEDOT['Time(s)_CV01000'].iloc[0]  # 1.00 V/s
PEDOT['Time(s)_CV03000'] = PEDOT['Time(s)_CV03000'] - PEDOT['Time(s)_CV03000'].iloc[0]  # 3.00 V/s
PEDOT['Time(s)_CV05000'] = PEDOT['Time(s)_CV05000'] - PEDOT['Time(s)_CV05000'].iloc[0]  # 5.00 V/s
PEDOT['Time(s)_CV10000'] = PEDOT['Time(s)_CV10000'] - PEDOT['Time(s)_CV10000'].iloc[0]  # 10.0 V/s
PEDOT['Time(s)_CV50000'] = PEDOT['Time(s)_CV50000'] - PEDOT['Time(s)_CV50000'].iloc[0]  # 50.0 V/s

# compile all dataframes into one dictionary
all_data = {"PEDOT":PEDOT}


#-----------------------------------------------------------------------------
# Process Example Data
#-----------------------------------------------------------------------------
Materials_list = list(all_data.keys())
Materials = all_data[Materials_list[0]]


#-----------------------------------------------------------------------------
#                               SECTION 4
#-----------------------------------------------------------------------------
# Create Plots (Manual)
#-----------------------------------------------------------------------------

# cv_data = px.line(data_frame=all_data['PEDOT'],x='Vf(V)_CV00050',y='Im(A)_CV00050',
#                   markers=True)

#cv_CSC = px.scatter(data_frame=all_data,)

#-----------------------------------------------------------------------------
#                               SECTION 5
#-----------------------------------------------------------------------------
# Create Web App
#-----------------------------------------------------------------------------
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout and Design
app.layout = dbc.Container([
    # Top Row = Page Header
    dbc.Row([
        dbc.Col(html.H1("Neural Engineering Electrochemistry"), style={'textAlign':'center'}) 
    ]),

    # 2nd Row = Data Selector
    dbc.Row([
        dbc.Col(dcc.Checklist(
            options=Materials_list, value=[Materials_list[0]],  # value=[Materials[0]] selectes first entry
            inline=True,id="materials_checklist"),
            width=14, style={'textAlign':'center'})
    ]),
    
    # Next Row = OCP and EIS Data
#!!!    dbc.Row([
#        dbc.Col(html.Div(f"Open Circuit Potential: {ocp_data}"), width=7),  
#        dbc.Col(html.Div(f"Electrochemical Impedance Spectroscopy: {eis_data}"), width=7)  
#    ]),  
    
    # Next Row = CV and VT Data
    dbc.Row([    
        dbc.Col(dcc.Graph(id="CV_figure")) #updates based on checklist
    ]), 
    
    # Last Row = Footer Information
    dbc.Row([
        dbc.Col(html.H3("© Rebecca A. Frederick, Ph.D."), style={'textAlign':'center'})
    ])
    
])


#-----------------------------------------------------------------------------
#                               SECTION 6
#-----------------------------------------------------------------------------
# Define Callbacks for Interactive Features
#-----------------------------------------------------------------------------
@app.callback(
    Output('CV_figure','figure'),
    Input('materials_checklist','value')
    )
#-----------------------------------------------------------------------------
def update_CV_graph(material):
    if not material:
        # CV_Plots = px.scatter(0,0,
        #                       title='Cyclic Voltammogram Data',
        #                       xaxis_title="Potential vs. Ag|AgCl (V)",
        #                       yaxis_title="Current (A)")
        # CV_Plots.update_xaxes(
        #     range=[-0.65,0.85],
        #     showgrid=True,
        #     ticks="cross")
        # CV_Plots.update_yaxes(
        #     autorange=True,
        #     showgrid=True,
        #     ticks="cross")
        return {} #CV_Plots
    
    # Get Input from Material Type Checkboxes
    selected = material[0]
    CV_df = all_data[selected]
    
    
    # Build CV Plot (subplot01)
    CV_Plots = px.scatter(CV_df,x='Vf(V)_CV00050',y='Im(A)_CV00050')
        # !!! color by Material & add legend
            
    # Build CSC - Potential vs. Time (subplot02)
    CV_VvsTime = px.scatter(CV_df,x='Time(s)_CV00050',y='Vf(V)_CV00050')
        
    # Build CSC - Current vs. Time (subplot03)
    CV_IvsTime = px.scatter(CV_df,x='Time(s)_CV00050',y='Im(A)_CV00050')
    
    
    # Build CV figure with subplots
    CV_figure = make_subplots(rows=2,cols=2,  # column_widths=[0.4,0.6]
                              specs=[
                                  [{"rowspan": 2}, {}],  # Cell (1,1) spans 2 rows, cell (1,2) is normal
                                  [None, {}],            # Cell (2,1) is empty (covered by rowspan), cell (2,2) is normal
                                  ],
                              subplot_titles=("Cyclic Voltammogram (Current vs. Potential)", "Potential vs. Time", "Current vs. Time")
                              )
    for trace in CV_Plots.data:
        CV_figure.add_trace(trace,row=1,col=1)
    for trace in CV_VvsTime.data:
        CV_figure.add_trace(trace,row=1,col=2)
    for trace in CV_IvsTime.data:
        CV_figure.add_trace(trace,row=2,col=2)


    # Uptdate figure formatting
    
    CV_figure.update_layout(
        font_color='black',
        title_text='Cyclic Voltammetry (CV) Data',
        title_x=0.5,
        title_xanchor='center',
        plot_bgcolor='white'
        )
    
    CV_figure.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgrey',
        zerolinecolor='black',
        ticks='outside',
        ticklen=8,
        tickwidth=2,
        tickcolor='black',
        showline=True,
        linecolor='black',
        linewidth=2,
        mirror=True
        )
    
    CV_figure.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgrey',
        zerolinecolor='black',
        ticks='outside',
        ticklen=8,
        tickwidth=2,
        tickcolor='black',
        showline=True,
        linecolor='black',
        linewidth=2,
        mirror=True
        )
    
    CV_figure.update_xaxes(row=1,col=1,
        title_text ='Potential vs. Ag|AgCl (V)',
        range=[-0.95,0.85],
        tickmode="linear",
        tick0=-0.9,
        dtick=0.1
        )
    
    CV_figure.update_yaxes(row=1,col=1,
        title_text ='Current (A)',
        autorange=True,
        tickmode="auto"
        )
    
    CV_figure.update_xaxes(row=1,col=2,    # Time axis, Potential vs. Time
        #title_text ='Time (s)',
        range=[0,60],      #!!! update so that range scales to selected data
        tickmode="linear",
        tick0=0,
        dtick=10
        )
    
    CV_figure.update_yaxes(row=1,col=2,   # Voltage axis, Potential vs. Time
        title_text ='Potential vs. Ag|AgCl (V)',
        range=[-0.9,0.9],
        tickmode="linear",
        tick0=-0.9,
        dtick=0.3
        )
    
    CV_figure.update_xaxes(row=2,col=2,   # Time axis, Current vs. Time
        title_text ='Time (s)',
        range=[0,60],      #!!! update so that range scales to selected data
        tickmode="linear",
        tick0=0,
        dtick=10
        )
    
    CV_figure.update_yaxes(row=2,col=2,   # Current axis, Current vs. Time
        title_text ='Current (A)',
        autorange=True,
        tickmode="auto",
        )
    
    CV_figure.add_vline(x=142, line_width=1, line_color="black", row=1, col=2)
    CV_figure.add_vline(x=142, line_width=1, line_color="black", row=2, col=2)
    
    return CV_figure



#-----------------------------------------------------------------------------
#                               SECTION 7
#-----------------------------------------------------------------------------
# Run App
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)


#-----------------------------------------------------------------------------
# End of File
#-----------------------------------------------------------------------------

# Example Code

# "label": html.Div(['PEDOT'], style={'color': 'Blue', 'font-size': 20}),
# "value": "PEDOT",
# },  # Material 1

#dcc.Markdown('''
#        #### Dash and Markdown
#        Dash supports [Markdown](http://commonmark.org/help).
#        Markdown is a simple way to write and format text.
#        It includes a syntax for things like **bold text** and *italics*,
#        [links](http://commonmark.org/help), inline `code` snippets, lists,
#        quotes, and more.
#    ''')

# CV_figure.add_shape(
# type="rect",
# xref="paper",
# yref="paper",
# x0=0,  # Start at the left edge of the plot area
# y0=0,  # Start at the bottom edge of the plot area
# x1=1,  # End at the right edge of the plot area
# y1=1,  # End at the top edge of the plot area
# line=dict(
#     color="Black",  # Set the color of the border line
#     width=2,        # Set the width of the border line
#     ),
# )
#    
#