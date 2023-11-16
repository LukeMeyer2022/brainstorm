
# limitations under the License.
import pandas as pd
import streamlit as st
from streamlit.logger import get_logger

# Title of the dashboard
st.title("Your Dashboard Title")

# Sidebar for interactive widgets
with st.sidebar:
    st.header("Sidebar")
    # Add interactive widgets here, e.g., st.slider(), st.selectbox()

@st.cache_data
def load_data():
    try:
        data = "DataMetsV5_Cleaned.xlsx"
        df = pd.read_excel(data)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Load and display the data
df = load_data()
if not df.empty:
    st.dataframe(df)

# Additional code for more dashboard features

