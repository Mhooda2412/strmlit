# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:46:18 2023

@author: Amani Reddy
"""
import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np 

@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(io="C:/Users/Amani Reddy/Cross_sell/files/cross_sell_Upsell.xlsx",engine="openpyxl")
    return df
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

df=get_data_from_excel()

st.sidebar.header("Please Select the UserID:")
user = st.sidebar.selectbox("Select the ID:",options=df['LoanId'].unique())

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
IRR	= df_selection['IRR'][0]
TopUp_Amount = df_selection['TopUp_Amount'][0]

table_2=f'''
        <head>
        
        <title>Page Title</title>
        </head>
        
        <body>
        
        <body bgcolor="transparent">
        <table border="1" cellpadding="5" cellspacing="1" align="left" color='white'>
        
        <tr>
        <th style="color: #0197F6">Dimensions</th>
        <th style="color: #0197F6">Variable</th>
        <th style="color: #0197F6">Value</th>
        </tr>
        
        <tr style="color: #0197F6">
        <th rowspan="4">Risk Profile</th>
        <td  style="color: white">A_Score Score</td>
        <td  style="color: white">{A_Score}</td>
        </tr>
        
        <tr>
        <td  style="color: white">Bureau_Score</td>
        <td  style="color: white">{Bureau_Score}</td>
        </tr>
        
        <tr>
        <td style="color: white">Cross_Sell_Score</td>
        <td style="color: white">{Cross_Sell_Score}</td></tr>
        
        <tr>
        <td style="color: white">Upsell_Score</td>
        <td style="color: white">{Upsell_Score}</td></tr>
        
        <tr style="color: #0197F6">
        <th rowspan="4">Offer</th>
        <td  style="color: white">Next_best_product</td>
        <td  style="color: white">{Next_best_product}</td></tr>
        
        <tr>
        <td  style="color: white">Maximum Limit</td>
        <td  style="color: white">{Maximum_Limit}</td></tr>
        
        <tr>
        <td  style="color: white">IRR</td>
        <td  style="color: white">{IRR}</td>
        </tr>
        
        <tr>
        <td style="color: white">TopUp_Amount</td>
        <td style="color: white">{TopUp_Amount}</td>
        </tr>
        
        </table>
        </body>
        </html>
        '''
st.markdown(table_2,unsafe_allow_html=True)
