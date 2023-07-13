import streamlit as st
import pandas as pd  
import numpy as np 
import base64
from streamlit_option_menu import option_menu
from streamlit_echarts import st_echarts
import datetime
from datetime import datetime

st.set_page_config(page_title="Collection", layout="wide")
selected_option = option_menu(menu_title=None,
                    options=['Overall Summary',"Case allocation Summary",'Borrower Profile','Collection Strategy'],
                    icons=['person-fill','person-fill-gear'],
                    menu_icon='cast',default_index=0,orientation='horizontal',
                    styles={"container":{"padding":"0!important","backgroundcolor":'transparent'},
                            "icon":{"color":"orange","font-size":"20px"},
                    "nav-link":{"font-size":"15px",
                                "text-align":"left",
                                "margin":"0px",
                                "--hover-color":"#eee"},
                    "nav-link-selected":{'background-color':"#0197F6"},},)
@st.cache_data
def get_data_from_excel():
        df = pd.read_excel(io="C:/Users/Amani Reddy/Dashboards/files_updated/files/A_Score_amani (1).xlsx",engine="openpyxl")
        return df
    
# @st.cache_data
# def get_image_as_base64(bin_file):
#         with open(bin_file, 'rb') as f:
#             data = f.read()
#         return base64.b64encode(data).decode()
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

##calculating overall summary-----
count=df[df['Collection_Priority']=='Medium_Risk']['LoanId'].count()
gh=df.count()
perc_population_p1=round(((df[df['Collection_Priority']=='High_Risk']['LoanId'].count())/df['LoanId'].count())*100,2)
perc_population_p2=round(((df[df['Collection_Priority']=='Medium_Risk']['LoanId'].count())/df['LoanId'].count())*100,2)
perc_population_p3=round(((df[df['Collection_Priority']=='Self_Cure']['LoanId'].count())/df['LoanId'].count())*100,2)

AUM_p1=df[df['Collection_Priority']=='High_Risk']['Outstanding_Amount'].sum()
AUM_p2=df[df['Collection_Priority']=='Medium_Risk']['Outstanding_Amount'].sum()
AUM_p3=df[df['Collection_Priority']=='Self_Cure']['Outstanding_Amount'].sum()

def apply_color(val):
    if val < 30000:
        return "bgcolor=#fff2f4"
    else:
        return 'background-color: "green"'
if selected_option=='Borrower Profile':
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
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
    #Alternate_contact_number=df_selection['alternate_mobile'][0]
    Address =df_selection['Address'][0]
    #Alternate_address=df_selection['Alternate_address'][0]
    Loan_Type =df_selection['Loan_Type'][0]
    Loan_Amount =df_selection['Loan_Amount'][0]
    EMI_Due_Date= df_selection['EMI_Due_Date'][0].date()
    
    EMI_Amount  =round(df_selection['EMI_Amount'][0],2)
    Overdue_Amount  =df_selection['Overdue_Amount'][0]
    Outstanding_Amount=df_selection['Outstanding_Amount'][0]
    max_dpd_in_last_3m_OnUs =df_selection['max_dpd_in_last_3m_OnUs'][0]
    last_contacted_date =df_selection['last_contacted_date'][0].date()
    Calling_despo   =df_selection['Calling_despo'][0]
    last_contacted_number =df_selection['last_contacted_number'][0]
    
    html_func=f'''
            <head>
            
            <title>Page Title</title>
            </head>
            <body>
            <div style="background: white; color: black;">
            <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
            
            <tr>
            <th rowspan="7" >Borrower Details</th>
            <td >Selected Loan ID</td>
            <td >{loan_id}</td>
            </tr>
            
            <tr>
            <td>Name</td>
            <td>{Name}</td></tr>
            
            <tr>
            <td>Mobile</td>
            <td><a href="tel:{Mobile}">{Mobile}</a></td></tr>
            
            <tr>
            <td>Alternate Mobile</td>
            <td>Alternate_contact_number</td></tr>
            
            <tr>
            <td>Last Contacted Number</td>
            <td><a href="tel:{last_contacted_number}">{last_contacted_number}</a></td>
            </tr>
            
            <tr>
            <td>Address</td>
            <td>{Address}</td>
            </tr>
            
            <tr>
            <td>Alternate Address</td>
            <td>Alternate_address</td>
            
            </tr>
            
            <tr>
            <th rowspan="9">Loan Details</th>
            <td>Loan type</td>
            <td>{Loan_Type}</td></tr>
            
            <tr>
            <td>Loan Amount</td>
            <td>INR {Loan_Amount}</td></tr>
            
            <tr>
            <td>EMI Due Date</td>
            <td>{EMI_Due_Date}</td>
            </tr>
            
            <tr>
            <td>EMI Amount</td>
            <td>INR {EMI_Amount}</td>
            </tr>
            
            <tr>
            <td>Overdue Amount</td>
            <td>INR {Overdue_Amount}</td>
            </tr>
            
            <tr>
            <td>Outstanding Amount</td>
            <td>INR {Outstanding_Amount}</td>
            </tr>
            
            <tr>
            <td>DPD in last 3M on-us</td>
            <td>{max_dpd_in_last_3m_OnUs}</td>
            </tr>
            
            <tr>
            <td>Last Contacted Date</td>
            <td>{last_contacted_date}</td>
            </tr>
            
            <tr>
            <td>Calling Desposition</td>
            <td>{Calling_despo}</td>
            </tr>
            
            </table>
            </div>
            </body>
            '''
    st.markdown(html_func,unsafe_allow_html=True)


