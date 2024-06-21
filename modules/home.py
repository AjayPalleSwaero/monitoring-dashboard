import streamlit as st

def main():
    # Main page introduction
    st.title("Welcome to Data and Insight Unit (DIU) Monitoring Dashboard")


    # Display the context text
    st.markdown("""
    ## Overview
    This dashboard serves as a monitoring to track dashboards built and managed by DIU team for various  projects under departments of 
    Ministry of Rural Development (MORD). It also provides data crawls status and inflow and out of data through APIs. 
    ### Purpose

    1. **Work Risk Dashboard**:  <br> 
        **Context**:
        <br>&emsp; As a part of work-risk analytics project DIU and NIC NREGA implements
        from NIC then process AI rule and GIS rule and sends back processed data to NIC NREGA by last day of that month. Then 
        NIC performs remaining rules updates workrisk dashboard and exposes it as API. This dashboard gives glimpse of above process.  
            
        **Metrics**:
    - **Summary**: Provides a high-level overview that month processed and sent records.
    - **AI Rule**: Provides AI rule key metrics and highlights discrepancy in data received, processed and sent to NIC NREGA, if any.
    - **GIS Rule**: Provides GIS rule key metrics and highlights discrepancy in data received, processed and sent to NIC NREGA, if any.
    - **Power Bi Dashboard**: 

    2. **ABPS Dashboard**: <br>
        **Context**:
        <br>&emsp; Since December 2023 MORD decided all the workers wage payments of NREGA should happen through Aadhaar Payment Bridge System (ABPS). 
                So DIU built a [dashboard](https://nrega.nic.in)  on June 2023 and hosted it in NIC NREGA offical site to enable states, district and blocks officals to know which regions are performing better and worse. The data 
                for this dashboard gets updated everday morning 7.00 Am. This dashboard gives an overview of crawl status, summary statistics and failed blocks if any   
        **Metrics**: 
        - **Summary**: Provides overview crawl status; number of blocks fetched and number of blocks failed 
        - **Logs**: A detailed log(s) if there are any failed block(s). 

    3. **DDUGKY Dashboard**:
    - Presents detailed metrics and performance indicators for the DDU-GKY project, helping stakeholders understand the progress and areas needing attention.

    ### Key Features

    - **Real-Time Tracking**: Continuously updates to provide the most current data on crawls and API calls.
    - **Error Monitoring**: Highlights failed status and issues, allowing for quick troubleshooting and resolution.
    - **Data Insights**: Offers detailed analytics and insights through integrated reports and visualizations.

    """, unsafe_allow_html=True)
    st.info("Use the sidebar to navigate through different dashboards and explore various metrics.")
    st.markdown("## Getting Started")
    st.markdown("""
    1. **Navigate**: Use the sidebar to select different dashboards.
    2. **Explore**: Dive into the metrics and analytics provided for each section.
    3. **Monitor**: Keep an eye on real-time updates and alerts.
    """)

if __name__ == "__main__":
    main()