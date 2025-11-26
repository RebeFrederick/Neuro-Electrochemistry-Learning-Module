# -*- coding: utf-8 -*-
"""
File: Echem_tutorial_app.py
Created: 2025-JUN-12
@author: RebeccaFrederick
Last Updated: 2025-NOV-25 by Rebecca A. Frederick
"""
#-----------------------------------------------------------------------------
# !!!  IN PROGRESS LIST  !!!
#-----------------------------------------------------------------------------

# PROJECT 01 = Upload example data for multiple materials and sizes.
# [ ] add .csv files with example data for other materials
#     columns = ocp time, ocp voltage, eis frequency, eis |Z|, eis phase, 
#         {cv scan rate, cv time, cv voltage, cv current} x all scan rates
#     data_PEDOT.csv        [DONE]
#     data_Pt.csv
#     data_GOLDmilli.csv
#     data_GOLDmicro.csv
#     data_GOLDultra.csv
#     data_SIROF.csv
#     data_AIROF.csv
#     data_EIROF.csv
#     data_SRUOF.csv
# [ ] Pull new data into dataframes
# [ ] Allow user to select what electrode material to view (one-at-a-time)
# [ ] Upgrade checkboxes to allow display of multiple materials simultaneously

# PROJECT 02 = change single page app to multi-page app.
# [ ] Migrate current app to new "CV.py" file.
# [ ] Create empty base layout for multi-page app in "Echem_tutorial_app.py".
# [ ] Link "CV.py" to new "Echem_tutorial_app.py".
# [ ] Copy similar layout from "CV.py" into new pages for OCP, EIS, and VT.

# PROJECT 03 = add more interactive functionality and education visualizations.
# [ ] Add animations connecting OCP <> CV (V vs I) <> EIS <> VT
# [ ] Add hover features
#     [ ] Highlight data point relationships to other/all graphs
#     [ ] Hightlight and explain |Z| and Phase (reference note (!) for 1kHz rationale)
#     [ ] Shade in and explain CSC
#     [ ] Shade in and explain Q/ph
#     [ ] Shade in and explain Q inj capacity (+ link to CSC)
#     [ ] Highlight and explain Emc
#     [ ] Highlight and explain Overpotentials
# [ ] Add measurement explainations
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
import plotly.graph_objects as go
import dash
from dash import Dash, dcc, Input, Output, html, callback
import dash_bootstrap_components as dbc
import numpy as np


# Define font size for page footer, figure annotations, etc.
unifiedfontsize = 12
titlestandoffvalue = 10




#-----------------------------------------------------------------------------
#                               SECTION 2
#-----------------------------------------------------------------------------
# Define Functions
#-----------------------------------------------------------------------------

def CSC_calc(timevals,currentvals,GSA) :
    # current vals should already be split by sign (+ or -)
    # current vals = Amps; time vals = Seconds
    q=[]
    timestep = timevals[2]-timevals[1]
    for i in range(len(timevals)-1):
        q.append(timestep*(abs(currentvals[i])+abs(currentvals[i+1]))/2)
    Q = sum(q)
    CSC = Q/GSA  # Coulomb/um^2
    CSC = CSC*(1e11)  # mC/cm^2
    CSC = round(CSC,2)
    return CSC

#-----------------------------------------------------------------------------
#                               SECTION 3
#-----------------------------------------------------------------------------
# Load Example Data
#-----------------------------------------------------------------------------
# load metadata
info = pd.read_csv('assets/Echem_medata.csv')

