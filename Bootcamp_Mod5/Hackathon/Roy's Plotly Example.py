#!/usr/bin/env python
# coding: utf-8
# In[1]:
import pandas as pd
import plotly.graph_objects as go
# In[2]:
covid_dat = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
covid_dat
# In[3]:
tot_permil_630 = covid_dat[covid_dat['date']=='2020-07-08'].reset_index(drop=True)[:-1]
tot_permil_630['total_cases']
# In[4]:
tot_permil_630 = covid_dat[covid_dat['date']=='2020-07-08'].reset_index(drop=True)[:-1]
fig = go.Figure(data=go.Choropleth(
    locations = tot_permil_630['iso_code'],
    z = tot_permil_630['total_cases'],
    text = tot_permil_630['location'],
    colorscale = 'RdBu',
    #autocolorscale=True,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Total cases',
))
multiplier_fig_size = 0.75
fig.update_layout(
    title_text='Total cases at July 8, 2020',
    height = (800 * multiplier_fig_size),
    width = (1200 * multiplier_fig_size),
    geo=dict(
        showframe=False, #border of the globe map
        showcoastlines=True, #slightly thicker lines on shorelines
        projection_type='natural earth' #mercator projections
    ),
    annotations = [dict(
        x=0.55, #where adding text X
        y=0.1, #where adding text Y
        xref='paper', 
        yref='paper',
        text='Source: Our World in Data', #text to add
        showarrow = False
    )]
)
fig.show()
fig.write_html("July8_Total_Covid.html")
#%%

countries = ['USA', 'BRA', 'FRA', 'CHN', 'KOR', 'IND', 'JPN']
vari = 'new_cases'

import plotly.io as pio
pio.templates.default = "plotly_dark"

temp = covid_dat[covid_dat['iso_code'].isin(countries)]

fig = go.Figure()

for count in countries:
    x = temp['date'][temp['iso_code']==count]
    y = temp[vari][temp['iso_code']==count]
    fig.add_trace(go.Scatter(x=x, y=y, 
                        mode='lines',
                        name=temp['location'][temp['iso_code']==count].values[0]
                            )
                 )

fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(#yaxis_type='log',
                 xaxis_title="Date",
                 #yaxis_title='',
                 annotations = [dict(xref='paper', yref='paper', x=0, y=1.1,
                              xanchor='left', yanchor='bottom',
                              text='Total Confirmed Cases',
                              font=dict(size=25),
                              showarrow=False)])
fig.show()