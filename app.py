# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:55:03 2023

@author: Amani Reddy
"""

import streamlit as st
import pandas as pd  # pip install pandas openpyxl
import numpy as np 
import base64

@st.cache_data
def get_image_as_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
img=get_image_as_base64("background_pic.jpg")
page_bg_img=f'''
<style>
    [data-testid='stAppViewContainer']{{
    background-image: url('data:image/png;base64,{img}');
    background-position: center;
    }}
</style>'''

user = st.sidebar.selectbox( "Please Select the UserID:",options=['Collection Module','Cross Sell','Portfolio Dashboard'])
if user=='Collection Module':
    selected_option=st.selectbox("",options=['Borrower Profile','Collection Strategy'],label_visibility='collapsed')
    @st.cache_data
    def get_data_from_excel():
            df = pd.read_excel(io="C:/Users/Amani Reddy/Dashboards/files/A_Score_amani.xlsx",engine="openpyxl")
            return df
        
    if selected_option=='Borrower Profile':
        st.write('Borrower Profile is selected')
        st.markdown(page_bg_img, unsafe_allow_html=True)
        df=get_data_from_excel()
        st.sidebar.header("Please Select the UserID:")
        user = st.sidebar.selectbox("Select the ID:",options=df['LoanId'].unique())
        df_selection = df.query("LoanId == @user")   
        df_selection.reset_index(inplace=True)
        data_selection=df.query("LoanId == @user")
        #key=st.session_state['key']
        Loan_type=df_selection['Name'][0]
        textColor='black'
        
        ##variables-------
        loan_id=df_selection['LoanId'][0]
        Name=df_selection['Name'][0]
        Mobile =df_selection['Mobile'][0]
        Address =df_selection['Address'][0]
        Loan_Type =df_selection['Loan_Type'][0]
        Loan_Amount =df_selection['Loan_Amount'][0]
        EMI_Due_Date= df_selection['EMI_Due_Date'][0]
        EMI_Amount  =df_selection['EMI_Amount'][0]
        Overdue_Amount  =df_selection['Overdue_Amount'][0]
        Outstanding_Amount=df_selection['Outstanding_Amount'][0]
        html_func=f'''
                <head>
                
                <title>Page Title</title>
                </head>
                
                <body>
                
                <body bgcolor="transparent">
                <table border="0" cellpadding="5" cellspacing="1" align="LEFT" color='black'>
                
                <tr>
                <th rowspan="4" bgcolor='transparent'><font color='0197F6'>Borrower Details</font></th>
                <td bgcolor='transparent' style="color:yellow">Selected Loan ID</td>
                <td >{loan_id}</td>
                </tr>
                
                <tr>
                <td style="color:yellow">Name</td>
                <td>{Name}</td></tr>
                
                <tr>
                <td style="color:yellow">Mobile</td>
                <td>{Mobile}</td></tr>
                
                <tr>
                <td style="color:yellow">Address</td>
                <td>{Address}</td>
                </tr>
                
                <tr>
                <th rowspan="6"><font color='0197F6'>Loan Details(On-us)</font></th>
                <td>Loan_type</td>
                <td>{Loan_Type}</td></tr>
                
                <tr>
                <td>Loan_Amount</td>
                <td>{Loan_Amount}</td></tr>
                
                <tr>
                <td>EMI_Due_Date</td>
                <td>{EMI_Due_Date}</td>
                </tr>
                
                <tr>
                <td>EMI_Amount</td>
                <td>{EMI_Amount}</td>
                </tr>
                
                <tr>
                <td>Overdue_Amount</td>
                <td>{Overdue_Amount}</td>
                </tr>
                
                <tr>
                <td>Outstanding_Amount</td>
                <td>{Outstanding_Amount}</td>
                </tr>
                
                </table>
                </body>
                '''
        st.markdown(html_func,unsafe_allow_html=True)
    else:
        st.write('Collection Strategy is selected')
    
        st.markdown(page_bg_img, unsafe_allow_html=True)
        df=get_data_from_excel()
        st.sidebar.header("Please Select the UserID:")
        user = st.sidebar.selectbox("Select the ID:",options=df['LoanId'].unique())
        df_selection = df.query("LoanId == @user")   
        df_selection.reset_index(inplace=True)
        data_selection=df.query("LoanId == @user")
        #key=st.session_state['key']
        ##data----
        Collection_Score = df_selection['Collection_Score'][0]
        Collection_Priority = df_selection['Collection_Priority'][0]
        Collection_Action_pre_EMI = df_selection['Collection_Action_pre_EMI'][0]
        Collection_Action_post_EMI = df_selection['Collection_Action_post_EMI'][0]
        Bureau_Score = df_selection['Bureau_Score'][0]
        loans_open_last_6m  = df_selection['loans_open_last_6m'][0]
        last_12m_max_dpd_all_prods  = df_selection['last_12m_max_dpd_all_prods'][0]
        percentage_0dpd_last_12m = round(df_selection['percentage_0dpd_last_12m'][0],2)
        ratio_loans_open_12m_36m = round(df_selection['ratio_loans_open_12m_36m'][0],2)
        highest_loan_amt_with_0dpd  = df_selection['highest_loan_amt_with_0dpd'][0]
        enquiries_L6M = df_selection['enquiries_L6M'][0]
        max_dpd_in_last_3m_OnUs =df_selection['max_dpd_in_last_3m_OnUs'][0]
        last_contacted_date =df_selection['last_contacted_date'][0]
        Calling_despo   =df_selection['Calling_despo'][0]
        last_contacted_number =df_selection['last_contacted_number'][0]
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
                <th style="color: #0197F6">Indicator</th>
                </tr>
                
                <tr style="color: #0197F6">
                <th rowspan="4">Collection Strategy</th>
                <td  style="color: white">Collection Score</td>
                <td  style="color: white">{Collection_Score}</td>
                <td  style="color: white">Good</td>
                </tr>
                
                <tr>
                <td  style="color: white">Collection Priority</td>
                <td  style="color: white">{Collection_Priority}</td>
                <td  style="color: white">Good</td>
                </tr>
                
                <tr>
                <td style="color: white">Action_Pre_EMI</td>
                <td style="color: white">{Collection_Action_pre_EMI}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">Action_Post_EMI</td>
                <td style="color: white">{Collection_Action_post_EMI}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr style="color: #0197F6">
                <th rowspan="7">Off-Us Behaviour</th>
                <td  style="color: white">Bureau Score</td>
                <td  style="color: white">{Bureau_Score}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td  style="color: white">loans_open_last_6m</td>
                <td  style="color: white">{loans_open_last_6m}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td  style="color: white">last_12m_max_dpd_all_prods</td>
                <td  style="color: white">{last_12m_max_dpd_all_prods}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">percentage_0dpd_last_12m</td>
                <td style="color: white">{percentage_0dpd_last_12m}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">ratio_loans_open_12m_36m</td>
                <td style="color: white">{ratio_loans_open_12m_36m}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">highest_loan_amt_with_0dpd</td>
                <td style="color: white">{highest_loan_amt_with_0dpd}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">enquiries_L6M</td>
                <td style="color: white">{enquiries_L6M}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr style="color: #0197F6">
                <th rowspan="4">On-Us Behaviour</th>
                <td style="color: white">Max_dpd_last_3m_OnUs</td>
                <td style="color: white">{max_dpd_in_last_3m_OnUs}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">last_contacted_date</td>
                <td style="color: white">{last_contacted_date}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">Calling_desposition</td>
                <td style="color: white">{Calling_despo}</td>
                <td  style="color: white">Good</td></tr>
                
                <tr>
                <td style="color: white">last_contacted_number</td>
                <td style="color: white">{last_contacted_number}</td>
                <td  style="color: white">----</td></tr>
                
                </table>
                </body>
                </html>
                '''
        st.markdown(table_2,unsafe_allow_html=True)
elif user=='Cross Sell':
    def get_data_from_excel():
        df = pd.read_excel(io="C:/Users/Amani Reddy/Dashboards/files/cross_sell_Upsell.xlsx",engine="openpyxl")
        return df
    selected_option=st.selectbox("",options=['Borrower Information','Offered Product Detail'])
    if selected_option=='Borrower Information':
        st.write('Borrower Information is selected')
    
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

        
    else:
        st.write('Offered Product Detail is selected')
        
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
        IRR	= round(df_selection['IRR'][0],2)
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

