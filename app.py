import streamlit as st
from phone_logic import get_number, check_phone, find_interpretations, check_input

st.set_page_config(page_title="Number Interpreter",layout="centered")

st.markdown("""
<style>
    .stApp {
        background-color: #0d1424;
        color: #e8eef8;
    }

    .block-container {
        max-width: 850px;
        padding-top: 3rem;
    }

    h1, h2, h3 {
        color: #f3f7ff !important;
    }

    div[data-testid="stMetric"] {
        background-color: #18243a;
        border: 1px solid #293b57;
        border-radius: 12px;
        padding: 18px;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff;
    }

    .subtitle {
        color: #a6b8d0;
        font-size: 18px;
        margin-bottom: 20px;
    }
</style>

""", unsafe_allow_html=True)

st.title("Number Interpreter")
st.markdown(
    '<p class="subtitle">Number Interpretation & Greek Phone Validation</p>',
    unsafe_allow_html=True
)
st.write("Explore possible interpretations of numeric sequences and validate greek phone numbers")

st.divider()
number_input = st.text_input(
    "Enter numeric groups:",
    placeholder= "2 10 69 30 6 6 4"
)
if "results" not in st.session_state:
    st.session_state.results = None

if st.button("Analyze Number", type="primary"):
    if not check_input(number_input):
        st.error("Invalid input. Use groups of 1 to 3 digits.")
        st.session_state.results = None
    else:
        st.session_state.number = get_number(number_input)
        st.session_state.results = find_interpretations(number_input)

if st.session_state.results is not None:
    results = st.session_state.results
    number = st.session_state.number

    valid_count = sum(check_phone(result) for result in results)

    st.subheader("Analysis Results")
    st.write("**Recognized number:**", number)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total", len(results))
    col2.metric("Valid", valid_count)
    col3.metric("Invalid", len(results) - valid_count)

    st.subheader("Possible Interpretations")

    selected_filter = st.radio(
        "Filter results",
        ["All", "Valid", "Invalid"],
        horizontal=True
    )

    if selected_filter == "Valid":
        displayed_results = [result for result in results if check_phone(result)]
    elif selected_filter == "Invalid":
        displayed_results = [result for result in results if not check_phone(result)]
    else:
        displayed_results = results

    for result in displayed_results:
        if check_phone(result):
            st.success(f"{result} - VALID")
        else:
            st.error(f"{result} - INVALID")

st.divider()

with st.expander ("Phone Number Validation Rules"):
    st.write("10 digits starting with 2 or 69")
    st.write("14 digits starting with 00302 or 003069")

st.caption("NumInterpret | Python & Streamlit")