import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from glob import glob

@st.cache_data
def load_csv(filepath, nrows = 40):
    return pd.read_csv(filepath, nrows=nrows)


ai_rule_df = load_csv('./data/ai_rule.csv')
powerbi_df = load_csv('./data/dashboard_rule.csv')


rd_options = ['Summary', 'AI Rule', 'GIS Rule', 'Power Bi Dashboard']
st_button_dict = {
    'Summary': 'summary_page',
    'AI Rule': 'ai_rule_page', 
    'GIS Rule':'gis_rule_page', 
    'Power Bi Dashboard':'powerbi_rule_page'
}


def display_aggrid(df, date_value):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_side_bar()
    gb.configure_default_column(editable=True, groupable=True)
    gridOptions = gb.build()
    st.markdown(f"#### Last Update: {date_value}")
    AgGrid(df, gridOptions=gridOptions)





date_value = '20-06-2024'
def main(select_button):

    if select_button == 'AI Rule':
        state, block, st_geography =  st.tabs(['State', 'Block', 'State Spatially'])
        with state:
            display_aggrid(ai_rule_df, date_value)            
            #placeholder.write(display_aggrid(ai_rule_df, date_value))
        with block:
            st.dataframe(ai_rule_df)
            st.write('Just selected block')
        with st_geography:
            st.write('Here would like to plot statwise spatial plot')
    elif select_button == 'GIS Rule':
        display_aggrid(powerbi_df, date_value) 
    elif select_button == 'Power Bi Dashboard':
        display_aggrid(powerbi_df, date_value)

        





    st.write(f"The shape of above dfs are {ai_rule_df.shape}, {powerbi_df.shape}")





if __name__ == '__main__':
    st.write(f"The shape of above df is {ai_rule_df.shape}")
    #main()  
