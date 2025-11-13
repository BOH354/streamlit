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
st.write("Rabbit MQ: http://10.137.0.149:15672/ ")
st.write("Streamlit: https://redback.it.deakin.edu.au/file-upload")
st.write("Airflow: http://10.137.0.149:8888/login/")
st.write("Kafka: https://redback.it.deakin.edu.au/kafka/")
st.write("Wazuh: https://redback.it.deakin.edu.au/wazuh")
st.write("Dremio: http://10.137.0.149:9047")
st.write("MinIO: https://redback.it.deakin.edu.au/minio")


st.markdown("---")
st.header("🛠️Maintenance")
st.write("Grafana: https://cyber.redback.it.deakin.edu.au:9443/monitor/login")