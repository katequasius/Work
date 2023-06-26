def home_page():
    st.markdown("Home")
    st.sidebar.markdown("Home")
    
def mode1():
    st.markdown("Mode 1")
    st.sidebar.markdown("Mode 1")
    
def mode2():
    st.markdown("Mode 2")
    st.sidebar.markdown("Mode 2")
    
page_names_to_funcs = {
	"Home": Mode2Page,
    "Mode 1": Mode2Page,
    "Mode 2": Mode2Page,
    }

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())