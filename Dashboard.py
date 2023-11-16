
# limitations under the License.
import pandas as pd
import streamlit as st
from streamlit.logger import get_logger

st.sidebar()
st.markdown("Tilte")

def brainstorm():
  url = "https://github.com/LukeMeyer2022/brainstorm/DataMetsV5_Cleaned.xlsx"
  df = pd.read_excel(url)
  return df

brainstorm()
