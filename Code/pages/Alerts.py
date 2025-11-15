import streamlit as st
import requests

st.title("🛡️ Security")
st.markdown("---")


st.header("🛡️ External Service Status")

services = {
    "Local Test Server": "http://127.0.0.1:8000",
    "Local Wazuh:": "http://localhost:5601/",
}

def check_service(url):
    try:
        r = requests.get(url, timeout=2)
        if r.status_code < 400:
            return "🟢 Online"
        else:
            return "🟠 Issues"
    except:
        return "🔴 Offline"

for name, url in services.items():
    status = check_service(url)
    st.write(f"**{name}** → {status} — [Open]({url})")
