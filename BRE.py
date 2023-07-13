import streamlit as st
import pandas as pd  
import numpy as np 
import base64
from streamlit_option_menu import option_menu
from streamlit_echarts import st_echarts
import datetime
from datetime import datetime


@st.cache_data
def get_data_from_excel(SheetName):
        df = pd.read_excel(io="C:\\Users\\Sajal Omar\\RiskDashboard\\data_for_BRE_rishu.xlsx",engine="openpyxl",sheet_name=SheetName)
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
    Credit_Card_Utilization= df_selection['Credit Card Utilization'][0]
    Age= df_selection['Age'][0]
    Vintage_in_Months= df_selection['Vintage in Months'][0]
    Missed_Payments= df_selection['%Missed Payments'][0]
    Outstanding_Amount= (round(df_selection['%Outstanding Amount'][0],2))*100
    CC_OD_Utilization= round((df_selection['CC/OD Utilization'][0])*100,2)
    Banking_to_turnver= df_selection['Banking to turnver (BTO)'][0]
    GST_to_previous_year_turnover= df_selection['GST to previous year turnover'][0]
    Debt_service_coverage_ratio= df_selection['Debt service coverage ratio'][0]
    Debt_Equity= df_selection['Debt/Equity'][0]
    EMI_bounces_and_Inward_returns= df_selection['EMI bounces and Inward returns '][0]
    DPD_in_commercial_tradelines= df_selection['DPD in commercial tradelines'][0]
    overdue_and_settlement_in_commercial_cibil= df_selection['overdue and settlement in commercial cibil'][0]
    CMR= df_selection['CMR'][0]

    html_func=f'''
                <head>
                
                <title>Page Title</title>
                </head>
                <body>
                <div style="background: white; color: black;">
                <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
                
                <tr>
                <th colspan="5" >BRE</th>
                </tr>
                <tr>
                <td>Application ID</td>
                <td>{application_id}</td></tr>

                <tr>
                <td>Application Score</td>
                <td>{application_score}</td></tr>
                
                <tr>
                <td>Behavioral Score</td>
                <td><a>{Behavioral_Score}</a></td></tr>
                
                
                <tr>
                <td>DPD last 6M</td>
                <td><a>{DPD_last_6_months}</a></td>
                </tr>
                
                <tr>
                <td>Enquiries last 3M</td>
                <td>{Enquiries_last_3_months}</td>
                </tr>
                
                <tr>
                <td>WriteOff SuitFiled Flag</td>
                <td>{WriteOff_SuitFiled_Flag}</td>
                
                </tr>
                
                <tr>
                <td>Credit Card Utilization</td>
                <td>{Credit_Card_Utilization}</td></tr>
                
                <tr>
                <td>Age</td>
                <td> {Age}</td></tr>
                
                <tr>
                <td>Vintage(in Months)</td>
                <td>{Vintage_in_Months}</td>
                </tr>
                
                <tr>
                <td>Missed Payments</td>
                <td> {Missed_Payments}</td>
                </tr>
                
                <tr>
                <td>Outstanding Amount</td>
                <td> {Outstanding_Amount}%</td>
                </tr>
                
                <tr>
                <td>CC/OD Utilization</td>
                <td> {CC_OD_Utilization}%</td>
                </tr>
                
                <tr>
                <td>Banking to turnver</td>
                <td>{Banking_to_turnver}</td>
                </tr>
                
                <tr>
                <td>GST to previous year turnover</td>
                <td>{GST_to_previous_year_turnover}</td>
                </tr>
                
                <tr>
                <td>Debt service coverage ratio</td>
                <td>{Debt_service_coverage_ratio}</td>
                </tr>

                <tr>
                <td>Debt Equity</td>
                <td>{Debt_Equity}</td></tr>

                <tr>
                <td>EMI bounces and Inward returns</td>
                <td>{EMI_bounces_and_Inward_returns}</td></tr>

                <tr>
                <td>DPD in commercial tradelines</td>
                <td>{DPD_in_commercial_tradelines}</td></tr>

                <tr>
                <td>overdue and settlement in commercial cibil</td>
                <td>{overdue_and_settlement_in_commercial_cibil}</td></tr>

                <tr>
                <td>CMR</td>
                <td>{CMR}</td></tr>
                
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
    Credit_Card_Utilization= df_selection['Credit Card Utilization'][0]
    Age= df_selection['Age'][0]
    Vintage_in_Months= df_selection['Vintage in Months'][0]
    Missed_Payments= df_selection['%Missed Payments'][0]
    Outstanding_Amount= (round(df_selection['%Outstanding Amount'][0],2))*100

    html_func=f'''
                <head>
                
                <title>Page Title</title>
                </head>
                <body>
                <div style="background: white; color: black;">
                <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
                
                <tr>
                <th colspan="5" >BRE</th>
                </tr>
                <tr>
                <td>Application ID</td>
                <td>{application_id}</td></tr>

                <tr>
                <td>Application Score</td>
                <td>{application_score}</td></tr>
                
                <tr>
                <td>Behavioral Score</td>
                <td><a>{Behavioral_Score}</a></td></tr>
                
                
                <tr>
                <td>DPD last 6M</td>
                <td><a>{DPD_last_6_months}</a></td>
                </tr>
                
                <tr>
                <td>Enquiries last 3M</td>
                <td>{Enquiries_last_3_months}</td>
                </tr>
                
                <tr>
                <td>WriteOff SuitFiled Flag</td>
                <td>{WriteOff_SuitFiled_Flag}</td>
                
                </tr>
                
                <tr>
                <td>Credit Card Utilization</td>
                <td>{Credit_Card_Utilization}</td></tr>
                
                <tr>
                <td>Age</td>
                <td> {Age}</td></tr>
                
                <tr>
                <td>Vintage(in Months)</td>
                <td>{Vintage_in_Months}</td>
                </tr>
                
                <tr>
                <td>Missed Payments</td>
                <td> {Missed_Payments}</td>
                </tr>
                
                <tr>
                <td>Outstanding Amount</td>
                <td> {Outstanding_Amount}%</td>
                </tr>
                
  
                </table>
                </div>
                </body>
                '''
    st.markdown(html_func,unsafe_allow_html=True)
