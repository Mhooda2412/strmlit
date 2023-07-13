import streamlit as st
import pandas as pd  
import numpy as np 
import base64
import random
from streamlit_option_menu import option_menu
from streamlit_echarts import st_echarts
st.set_page_config(page_title="PortFolioDashboard", page_icon=":bar_chart:", layout="wide")
#selected_option=st.selectbox("",options=['Overall Portfolio Snapshot','Customer Profile'],label_visibility='collapsed')
selected_option = option_menu(menu_title=None,
                    options=['Overall Portfolio Snapshot','Customer Profile'],
                    icons=['barchart','person'],
                    menu_icon='cast',default_index=0,orientation='horizontal',
                    styles={"container":{"padding":"0!important","backgroundcolor":'transparent'},
                            "icon":{"color":"orange","font-size":"20px"},
                    "nav-link":{"font-size":"20px",
                                "text-align":"left",
                                "margin":"0px",
                                "--hover-color":"#eee"},
                    "nav-link-selected":{'background-color':"0197F6"},},)
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(io="C:/Users/Amani Reddy/Dashboards/files/c_score.xlsx",engine="openpyxl",nrows=10)
    return df
@st.cache_data
def get_data_from_excel2():
    df = pd.read_excel(io="C:/Users/Amani Reddy/Dashboards/files/c_score_graph.xlsx",engine="openpyxl",nrows=10)
    return df    


