from pathlib import Path
import streamlit as st

from csv_profiler.error_handler import check_csv_file
from csv_profiler.profile import basic_profile
from csv_profiler.render import render_json, render_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if "report" not in st.session_state:
    st.session_state.report = None
if "report_json" not in st.session_state:
    st.session_state.report_json = None
if "report_md" not in st.session_state:
    st.session_state.report_md = None

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    file_bytes = uploaded_file.getvalue()
    file_text = file_bytes.decode("utf-8", errors="replace")

    if st.button("Profile CSV"):
        st.session_state.report = None
        st.session_state.report_json = None
        st.session_state.report_md = None

        rows, error_message = check_csv_file(file_text)
        if error_message:
            st.error(error_message)
            st.stop()

        report = basic_profile(rows)

        st.session_state.report = report
        st.session_state.report_json = render_json(report)
        st.session_state.report_md = render_markdown(report)

    if st.session_state.report is not None:
        base = Path(uploaded_file.name).stem
        md_name = f"{base}.md"
        json_name = f"{base}.json"

        tab_md, tab_json = st.tabs(["Markdown", "JSON"])

        with tab_md:
            st.download_button(
                "Download Markdown report",
                data=st.session_state.report_md,
                file_name=md_name,
                mime="text/markdown",
            )
            st.markdown(st.session_state.report_md)

        with tab_json:
            st.download_button(
                "Download JSON report",
                data=st.session_state.report_json,
                file_name=json_name,
                mime="application/json",
            )
            st.json(st.session_state.report)


else:
    st.info("Please upload a CSV file to profile.")
