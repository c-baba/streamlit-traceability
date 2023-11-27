import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner  


st.write("Please Scan Barcode of Pallet")
qr_code = qrcode_scanner(key='qrcode_scanner')  

if qr_code:  
  st.write(qr_code)
  st.table({qr_code : "1"})
