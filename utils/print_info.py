import streamlit as st
import graphviz as graphviz

def print_choose():
	st.info("Data Analysis dives deeper into the Data Preprocessing and Tokenization pipeline to \
			give a better visualization about the whole process. This section will try to summarise \
			how the data is taken in its RAW form and change into model ready format.")

	st.markdown("To get started, please choose the approporiate\
				action from the 'Select Function' on the sidebar")

def print_tokenization():
	st.subheader("Information about Tokienization")
	st.markdown("General overview of what we want to achieve: ")
	st.image("./images/note_token.png", use_column_width=True)

	st.subheader("Steps to achieve tokenization")
	st.markdown("As we already have established we will be using MIDI files for our problem. \
				We use MIDI because it’s one of the most popular digital music formats and \
				there’s a ton of these files on the internet. \
				Raw MIDI is represented in bytes. Even when converted to text, \
				it’s not very human readable.\
				Instead of doing that, we will be showing MIDI as for visualizations:")
	st.image("./images/note_pic.png", use_column_width=True)

	st.markdown("Turns out, there’s a couple of gotchas to keep in mind when encoding music files to tokens.\
	 			For text, it’s a pretty straight forward conversion.\
	 			Here’s how you would encode text to a sequence of tokens:")
	st.code("Vocabulary:{'a': 1, 'is': 2, 'language': 3, 'like': 4,'model': 5,'music': 6}")
	st.code("Text: “a music model is like a language model”")
	st.code("Tokenized: [1,6,5,2,4,13,5]")

	st.markdown("It’s a straight one-to-one mapping — word to token. \
				You can do other types of encoding like splitting contractions or byte-pair encoding,\
				but it’s still a sequential conversion.\
				Music however, is best represented in 2D as seen in the above figure")
	st.write("\n")
	st.markdown("Here’s another way of looking at the MIDI using piano roll representation")
	st.image("./images/piano_roll.png",use_column_width=True)
	st.markdown("From here we notice that: ")
	st.markdown("1. A single music note is a collection of values (pitch+duration)")
	st.markdown("2. Multiple notes can be played at a single point in time (polyphony)")
	st.markdown("The objective is to our model using this 2D representation of music. So our tokenization\
				 should be able to handle this 2D representation easily")

	st.subheader("Notes— One to Many")
	st.write("A single music note represents a collection of values: \n - Pitch (C, C#, … A#, B) \n - Duration (quarter note, whole note)")
	st.write("The easiest way to go about this is to encode a single note into a sequence of tokens")
	st.image("./images/one_to_many.png", use_column_width=True)

	st.subheader("Polyphony — Many to One")
	st.write("Another music model called “bachbot” has a clever solution to this. \
			  Play notes sequentially if it’s separated by a special “SEP” token. \
			  If not, play all the notes at once.")
	st.image("./images/bachbot.png", use_column_width=True)

	st.subheader("Putting it all together")
	st.write("When we put these above explained methods and with some magic \
			  (not really, just some manipulations) we get to this final tokenization result")
	st.image("./images/last_img.png", use_column_width=True)
	st.write("This is the same tokenization that we desired in the beginning.")

	st.markdown("reference : https://towardsdatascience.com/creating-a-pop-music-generator-with-the-transformer-5867511b382a", 
				 unsafe_allow_html=True)


def print_lakh():
	st.markdown("The Lakh MIDI dataset is a collection of 176,581 unique MIDI files, \
                45,129 of which have been matched and aligned to entries in the Million Song Dataset.\
                Its goal is to facilitate large-scale music information retrieval, both symbolic \
                and audio content-based.")

	st.markdown("reference : https://colinraffel.com/projects/lmd/", unsafe_allow_html=True)
	
def print_intro():
	st.title("Music Generation Using Neural Networks")
	st.info("This Demo is created to help you understand and visualize our software project in a more \
		interactive and easy way. \n To switch in between different functionalities, please choose from the sidebar. " 
		)
	st.subheader("Software Project in Neural Networks")
	# Semester
	st.subheader("Winter Semester 19/20")

