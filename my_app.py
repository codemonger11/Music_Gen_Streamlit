import os
import time

from utils.utils import *

def main():
    st.sidebar.title("What to do:")
    app_mode = st.sidebar.radio("Go to", ["Introduction", "Data Analysis",
                                          "Model Description", "Predictions"])

    if app_mode == "Data Analysis":
        st.title("Data Analysis of MIDI Files")
        select_action = st.sidebar.selectbox("Select function", ["Choose", "Data Info", 
                                                                "Raw MIDI", "Tokenized MIDI", "Play MIDI"])
        data_functions(select_action)

    elif app_mode == "Model Description":
        phase = st.sidebar.selectbox("Choose Phase", ["Phase I", "Phase II"])
        if phase == "Phase I":
            st.title("Phase I")
            print_phase1()
        else:
            st.title("Phase II")
            print_phase2()
    elif app_mode == "Predictions":
    	st.title("Music Generation Predictions")
    	predictions()
    elif app_mode == "Introduction":
        print_intro()
        intro()

if __name__ == "__main__":
    main()