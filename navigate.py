import streamlit as st 
from util import GitHubStats, HomePage, Social, YoloforLogo, NewsQA
from Clustering.cluster_util import showData,Cluster

def navigator():

    # Get the current page from the query parameters
    
    page = "page"
    
    if page in st.query_params.keys():
        page = st.query_params["page"]
    else: page = "home"

    # Display content based on the selected menu item
    if page == "home":
        HomePage()
        

    elif page == "Home":
        HomePage()

    # Page content based on the selected menu item
    elif page == "yolologo":
        st.title("🚀:rainbow[YOLO for Logo!] :sunglasses:")
        YoloforLogo()
        
    elif page == "newsqa":
        st.title("📚:rainbow[News QA System using LLM] :sunglasses:")
        NewsQA()
        
    elif page == "image_classifer":
        st.title("🚀:rainbow[Image Classification ] :sunglasses:")
        st.subheader("Coming Soon ..")
        
    elif page == "clusterplay":
        st.title("🐙:rainbow[Play with Clusters] :sunglasses:")
        Cluster()
        
    elif page == "Social":
        Social(sidebarPos=False,heading="Social")

        

    else:
        st.subheader("Home Page")
        st.write("Welcome to the Streamlit Portfolio. Use the sidebar to navigate.")
