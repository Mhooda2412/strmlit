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
                    icons=['people-fill','person-fill'],
                    menu_icon='cast',default_index=0,orientation='horizontal',
                    styles={"container":{"padding":"0!important","backgroundcolor":'transparent'},
                            "icon":{"color":"orange","font-size":"20px"},
                    "nav-link":{"font-size":"20px",
                                "text-align":"left",
                                "margin":"0px",
                                "--hover-color":"#eee"},
                    "nav-link-selected":{'background-color':"#0197F6"},},)
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(io=r"C:\Users\Sarthak\Downloads\Dashboards\Dashboards\files_updated\files\c_score.xlsx",engine="openpyxl",nrows=10)
    return df
@st.cache_data
def get_data_from_excel2():
    df = pd.read_excel(io=r"C:\Users\Sarthak\Downloads\Dashboards\Dashboards\files_updated\files\c_score_graph.xlsx",engine="openpyxl",nrows=10)
    return df    

@st.cache_data
def get_image_as_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
#img=get_image_as_base64(r'background_pic.jpg')
page_bg_img=f'''
<style>
    [data-testid='stAppViewContainer']{{
    background: linear-gradient(to right, #4A00E0, #8E2DE2);
    background-position: center;
    }}
</style>'''

if selected_option=="Overall Portfolio Snapshot":
    st.markdown(page_bg_img, unsafe_allow_html=True)
    #st.markdown('<h1 style="color: skyblue; font-size: 35px;background-color: #005a92;font-size: 35px; padding: 10px;">Risk dashboard - Disbursement Portfolio</h1>', unsafe_allow_html=True)
    st.write(".")
    from streamlit_echarts import st_echarts
    Disbursal_trends = {
      "backgroundColor":'white',
      "title": {
        "text": 'Disbursal trends',
        "textStyle":{"color":'black'},
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
          "itemStyle":{"color":'black'},
          "axisLabel": {"color":'black',"fontSize": 9, 'rotate': 40}
        }
      ],
      "yAxis": [
        {
          "splitLine":{"show":False},
          "axisLine":{"show":True},
          "type": 'value',
          "min":0,
          "max":10,
          "interval":1,
          "name":'Disbursement(INR Cr)',
          "axisname":{"color":'black'},
          "axisLabel": {"color":'black'}
        },
        {
          "splitLine":{"show":False},
          "axisLine":{"show":True},
          "axisLabel":{"color":'black'},
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
            2.8, 4.9, 7.0, 3.2, 5.6, 6.7, 5.6, 2.2, 2.6, 2.2, 6.4, 3.3
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
            3.4, 3.9, 3.2, 3.5, 4.4, 5.1, 5.2, 4.9, 4.6, 4.3, 4.1, 4.2
          ],
          "itemStyle":{"color":'#red'},
          "label": {
            "show": False,
            "position": 'outside',
            "color":'black'
          }
        }
      ]
    }

    lead_funnel = {
        "backgroundColor":'white',
        "title": {
        "text": 'Lead funnel',
        "textStyle":{"color":'black'}},
        "tooltip": {
          "trigger": 'item'
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
        "data": ['Received',"KYC Approved","BRE Approved", 'Disbursed'],
        "axisLabel": {"color":'black',"fontSize": 12, 'rotate': 30}
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
                                                "borderColor": '#9370db',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":"12.4 Cr"} }],
          "type": 'line',
          "symbol": 'circle',
          "symbolSize": 50,
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
                { "value": 58202, "itemStyle": { "color": '#9370db' } }],
                "type": 'bar',
                "barWidth":55,
                "color":'skyblue',
                "label": {
            "show": True,
            "position": 'inside'}
                
            }
      ]
    }
    #st_echarts(options=option)

    risk_profile = {
      "backgroundColor": 'white',
      "title": {
        "text": 'Risk Profile(Disbursed Population)',
        "textStyle" :{"color": 'black'},
        "subtext": '% of Customers',
        "subtextStyle" : {"color": 'black'}
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
        "data": ['NTC','600-700','700-750','750-800','800-850','Total'],
        "axisLabel": {"color":'black',"fontSize": 10,"rotate":40}
      },
      "yAxis": {
        "show": False,
        "type": 'value',
        "min": 0,
        "max": 100,

      },
      "series": [
        {
          "name": 'Cummulative Percentage',
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
        "data": [0,10,25,55,90,0]
        },
        {
          "name": '% of Customers',
          "type": 'bar',
          "stack": 'Total',
          "label": {
            "show": True,
            "position": 'inside'
          },
          "data":[{ "value": 10, "itemStyle": { "color": '#FF5C5C' } },
          { "value": 15, "itemStyle": { "color": '#82EEFD' } },
          { "value": 30, "itemStyle": { "color": '#6495ED' } },
          { "value": 35, "itemStyle": { "color": '#green' } },
          { "value": 10, "itemStyle": { "color": '#D1EAF0' } },
          { "value": 100, "itenStyle": {"color": 'grey'} }]
      }
    ]
    }
    #st_echarts(options=option1)

    non_approval = {
      "backgroundColor":'white',
      "title": {
        "text": 'Non Approval reasons(BRE)',
        "subtext":'(# of files)',
        "subtextStyle":{"fontSize":14,"color":'black'},
        "textStyle":{"color":'black'},
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
          "data": ['Demographics', 'Bureau Derog', 'Model Rejects', 'Others'],
          "itemStyle":{"color":'black'},
          "axisLabel":{"color":'black',"fontSize":15}
        }
      ],
      "series": [
        {
          "name": 'Number of Customers',
          "type": 'bar',
          "data": [{ "value": 1329, "itemStyle": { "color": '#0197f6' } },
          { "value": 2056, "itemStyle": { "color": '#FF5C5C' } },
          { "value": 2787, "itemStyle": { "color": '#82EEFD' } },
          { "value": 128, "itemStyle": { "color": '#6495ED' } }
          ],
          "label": {
            "show": True,
            "position": 'right',
            "color":'black',
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
        with open(r'C:\Users\Sarthak\Downloads\Dashboards\Dashboards\index.html', 'r') as f:
            html_code = f.read()
       
        st.markdown(html_code, unsafe_allow_html=True)
        
    with col2:
        #st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#0197F6;" /> """, unsafe_allow_html=True)
        with open(r'C:\Users\Sarthak\Downloads\Dashboards\Dashboards\index2.html', 'r') as f:
            html2_code = f.read()
       
        st.markdown(html2_code, unsafe_allow_html=True)


else:
    st.markdown(page_bg_img, unsafe_allow_html=True)

    dashboard=st.sidebar.radio("Please select required field",('A-Score','C-Score','BRE'))
    df = get_data_from_excel()
    data=get_data_from_excel2()

    @st.cache_data
    def get_data_from_a():
        df=pd.read_excel(r"C:\Users\Sarthak\Downloads\Dashboards\Dashboards\files_updated\files\a_score_new.xlsx",nrows=10)
        return df
    
    def get_data_from_excel(SheetName):
            df = pd.read_excel(io=r"C:\Users\Sarthak\Downloads\Dashboards\Dashboards\files_updated\files\data_for_BRE.xlsx",engine="openpyxl",sheet_name=SheetName)
            return df
    if dashboard=='C-Score':
        
        user=st.sidebar.selectbox( "Please Select the UserID:",options=df['custid'])
        
        st.subheader(f"C SCORE for {user}")
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
            option = {'backgroundColor':'white',
                'title':{"show":True,'text':'Score','left':'center','textStyle':{'color':'black','textBorderColor':'black'}},
            'xAxis': {
                'type': 'category',
                'data': months,
                'axisLabel': { 'rotate': 30 },
                'textStyle':{'color':'black'},
                'axisLine': {
                    'lineStyle': {
                    'color': 'black'
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
                'label':{'show':True, 'borderColor':"black", 'borderType' : 'dotted','position':'insideTopRight', 'distance' : 10,'fontSize':18,'color':'black','fontWeight':'bold','fontFamily':'monospace'},
                'universalTransition':{"enabled":True}
                }
            ]
            }
            with st.container():
                st_echarts(options=option,height="300px")
        with col2:
                value=int(df_selection['EWS_Score'])
                option = {
                    'backgroundColor':'white',
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
                        'color': 'black',
                        'width': 2
                        }
                    },
                    'axisLabel': {'show':True,
                        'color': 'black',
                        'distance': 30,
                        'fontSize': 11
                    },
                    'startAngle':190,
                    'endAngle':-10,
                    'min':300,
                    'max':900,
                    'splitNumber':4,
                    'radius':'90%',
                    'detail': {
                        'formatter': value,
                        'color': 'auto'
                    },
                    
                    
                    'legend':{"animationDurationUpdate":2000},
                    'data': [
                        {
                        'value':value,
                        'title': {'show':True,'color':'black'},
                        "name": 'SCORE',
                        'itemStyle':{'color':'black','borderColor':'black'},
                        "textStyle":{ 'fontWeight' : 'lighter'}
                        }
                    ]
                    }
                ]
                }
                with st.container():
                    st_echarts(options=option,height="300px")
        #first row
        col1,col2,col4=st.columns(3,gap="medium")
        with col1:
            with st.container():
                # st.write("Loans opened last 6M")
                rishu="""
        <h1 style="color:black;text-align:center;font-size:120%;font-family:times;">Loans opened last 6M</h1>
        """
                st.write(rishu,unsafe_allow_html=True)
                html_temp = f"""
                <div style="background-color:white;padding:4px;border-radius: 25px">
                <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{L6M_loans_cat3_UnSec_exclCONSKCC} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col2:
            with st.container():
                # st.write("DPD in last 12M")
                rishu="""
        <h1 style="color:black;text-align:center;font-size:120%;font-family:times;">DPD in last 12M</h1>
        """
                st.write(rishu,unsafe_allow_html=True)
                html_temp = f"""
                <div style="background-color:white;padding:4px;border-radius: 25px">
                <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{L12M_DPD_cat0_PL_below50K} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col4:
            with st.container():
                # st.write("Ratio loan opened:12M/36M")
                rishu="""
        <h1 style="color:black;text-align:center;font-size:120%;font-family:times;">Ratio loan opened:12M/36M</h1>
        """
                st.write(rishu,unsafe_allow_html=True)
                html_temp = f"""
                <div style="background-color:white;padding:4px;border-radius: 25px">
                <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{trend_loan_opened_L12M_36M} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        # with col6:
        #     with st.container():
        #         st.write("Max DPD(lst 24M):")
        #         html_temp = f"""
        #         <div style="background-color:#E5BA1D;padding:4px;border-radius: 25px">
        #         <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{max_dpd_l24m} </h1>
        #         </div><br>"""
        #         st.markdown(html_temp,unsafe_allow_html=True)
        
        #second row
        col1,col2,col5=st.columns(3,gap="medium")
        with col1:
            with st.container():
                # st.write("DPD in last 3M")
                rishu="""
        <h1 style="color:black;text-align:center;font-size:120%;font-family:times;">DPD in last 3M</h1>
        """
                st.write(rishu,unsafe_allow_html=True)
                html_temp = f"""
                <div style="background-color:white;padding:4px;border-radius: 25px">
                <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{L3M_DPD_cat2_NonCC} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        with col2:
            with st.container():
                # st.write("Enquiries in last 6M:")
                rishu="""
        <h1 style="color:black;text-align:center;font-size:120%;font-family:times;">Enquiries in last 6M</h1>
        """
                st.write(rishu,unsafe_allow_html=True)
                html_temp = f"""
                <div style="background-color:white;padding:4px;border-radius: 25px">
                <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{Total_enquiries_L6M_30_210} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
        # with col4:
        #     with st.container():
        #         st.write("Has Secure Loan:")
        #         html_temp = f"""
        #         <div style="background-color:#46A042;padding:4px;border-radius: 25px">
        #         <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{no_secure_loan} </h1>
        #         </div><br>"""
                # st.markdown(html_temp,unsafe_allow_html=True)
        with col5:
            with st.container():
                # st.write("Days b/w two opened loans")
                rishu="""
        <h1 style="color:black;text-align:center;font-size:120%;font-family:times;">Days b/w two opened loans</h1>
        """
                st.write(rishu,unsafe_allow_html=True)
                html_temp = f"""
                <div style="background-color:#CD2D23;padding:4px;border-radius: 25px">
                <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{cat3_gap_btw_UnSec_exclCONSKCC} </h1>
                </div><br>"""
                st.markdown(html_temp,unsafe_allow_html=True)
            st.markdown("---")   

    elif(dashboard=='A-Score'):
        
        user=st.sidebar.selectbox( "Please Select the UserID:",options=df['custid'])

        df=get_data_from_a()
        st.subheader(f"A-SCORE for {user}")

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

         option = {'backgroundColor':'white','title':{"show":True,'text':'Live Account Buildup','left':'center','textStyle':{'color':'black','textBorderColor':'pink'}},

          'xAxis': {
            
            'type': 'category',
             'data': months,
             'axisLabel': { 'rotate': 30 },
             'textStyle':{'color':'black'},
             'axisLine': {
                'lineStyle': {
                  'color': 'black'
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
              'label':{'show':True, 'borderColor':"blue", 'borderType' : 'dotted','position':'insideTopRight', 'distance' : 8,'fontSize':18,'color':'black','fontWeight':'bold','fontFamily':'monospace'},
              'universalTransition':{"enabled":True},
              'labelLine':{"show":True}
              
            }
          ]
        }
         with st.container():
            st_echarts(options=option,height="300px")
        with col2:
         

         option = {'backgroundColor':'white',
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
                  'color': 'black',
                  'width': 2
                }
              },
              
              
              'axisLabel': {'show':True,
                'color': 'black',
                'distance': 15,
                'fontSize': 11
              },
              'startAngle':190,
              'endAngle':-10,
              'min':300,
              'max':900,
              'splitNumber':4,
              'radius':'90%',
              'detail': {
                'formatter': value,
                'color': 'black'
              },
               
              
              'legend':{"animationDurationUpdate":2000},
              'data': [
                {
                  'value':value,
                  'title': {'show':True,'color':'black'},
                  "name": 'SCORE',
                  'itemStyle':{'color':'black','borderColor':'black'},
                   "textStyle":{ 'fontWeight' : 'lighter'}

                }
              ]
            }
          ]
        }
         with st.container():
            st_echarts(options=option,height="300px")

        colors=['red','#FFCE30','green','white']

        col1,col2,col4,col6=st.columns(4,gap="large")
        with col1:
          with st.container():
            # st.write("#Enq L12M UnSec:")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">#Enq L12M UnSec</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
              <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{Enq_L12M_UnSec} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)

        with col2:
          with st.container():
            # st.write("Month since last npa")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">Mnths since lst NPA</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
              <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{Months_since_last_npa} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)

        with col4:
          with st.container():
            # st.write("Avg gap b/w two loans:")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">Avg gap b/w loans</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
              <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{Avg_gap_two_loans} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)

        with col6:
          with st.container():
            # st.write("Total Enq L6M:")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">Total Enq L6M</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
             <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{Total_Enq_L6M} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)
         
        #second row
        col1,col2,col4,col5=st.columns(4,gap="large")
        with col1:
          with st.container():
            # st.write("max cons dpd L12M NPA:")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">DPD L12M NPA</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
              <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{max_consecutive_dpd_L12M_NPA} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)
        with col2:
          with st.container():
            # st.write("POS left:")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">POS left</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
              <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{POS_left} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)

        with col4:
          with st.container():
            # st.write("POS in 90DPD:")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">POS in 90DPD</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
              <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{POS_in_90DPD} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)

        with col5:
          with st.container():
            # st.write("Utilization on CC:")
            rishu="""
    <h1 style="color:black;text-align:center;font-size:100%;font-family:times;">Utilization on CC</h1>
    """
            st.write(rishu,unsafe_allow_html=True)
            html_temp = f"""
              <div style="background-color:{colors[3]};padding:4px;border-radius: 25px">
              <h1 style="color:black;text-align:center;font-size:150%;font-family:courier;">{Utilization_on_CC} </h1>
              </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)
        st.markdown("---")     
    else:
        def get_data_from_excel(SheetName):
                df = pd.read_excel(io=r"C:\Users\Sarthak\Downloads\Dashboards\Dashboards\files_updated\files\data_for_BRE.xlsx",engine="openpyxl",sheet_name=SheetName)
                return df


        #creating tabs for Retail and SME:
        selected_option = option_menu(menu_title=None,
                            options=['Retail','SME'],
                            icons=['person-fill','person-fill-gear'],
                            menu_icon='cast',default_index=0,orientation='horizontal',
                            styles={"container":{"padding":"0!important","backgroundcolor":'transparent'},
                                    "icon":{"color":"yellow","font-size":"15px"},
                            "nav-link":{"font-size":"12px",
                                        "text-align":"left",
                                        "margin":"0px",
                                        "--hover-color":"#eee"},
                            "nav-link-selected":{'background-color':"#0197F6"},},)

        if selected_option=='SME':
            #getting data from sheet2 named SME
            df_sme=get_data_from_excel(SheetName='SME')
            user = st.sidebar.selectbox("Select the ID:",options=df_sme['Application ID'].unique())

            df_selection = df_sme[df_sme["Application ID"] == user]
            df_selection.reset_index(inplace=True)

            ##variables-------
            application_id=df_selection['Application ID'][0]
            application_score=df_selection['Application Score'][0]
            Behavioral_Score =df_selection['Behavioral Score'][0]
            DPD_last_6_months =df_selection['DPD last 6 months'][0]
            Enquiries_last_3_months =df_selection['Enquiries last 3 months'][0]
            WriteOff_SuitFiled_Flag =df_selection['WriteOff/SuitFiled Flag'][0]
            Credit_Card_Utilization= round(df_selection['Credit Card Utilization'][0]*100,2)
            Age= df_selection['Age'][0]
            Vintage_in_Months= df_selection['Vintage in Months'][0]
            Missed_Payments=round(df_selection['%Missed Payments'][0],2)
            Outstanding_Amount= (round(df_selection['%Outstanding Amount'][0],2))*100
            CC_OD_Utilization= round((df_selection['CC/OD Utilization'][0])*100,2)
            Banking_to_turnver= round(df_selection['Banking to turnver (BTO)'][0]*100,2)
            GST_to_previous_year_turnover= round(df_selection['GST to previous year turnover'][0]*100,2)
            Debt_service_coverage_ratio= df_selection['Debt service coverage ratio'][0]
            Debt_Equity= df_selection['Debt/Equity'][0]
            EMI_bounces_and_Inward_returns= df_selection['EMI bounces and Inward returns '][0]
            DPD_in_commercial_tradelines= df_selection['DPD in commercial tradelines'][0]
            overdue_and_settlement_in_commercial_cibil= df_selection['overdue and settlement in commercial cibil'][0]
            CMR= df_selection['CMR'][0]
            loans_open_last_6_months=df_selection['loans open last 6 months'][0]

            
            flag=0
            if((Banking_to_turnver>80)&(GST_to_previous_year_turnover>=120)&(Debt_service_coverage_ratio>0.9)&(Debt_Equity<3)&(EMI_bounces_and_Inward_returns<=2)
                &(DPD_in_commercial_tradelines==0)&(overdue_and_settlement_in_commercial_cibil==0)&(CMR<5)&(WriteOff_SuitFiled_Flag==0)):
                status="Approved"
                status_color="green"
            else:
                status="Rejected"
                status_color="red"
            def parameter_check_sme(parameter):
              if (parameter=="Banking_to_turnver") and (eval(parameter)>80):
                return ('Approved','green')
              if (parameter=='GST_to_previous_year_turnover') and (eval(parameter)>=120):
                return ('Approved','green')
              if (parameter=='Debt_service_coverage_ratio') and (eval(parameter)>0.9):
                return ('Approved','green')
              if (parameter=='Debt_Equity') and (eval(parameter)<3):
                return ('Approved','green')
              if (parameter=='EMI_bounces_and_Inward_returns') and (eval(parameter)<=2):
                return ('Approved','green')
              if (parameter=='DPD_in_commercial_tradelines') and (eval(parameter)==0):
                return ('Approved','green')
              if (parameter=='overdue_and_settlement_in_commercial_cibil') and (eval(parameter)==0):
                return ('Approved','green')
              if (parameter=='CMR') and (eval(parameter)<5):
                return ('Approved','green')
              if (parameter=="application_score") and (eval(parameter)>700):
                return ('Approved','green')
              if (parameter=='Behavioral_Score') and (eval(parameter)>700):
                return ('Approved','green')
              if (parameter=='DPD_last_6_months') and (eval(parameter)<=0):
                return ('Approved','green')
              if (parameter=='Enquiries_last_3_months') and (eval(parameter)<3):
                return ('Approved','green')
              if (parameter=='WriteOff_SuitFiled_Flag') and (eval(parameter)==0):
                return ('Approved','green')
              if (parameter=='Credit_Card_Utilization') and (eval(parameter)<70):
                return ('Approved','green')
              if (parameter=='Vintage_in_Months') and (eval(parameter)>=6):
                return ('Approved','green')
              if (parameter=='Missed_Payments') and (eval(parameter)<=10):
                return ('Approved','green')
              if (parameter=='Outstanding_Amount') and (eval(parameter)<=70):
                return ('Approved','green')
              if (parameter=="loans_open_last_6_months") and (eval(parameter)<=3):
                return ('Approved','green')
              return ('Rejected','red')
             
            counter="Approved"

            html_func=f'''
                        <head>
                        
                        <title>Page Title</title>
                        </head>
                        <body>
                        <div style="background: white; color: black;">
                        <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
                        
                        <tr>
                        <th colspan="5" >Loan Status:  <font size=5 color={status_color}>{status}</font></th>
                        </tr>
                        <tr>
                        <td>Application ID</td>
                        <td>{application_id}</td>
                        <td>-----</td></tr>
                        
                        <tr>
                        <td>Banking to turnover</td>
                        <td>{Banking_to_turnver}%</td>
                        <td><font color='{parameter_check_sme("Banking_to_turnver")[1]}'>{parameter_check_sme("Banking_to_turnver")[0]}</font></td></tr>

                        <tr>
                        <td>GST to previous year turnover</td>
                        <td>{GST_to_previous_year_turnover}%</td>
                        <td><font color='{parameter_check_sme("GST_to_previous_year_turnover")[1]}'>{parameter_check_sme("GST_to_previous_year_turnover")[0]}</font></td></tr>
                        
                        <tr>
                        <td>Debt Service Coverage Ratio</td>
                        <td>{Debt_service_coverage_ratio}</td>
                        <td><font color='{parameter_check_sme("Debt_service_coverage_ratio")[1]}'>{parameter_check_sme("Debt_service_coverage_ratio")[0]}</font></td></tr>

                        <tr>
                        <td>Debt/Equity</td>
                        <td>{Debt_Equity}</td>
                        <td><font color='{parameter_check_sme("Debt_Equity")[1]}'>{parameter_check_sme("Debt_Equity")[0]}</font></td></tr>
                        
                        <tr>
                        <td>EMI bounces and Inward returns</td>
                        <td>{EMI_bounces_and_Inward_returns}</td>
                        <td><font color='{parameter_check_sme("EMI_bounces_and_Inward_returns")[1]}'>{parameter_check_sme("EMI_bounces_and_Inward_returns")[0]}</font></td></tr>

                        <tr>
                        <td>DPD in commercial tradelines</td>
                        <td>{DPD_in_commercial_tradelines}</td>
                        <td><font color='{parameter_check_sme("DPD_in_commercial_tradelines")[1]}'>{parameter_check_sme("DPD_in_commercial_tradelines")[0]}</font></td></tr>
                        
                        <tr>
                        <td>Overdue and settlement in commercial cibil</td>
                        <td>{overdue_and_settlement_in_commercial_cibil}</td>
                        <td><font color='{parameter_check_sme("overdue_and_settlement_in_commercial_cibil")[1]}'>{parameter_check_sme("overdue_and_settlement_in_commercial_cibil")[0]}</font></td></tr>

                        <tr>
                        <td>WriteOff SuitFiled</td>
                        <td>{WriteOff_SuitFiled_Flag}</td>
                        <td><font color='{parameter_check_sme("WriteOff_SuitFiled_Flag")[1]}'>{parameter_check_sme("WriteOff_SuitFiled_Flag")[0]}</font></td></tr>
                        
                        <tr>
                        <td>CMR Score</td>
                        <td>{CMR}</td>
                        <td><font color='{parameter_check_sme("CMR")[1]}'>{parameter_check_sme("CMR")[0]}</font></td></tr>
                        
                        </table>
                        </div>
                        </body>
                        '''
            st.markdown(html_func,unsafe_allow_html=True)
            
        else:
            
            #getting data from sheet2 named Retail
            df_retail=get_data_from_excel(SheetName='Retail')
            user = st.sidebar.selectbox("Select the ID:",options=df_retail['Application ID'].unique())
            df_selection = df_retail[df_retail["Application ID"] == user]
            df_selection.reset_index(inplace=True)
            #variables-------
            application_id=df_selection['Application ID'][0]
            application_score=df_selection['Application Score'][0]
            Behavioral_Score =df_selection['Behavioral Score'][0]
            DPD_last_6_months =df_selection['DPD last 6 months'][0]
            Enquiries_last_3_months =df_selection['Enquiries last 3 months'][0]
            WriteOff_SuitFiled_Flag =df_selection['WriteOff/SuitFiled Flag'][0]
            Credit_Card_Utilization= round(df_selection['Credit Card Utilization'][0]*100,2)
            Age= df_selection['Age'][0]
            Vintage_in_Months= df_selection['Vintage in Months'][0]
            Missed_Payments= df_selection['%Missed Payments'][0]
            loans_open_last_6_months=df_selection['loans open last 6 months'][0]
            Outstanding_Amount= (round(df_selection['%Outstanding Amount'][0],2))*100
            
            counter="Approved"
            
            #if((application_score>700)&(Behavioral_Score>700)):
            # parameter should be a string
            def parameter_check_retail(parameter):
              if (parameter=="application_score") and (eval(parameter)>700):
                return ('Approved','green')
              if (parameter=='Behavioral_Score') and (eval(parameter)>700):
                return ('Approved','green')
              if (parameter=='DPD_last_6_months') and (eval(parameter)<=0):
                return ('Approved','green')
              if (parameter=='Enquiries_last_3_months') and (eval(parameter)<3):
                return ('Approved','green')
              if (parameter=='WriteOff_SuitFiled_Flag') and (eval(parameter)==0):
                return ('Approved','green')
              if (parameter=='Credit_Card_Utilization') and (eval(parameter)<70):
                return ('Approved','green')
              if (parameter=='Vintage_in_Months') and (eval(parameter)>=6):
                return ('Approved','green')
              if (parameter=='Missed_Payments') and (eval(parameter)<=10):
                return ('Approved','green')
              if (parameter=='Outstanding_Amount') and (eval(parameter)<=70):
                return ('Approved','green')
              if (parameter=="loans_open_last_6_months") and (eval(parameter)<=3):
                return ('Approved','green')
              if (parameter=="Age") and (eval(parameter)>=18):
                return ('Approved','green')
              return ('Rejected','red')
            if((Age>18) & (application_score>700) &(Behavioral_Score>700) &(Credit_Card_Utilization<70) & (WriteOff_SuitFiled_Flag==0) &(Enquiries_last_3_months<3) & (DPD_last_6_months<=0)):
                status="Approved"
                status_color='green'
            else:
                status="Rejected"
                status_color='red'

            html_func=f'''
                        <head>
                        
                        <title>Page Title</title>
                        </head>
                        <body>
                        <div style="background: white; color: black;">
                        <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
                        
                        <tr>
                        <th colspan="5" >Loan Status:  <font size=5 color='{status_color}'>{status}</font></th>
                        </tr>
                        
                        <td>Application ID</td>
                        <td>{application_id}</td>
                        <td>-----</td></tr>
                        
                        <td>Age</td>
                        <td> {Age}</td>
                        <td><font color='{parameter_check_retail("Age")[1]}'>{parameter_check_retail("Age")[0]}</font></td></tr>

                        <tr>
                        <td>Application Score</td>
                        <td>{application_score}</td>
                        <td><font color='{parameter_check_retail("application_score")[1]}'>{parameter_check_retail("application_score")[0]}</font></td></tr>
                        
                        <tr>
                        <td>Behavioral Score</td>
                        <td>{Behavioral_Score}</td>
                        <td><font color='{parameter_check_retail("Behavioral_Score")[1]}'>{parameter_check_retail("Behavioral_Score")[0]}</font></td></tr>

                        <tr>
                        <td>Credit Card Utilization</td>
                        <td>{Credit_Card_Utilization}</td>
                        <td><font color='{parameter_check_retail("Credit_Card_Utilization")[1]}'>{parameter_check_retail("Credit_Card_Utilization")[0]}</font></td></tr>
                        
                        <tr>
                        <td>WriteOff SuitFiled Flag</td>
                        <td>{WriteOff_SuitFiled_Flag}</td>
                        <td><font color='{parameter_check_retail("WriteOff_SuitFiled_Flag")[1]}'>{parameter_check_retail("WriteOff_SuitFiled_Flag")[0]}</font></td></tr>
 
                        <tr>
                        <td>Enquiries last 3M</td>
                        <td>{Enquiries_last_3_months}</td>
                        <td><font color='{parameter_check_retail("Enquiries_last_3_months")[1]}'>{parameter_check_retail("Enquiries_last_3_months")[0]}</font></td></tr>
                        
                        <tr>
                        <td>DPD last 6M</td>
                        <td>{DPD_last_6_months}</td>
                        <td><font color='{parameter_check_retail("DPD_last_6_months")[1]}'>{parameter_check_retail("DPD_last_6_months")[0]}</font></td></tr>
                   
                        
                        
          
                        </table>
                        </div>
                        </body>
                        '''
            st.markdown(html_func,unsafe_allow_html=True)

    # elif(dashboard=='BRE-SME'):

    #     #getting data from sheet2 named SME
    #     df_sme=get_data_from_excel(SheetName='SME')
    #     user = st.sidebar.selectbox("Select the ID:",options=df_sme['Application ID'].unique())

    #     df_selection = df_sme[df_sme["Application ID"] == user]
    #     df_selection.reset_index(inplace=True)
    #     ##variables-------
    #     application_id=df_selection['Application ID'][0]
    #     application_score=df_selection['Application Score'][0]
    #     Behavioral_Score =df_selection['Behavioral Score'][0]
    #     DPD_last_6_months =df_selection['DPD last 6 months'][0]
    #     Enquiries_last_3_months =df_selection['Enquiries last 3 months'][0]
    #     WriteOff_SuitFiled_Flag =df_selection['WriteOff/SuitFiled Flag'][0]
    #     Credit_Card_Utilization=round(df_selection['Credit Card Utilization'][0],2)
    #     #Credit_Card_Utilization= round(float(df_selection['Credit Card Utilization'][0]),2)
    #     Age= df_selection['Age'][0]
    #     Vintage_in_Months= df_selection['Vintage in Months'][0]
    #     Missed_Payments= round(df_selection['%Missed Payments'][0]*100,2)
    #     st.write(Credit_Card_Utilization)
    #     Outstanding_Amount= (round(df_selection['%Outstanding Amount'][0],2))*100
    #     CC_OD_Utilization= round((df_selection['CC/OD Utilization'][0])*100,2)
    #     Banking_to_turnver= df_selection['Banking to turnver (BTO)'][0]
    #     GST_to_previous_year_turnover= df_selection['GST to previous year turnover'][0]
    #     Debt_service_coverage_ratio= df_selection['Debt service coverage ratio'][0]
    #     Debt_Equity= df_selection['Debt/Equity'][0]
    #     EMI_bounces_and_Inward_returns= df_selection['EMI bounces and Inward returns '][0]
    #     DPD_in_commercial_tradelines= df_selection['DPD in commercial tradelines'][0]
    #     overdue_and_settlement_in_commercial_cibil= df_selection['overdue and settlement in commercial cibil'][0]
    #     CMR= df_selection['CMR'][0]

    #     html_func_SME=f'''
    #                 <head>
                    
    #                 <title>Page Title</title>
    #                 </head>
    #                 <body>
    #                 <div style="background: white; color: black;">
    #                 <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
                    
    #                 <tr>
    #                 <th colspan="5" >BRE</th>
    #                 </tr>
    #                 <tr>
    #                 <td>Application ID</td>
    #                 <td>{application_id}</td></tr>

    #                 <tr>
    #                 <td>Application Score</td>
    #                 <td>{application_score}</td></tr>
                    
    #                 <tr>
    #                 <td>Behavioral Score</td>
    #                 <td><a>{Behavioral_Score}</a></td></tr>
                    
                    
    #                 <tr>
    #                 <td>DPD last 6M</td>
    #                 <td><a>{DPD_last_6_months}</a></td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Enquiries last 3M</td>
    #                 <td>{Enquiries_last_3_months}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>WriteOff SuitFiled Flag</td>
    #                 <td>{WriteOff_SuitFiled_Flag}</td>
                    
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Credit Card Utilization</td>
    #                 <td>{Credit_Card_Utilization}</td></tr>
                    
    #                 <tr>
    #                 <td>Age</td>
    #                 <td> {Age}</td></tr>
                    
    #                 <tr>
    #                 <td>Vintage(in Months)</td>
    #                 <td>{Vintage_in_Months}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Missed Payments</td>
    #                 <td> {Missed_Payments}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Outstanding Amount</td>
    #                 <td> {Outstanding_Amount}%</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>CC/OD Utilization</td>
    #                 <td> {CC_OD_Utilization}%</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Banking to turnver</td>
    #                 <td>{Banking_to_turnver}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>GST to previous year turnover</td>
    #                 <td>{GST_to_previous_year_turnover}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Debt service coverage ratio</td>
    #                 <td>{Debt_service_coverage_ratio}</td>
    #                 </tr>

    #                 <tr>
    #                 <td>Debt Equity</td>
    #                 <td>{Debt_Equity}</td></tr>

    #                 <tr>
    #                 <td>EMI bounces and Inward returns</td>
    #                 <td>{EMI_bounces_and_Inward_returns}</td></tr>

    #                 <tr>
    #                 <td>DPD in commercial tradelines</td>
    #                 <td>{DPD_in_commercial_tradelines}</td></tr>

    #                 <tr>
    #                 <td>overdue and settlement in commercial cibil</td>
    #                 <td>{overdue_and_settlement_in_commercial_cibil}</td></tr>

    #                 <tr>
    #                 <td>CMR</td>
    #                 <td>{CMR}</td></tr>
                    
    #                 </table>
    #                 </div>
    #                 </body>
    #                 '''
    #     st.markdown(html_func_SME,unsafe_allow_html=True)
        
    # else:
    #     Approved_flag=0
    #     #getting data from sheet2 named Retail
    #     df_retail=get_data_from_excel(SheetName='Retail')
    #     user = st.sidebar.selectbox("Select the ID:",options=df_retail['Application ID'].unique())
    #     df_selection = df_retail[df_retail["Application ID"] == user]
    #     df_selection.reset_index(inplace=True)
    #     #variables-------
    #     application_id=df_selection['Application ID'][0]
    #     application_score=df_selection['Application Score'][0]
    #     if(application_score>700):
    #     Behavioral_Score =df_selection['Behavioral Score'][0]
    #     DPD_last_6_months =df_selection['DPD last 6 months'][0]
    #     Enquiries_last_3_months =df_selection['Enquiries last 3 months'][0]
    #     WriteOff_SuitFiled_Flag =df_selection['WriteOff/SuitFiled Flag'][0]
    #     Credit_Card_Utilization= round(df_selection['Credit Card Utilization'][0],2)
    #     Age= df_selection['Age'][0]
    #     Vintage_in_Months= df_selection['Vintage in Months'][0]
    #     Missed_Payments= round(df_selection['%Missed Payments'][0],2)
    #     Outstanding_Amount= (round(df_selection['%Outstanding Amount'][0],2))*100

    #     html_func_retail=f'''
    #                 <head>
                    
    #                 <title>Page Title</title>
    #                 </head>
    #                 <body>
    #                 <div style="background: white; color: black;">
    #                 <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
                    
    #                 <tr>
    #                 <th colspan="5" >BRE</th>
    #                 </tr>
    #                 <tr>
    #                 <td>Application ID</td>
    #                 <td>{application_id}</td></tr>

    #                 <tr>
    #                 <td>Application Score</td>
    #                 <td>{application_score}</td></tr>
                    
    #                 <tr>
    #                 <td>Behavioral Score</td>
    #                 <td><a>{Behavioral_Score}</a></td></tr>
                    
                    
    #                 <tr>
    #                 <td>DPD last 6M</td>
    #                 <td><a>{DPD_last_6_months}</a></td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Enquiries last 3M</td>
    #                 <td>{Enquiries_last_3_months}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>WriteOff SuitFiled Flag</td>
    #                 <td>{WriteOff_SuitFiled_Flag}</td>
                    
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Credit Card Utilization</td>
    #                 <td>{Credit_Card_Utilization}</td></tr>
                    
    #                 <tr>
    #                 <td>Age</td>
    #                 <td> {Age}</td></tr>
                    
    #                 <tr>
    #                 <td>Vintage(in Months)</td>
    #                 <td>{Vintage_in_Months}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Missed Payments</td>
    #                 <td> {Missed_Payments}</td>
    #                 </tr>
                    
    #                 <tr>
    #                 <td>Percentage of Outstanding Amount</td>
    #                 <td> {Outstanding_Amount}%</td>
    #                 </tr>
                    
      
    #                 </table>
    #                 </div>
    #                 </body>
    #                 '''
    #     st.markdown(html_func_retail,unsafe_allow_html=True)
    # <tr>
    # <td>Application Score</td>
    # <td>{application_score}</td>
    # <td><font color='{parameter_check_sme("application_score")[1]}'>{parameter_check_sme("application_score")[0]}</font></td></tr>
    
    # <tr>
    # <td>Behavioral Score</td>
    # <td><a>{Behavioral_Score}</a></td>
    # <td><font color='{parameter_check_sme("Behavioral_Score")[1]}'>{parameter_check_sme("Behavioral_Score")[0]}</font></td></tr>
    
    
    # <tr>
    # <td>DPD last 6M</td>
    # <td><a>{DPD_last_6_months}</a></td>
    # <td><font color='{parameter_check_sme("DPD_last_6_months")[1]}'>{parameter_check_sme("DPD_last_6_months")[0]}</font></td></tr>
    
    # <tr>
    # <td>Enquiries last 3M</td>
    # <td>{Enquiries_last_3_months}</td>
    # <td><font color='{parameter_check_sme("Enquiries_last_3_months")[1]}'>{parameter_check_sme("Enquiries_last_3_months")[0]}</font></td></tr>
    
    # <tr>
    # <td>WriteOff SuitFiled Flag</td>
    # <td>{WriteOff_SuitFiled_Flag}</td>
    # <td><font color='{parameter_check_sme("WriteOff_SuitFiled_Flag")[1]}'>{parameter_check_sme("WriteOff_SuitFiled_Flag")[0]}</font></td></tr>
    
    # <tr>
    # <td>Credit Card Utilization</td>
    # <td>{Credit_Card_Utilization}</td>
    # <td><font color='{parameter_check_sme("Credit_Card_Utilization")[1]}'>{parameter_check_sme("Credit_Card_Utilization")[0]}</font></td></tr>
    
    # <tr>
    # <td>Age</td>
    # <td> {Age}</td>
    # <td>-----</td></tr>
    
    # <tr>
    # <td>Vintage(in Months)</td>
    # <td>{Vintage_in_Months}</td>
    # <td><font color='{parameter_check_sme("Vintage_in_Months")[1]}'>{parameter_check_sme("Vintage_in_Months")[0]}</font></td></tr>
    
    # <tr>
    # <td>Missed Payments</td>
    # <td> {Missed_Payments}</td>
    # <td><font color='{parameter_check_sme("Missed_Payments")[1]}'>{parameter_check_sme("Missed_Payments")[0]}</font></td></tr>
    
    # <tr>
    # <td>Outstanding Amount</td>
    # <td> {Outstanding_Amount}%</td>
    # <td><font color='{parameter_check_sme("Outstanding_Amount")[1]}'>{parameter_check_sme("Outstanding_Amount")[0]}</font></td></tr>
    
    # <tr>
    # <td>CC/OD Utilization</td>
    # <td> {CC_OD_Utilization}%</td>
    # <td>-----</td></tr>
    
    
    # <tr>
    # <td>DPD in commercial tradelines</td>
    # <td>{DPD_in_commercial_tradelines}</td>
    # <td><font color='{parameter_check_sme("DPD_in_commercial_tradelines")[1]}'>{parameter_check_sme("DPD_in_commercial_tradelines")[0]}</font></td></tr>


    # <tr>
    # <td>overdue and settlement in commercial cibil</td>
    # <td>{overdue_and_settlement_in_commercial_cibil}</td>
    # <td><font color='{parameter_check_sme("overdue_and_settlement_in_commercial_cibil")[1]}'>{parameter_check_sme("overdue_and_settlement_in_commercial_cibil")[0]}</font></td></tr>


    # <tr>
    # <td>CMR</td>
    # <td>{CMR}</td>
    # <td><font color='{parameter_check_sme("CMR")[1]}'>{parameter_check_sme("CMR")[0]}</font></td></tr>
    # <tr>
    # <td>Enquiries last 3M</td>
    # <td>{Enquiries_last_3_months}</td>
    # <td><font color='{parameter_check_retail("Enquiries_last_3_months")[1]}'>{parameter_check_retail("Enquiries_last_3_months")[0]}</font></td></tr>
    
    # <tr>
    # <td>Age</td>
    # <td> {Age}</td>
    # <td>-----</td></tr>
    
    # <tr>
    # <td>Vintage(in Months)</td>
    # <td>{Vintage_in_Months}</td>
    # <td><font color='{parameter_check_retail("Vintage_in_Months")[1]}'>{parameter_check_retail("Vintage_in_Months")[0]}</font></td></tr>

    
    # <tr>
    # <td>Missed Payments</td>
    # <td> {Missed_Payments}</td>
    # <td><font color='{parameter_check_retail("Missed_Payments")[1]}'>{parameter_check_retail("Missed_Payments")[0]}</font></td></tr>

    
    # <tr>
    # <td>Loans opened in last 6 months</td>
    # <td> {loans_open_last_6_months}</td>
    # <td><font color='{parameter_check_retail("loans_open_last_6_months")[1]}'>{parameter_check_retail("loans_open_last_6_months")[0]}</font></td></tr>

    
    # <tr>
    # <td>Outstanding Amount</td>
    # <td> {Outstanding_Amount}%</td>
    # <td><font color='{parameter_check_retail("Outstanding_Amount")[1]}'>{parameter_check_retail("Outstanding_Amount")[0]}</font></td></tr>
