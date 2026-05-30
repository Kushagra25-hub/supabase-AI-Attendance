import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    
    st.markdown("""
<style>
                

/* Dialog text */
[data-testid="stDialog"] h1,
[data-testid="stDialog"] h2,
[data-testid="stDialog"] h3,
[data-testid="stDialog"] h4,
[data-testid="stDialog"] p,
[data-testid="stDialog"] label {
    color: white !important;
}


                
/* Dialog background */
[data-testid="stDialog"] > div {
    background-color: #0B1020 !important;
}

/* Input text */
[data-testid="stDialog"] input {
    color: white !important;
}

/* Toast container */
[data-testid="stToast"] {
    background: #5865F2 !important;
    color: white !important;
    border-radius: 16px !important;
    border: 2px solid #EB459E !important;
    padding: 12px !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25) !important;
}

/* Toast text */
[data-testid="stToast"] p,
[data-testid="stToast"] span,
[data-testid="stToast"] div {
    color: white !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
}

/* Toast icon */
[data-testid="stToast"] svg {
    fill: white !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h1 {
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                font-family: 'Climate Crisis', sans-serif !important;
                margin-bottom:0rem !important;
                color:black !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color:black !important;
             }

h3, h4, p {
    font-family: 'Outfit', sans-serif !important;
    color:black !important;
}
                

            /* ---------- Buttons ---------- */

button {
    border-radius: 1.5rem !important;
    background-color: #5865F2 !important;
    border: none !important;
    color: white !important;
    transition: all 0.25s ease !important;
}

/* Force ALL nested content inside buttons */

button * {
    color: white !important;
    fill: white !important;
    stroke: white !important;
}


                
                
/* Secondary buttons */

button[kind="secondary"] {
    background-color: #EB459E !important;
}


/* Tertiary buttons */

button[kind="tertiary"] {
    background-color: black !important;
}


/* Hover */

button:hover {
    transform: scale(1.05);
    opacity: .95;
}
        </style>  

                """
            ,unsafe_allow_html=True)
    




