
# limitations under the License.
import pandas as pd
import streamlit as st
from streamlit.logger import get_logger

st.sidebar()
st.markdown("Tilte")

def brainstorm():
  url = "https://github.com/LukeMeyer2022/brainstorm.git"
  df = pd.read_excel(url)
  return df

if __name__ == "__main__":
    run()
