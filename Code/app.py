from pathlib import Path
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Redback Operations", layout="wide")


LOGO = Path(__file__).resolve().parent / "images" / "logo.png"

if LOGO.exists():
    image = Image.open(LOGO)
    image = image.resize((80, 80), Image.Resampling.LANCZOS)
else:
    image = None

col1, col2 = st.columns([0.1, 0.9])
with col1:
    if image:
        st.image(image, use_container_width=False)
with col2:
    st.markdown(
        """
        <h1 style='margin-bottom: 0;'>
            Redback Operations Dashboard
        </h1>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.header("🔗Important Links")
st.write("Rabbit MQ: (REDACTED FOR SECURITY PURPOSES) ")
st.write("Streamlit: (REDACTED FOR SECURITY PURPOSES)")
st.write("Airflow: (REDACTED FOR SECURITY PURPOSES)")
st.write("Kafka: (REDACTED FOR SECURITY PURPOSES)")
st.write("Wazuh: (REDACTED FOR SECURITY PURPOSES)")
st.write("Dremio: (REDACTED FOR SECURITY PURPOSES)")
st.write("MinIO: (REDACTED FOR SECURITY PURPOSES)")


st.markdown("---")
st.header("🛠️Maintenance")
st.write("Grafana: (REDACTED FOR SECURITY PURPOSES)")