elif selected_option=='Collection Strategy':
    #img=get_image_as_base64("C:/Users/Amani Reddy/Dashboards/background_pic.jpg")
    st.markdown(page_bg_img, unsafe_allow_html=True)
    df_selection = df.query("LoanId == @user")   
    df_selection.reset_index(inplace=True)
    data_selection=df.query("LoanId == @user")
    #key=st.session_state['key']
    ##data----
    Collection_Score = df_selection['Collection_Score'][0]
    
    if(Collection_Score>=550 & Collection_Score<676):
        Collection_Score_indicator="Bad"
        Collection_Score_color="red"
    elif(Collection_Score>=646 & Collection_Score<726):
        Collection_Score_indicator="Average"
        Collection_Score_color="#fca510"
    else:
        Collection_Score_indicator="Good"
        Collection_Score_color="green"
        
    Collection_Priority = df_selection['Collection_Priority'][0]
    if(Collection_Priority=='High_Risk'):
        Collection_Priority_indicator="Bad"
        Collection_Priority_color="red"
    elif(Collection_Priority=='Medium_Risk'):
        Collection_Priority_indicator="Average"
        Collection_Priority_color="#fca510"
    else:
        Collection_Priority_indicator="Good"
        Collection_Priority_color="green"
    
    
    Collection_Action_pre_EMI = df_selection['Collection_Action_pre_EMI'][0]
    if(Collection_Action_pre_EMI=='Digital'):
        Collection_Action_pre_EMI_indicator="Good"
        Collection_Action_pre_EMI_color="green"
    elif(Collection_Priority=='Calling(-4, -1) + Digital'):
        Collection_Action_pre_EMI_indicator="Average"
        Collection_Action_pre_EMI_color="#fca510"
    else:
        Collection_Action_pre_EMI_indicator="Bad"
        Collection_Action_pre_EMI_color="red"
        
    Collection_Action_post_EMI = df_selection['Collection_Action_post_EMI'][0]
    if(Collection_Action_post_EMI=='Digital + Calling(after 5 days)'):
        Collection_Action_post_EMI_indicator="Good"
        Collection_Action_post_EMI_color="green"
    elif(Collection_Priority=='Calling + Field (after 10 days)'):
        Collection_Action_post_EMI_indicator="Average"
        Collection_Action_post_EMI_color="#fca510"
    else:
        Collection_Action_post_EMI_indicator="Bad"
        Collection_Action_post_EMI_color="red"
    
    Bureau_Score = df_selection['Bureau_Score'][0]
    if(Bureau_Score>=750):
        Bureau_Score_indicator="Good"
        Bureau_Score_color="green"
    elif(Bureau_Score>=600 & Bureau_Score<750):
        Bureau_Score_indicator="Average"
        Bureau_Score_color="#fca510"
    else:
        Bureau_Score_indicator="Bad"
        Bureau_Score_color="red"
    
    loans_open_last_6m  = df_selection['loans_open_last_6m'][0]
    if(loans_open_last_6m<=1):
        loans_open_last_6m_indicator="Good"
        loans_open_last_6m_color="green"
    elif(loans_open_last_6m==2 or loans_open_last_6m==3):
        loans_open_last_6m_indicator="Average"
        loans_open_last_6m_color="#fca510"
    else:
        loans_open_last_6m_indicator="Bad"
        loans_open_last_6m_color="red"
        
    last_12m_max_dpd_all_prods  = df_selection['last_12m_max_dpd_all_prods'][0]
    if(last_12m_max_dpd_all_prods<=29):
        last_12m_max_dpd_all_prods_indicator="Good"
        last_12m_max_dpd_all_prods_color="Green"
    elif(last_12m_max_dpd_all_prods>29 and last_12m_max_dpd_all_prods<=89):
        last_12m_max_dpd_all_prods_indicator="Average"
        last_12m_max_dpd_all_prods_color="#fca510"
    else:
        last_12m_max_dpd_all_prods_indicator="Bad"
        last_12m_max_dpd_all_prods_color="red"
        
    latest_bank_balance=df_selection["latest_bank_balance"][0]
    last_EMI=df_selection['last_EMI'][0]
    

    table_2=f'''
            <head>
            
            <title>Page Title</title>
            
            </head>
            
            <body>
            
            <body>
            <div style="background: #ffffff; color: black;">
            <table width=100%" bordercolor="black" border="5" cellpadding="30" cellspacing="5" align="Center">
            
            <tr>
            <th>Dimensions</th>
            <th>Variable</th>
            <th>Value</th>
            <th>Indicator</th>
            </tr>
            
            <tr>
            <th rowspan="4">Collection Strategy</th>
            <td >Collection Score</td>
            <td>{Collection_Score}</font></td>
            <td><font color='{Collection_Score_color}'>{Collection_Score_indicator}</font></td>
            </tr>
            
            <tr>
            <td>Collection Priority</td>
            <td>{Collection_Priority}</td>
            <td><font color='{Collection_Priority_color}'>{Collection_Priority_indicator}</font></td>
            </tr>
            
            <tr>
            <td>Action Pre EMI</td>
            <td>{Collection_Action_pre_EMI}</td>
            <td><font color='{Collection_Action_pre_EMI_color}'>{Collection_Action_pre_EMI_indicator}</font></td></tr>
            
            <tr>
            <td>Action Post EMI</td>
            <td>{Collection_Action_post_EMI}</td>
            <td><font color='{Collection_Action_post_EMI_color}'>{Collection_Action_post_EMI_indicator}</font></td></tr>
            
            <tr >
            <th rowspan="5">Key Features</th>
            <td >Bureau Score</td>
            <td >{Bureau_Score}</td>
            <td><font color='{Bureau_Score_color}'>{Bureau_Score_indicator}</font></td></tr>
            
            <tr>
            <td >Loans opened in last 6M</td>
            <td >{loans_open_last_6m}</td>
            <td><font color='{loans_open_last_6m_color}'>{loans_open_last_6m_indicator}</font></td></tr>
            
            <tr>
            <td >DPD in last 12M</td>
            <td >{last_12m_max_dpd_all_prods}</td>
            <td><font color='{last_12m_max_dpd_all_prods_color}'>{last_12m_max_dpd_all_prods_indicator}</font></td></tr>
            
            <tr>
            <td >Latest Bank Balance</td>
            <td >INR {latest_bank_balance}</td>
            <td><font color='black'>----</font></td></tr>
            
            <tr>
            <td >Last EMI amount</td>
            <td >INR {last_EMI}</td>
            <td><font color='black'>----</font></td></tr>
            
            </table>
            </div>
            </body>
            ''' 
    with st.container():        
            st.markdown(table_2,unsafe_allow_html=True)