# load PEDOT data
PEDOT = pd.read_csv('assets/data_PEDOT.csv')
# shift CV time values to start at zero...
PEDOTtimestep = PEDOT['Time(s)_CV00050'].iloc[1]-PEDOT['Time(s)_CV00050'].iloc[0]
PEDOT['Time(s)_CV00050'] = round((PEDOT['Time(s)_CV00050']-PEDOT['Time(s)_CV00050'].iloc[0]+PEDOTtimestep), 2)  # 0.05 V/s
PEDOT['Time(s)_CV00100'] = round((PEDOT['Time(s)_CV00100']-PEDOT['Time(s)_CV00100'].iloc[0]+PEDOTtimestep), 2)  # 0.10 V/s
PEDOT['Time(s)_CV00500'] = round((PEDOT['Time(s)_CV00500']-PEDOT['Time(s)_CV00500'].iloc[0]+PEDOTtimestep), 2)  # 0.50 V/s
PEDOT['Time(s)_CV01000'] = round((PEDOT['Time(s)_CV01000']-PEDOT['Time(s)_CV01000'].iloc[0]+PEDOTtimestep), 2)  # 1.00 V/s
PEDOT['Time(s)_CV03000'] = round((PEDOT['Time(s)_CV03000']-PEDOT['Time(s)_CV03000'].iloc[0]+PEDOTtimestep), 2)  # 3.00 V/s
PEDOT['Time(s)_CV05000'] = round((PEDOT['Time(s)_CV05000']-PEDOT['Time(s)_CV05000'].iloc[0]+PEDOTtimestep), 2)  # 5.00 V/s
PEDOT['Time(s)_CV10000'] = round((PEDOT['Time(s)_CV10000']-PEDOT['Time(s)_CV10000'].iloc[0]+PEDOTtimestep), 2)  # 10.0 V/s
PEDOT['Time(s)_CV50000'] = round((PEDOT['Time(s)_CV50000']-PEDOT['Time(s)_CV50000'].iloc[0]+PEDOTtimestep), 2)  # 50.0 V/s


#-----------------------------------------------------------------------------
# compile all dataframes into one dictionary
    #  all_data[~Material Key~][0] = metadata
    #  all_data[~Material Key~][1] = rawdata
all_data = {}
all_data["PEDOT-PSS"] = [info.loc[info['Material']=='PEDOT-PSS'],PEDOT]


#-----------------------------------------------------------------------------
# Process Example Data
#-----------------------------------------------------------------------------
Materials_list = list(all_data.keys())
Materials = all_data[Materials_list[0]]


#-----------------------------------------------------------------------------
#                               SECTION 4
#-----------------------------------------------------------------------------
# Create Plotly Dash Web App
#-----------------------------------------------------------------------------
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout and Design
app.layout = html.Div(
    style={"height":"100vh", "width":"100vw", "display":"flex", 
           "flex-direction":"column", "align-items":"center"},
    children=[
        # Top Row = Page Header
        html.Header([
            html.H3("Neural Engineering Electrochemistry"),
            html.H4("Cyclic Voltammetry (CV) Measurements",
                    style={'color':'darkblue',
                           'padding':'5px 0px 0px 0px'}),
            ],
            style={'textAlign':'center',
                   'backgroundColor':'rgba(211,211,211,0.8)',
                    'padding': '10px 30px 10px 30px'} 
            ),  # end header row brackets

        # 2nd Row = Data Selector
            html.Label(
            children=[
                html.Span("Select Electrode Material to Display: ",
                          style={"margin-right": "10px"}),
                dcc.Checklist(    #!!! [to-do] change to: dcc.RadioItems(
                    options=Materials_list, value=[Materials_list[0]],  # value=[Materials[0]] selectes first entry
                    inputStyle={"margin-right": "7px"},
                    inline=True, id="materials_checklist",),  #style={'padding': '5px 5px 5px 5px'}
                   ], 
            style={'display':'inline-flex', 'alignItems':'center',
                   'padding':'4px 0px 10px 0px',} # Use flex for alignment within the label
                ),
    
        # Next Row = CV and VT Data  
            dcc.Graph(id="CV_figure",
                style={'height': '100%', 'width': '100%', # Make graph fill its parent
                       'minHeight': '600px','minWidth': '1000px',
                       'padding': '15px'}, 
                config={'responsive': True}), #updates based on checklist
    
        # Last Row = Footer Information
        html.Footer(
            children=[
            html.P("© 2025 Rebecca A. Frederick, Ph.D. All rights reserved."),
            ],
            style={
            'textAlign': 'center',
            'padding': '0px 5px 5px 5px',
            'font_size':unifiedfontsize,
            'font-weight': 'bold'
            }),
    
        ],)  # end Container brackets


