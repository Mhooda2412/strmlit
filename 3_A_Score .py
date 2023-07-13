import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts 
import numpy as np
import random

st.set_page_config(page_title="A-Score", page_icon=":bar_chart:", layout="wide")

@st.cache_data
def get_data_from_a():
    df=pd.read_excel("C:/Users/Amani Reddy/Downloads/a_score_new.xlsx",nrows=10)
    return df

df=get_data_from_a()

user = st.sidebar.selectbox( "Please Select the UserID:",options=df['custid'])

# user from 1st page...
# user=st.session_state['user']

st.title(f":chart_with_upwards_trend: A SCORE for {user}")

st.markdown("---")

df_selection = df.query(
    "custid == @user"
) 

Enq_L12M_UnSec=round(float(df_selection['Enq L12M UnSec']),0)
Months_since_last_npa=round(float(df_selection['Months_since_last_npa']),2)
Avg_gap_two_loans=round(float(df_selection['Avg gap b/w two loans']),2)
Total_Enq_L6M=round(float(df_selection['Total Enq L6M']),2)
max_consecutive_dpd_L12M_NPA=round(float(df_selection['max_consecutive_dpd_L12M_NPA']),2)
POS_left=round(float(df_selection['POS left']),2)
POS_in_90DPD=round(float(df_selection['%POS in 90DPD']),2)
Utilization_on_CC=round(float(df_selection['Utilization on CC']),2)
value=round(float(df_selection['A Score']),2)

col1,col2=st.columns(2,gap="large")
with col1:
 d=[{"Mar-22":random.randint(2, 4),'Apr-22':random.randint(2, 4),'May-22':random.randint(2, 4),'Jun-22':random.randint(2, 4),'Nov-22':random.randint(2, 4)}]
 df=pd.DataFrame(d)
 months=(df.columns).tolist()
 values=(df.iloc[0]).tolist()

 option = {'title':{"show":True,'text':'Live Account Buildup','left':'center','textStyle':{'color':'#E2DEE7','textBorderColor':'pink'}},

  'xAxis': {
    'type': 'category',
     'data': months,
     'axisLabel': { 'rotate': 30 },
     'textStyle':{'color':'#FFFFFF'},
     'axisLine': {
        'lineStyle': {
          'color': '#E2DEE7'
        }
     }
  },
  'yAxis': {
    'type': 'value',
    'show':False,
    'axisLine':{"show":False},
    'splitLine':{'show':False}
  },
  'grid':{"show":False,},
  'legend':{"animationDurationUpdate":5000, 'animationDelay':20000, 'animationDurationUpdate' : 2000},
  'series': [
    {
      'data': values,
      'type': 'line',
      'label':{'show':True, 'borderColor':"blue", 'borderType' : 'dotted','position':'insideTopRight', 'distance' : 8,'fontSize':18,'color':'#FFFFFF','fontWeight':'bold','fontFamily':'monospace'},
      'universalTransition':{"enabled":True},
      'labelLine':{"show":True}
      
    }
  ]
}
 with st.container():
    st_echarts(options=option,height="300px")
with col2:
 

 option = {
  'tooltip': {
    'formatter': '{a} <br/>{b} : {c}'
  },
  'series': [
    {
      'name': 'SCORE',
      'type': 'gauge',
      'progress':{'show':False},
      'axisLine': {
        'lineStyle': {
          'width': 30,
          'color': [
            [0.5, '#C62208'],
            [0.75, 'yellow'],
            [1, 'green']
          ]
        }
      },
      'pointer': {
        'itemStyle': {
          'color': 'auto'
        }
      },
      'axisTick': {
        'distance': -30,
        'length': 5,
        'lineStyle': {
          'color': '#fff',
          'width': 2
        }
      },
      
      
      'axisLabel': {'show':True,
        'color': '#FFFFFF',
        'distance': 20,
        'fontSize': 15
      },
      'startAngle':190,
      'endAngle':-10,
      'min':300,
      'max':900,
      'splitNumber':2,
      'radius':'90%',
      'detail': {
        'formatter': value,
        'color': '#FFFFFF'
      },
       
      
      'legend':{"animationDurationUpdate":2000},
      'data': [
        {
          'value':value,
          'title': {'show':True,'color':'#FFFFFF'},
          "name": 'SCORE',
          'itemStyle':{'color':'#FFFFFF','borderColor':'pink'},
           "textStyle":{ 'fontWeight' : 'lighter'}

        }
      ]
    }
  ]
}
 with st.container():
    st_echarts(options=option,height="350px")

colors=['red','#FFCE30','green','#38BFDA']

col1,col2,col4,col6=st.columns(4,gap="large")
with col1:
  with st.container():
    st.write("#Enq L12M UnSec:")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{Enq_L12M_UnSec} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

with col2:
  with st.container():
    st.write("Month since last npa")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{Months_since_last_npa} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

with col4:
  with st.container():
    st.write("Avg gap b/w two loans:")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{Avg_gap_two_loans} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

with col6:
  with st.container():
    st.write("Total Enq L6M:")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
     <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{Total_Enq_L6M} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
 
#second row
col1,col2,col4,col5=st.columns(4,gap="large")
with col1:
  with st.container():
    st.write("max cons dpd L12M NPA:")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{max_consecutive_dpd_L12M_NPA} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
with col2:
  with st.container():
    st.write("POS left:")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{POS_left} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

with col4:
  with st.container():
    st.write("POS in 90DPD:")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{POS_in_90DPD} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

with col5:
  with st.container():
    st.write("Utilization on CC:")
    html_temp = f"""
      <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{Utilization_on_CC} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
st.markdown("---")