elif(selected_option=='Overall Summary'):
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    p1_perc_population=df[df['Collection_Priority']=='High_Risk']['LoanId'].count()
    p2_perc_population=df[df['Collection_Priority']=='Medium_Risk']['LoanId'].count()
    p3_perc_population=df[df['Collection_Priority']=='High_Risk']['LoanId'].count()

    p1_AUM=round(df[df['Collection_Priority']=="High_Risk"]['Outstanding_Amount'].sum()/10000000,2)
    p2_AUM=round(df[df['Collection_Priority']=='Medium_Risk']['Outstanding_Amount'].sum()/10000000,2)
    p3_AUM=round(df[df['Collection_Priority']=="Self_Cure"]['Outstanding_Amount'].sum()/10000000,2)


        
    summary = {"title": {
        "text": 'Overall Summary',
        "textStyle":{"color":'black'}},
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
        "legend":{"data":["Number of Customers","AUM"],'backgroundColor':'white'},
        "grid": { "containLabel": True },
      "xAxis": {
        "type": 'category',
        "data": ['Priority 1','Priority 2','Self Cure'],
        "axisLabel": {"color":'black',"fontSize": 15}
      },
      "yAxis": {
        "show":False,
        "type": 'value',
      },
      "series": [
        {
         "name":"AUM",
          "data":[{ "value": 20000, "itemStyle": {"borderWidth": 4,
                                                "borderColor": '#82eefd',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":str(p1_AUM)+" Cr"}},
                { "value": 30000, "itemStyle": {"borderWidth": 4,
                                                "borderColor": '#63c5da',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":str(p2_AUM)+" Cr"} },
                { "value":40762, "itemStyle": { "borderWidth": 4,
                                                "borderColor": '#63c5da',
                                                "color": 'white'},"label": {"show": True,
                                                                        "position": 'inside',
                                                                        "formatter":str(p3_AUM)+" Cr"} }],
          "type": 'line',
          "symbol": 'circle',
          "symbolSize": 75,
          "lineStyle": {
            "color": 'green',
            "width": 0,
            "type": 'hidden'
          }
        },
        {"name":"Number of Customers",
                "data":[{"value": 5238, "itemStyle": { "color": "red" } },
                {"value": 12202, "itemStyle": { "color": 'yellow' } },
                {"value": 40762, "itemStyle": { "color": 'green' } }],
                "type": 'bar',
                "barWidth":80,
                "color":'black',
                "label": {
            "show": True,
            "position": 'inside'}
                
            }
      ]
    }
    st_echarts(options=summary)
    
    selected_type=st.radio(label="",options=['Priority1','Priority2','Self-Cure'],horizontal=True,help='help',label_visibility='collapsed',index=0)
    if selected_type=="Priority1":
        st.write('Priority1 is selected:')
        p1=df[df['Collection_Priority']=='High_Risk']
        st.dataframe(p1)
    elif selected_type=='Priority2':
        st.write('Priority 2 is selected')
        p2=df[df['Collection_Priority']=='Medium_Risk']
        st.dataframe(p2)
    else:
        st.write('Self-cure is selected')
        sc=df[df['Collection_Priority']=='Self_Cure']
        st.dataframe(sc)






elif(selected_option=='Case allocation Summary'):
    st.markdown(page_bg_img, unsafe_allow_html=True)
    def function():
        return np.random.randint(10000,100000)
    # def sort_func(a,b):
    values=[]

    # values.append(df[df['Upsell_Score']>=800]["TopUp_Amount"].sum())
    # values.append(df[(df['Upsell_Score']<800) & df['Upsell_Score']<=750]["TopUp_Amount"].sum())
    # values.append(df[(df['Upsell_Score']<750) & df['Upsell_Score']<=700]["TopUp_Amount"].sum())
    # values.append(df[df['Upsell_Score']<700]["TopUp_Amount"].sum())
    # values=[int(value) for value in values]
    # # st.write(values)
    def create_data_for_pie(columns,values):
        return [{'value':values[i],'name':columns[i]} for i in range(len(columns))]
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    Digital_count=df[df["Collection_Action_pre_EMI"]=="Digital"]["LoanId"].count()
    #Calling_count=df[df["Collection_Action_pre_EMI"]!="Digital" &(df["Collection_Action_pre_EMI"].str.notcontains("Field"))]["LoanId"].count()
    Field_count=df[df["Collection_Action_pre_EMI"].str.contains("Field")]['LoanId'].count()
    Calling_count=df['LoanId'].count()-(Digital_count+Field_count)
    option = {
     "backgroundColor": 'white',
     'title': {"text": 'Case Allocation Summary',
       'left': 'center',
       'top': 20,
       'textStyle': {
         'color': 'black'
       }
     },
      "tooltip": {
        "trigger": 'item'
      },
      "legend": {
        "orient": 'vertical',
        "left": 'right'
      },
      "series": [
        {
          "name": 'Number of Customers',
          "type": 'pie',
          "radius": '60%',
          "label": {"position": 'inside', "formatter": '{d}%', "color":'black',  "fontSize":12},
          "data":sorted(create_data_for_pie(['Only Digital','Digital+Calling','Digital+Calling+Field'],[30762,25202,3024]),key=lambda x:x['value']),
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

# def get_data_from_excel():
#         df = pd.read_excel(io="C:/Users/Amani Reddy/Dashboards/files_updated/files/data_for_BRE.xlsx",engine="openpyxl")
#         return df

# df=get_data_from_excel()
# st.write(df)