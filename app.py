import streamlit as st
from modules import workrisk, home
from st_aggrid import AgGrid, GridOptionsBuilder


# test change for work-risk branch

home.main()
# Sidebar section
with st.sidebar.expander("Work Risk"):
    wr_select_bt = st.radio(label='Select', options=workrisk.rd_options, key="wr_dashboard")

with st.sidebar.expander("ABPS"):
    abps_select_bt = st.radio(label='Select', options=['Summary', 'Logs'], key="abps_dashboard") 
    st.write(f"ABPS success will show here, {abps_select_bt}") 

with st.sidebar.expander("DOCU AI"):
    ddugky_select_bt = st.radio(label='Select', options=['Summary', 'Dashboard'], key="ddugky_dashboard") 
    st.write("DDUGKY metric will show here")

workrisk.main(wr_select_bt) 






# import streamlit as st
# from modules import home, workrisk

# # Define your pages as functions
# def home_page():
#     home.main()

# def work_risk_page():
#     st.title("Work Risk Dashboard")
#     wr_select_bt = st.radio(label='Select', options=workrisk.rd_options, key="wr_dashboard")
#     st.write(wr_select_bt)
#     # Additional content for Work Risk Dashboard can be added here

# def abps_page():
#     st.title("ABPS Dashboard")
#     abps_select_bt = st.radio(label='Select', options=['Summary', 'Logs'], key="abps_dashboard")
#     st.write(f"ABPS success will show here, {abps_select_bt}")
#     # Additional content for ABPS Dashboard can be added here

# def ddugky_page():
#     st.title("DDUGKY Dashboard")
#     ddugky_select_bt = st.radio(label='Select', options=['Summary', 'Dashboard'], key="ddugky_dashboard")
#     st.write("DDUGKY metric will show here")
#     # Additional content for DDUGKY Dashboard can be added here

# # Create a dictionary of pages
# pages = {
#     "Home": home_page,
#     "Work Risk Dashboard": work_risk_page,
#     "ABPS Dashboard": abps_page,
#     "DDUGKY Dashboard": ddugky_page
# }

# # Sidebar for navigation
# st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Go to", list(pages.keys()))

# # Render the selected page
# if selection:
#     pages[selection]()





# # Mapping of page names to DataFrames
# page_to_df = {
#     'Page 1': df1,
#     'Page 2': df2,
#     'Page 3': df3,
#     'Page 4': df4,
#     'Page 5': df5,
#     'Page 6': df6
# }

# # Function to display a DataFrame using AG Grid
# def display_aggrid(df, date_value):
#     gb = GridOptionsBuilder.from_dataframe(df)
#     gb.configure_pagination(paginationAutoPageSize=True)
#     gb.configure_side_bar()
#     gb.configure_default_column(editable=True, groupable=True)
#     gridOptions = gb.build()
#     st.markdown(f"<div style='text-align: right; float: right;'>#### Last Update: {date_value}</div>", unsafe_allow_html=True)
#     AgGrid(df, gridOptions=gridOptions)


# # Display the appropriate DataFrame based on sidebar selection
# if page:
#     st.title(f'DataFrame from {page.lower()}')
#     display_aggrid(page_to_df[page], date_value)




# import streamlit as st
# from modules import home, workrisk

# # Function to display home content
# def home_page():
#     home.main()

# # Function to display work risk dashboard content
# def work_risk_page(selection):
#     st.title("Work Risk Dashboard")
#     st.write(selection)
#     # Additional content for Work Risk Dashboard can be added here

# # Function to display ABPS dashboard content
# def abps_page(selection):
#     st.title("ABPS Dashboard")
#     st.write(f"ABPS success will show here, {selection}")
#     # Additional content for ABPS Dashboard can be added here

# # Function to display DDUKGY dashboard content
# def ddugky_page(selection):
#     st.title("DDUGKY Dashboard")
#     st.write("DDUGKY metric will show here")
#     # Additional content for DDUKGY Dashboard can be added here

# # Main content display logic
# if 'main_page' not in st.session_state:
#     st.session_state['main_page'] = 'Home'

# # Sidebar section with expanders    
# with st.sidebar.expander("Home"):
#     if st.button("Go to Home"):
#         st.session_state['main_page'] = 'Home'

# with st.sidebar.expander("Work Risk Dashboard"):
#     wr_select_bt = st.radio(label='Select', options=workrisk.rd_options, key="wr_dashboard")
#     if wr_select_bt:
#         st.session_state['main_page'] = 'Work Risk Dashboard'
#         st.session_state['work_risk_selection'] = wr_select_bt

# with st.sidebar.expander("ABPS Dashboard"):
#     abps_select_bt = st.radio(label='Select', options=['Summary', 'Logs'], key="abps_dashboard")
#     if abps_select_bt:
#         st.session_state['main_page'] = 'ABPS Dashboard'
#         st.session_state['abps_selection'] = abps_select_bt

# with st.sidebar.expander("DDUGKY Dashboard"):
#     ddugky_select_bt = st.radio(label='Select', options=['Summary', 'Dashboard'], key="ddugky_dashboard")
#     if ddugky_select_bt:
#         st.session_state['main_page'] = 'DDUGKY Dashboard'
#         st.session_state['ddugky_selection'] = ddugky_select_bt


# st.write(st.session_state)
# # Display the selected main content
# if st.session_state['main_page'] == 'Home':
#     st.write('I have come here once')
#     home_page()
# elif st.session_state['main_page'] == 'Work Risk Dashboard':
#     work_risk_page(st.session_state.get('work_risk_selection', ''))
# elif st.session_state['main_page'] == 'ABPS Dashboard':
#     abps_page(st.session_state.get('abps_selection', ''))
# elif st.session_state['main_page'] == 'DDUGKY Dashboard':
#     ddugky_page(st.session_state.get('ddugky_selection', ''))