if selected_option=="Overall Portfolio Snapshot":
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
    #st.markdown('<h1 style="color: skyblue; font-size: 35px;background-color: #005a92;font-size: 35px; padding: 10px;">Risk dashboard - Disbursement Portfolio</h1>', unsafe_allow_html=True)
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
        "data": ['Received',"After KYC","After BRE Rejection", 'Disbursed'],
        "axisLabel": {"color":'white',"fontSize": 15}
      },
      "yAxis": {
        "show":False,
        "type": 'value',
      },
      "series": [
        {
          "data":[{ "value": 98000, "itemStyle": {"borderWidth": 4,
                                                "borderColor": '#82eefd',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":"20.2Cr"}},
                { "value": 76000, "itemStyle": {"borderWidth": 4,
                                                "borderColor": '#63c5da',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":"16.4Cr"} },
                { "value": 68700, "itemStyle": { "borderWidth": 4,
                                                "borderColor": '#5d8aa8',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":"14.6 Cr"} },
                { "value": 58202, "itemStyle": { "borderWidth": 4,
                                                "borderColor": 'grey',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":"12.4 Cr"} }],
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
                "data":[{ "value": 98000, "itemStyle": { "color": "#82eefd" } },
                { "value": 76000, "itemStyle": { "color": '#63c5da' } },
                { "value": 68700, "itemStyle": { "color": '#5d8aa8' } },
                { "value": 58202, "itemStyle": { "color": 'grey' } }],
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


else:
    dashboard=st.sidebar.radio("Please select the Score Type",('A-Score','C-Score'))
    df = get_data_from_excel()
    data=get_data_from_excel2()
    user=st.sidebar.selectbox( "Please Select the UserID:",options=df['custid'])

    @st.cache_data
    def get_data_from_a():
        df=pd.read_excel("C:/Users/Amani Reddy/Dashboards/files/a_score_new.xlsx",nrows=10)
        return df

    if dashboard=='C-Score':
        
        st.title(f":chart_with_upwards_trend: C SCORE for {user}")
        st.markdown("---")
        df_selection = df.query("custid == @user")   
        df_selection.reset_index(inplace=True)
        data_selection=data.query("custid == @user")
        L6M_loans_cat3_UnSec_exclCONSKCC=round(float(df_selection['L6M_loans_cat3_UnSec_exclCONSKCC']),2)
        L12M_DPD_cat0_PL_below50K=round(float(df_selection['L12M_DPD_cat0_PL_below50K']),2)
        trend_loan_opened_L12M_36M=round(float(df_selection['trend_loan_opened_L12M_36M']),2)
        Highcredit_L12M_cat4_ALL_STD=round(float(df_selection['Highcredit_L12M_cat4_ALL_STD']),0)
        L3M_DPD_cat2_NonCC=round(float(df_selection['L3M_DPD_cat2_NonCC']),0)
        Total_enquiries_L6M_30_210=round(float(df_selection['Total_enquiries_L6M_30_210']),2)
        max_dpd_l24m=(df_selection['max_dpd_l24m'][0])
        no_secure_loan=round(float(df_selection['no_secure_loan']) ,0)
        cat3_gap_btw_UnSec_exclCONSKCC=round(float(df_selection['cat3_gap_btw_UnSec_exclCONSKCC']),0)
        colors=['green','#FFCE30','red']
        if L6M_loans_cat3_UnSec_exclCONSKCC<2:
            L6M_loans_cat3_UnSec_exclCONSKCC_color=colors[0]
        elif 2<=L6M_loans_cat3_UnSec_exclCONSKCC<4:
            L6M_loans_cat3_UnSec_exclCONSKCC_color=colors[1]
        else:
            L6M_loans_cat3_UnSec_exclCONSKCC_color=colors[2]   
        if L12M_DPD_cat0_PL_below50K<30:
            L12M_DPD_cat0_PL_below50K_color=colors[0]
        elif 30<=L6M_loans_cat3_UnSec_exclCONSKCC<60:
            L12M_DPD_cat0_PL_below50K_color=colors[1]
        else:
            L12M_DPD_cat0_PL_below50K_color=colors[2]  
        if trend_loan_opened_L12M_36M<0.1:
            trend_loan_opened_L12M_36M_color=colors[0]
        elif 0.1<=trend_loan_opened_L12M_36M<0.5:
            trend_loan_opened_L12M_36M_color=colors[1]
        else:
            trend_loan_opened_L12M_36M_color=colors[2]  
        if L3M_DPD_cat2_NonCC<30:
            L3M_DPD_cat2_NonCC_color=colors[0]
        elif 30<=L3M_DPD_cat2_NonCC<60:
            L3M_DPD_cat2_NonCC_color=colors[1]
        else:
            L3M_DPD_cat2_NonCC_color=colors[2]
        if Total_enquiries_L6M_30_210<2:
            Total_enquiries_L6M_30_210_color=colors[0]
        elif 2<=Total_enquiries_L6M_30_210<4:
            Total_enquiries_L6M_30_210_color=colors[1]
        else:
            Total_enquiries_L6M_30_210_color=colors[2]
        if max_dpd_l24m=="'0'" or max_dpd_l24m=="'1-29'":
            max_dpd_l24m_color=colors[0]
        elif max_dpd_l24m=="'30-59'":
            max_dpd_l24m_color=colors[1]
        else :
            max_dpd_l24m_color=colors[2]
        if no_secure_loan>=1:
            no_secure_loan_color=colors[0]
        else:
            no_secure_loan_color=colors[2]  
        if cat3_gap_btw_UnSec_exclCONSKCC<2:
            cat3_gap_btw_UnSec_exclCONSKCC_color=colors[0]
        elif 2<=cat3_gap_btw_UnSec_exclCONSKCC<6:
            cat3_gap_btw_UnSec_exclCONSKCC_color=colors[1]
        else:
            cat3_gap_btw_UnSec_exclCONSKCC_color=colors[2]
        col1,col2=st.columns(2)
        with col1:
            months=['Oct-22'	,'Sep-22'	,'Aug-22'	,'Jul-22',	'Jun-22'	,'May-22']
            values=((data_selection.iloc[:,[1,2,3,4,5,6]]).iloc[0]).tolist()
            option = {'title':{"show":True,'text':'Score','left':'center','textStyle':{'color':'#FFFFFF','textBorderColor':'#FFFFFF'}},
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
            'grid':{"show":False},
            'legend':{"animationDurationUpdate":1000},
            'series': [
                {
                'data': values,
                'type': 'line',
                'label':{'show':True, 'borderColor':"blue", 'borderType' : 'dotted','position':'insideTopRight', 'distance' : 10,'fontSize':18,'color':'#FFFFFF','fontWeight':'bold','fontFamily':'monospace'},
                'universalTransition':{"enabled":True}
                }
            ]
            }
            with st.container():
                st_echarts(options=option,height="300px")
        with col2:
                value=int(df_selection['EWS_Score'])
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
                            [0.75, '#E5BA1D'],
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
                        'color': 'auto'
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
        #first row
        col1,col2,col4,col6=st.columns(4,gap="large")
        with col1:
            with st.container():
                st.write("Number of loans open in last 6 months:")
                html_temp = f"""
                <div style="background-color:#46A042;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{L6M_loans_cat3_UnSec_exclCONSKCC} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col2:
            with st.container():
                st.write("Max dpd in last 12 months on PL <=50K")
                html_temp = f"""
                <div style="background-color:#46A042;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{L12M_DPD_cat0_PL_below50K} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col4:
            with st.container():
                st.write("Loans open: 12M vs 36M")
                html_temp = f"""
                <div style="background-color:#46A042;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{trend_loan_opened_L12M_36M} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col6:
            with st.container():
                st.write("Max DPD(lst 24M):")
                html_temp = f"""
                <div style="background-color:#E5BA1D;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{max_dpd_l24m} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        
        #second row
        col1,col2,col4,col5=st.columns(4,gap="large")
        with col1:
            with st.container():
                st.write("Max dpd lst 3M excluding CC:")
                html_temp = f"""
                <div style="background-color:#46A042;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{L3M_DPD_cat2_NonCC} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col2:
            with st.container():
                st.write("#enquiries in last 6M:")
                html_temp = f"""
                <div style="background-color:#46A042;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{Total_enquiries_L6M_30_210} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col4:
            with st.container():
                st.write("Has Secure Loan:")
                html_temp = f"""
                <div style="background-color:#46A042;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{no_secure_loan} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col5:
            with st.container():
                st.write("Gap b/w two loans:")
                html_temp = f"""
                <div style="background-color:#CD2D23;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{cat3_gap_btw_UnSec_exclCONSKCC} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
            st.markdown("---")   

    else:
        
        df=get_data_from_a()
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