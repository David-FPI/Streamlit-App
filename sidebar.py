import streamlit as st 
from util import Social

# Function to manage navigation
def navigate(page):
    st.query_params["page"]=page


def SideBar():
    # Sidebar layout with navigation
    
    with st.sidebar:
        
        st.image("booms.png", use_column_width=True)
        st.markdown(
            """
            <style>
            [data-testid="stImage"] img {
                border-radius: 50%;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        Social(sidebarPos=True)
        
        st.header("Menu")
        
        if st.button("🎃 Home"):
            navigate("Home")
        
        if st.button("🚀 Yolo for Logo"):
            navigate("yolologo")
            
        if st.button("🧠 News QA System using LLM"):
            navigate("newsqa")
            
        if st.button("🐙 Image Classifier"):
            navigate("image_classifer")
            
        if st.button("🐙 Play with Cluster"):
            navigate("clusterplay")
            
        if st.button("🌐 Social"):
            navigate("Social")
            
        

        