#-----------------------------------------------------------------------------
#                               SECTION 5
#-----------------------------------------------------------------------------
# Define Callbacks for Interactive Features
#-----------------------------------------------------------------------------
@app.callback(
    Output('CV_figure','figure'),
    Input('materials_checklist','value')
    )
#-----------------------------------------------------------------------------
def update_CV_graph(material):
    
    # Remove data/plots if no material is selected
    if not material:
# !!! [to-do] add empty plots to keep desired formatting when nothing is selected
        return {} # Return Empty CV_Plots Figure
    
    # If a box is checked, get input from materials checkbox
    selected = material[0]
    CV_df = all_data[selected][1]
    meta_df = all_data[selected][0]
    GSA = meta_df['SurfaceArea_µm^2'][0]
    
    # split positive and negative current values for CSC calculations
    splitmask = CV_df['Im(A)_CV00050'] >= 0
    CV_df['Ia_CV00050'] = np.where(splitmask, CV_df['Im(A)_CV00050'], 0)    
    CV_df['Ic_CV00050'] = np.where(splitmask, 0, CV_df['Im(A)_CV00050'])
    
    # send split current values to CSC_calc function
    CSCc_CV00050 = CSC_calc(CV_df['Time(s)_CV00050'],CV_df['Ic_CV00050'],GSA)
    print(CSCc_CV00050)
    CSCa_CV00050 = CSC_calc(CV_df['Time(s)_CV00050'],CV_df['Ia_CV00050'],GSA)
    print(CSCa_CV00050)
    
    #!!! [to-do] account for CVs in different direction, i.e. half-way = max not min
    minvoltidx = CV_df['Vf(V)_CV00050'].idxmin();
    mintime = CV_df.loc[minvoltidx, 'Time(s)_CV00050']
    print(mintime)

    # Build CV figure with subplots
        #!!! [to-do] coordinate hover to display same data point on all subplots
        #    http://plotly.com/python/hover-text-and-formatting/

    # SETUP FIGURE LAYOUT
    CV_figure = make_subplots(
        rows=2, cols=2,
        #shared_xaxes=True, # Optional, if subplots share an x-axis
        vertical_spacing=0.3,
        specs=[
        [{"type": "scatter"}, {"type": "scatter"}],  # Row 1: Two scatter plots
        [{"type": "table"}, {"type": "scatter"}]   # Row 2: One scatter plot and one table
        ])
    
    # SETUP SUBPLOT 01 AT POSITION (1,1)
    # ADD Current vs. Potential PLOT
    CV_figure.add_trace(go.Scatter(x=CV_df['Vf(V)_CV00050'], 
                                   y=CV_df['Im(A)_CV00050'], 
                                   mode='lines+markers', 
                                   name='CV - Current vs. Potential',
                                   customdata=CV_df[['Time(s)_CV00050']].values,
                                   hovertemplate="Potential = %{x}<br>Current = %{y}<br>Time = %{customdata[0]}<extra></extra>"),
                        row=1, col=1)
    # Add text annotation for Scan Rate
    CV_figure.add_annotation(
        xref="x",         # Reference x-axis of the subplot
        yref="y",     # Reference y-axis of the subplot ("paper"= 0 to 1 for the subplot's height)
        x=-0.8,      # Adjust x-position slightly to the left
        y=0.75*max(CV_df['Im(A)_CV00050']),            # Y-position (normalized to paper coordinates for the subplot)
        #textangle=90, # Rotate text by -90 degrees
        text="<b>Scan Rate<br>0.05 V/s</b>",
        font_color='darkblue',
        font_size=unifiedfontsize,
        bgcolor="rgba(255,255,255,0.8)",
        showarrow=False,
        row=1, col=1
        )
    
    # SETUP SUBPLOT 02 AT POSITION (1,2)
    # ADD Potential vs. Time PLOT
    CV_figure.add_trace(go.Scatter(x=CV_df['Time(s)_CV00050'], 
                                   y=CV_df['Vf(V)_CV00050'], 
                                   mode='lines+markers', 
                                   name='Potential vs. Time',
                                   customdata=CV_df[['Im(A)_CV00050']].values,
                                   hovertemplate="Potential = %{y}<br>Current = %{customdata[0]}<br>Time = %{x}<extra></extra>"),
                        row=1, col=2)    
    # Add vertical line at transition between redcution & oxidation sweeps
    CV_figure.add_vline(x=mintime, line_width=1, line_color="black", 
                        row=1, col=2, exclude_empty_subplots=True)
    # Add text annotation to the left of the vertical line in the subplot
    CV_figure.add_annotation(
        xref="x",         # Reference x-axis of the subplot
        yref="y",     # Reference y-axis of the subplot ("paper"= 0 to 1 for the subplot's height)
        x=mintime-6,    # Adjust x-position slightly to the left
        y=0.5,            # Y-position (normalized to paper coordinates for the subplot)
        #textangle=90, # Rotate text by -90 degrees
        text="Reduction<br>Sweep",
        font_size=unifiedfontsize,
        bgcolor="rgba(255,255,255,0.8)",
        showarrow=False,
        row=1, col=2
        )
    # Add text annotation to the right of the vertical line in the subplot
    CV_figure.add_annotation(
        xref="x",
        yref="y",
        x=mintime+6,  # Adjust x-position slightly to the right
        y=0.5,
        #textangle=-90, # Rotate text by -90 degrees
        text="Oxidation<br>Sweep",
        font_size=unifiedfontsize,
        bgcolor="rgba(255,255,255,0.8)",
        showarrow=False,
        row=1, col=2
        )
    
    # SETUP SUBPLOT 03 AT POSITION (2,2)
    # ADD Current vs. Time PLOT
    CV_figure.add_trace(go.Scatter(x=CV_df['Time(s)_CV00050'], 
                                   y=CV_df['Im(A)_CV00050'], 
                                   mode='lines+markers',  # Or 'lines' if only fill is desired
                                   fill='tozeroy',       # Fills to the y-axis (or 'tonexty' for filling between traces)
                                   fillcolor='rgba(0, 128, 0, 0.2)', # Transparent fill
                                   name='Current vs. Time', 
                                   customdata=CV_df[['Vf(V)_CV00050']].values,
                                   hovertemplate="Potential = %{customdata[0]}<br>Current = %{y}<br>Time = %{x}<extra></extra>"),
                        row=2, col=2)
    # Add vertical line at transition between redcution & oxidation sweeps
    CV_figure.add_vline(x=mintime, line_width=1, line_color="black", 
                        row=2, col=2, exclude_empty_subplots=True)
    # Add text annotation to the left of the vertical line in the subplot
    CV_figure.add_annotation(
        xref="x",         # Reference x-axis of the subplot
        yref="y",     # Reference y-axis of the subplot ("paper"= 0 to 1 for the subplot's height)
        x=mintime-20,      # Adjust x-position slightly to the left
        y=0.55*max(CV_df['Im(A)_CV00050']),            # Y-position (normalized to paper coordinates for the subplot)
        #textangle=90, # Rotate text by -90 degrees
        text="Reduction<br>Sweep",
        font_size=unifiedfontsize,
        bgcolor="rgba(255,255,255,0.8)",
        showarrow=False,
        row=2, col=2
        )
    # Add text annotation to the right of the vertical line in the subplot
    CV_figure.add_annotation(
        xref="x",         # Reference x-axis of the subplot
        yref="y",     # Reference y-axis of the subplot ("paper"= 0 to 1 for the subplot's height)
        x=mintime+20,      # Adjust x-position slightly to the left
        y=0.55*min(CV_df['Im(A)_CV00050']),
        #textangle=-90, # Rotate text by -90 degrees
        text="Oxidation<br>Sweep",
        font_size=unifiedfontsize,
        bgcolor="rgba(255,255,255,0.8)",
        showarrow=False,
        row=2, col=2
        )
    # Add text annotation for CSCc
    CV_figure.add_annotation(
        xref="x",         # Reference x-axis of the subplot
        yref="y",     # Reference y-axis of the subplot ("paper"= 0 to 1 for the subplot's height)
        x=mintime-8,      # Adjust x-position slightly to the left
        y=0.4*min(CV_df['Im(A)_CV00050']),            # Y-position (normalized to paper coordinates for the subplot)
        #textangle=90, # Rotate text by -90 degrees
        text="<b>CSCc</b>",
        font_color='darkgreen',
        font_size=unifiedfontsize,
        bgcolor="rgba(255,255,255,0)",
        showarrow=False,
        row=2, col=2
        )
    # Add text annotation for CSCa
    CV_figure.add_annotation(
        xref="x",         # Reference x-axis of the subplot
        yref="y",     # Reference y-axis of the subplot ("paper"= 0 to 1 for the subplot's height)
        x=mintime+18,      # Adjust x-position slightly to the left
        y=0.4*max(CV_df['Im(A)_CV00050']),            # Y-position (normalized to paper coordinates for the subplot)
        #textangle=90, # Rotate text by -90 degrees
        text="<b>CSCa</b>",
        font_color='darkgreen',
        font_size=unifiedfontsize,
        bgcolor="rgba(255,255,255,0)",
        showarrow=False,
        row=2, col=2
        )
    
    # SETUP DATA TABLE AT POSITION (2,1)
    # ADD CSC DATA TABLE
    CV_figure.add_trace(go.Table(
        header=dict(values=["    Material <br>Abbreviation", "    CSCc <br>mC/cm^2", "    CSCa <br>mC/cm^2"], align='center',
                    height=30, fill_color='rgb(60,60,60)', line_color='black', 
                    font=dict(weight="bold", color='white', size=unifiedfontsize+2)),
        cells=dict(values=[selected, CSCc_CV00050, CSCa_CV00050], align='center',
                   height=30, fill_color='white', line_color='black', 
                   font=dict(weight="bold", color='black', size=unifiedfontsize+2)) 
    ), row=2, col=1)


    # UPDATE FIGURE FORMATTING
    
    CV_figure.update_layout(
        showlegend=False,
        autosize=True,
        margin=dict(t=0),  #r=40,b=40,l=40
        font_color='black',
        font_size=unifiedfontsize,
        #title_text='Cyclic Voltammetry (CV) Data',
        #title_x=0.5,
        #title_xanchor='center',
        plot_bgcolor='white'
        )

    CV_figure.update_xaxes(row=1,col=1,  # Potential axis, Current vs. Potential Plot
        title_text ='Potential vs. Ag|AgCl (V)',
        title_standoff = titlestandoffvalue,
        automargin=True,
        range=[-0.95,0.85],
        tickmode="linear",
        tick0=-0.9,
        dtick=0.1,
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
    
    CV_figure.update_yaxes(row=1,col=1,  # Current axis, Current vs. Potential Plot
        title_text ='Current (A)',
        title_standoff = titlestandoffvalue,
        automargin=True,
        autorange=True,
        #range=[0,60],      #!!! [to-do] update so that range scales to selected data
        tickmode="auto",
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
    
    CV_figure.update_xaxes(row=1,col=2,  # Time axis, Potential vs. Time Plot
        title_text ='Time (s)',
        title_standoff = titlestandoffvalue,
        automargin=True,
        range=[0,60],      #!!! [to-do] update so that range scales to selected data
        tickmode="linear",
        tick0=0,
        dtick=10,
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
    
    CV_figure.update_yaxes(row=1,col=2,   # Voltage axis, Potential vs. Time Plot
        title_text ='Potential (V_ref)',
        title_standoff = titlestandoffvalue,
        automargin=True,
        range=[-0.9,0.9],
        tickmode="linear",
        tick0=-0.9,
        dtick=0.3,
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
    
    CV_figure.update_xaxes(row=2,col=2,   # Time axis, Current vs. Time Plot
        title_text ='Time (s)',
        title_standoff = titlestandoffvalue,
        automargin=True,
        range=[0,60],      #!!! [to-do] update so that range scales to selected data
        tickmode="linear",
        tick0=0,
        dtick=10,
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
    
    CV_figure.update_yaxes(row=2,col=2,   # Current axis, Current vs. Time Plot
        title_text ='Current (A)',
        title_standoff = titlestandoffvalue,
        automargin=True,
        autorange=True,
        tickmode="auto",
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
    
    
    return CV_figure



#-----------------------------------------------------------------------------
#                               SECTION 6
#-----------------------------------------------------------------------------
# Run App
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)


#-----------------------------------------------------------------------------
# END OF FILE
#-----------------------------------------------------------------------------

