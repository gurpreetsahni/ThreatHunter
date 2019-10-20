from virustotal_python import Virustotal
from pprint import pprint
import json
import streamlit as st
url=st.text_input('Enter the url')
vtotal = Virustotal("939b160778c93a24ed0985dbc90a98d2def25cf82ed92046a95cfe553f63ade1")
url_scan = vtotal.url_report([url])
a=url_scan['json_resp']['positives']
if(a>0):
    print('malicious website')
else:
    print('Clean Website')
