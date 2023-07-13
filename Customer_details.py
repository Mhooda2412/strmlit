# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:06:01 2023

@author: Amani Reddy
"""

import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np 
def customer_details():
    @st.cache_data
    def get_data_from_excel():
        df = pd.read_excel(io="C:/Users/Amani Reddy/Dashboards/files/cross_sell_Upsell.xlsx",engine="openpyxl")
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
    
    ##variables-------
    
    loan_id=df_selection['LoanId'][0]
    Name=df_selection['Name'][0]
    Mobile =df_selection['Mobile'][0]
    Loan_Type =df_selection['Current_Loan_type'][0]
    Loan_Amount	=df_selection['Loan_Amount'][0]
    max_dpd_in_last_3m_OnUs =df_selection['max_dpd_in_last_3m_OnUs'][0]
    Outstanding_Amount	=df_selection['Outstanding_Amount'][0]
    
    
    html_func=f'''
            <head>
            
            <title>Page Title</title>
            </head>
            
            <body>
            
            <body bgcolor="transparent">
            <table border="0" cellpadding="5" cellspacing="1" align="LEFT" color='black'>
            
            <tr>
            <th rowspan="3" bgcolor='transparent'><font color='0197F6'>Borrower Details</font></th>
            <td bgcolor='transparent'>Selected Loan ID</td>
            <td >{loan_id}</td>
            </tr>
            
            <tr>
            <td>Name</td>
            <td>{Name}</td></tr>
            
            <tr>
            <td>Mobile</td>
            <td>{Mobile}</td></tr>
            
            <tr>
            <th rowspan="4"><font color='0197F6'>Current Product</font></th>
            <td>Loan_type</td>
            <td>{Loan_Type}</td></tr>
            
            <tr>
            <td>Loan_Amount</td>
            <td>{Loan_Amount}</td></tr>
            
            <tr>
            <td>max_dpd_in_last_3m_OnUs</td>
            <td>{max_dpd_in_last_3m_OnUs}</td>
            </tr>
            
            <tr>
            <td>Outstanding_Amount</td>
            <td>{Outstanding_Amount}</td>
            </tr>
            
            </table>
            </body>
    
            '''
    st.markdown(html_func,unsafe_allow_html=True)
