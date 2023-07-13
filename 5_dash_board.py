
import pandas as pd
import streamlit as st
import plotly.express as px
import os
import streamlit.components.v1 as components
st.set_page_config(page_title="Risk DashBoards",layout='wide',initial_sidebar_state='expanded')

import base64

@st.cache_data
def get_image_as_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
img=get_image_as_base64(r'background_pic.jpg')
page_bg_img=f'''
<style>
    [data-testid='stAppViewContainer']{{
    background-image: url('data:image/png;base64,{img}');
    background-position: center;
    }}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown('<h1 style="color: skyblue; font-size: 35px;background-color: #005a92;font-size: 35px; padding: 10px;">Risk dashboard - Disbursement Portfolio</h1>', unsafe_allow_html=True)
st.write(".")
from streamlit_echarts import st_echarts
Disbursal_trends = {
  "backgroundColor":'transparent',
  "title": {
    "text": 'Disbursal trends',
    "textStyle":{"color":'#0197F6'},
  },
  "tooltip": {
    "trigger": 'axis'
  },
  "toolbox": {
    "show": True,
    "feature": {
      "dataView": { "show": True, "readOnly": False },
      "magicType": { "show": True, "type": ['line', 'bar'] },
      "restore": { "show": True },
      "saveAsImage": { "show": True }
    }
  },
  "grid": { "containLabel": True },
  "calculable": True,
  "xAxis": [
    {
      "type": 'category',
      "data": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      "itemStyle":{"color":'white'},
      "axisLabel": {"color":'white'}
    }
  ],
  "yAxis": [
    {
      "splitLine":{"show":False},
      "axisLine":{"show":True},
      "type": 'value',
      "name":'Disbursement(INR Cr)',
      "axisname":{"color":'white'},
      "axisLabel": {"color":'white'}
    },
    {
      "splitLine":{"show":False},
      "axisLine":{"show":True},
      "axisLabel":{"color":'white'},
      "min":0,
      "max":30,
      "interval":5,
      "type": 'value',
      "name":'npa(%)',
      "color":'green'
    }
  ],
  "series": [
    {
      "name": 'Disbursed Amount(in Cr)',
      "type": 'bar',
      "data": [
        2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
      ],
      "itemStyle":{"color":'#00BFFF'},
      "label": {
        "show": True,
        "position": 'outside',
        "color":'white'
      }
    },
    {
     "name":"npa(%)",
      "type": 'line',
      "yAxisIndex":1,
      "data": [
        26.0, 42.9, 77.0, 23.2, 25.6, 776.7, 135.6, 12.2, 52.6, 20.0, 6.4, 3.3
      ],
      "itemStyle":{"color":'#00BFFF'},
      "label": {
        "show": False,
        "position": 'outside',
        "color":'white'
      }
    }
  ]
}

lead_funnel = {"title": {
    "text": 'Lead funnel',
    "textStyle":{"color":'#0197F6'}},
    "tooltip": {
      "trigger": 'axis'
    },
    "toolbox": {
      "show": True,
      "feature": {
        "dataView": { "show": True, "readOnly": False },
        "magicType": { "show": True, "type": ['line', 'bar'] },
        "restore": { "show": True },
        "saveAsImage": { "show": True }
      }
    },
    "grid": { "containLabel": True },
  "xAxis": {
    "type": 'category',
    "data": ['Received', 'Approved', 'Disbursed'],
    "axisLabel": {"color":'white',"fontSize": 15}
  },
  "yAxis": {
    "show":False,
    "type": 'value',
  },
  "series": [
    {
      "data":[{ "value": 200, "itemStyle": {"borderWidth": 4,
                                            "borderColor": '#82eefd',
                                            "color": 'white'},"label": {"show": True,
                                                                    "position": 'inside',
                                                                    "formatter":"8.2Cr"}},
            { "value": 150, "itemStyle": {"borderWidth": 4,
                                            "borderColor": '#63c5da',
                                            "color": 'white'},"label": {"show": True,
                                                                    "position": 'inside',
                                                                    "formatter":"6.4Cr"} },
            { "value": 100, "itemStyle": { "borderWidth": 4,
                                            "borderColor": '#5d8aa8',
                                            "color": 'white'},"label": {"show": True,
                                                                    "position": 'inside',
                                                                    "formatter":"5 Cr"} }],
      "type": 'line',
      "symbol": 'circle',
      "symbolSize": 75,
      "lineStyle": {
        "color": 'green',
        "width": 0,
        "type": 'hidden'
      }
    },
    {
     "name":"Number of Applications",
            "data":[{ "value": 200, "itemStyle": { "color": "#82eefd" } },
            { "value": 150, "itemStyle": { "color": '#63c5da' } },
            { "value": 100, "itemStyle": { "color": '#5d8aa8' } } ],
            "type": 'bar',
            "barWidth":80,
            "color":'skyblue',
            "label": {
        "show": True,
        "position": 'inside'}
            
        }
  ]
}
#st_echarts(options=option)

risk_profile = {
  "backgroundColor": 'transparent',
  "title": {
    "text": 'Risk Profile',
    "textStyle" :{"color": '#0197F6'},
    "subtext": '% of Customers',
    "subtextStyle" : {"color": 'white'}
  },
  "tooltip": {
    "trigger": 'axis',
    "axisPointer": {
      "type": 'shadow'
    }
  },
  "grid": {
    "left": '3%',
    "right": '4%',
    "bottom": '3%',
    "containLabel": True
  },
  "xAxis": {
    "type": 'category',
    "splitLine": { "show": False },
    "data": ['500-600','600-700','700-750','750-800','800-850','NTC','Total'],
    "axisLabel": {"color":'white',"fontSize": 10}
  },
  "yAxis": {
    "show": False,
    "type": 'value',
    "min": 0,
    "max": 100,

  },
  "series": [
    {
      "name": '% of Customers',
      "type": 'bar',
      "stack": 'Total',
      "itemStyle": {
        "borderColor": 'transparent',
        "color": 'transparent'
      },
      "emphasis": {
        "itemStyle": {
          "borderColor": 'transparent',
          "color": 'transparent'
        }
    },
    "data": [0,0,13,56,69,70,0]
    },
    {
      "name": '% of Customers',
      "type": 'bar',
      "stack": 'Total',
      "label": {
        "show": True,
        "position": 'inside'
      },
      "data":[{ "value": 0, "itemStyle": { "color": 'white' } },
      { "value": 13, "itemStyle": { "color": '#FF5C5C' } },
      { "value": 43, "itemStyle": { "color": '#82EEFD' } },
      { "value": 13, "itemStyle": { "color": '#6495ED' } },
      { "value": 1, "itemStyle": { "color": '#green' } },
      { "value": 30, "itemStyle": { "color": '#D1EAF0' } },
      { "value": 100, "itenStyle": {"color": 'grey'} }]
  }
]
}
#st_echarts(options=option1)

non_approval = {
  "backgroundColor":'transparent',
  "title": {
    "text": 'Non Approval reasons',
    "subtext":'(# of files)',
    "subtextStyle":{"fontSize":14,"color":'white'},
    "textStyle":{"color":'#0197F6'},
  },
  "tooltip": {
    "trigger": 'axis'
  },
  "toolbox": {
    "show": True,
    "feature": {
      "dataView": { "show": True, "readOnly": False },
      "magicType": { "show": True, "type": ['line', 'bar'] },
      "restore": { "show": True },
      "saveAsImage": { "show": True }
    }
  },
  "grid": { "containLabel": True },
  "calculable": True,
  "xAxis": [
    {
      "show":False
    }
  ],
  "yAxis": [
    {
      "type": 'category',
      "data": ['Credit Reasons', 'KYC failure', 'Negative list', 'Others'],
      "itemStyle":{"color":'white'},
      "axisLabel":{"color":'white',"fontSize":15}
    }
  ],
  "series": [
    {
      "name": 'Number of Customers',
      "type": 'bar',
      "data": [{ "value": 2, "itemStyle": { "color": 'white' } },
      { "value": 4.9, "itemStyle": { "color": '#FF5C5C' } },
      { "value": 7, "itemStyle": { "color": '#82EEFD' } },
      { "value": 23.2, "itemStyle": { "color": '#6495ED' } }
      ],
      "label": {
        "show": True,
        "position": 'right',
        "color":'white',
        "fontSize":15
      }
    }
  ]
}


# Set up the layout using Streamlit columns
col1, col2= st.columns(2,gap='large')

# Render the first graph in the first column
with col1:
    #st.subheader('Graph 1')
    st_echarts(options=Disbursal_trends)

# Render the second graph in the second column
with col2:
    #st.subheader('Graph 2')
    st_echarts(options=lead_funnel)

with col1:
    st_echarts(options=non_approval)

with col2:
    #st.markdown("<h2 style='color: #0197F6;'>Lead Funnel</h2>", unsafe_allow_html=True)
    st_echarts(options=risk_profile)
    
st.write(".")   
st.write(".") 

with col1:
    
    #st.markdown("<h2 style='color: #0197F6;'>Lead Funnel</h2>", unsafe_allow_html=True)
    with open('index.html', 'r') as f:
        html_code = f.read()
   
    st.markdown(html_code, unsafe_allow_html=True)
    
with col2:
    #st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#0197F6;" /> """, unsafe_allow_html=True)
    with open('index2.html', 'r') as f:
        html2_code = f.read()
   
    st.markdown(html2_code, unsafe_allow_html=True)