def print_outline():
	st.title("Outline")
	# GOAL
	st.subheader("Goal:")
	st.markdown("Initially proposed: ")
	st.markdown("Generate multi-instrument music using deep learning (for any specific genre)")
	st.markdown("Revised proposal: ")
	st.markdown("Use deep learning techniques to create a system that can predict/create \
				 just piano (single instrument) music, given a clipped music file.")
	# DATA
	st.subheader("Data:")
	st.markdown("Data collection/processing phase took around ~2 weeks. More Analytics about the data will be \
				 discussed in the Data Analysis section. During Phase 1, our take for a single instrument music \
				 generation included us extracting piano melodies from all the music sources we found, since the amount \
				 of data we had for just piano was not enough to train a model like OPENGPT2 or TRANSFORMERXL\
				 from scratch.")
	st.markdown("During Phase 2, we used two major midi file sources without any extraction processes, since the \
				data preprocessing pipeline for model training took care of that in the code. Our major resources \
				for the data in phase 2 included the Lakh Midi Dataset and Reddit Pop midi Dataset (more will \
				discussed in the Data Analysis section)")
	# PHASES
	st.subheader("Phases:")
	st.markdown("Our project, like every other group project evolved during the course. Our initial specifications \
				included using the extracted piano midi files, and hugging face OPENGPT2 API for music generation \
				but after running into problems which delayed our progress, we started to work in parallel \
				with other model architectures and methodolgies to keep the pace of our project intact. The key \
				differences between Phase 1 & Phase 2 are: ")
	st.markdown("1. Model Architecture")
	st.markdown("2. Use of extracted piano files in Phase 1 & use of original files in Phase 2 for the models")

	# Predictions
	st.subheader("Predictions:")
	st.markdown("We generate predictions by clipping a testing file and letting the trained model\
				 predict the rest of the music part by itself.")

def print_gui_info():
	# SECTIONS
	st.title("GUI Information")

	# Introduction
	st.title("Section 1: Introduction")
	st.markdown("This section is the welcome interface for the project. This section will help \
				explain what the GUI is all about, the different sections it has, how are they divided \
				, so that navigation is easy and without hindrance.")
	st.markdown("On the sidebar you have the option to choose between three sub-sections")
	st.markdown("1. GUI Information" )
	st.markdown("2. Outline ")
	st.markdown("3. Literature Review")
	st.subheader("GUI Information ")
	st.markdown("This is the page where the user will land by defualt, which contains all the \
				 information about the GUI for guidance, divided into subsections by the sidebar.")
	st.subheader("Outline")
	st.markdown("This section will provide a brief overview of how the project was approached and its outline.")

	st.subheader("Literature Review")
	st.markdown("This sub section will include the existing literature and methodologies that have been \
				developed and researched for producing music through deep learning.")
	
	# Data Analysis
	st.title("Section 2: Data Analysis")
	st.markdown("This section dives deeper into the Data Processing pipeline and tries to \
				take a visual/audio eplanatory approach. Subsections include ")
	st.markdown("1. Data Info")
	st.markdown("1. Raw MIDI")
	st.markdown("1. Tokenized MIDI")
	st.markdown("1. Play MIDI")

	st.subheader("Data Info")
	st.markdown("Shows the user visual representation of the data collected and the sources used \
				for the project's pipeline")

	st.subheader("RAW MIDI")
	st.markdown("Shows the RAW version of the MIDI file that we choose from the sidebar. Moreover, \
				briefly explains about the music21 library which was used for data processing.")
	
	st.subheader("Tokenized MIDI")
	st.markdown("Shows tokenized version of our midi files and also explains the process of tokenization.")

	st.subheader("Play MIDI")
	st.markdown("Uses the loaded files and plays for the user the original MIDI file and the piano extraction \
				of the MIDI file (some files may be piano in the original as well as extracted version)")
	
	# Model Description
	st.title("Section 3: Model Description")

	# Prediction
	st.title("Section 4: Predictions")

def print_lit_review():
	pass

def print_phase1():
	st.title("Huggingface Transformers")
	st.subheader("Language Modeling")
	st.image("./images/phase1.jpg", use_column_width=True)
	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("Our Plan")
	st.image("./images/phase1_msuic.png", use_column_width=True)

	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("The Model")	
	st.image("./images/openAI-GPT-2-3.png", use_column_width=True)
	st.markdown("""
	* Decoder based transfoermer. \n
	* Auto-regressive in nature
	""")
	
	st.markdown("## Reasons for going with GPT2")
	st.markdown("1.	Text Generation Capipilities")
	st.image("./images/tr.png", use_column_width=True)
	st.markdown("2. replicate the MuseNet Open AI approach")

	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("Used Data")
	st.markdown("We used only Piano data after running the extraction due to")
	st.markdown("* Availability of data")
	st.markdown("* Our search was not done yet")

	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("Problems, why did we shift to Phase ||")
	st.image("./images/phase1_msuic_problems.png", use_column_width=True)
	st.markdown("""
	* Generating features and vocabulary out of step 1
	""")

def print_phase2():
	pass