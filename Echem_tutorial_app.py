# -*- coding: utf-8 -*-
"""
File: Echem_tutorial_app.py
Created: 2025-JUN-12
@author: RebeccaFrederick
Last Updated: 2025-OCT-14 by Rebecca A. Frederick
"""
#-----------------------------------------------------------------------------
# !!!  TO DO LIST  !!!
#-----------------------------------------------------------------------------
# [1] create .csv files with example data
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
import dash
from dash import dcc, Input, Output, html
import dash_bootstrap_components as dbc
#import numpy as np
#import matplotlib.pyplot as plt  # used to make plots
#import matplotlib.mlab as mlab
#import matplotlib.ticker as ticker # used to setup minor ticks in plots
#
#
#-----------------------------------------------------------------------------
#                               SECTION 2
#-----------------------------------------------------------------------------
# Load Example Data
#-----------------------------------------------------------------------------
def load_data():
    data_PEDOT = pd.read_csv('assets/data_PEDOT.csv')
    data_GOLD = pd.read_csv('assets/data_GOLD.csv')
    return data
#
data = load_data()
#
#
#-----------------------------------------------------------------------------
#                               SECTION 3
#-----------------------------------------------------------------------------
# Create Web App
#-----------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout and Design
app.layout = dbc.Container([
    # Top Row / Page Header
    dbc.Row([
        dbc.Col(html.H1("Neural Engineering Electrochemistry"), width=15, className="text-center my-5")
    ])

    # 2nd Row = OCP and EIS Data
    dbc.Row([
        dbc.Col(html.Div(f"Open Circuit Potential: {ocp_data}", className="text-center my-3 top-text"), width=7),
        dbc.Col(html.Div(f"Electrochemical Impedance Spectroscopy: {eis_data}", className="text-center my-3 top-text"), width=7)
    ], className="mb-5")
    
    # 3rd Row = CV and VT Data
    dbc.Row([
        dbc.Col(html.Div(f"Cyclic Voltammogram: {cv_data}", className="text-center my-3 top-text"), width=7),
        dbc.Col(html.Div(f"Voltage Transient Measurements: {vt_data}", className="text-center my-3 top-text"), width=7)
    ], className="mb-5")
])





if __name__ == '__main__':
app.run_server(debug=True)



#-----------------------------------------------------------------------------
# End of File
#-----------------------------------------------------------------------------
