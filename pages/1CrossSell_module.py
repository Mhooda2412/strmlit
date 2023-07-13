# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:44:42 2023

@author: Amani Reddy
"""

import streamlit as st
import pandas as pd  
import numpy as np 
import base64
from streamlit_option_menu import option_menu
from streamlit_echarts import st_echarts

st.set_page_config(page_title="CrossSell", layout="wide")

#selected_option=st.selectbox("",options=['Borrower Information','Offered Product Detail'],label_visibility='collapsed')
selected_option = option_menu(menu_title=None,
                    options=['Cross sell Summary','Upsell Summary','Borrower Information','Offered Product Detail'],
                    icons=['person-fill','person-fill-up'],
                    menu_icon='cast',default_index=0,orientation='horizontal',
                    styles={"container":{"padding":"0!important","backgroundcolor":'transparent'},
                            "icon":{"color":"orange","font-size":"20px"},
                    "nav-link":{"font-size":"20px",
                                "text-align":"left",
                                "margin":"0px",
                                "--hover-color":"#eee"},
                    "nav-link-selected":{'background-color':"#0197F6"},},)
def get_data_from_excel():
        df = pd.read_excel(io=r"C:\Users\Sarthak\Downloads\Dashboards\Dashboards\files_updated\files\cross_sell_Upsell (2).xlsx",engine="openpyxl")
        return df
    
page_bg_img=f'''
<style>
    [data-testid='stAppViewContainer']{{
    background: linear-gradient(to right, #4A00E0, #8E2DE2);
    background-position: center;
    }}
</style>'''

df=get_data_from_excel()
st.sidebar.header("Please Select the UserID:")
user = st.sidebar.selectbox("Select the ID:",options=df['LoanId'].unique())

if selected_option=='Borrower Information':

    st.markdown(page_bg_img, unsafe_allow_html=True)

    df=get_data_from_excel()
    
    df_selection = df.query("LoanId == @user")   
    df_selection.reset_index(inplace=True)
    data_selection=df.query("LoanId == @user")
    #key=st.session_state['key']

    ##variables-------

    loan_id=df_selection['LoanId'][0]
    Name=df_selection['Name'][0]
    Mobile =df_selection['Mobile'][0]
    Loan_Type =df_selection['Current_Loan_type'][0]
    Loan_Amount	=df_selection['Loan_Amount'][0]
    max_dpd_in_last_3m_OnUs =df_selection['max_dpd_in_last_3m_OnUs'][0]
    Outstanding_Amount	=df_selection['Outstanding_Amount'][0]

    st.write("hloo")
    html_func=f'''
            <head>
            
            <title>Page Title</title>
            </head>
            
            <body>
            
            <body>
            <div style="background: white; color: black;">
            <table width=100%" bordercolor="black" border="2" cellpadding="30" cellspacing="5" align="Center">
            
            
            <tr>
            <th rowspan="3"><font color='black'>Borrower Details</font></th>
            <td>Loan ID</td>
            <td >{loan_id}</td>
            </tr>
            
            <tr>
            <td>Name</td>
            <td>{Name}</td></tr>
            
            <tr>
            <td>Mobile</td>
            <td><a href="tel:{Mobile}">{Mobile}</a></td></tr>
            
            <tr>
            <th rowspan="4"><font color='black'>Current Product</font></th>
            <td>Loan Type</td>
            <td>{Loan_Type}</td></tr>
            
            <tr>
            <td>Loan Amount</td>
            <td>INR {Loan_Amount}</td></tr>
            
            <tr>
            <td>DPD in last 3m on-us</td>
            <td>{max_dpd_in_last_3m_OnUs}</td>
            </tr>
            
            <tr>
            <td>Outstanding Amount</td>
            <td>INR {Outstanding_Amount}</td>
            </tr>
            
            </table>
            </div>
            </body>
            </html>

            '''
    st.markdown(html_func,unsafe_allow_html=True)

elif(selected_option=='Offered Product Detail'):
    
    st.markdown(page_bg_img, unsafe_allow_html=True)

    df=get_data_from_excel()

    df_selection = df.query("LoanId == @user")   
    df_selection.reset_index(inplace=True)
    data_selection=df.query("LoanId == @user")
    #key=st.session_state['key']

    ##data----
    A_Score = df_selection['A_Score'][0]
    Bureau_Score = df_selection['Bureau_Score'][0]
    Cross_Sell_Score = df_selection['Cross_Sell_Score'][0]
    Upsell_Score = df_selection['Upsell_Score'][0]
    Next_best_product = df_selection['Next_best_product'][0]
    Maximum_Limit	= df_selection['Maximum Limit'][0]
    IRR_crossell= str(round(df_selection['IRR_crossell'][0]*100,2))+"%"
    IRR_upsell= str(round(df_selection['IRR_upsell'][0]*100,2))+"%"
    tenure_crossell=df_selection['tenure_crossell'][0]
    tenure_upsell=df_selection['tenure_upsell'][0]
    TopUp_Amount = df_selection['TopUp_Amount'][0]

    table_2=f'''
            <head>
            
            <title>Page Title</title>
            </head>
            
            <body>
            
            <body bgcolor="white">
            <div style="background: white; color: black;">
            <table width=100%" bordercolor="black" border="2" cellpadding="30" cellspacing="5" align="Center">
            
            <tr>
            <th style="color: black">Dimensions</th>
            <th style="color: black">Variable</th>
            <th style="color: black">Value</th>
            </tr>
            
            <tr style="color:black">
            <th rowspan="7">Cross-sell</th>
            <td  style="color: black">A Score</td>
            <td  style="color: black">{A_Score}</td>
            </tr>
            
            <tr>
            <td  style="color: black">Bureau Score</td>
            <td  style="color: black">{Bureau_Score}</td>
            </tr>
            
            <tr>
            <td style="color: black">Cross-sell Score</td>
            <td style="color: black">{Cross_Sell_Score}</td></tr>
            
            <tr>
            <td style="color: black">Next Best Product</td>
            <td style="color: black">{Next_best_product}</td></tr>
            
            <tr>
            <td  style="color: black">Eligible Limit</td>
            <td  style="color: black">INR {Maximum_Limit}</td></tr>
            
            <tr>
            <td  style="color: black">IRR</td>
            <td  style="color: black">{IRR_crossell}</td>
            </tr>
            
            <tr>
            <td  style="color: black">Tenure(in months)</td>
            <td  style="color: black">{tenure_crossell}</td>
            </tr>
            
            
            <tr style="color: black">
            <th rowspan="4">Upsell</th>
            <td  style="color: black">Upsell Score</td>
            <td  style="color: black">{Upsell_Score}</td></tr>

            <tr>
            <td style="color: black">TopUp Amount</td>
            <td style="color: black">INR {TopUp_Amount}</td>
            </tr>
            
            <tr>
            <td  style="color: black">IRR</td>
            <td  style="color: black">{IRR_upsell}</td>
            </tr>
            
            <tr>
            <td  style="color: black">Tenure(in months)</td>
            <td  style="color: black">{tenure_upsell}</td>
            </tr>
            
            </table>
            </div>
            </body>
            </html>
            '''
    st.markdown(table_2,unsafe_allow_html=True)
elif(selected_option=='Cross sell Summary'):
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    Next_best_products=df["Next_best_product"].unique().tolist()
    count_of_customers=[]
    amounts=[]
    for i in Next_best_products:
        Number_of_Customers=df[df['Next_best_product']==i]['LoanId'].count()
        count_of_customers.append(int(Number_of_Customers))
        # st.write(percentages)
        amount=round((df[df['Next_best_product']==i]['Maximum Limit'].sum())/10000000,2)
        amounts.append(float(amount))

    result = []
    amounts=[40.23,29.27,25.97]
    count_of_customers=[12262,10464,8328]
    for i in range(len(Next_best_products)):
        dictionary = {"value": int(count_of_customers[i])+120,"itemStyle": {"borderWidth": 4,
                                        "borderColor": '#63c5da',
                                        "color": 'white'},"label": {"show": True,
                                                                "position": 'inside',
                                                                "formatter":str(amounts[i])+str(' Cr')}}
        result.append(dictionary)
        
    summary = {"title": {
        "text": 'Cross Sell Summary',
        "textStyle":{"color":'white'}},
        "tooltip": {
          "trigger": 'item'
        },
        "backgroundColor": 'white',
        "toolbox": {
          "show": False,
          "feature": {
            "dataView": { "show": False, "readOnly": False },
            "magicType": { "show": False, "type": ['line', 'bar'] },
            "restore": { "show": False },
            "saveAsImage": { "show": True }
          }
        },
        "legend":{"color":'green','backgroundColor':'white'},
        "grid": { "containLabel": True },
      "xAxis": {
        "type": 'category',
        "data": Next_best_products,
        "axisLabel": {"color":'black',"fontSize": 15}
      },
      "yAxis": {
        "show":False,
        "type": 'value',
      },
      "series": [
        {
         "name":"Potential Disbursal",
          "data":result,
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
         "name":"Number of Customers",
                "data":[12262,10464,6328],
                "type": 'bar',
                "barWidth":80,
                "color":'skyblue',
                "label": {
            "show": True,
            "position": 'inside'}
                
            }
      ]
    }
    st_echarts(options=summary)
else:
    st.markdown(page_bg_img, unsafe_allow_html=True)

    def function():
        return np.random.randint(10000,100000)
    # def sort_func(a,b):
    values=[]

    values.append(df[df['Upsell_Score']>=800]["TopUp_Amount"].sum())
    values.append(df[(df['Upsell_Score']<800) & df['Upsell_Score']<=750]["TopUp_Amount"].sum())
    values.append(df[(df['Upsell_Score']<750) & df['Upsell_Score']<=700]["TopUp_Amount"].sum())
    values.append(df[df['Upsell_Score']<700]["TopUp_Amount"].sum())
    values=[int(value) for value in values]
    #additional
    values=[5.34,4.67,3.23,2.21]
    # st.write(values)
    def create_data_for_pie(columns,values):
       return [{'value':values[i],'name':columns[i]} for i in range(len(columns))]
    r=create_data_for_pie(['>800','750-800','700-750',"<700"],values)
    # st.write(r)
    option = {
      "backgroundColor":"white",
      "title": {
        "text": 'Upsell Score Summary',
        "left": 'center'
      },
      "tooltip": {
        "trigger": 'item'
      },
      "legend": {
        "data":['>800','750-800','700-750',"<700"],
        "orient": 'vertical',
        "left": 'right'
      },
      "series": [
        {
          "name": 'Topup Amount(in Cr)',
          "type": 'pie',
          "radius": '60%',
          "label": {"position": 'inside', "formatter": '{c}Cr', "color":'black',  "fontSize":12},
          "data":sorted(create_data_for_pie(['>800','750-800','700-750',"<700"],values),key=lambda x:x['value']),
          "emphasis": {
            "itemStyle": {
              "shadowBlur": 10,
              "shadowOffsetX": 0,
              "shadowColor": 'rgba(0, 0, 0, 0.5)'
            }
          }
        }
      ]
    }
    st_echarts(options=option)









