# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:47:31 2023

@author: Amani Reddy
"""

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
    Credit_Card_Utilization= round(df_selection['Credit Card Utilization'][0],2)
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

    
    # flag=0
    # if((Banking_to_turnver>80)&(GST_to_previous_year_turnover>=120)&(Debt_service_coverage_ratio>0.9)&(Debt_Equity<3)&(EMI_bounces_and_Inward_returns<2)
    #    &(DPD_in_commercial_tradelines==0)&(overdue_and_settlement_in_commercial_cibil==0)&(CMR<=5)&(application_score>700)
    #    &(Behavioral_Score>700)&(DPD_last_6_months<=0)&(Enquiries_last_3_months<3)&(WriteOff_SuitFiled_Flag==0)
    #    &(Credit_Card_Utilization<70)&(Vintage_in_Months>=6)&(Missed_Payments<=10)&(Outstanding_Amount<=70)&(loans_open_last_6_months<=3)):
    #     st.write("Approved")
    # else:
    #     st.write("Rejected")
    def parameter_check_sme(parameter):
      if (parameter=="Banking_to_turnver") and (eval(parameter)>80):
        return ('approved','green')
      if (parameter=='GST_to_previous_year_turnover') and (eval(parameter)>=120):
        return ('approved','green')
      if (parameter=='Debt_service_coverage_ratio') and (eval(parameter)>0.9):
        return ('approved','green')
      if (parameter=='Debt_Equity') and (eval(parameter)<3):
        return ('approved','green')
      if (parameter=='EMI_bounces_and_Inward_returns') and (eval(parameter)<=2):
        return ('approved','green')
      if (parameter=='DPD_in_commercial_tradelines') and (eval(parameter)==0):
        return ('approved','green')
      if (parameter=='overdue_and_settlement_in_commercial_cibil') and (eval(parameter)==0):
        return ('approved','green')
      if (parameter=='CMR') and (eval(parameter)<=5):
        return ('approved','green')
      if (parameter=="application_score") and (eval(parameter)>700):
        return ('approved','green')
      if (parameter=='Behavioral_Score') and (eval(parameter)>700):
        return ('approved','green')
      if (parameter=='DPD_last_6_months') and (eval(parameter)<=0):
        return ('approved','green')
      if (parameter=='Enquiries_last_3_months') and (eval(parameter)<3):
        return ('approved','green')
      if (parameter=='WriteOff_SuitFiled_Flag') and (eval(parameter)==0):
        return ('approved','green')
      if (parameter=='Credit_Card_Utilization') and (eval(parameter)<70):
        return ('approved','green')
      if (parameter=='Vintage_in_Months') and (eval(parameter)>=6):
        return ('approved','green')
      if (parameter=='Missed_Payments') and (eval(parameter)<=10):
        return ('approved','green')
      if (parameter=='Outstanding_Amount') and (eval(parameter)<=70):
        return ('approved','green')
      if (parameter=="loans_open_last_6_months") and (eval(parameter)<=3):
        return ('approved','green')
      return ('rejected','red')
      return ('rejected','red')
     

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
                <td>{application_id}</td>
                <td>-----</td></tr>

                <tr>
                <td>Application Score</td>
                <td>{application_score}</td>
                <td><font color='{parameter_check_sme("application_score")[1]}'>{parameter_check_sme("application_score")[0]}</font></td></tr>
                
                <tr>
                <td>Behavioral Score</td>
                <td><a>{Behavioral_Score}</a></td>
                <td><font color='{parameter_check_sme("Behavioral_Score")[1]}'>{parameter_check_sme("Behavioral_Score")[0]}</font></td></tr>
                
                
                <tr>
                <td>DPD last 6M</td>
                <td><a>{DPD_last_6_months}</a></td>
                <td><font color='{parameter_check_sme("DPD_last_6_months")[1]}'>{parameter_check_sme("DPD_last_6_months")[0]}</font></td></tr>
                
                <tr>
                <td>Enquiries last 3M</td>
                <td>{Enquiries_last_3_months}</td>
                <td><font color='{parameter_check_sme("Enquiries_last_3_months")[1]}'>{parameter_check_sme("Enquiries_last_3_months")[0]}</font></td></tr>
                
                <tr>
                <td>WriteOff SuitFiled Flag</td>
                <td>{WriteOff_SuitFiled_Flag}</td>
                <td><font color='{parameter_check_sme("WriteOff_SuitFiled_Flag")[1]}'>{parameter_check_sme("WriteOff_SuitFiled_Flag")[0]}</font></td></tr>
                
                <tr>
                <td>Credit Card Utilization</td>
                <td>{Credit_Card_Utilization}</td>
                <td><font color='{parameter_check_sme("Credit_Card_Utilization")[1]}'>{parameter_check_sme("Credit_Card_Utilization")[0]}</font></td></tr>
                
                <tr>
                <td>Age</td>
                <td> {Age}</td>
                <td>-----</td></tr>
                
                <tr>
                <td>Vintage(in Months)</td>
                <td>{Vintage_in_Months}</td>
                <td><font color='{parameter_check_sme("Vintage_in_Months")[1]}'>{parameter_check_sme("Vintage_in_Months")[0]}</font></td></tr>
                
                <tr>
                <td>Missed Payments</td>
                <td> {Missed_Payments}</td>
                <td><font color='{parameter_check_sme("Missed_Payments")[1]}'>{parameter_check_sme("Missed_Payments")[0]}</font></td></tr>
                
                <tr>
                <td>Outstanding Amount</td>
                <td> {Outstanding_Amount}%</td>
                <td><font color='{parameter_check_sme("Outstanding_Amount")[1]}'>{parameter_check_sme("Outstanding_Amount")[0]}</font></td></tr>
                
                <tr>
                <td>CC/OD Utilization</td>
                <td> {CC_OD_Utilization}%</td>
                <td>-----</td></tr>
                
                <tr>
                <td>Banking to turnver</td>
                <td>{Banking_to_turnver}%</td>
                <td><font color='{parameter_check_sme("Banking_to_turnver")[1]}'>{parameter_check_sme("Banking_to_turnver")[0]}</font></td></tr>

                
                <tr>
                <td>GST to previous year turnover</td>
                <td>{GST_to_previous_year_turnover}%</td>
                <td><font color='{parameter_check_sme("GST_to_previous_year_turnover")[1]}'>{parameter_check_sme("GST_to_previous_year_turnover")[0]}</font></td></tr>

                
                <tr>
                <td>Debt service coverage ratio</td>
                <td>{Debt_service_coverage_ratio}</td>
                <td><font color='{parameter_check_sme("Debt_service_coverage_ratio")[1]}'>{parameter_check_sme("Debt_service_coverage_ratio")[0]}</font></td></tr>


                <tr>
                <td>Debt Equity</td>
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
                <td>overdue and settlement in commercial cibil</td>
                <td>{overdue_and_settlement_in_commercial_cibil}</td>
                <td><font color='{parameter_check_sme("overdue_and_settlement_in_commercial_cibil")[1]}'>{parameter_check_sme("overdue_and_settlement_in_commercial_cibil")[0]}</font></td></tr>


                <tr>
                <td>CMR</td>
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
    Credit_Card_Utilization= df_selection['Credit Card Utilization'][0]
    Age= df_selection['Age'][0]
    Vintage_in_Months= df_selection['Vintage in Months'][0]
    Missed_Payments= df_selection['%Missed Payments'][0]
    loans_open_last_6_months=df_selection['loans open last 6 months'][0]
    Outstanding_Amount= (round(df_selection['%Outstanding Amount'][0],2))*100
    
    counter=0
    #if((application_score>700)&(Behavioral_Score>700)):
    # parameter should be a string
    def parameter_check_retail(parameter):
      if (parameter=="application_score") and (eval(parameter)>700):
        return ('approved','green')
      if (parameter=='Behavioral_Score') and (eval(parameter)>700):
        return ('approved','green')
      if (parameter=='DPD_last_6_months') and (eval(parameter)<=0):
        return ('approved','green')
      if (parameter=='Enquiries_last_3_months') and (eval(parameter)<3):
        return ('approved','green')
      if (parameter=='WriteOff_SuitFiled_Flag') and (eval(parameter)==0):
        return ('approved','green')
      if (parameter=='Credit_Card_Utilization') and (eval(parameter)<70):
        return ('approved','green')
      if (parameter=='Vintage_in_Months') and (eval(parameter)>=6):
        return ('approved','green')
      if (parameter=='Missed_Payments') and (eval(parameter)<=10):
        return ('approved','green')
      if (parameter=='Outstanding_Amount') and (eval(parameter)<=70):
        return ('approved','green')
      if (parameter=="loans_open_last_6_months") and (eval(parameter)<=3):
        return ('approved','green')
      return ('rejected','red')

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
                <td>{application_id}</td>
                <td>-----</td></tr>

                <tr>
                <td>Application Score</td>
                <td>{application_score}</td>
                <td><font color='{parameter_check_retail("application_score")[1]}'>{parameter_check_retail("application_score")[0]}</font></td></tr>
                
                <tr>
                <td>Behavioral Score</td>
                <td><a>{Behavioral_Score}</a></td>
                <td><font color='{parameter_check_retail("Behavioral_Score")[1]}'>{parameter_check_retail("application_score")[0]}</font></td></tr>

                <tr>
                <td>DPD last 6M</td>
                <td><a>{DPD_last_6_months}</a></td>
                <td><font color='{parameter_check_retail("DPD_last_6_months")[1]}'>{parameter_check_retail("DPD_last_6_months")[0]}</font></td></tr>

                
                <tr>
                <td>Enquiries last 3M</td>
                <td>{Enquiries_last_3_months}</td>
                <td><font color='{parameter_check_retail("Enquiries_last_3_months")[1]}'>{parameter_check_retail("Enquiries_last_3_months")[0]}</font></td></tr>
                
                <tr>
                <td>WriteOff SuitFiled Flag</td>
                <td>{WriteOff_SuitFiled_Flag}</td>
                <td><font color='{parameter_check_retail("WriteOff_SuitFiled_Flag")[1]}'>{parameter_check_retail("WriteOff_SuitFiled_Flag")[0]}</font></td></tr>

                
                <tr>
                <td>Credit Card Utilization</td>
                <td>{Credit_Card_Utilization}</td>
                <td><font color='{parameter_check_retail("Credit_Card_Utilization")[1]}'>{parameter_check_retail("Credit_Card_Utilization")[0]}</font></td></tr>

                
                <tr>
                <td>Age</td>
                <td> {Age}</td>
                <td>-----</td></tr>
                
                <tr>
                <td>Vintage(in Months)</td>
                <td>{Vintage_in_Months}</td>
                <td><font color='{parameter_check_retail("Vintage_in_Months")[1]}'>{parameter_check_retail("Vintage_in_Months")[0]}</font></td></tr>

                
                <tr>
                <td>Missed Payments</td>
                <td> {Missed_Payments}</td>
                <td><font color='{parameter_check_retail("Missed_Payments")[1]}'>{parameter_check_retail("Missed_Payments")[0]}</font></td></tr>

                
                <tr>
                <td>Loans opened in last 6 months</td>
                <td> {loans_open_last_6_months}</td>
                <td><font color='{parameter_check_retail("loans_open_last_6_months")[1]}'>{parameter_check_retail("loans_open_last_6_months")[0]}</font></td></tr>

                
                <tr>
                <td>Outstanding Amount</td>
                <td> {Outstanding_Amount}%</td>
                <td><font color='{parameter_check_retail("Outstanding_Amount")[1]}'>{parameter_check_retail("Outstanding_Amount")[0]}</font></td></tr>

                
  
                </table>
                </div>
                </body>
                '''
    st.markdown(html_func,unsafe_allow_html=True)
