## First we need to install these packages using pip install <package-name>

########################## Importing the Packages ####################3

import streamlit as st  # this is the core package in the project
import pandas as pd
import base64, random
import time,datetime
import pymysql
import os
import socket
import platform
import geocoder
import secrets
import io,random
import plotly.express as px # to create visualisations at the admin session
import plotly.graph_objects as go
from geopy.geocoders import Nominatim


######################## should import the spacy  """Getting some error Need to re Check!!!!"""
# import spacy
# nlp = spacy.load('/home/vinayak/Desktop/Project/AI-Resume-Analyzer/App/en_core_web_sm-3.7.1/en_core_web_sm/en_core_web_sm-3.7.1')


######################## To parse the pdf file ########
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
from streamlit_tags import st_tags
from PIL import Image

# pre stored data for prediction purposes """Courses.py""" 
from Courses import ds_course,web_course,android_course,ios_course,uiux_course,resume_videos,interview_videos


###### NLP package importing ######
import nltk
nltk.download('stopwords', download_dir='/home/vinayak/Desktop/Project_Test/App')





























######################################## PREPROCESSING FUNCTIONS #######################
def get_csv_download_link(df,filename,text):
    """
     Generates a download link for a Pandas DataFrame in CSV format.

    Parameters:
    - df (pd.DataFrame): The Pandas DataFrame to be converted to a CSV file.
    - filename (str): The name for the downloaded CSV file.
    - text (str): The text or label for the download link.

    Returns:
    str: An HTML link (<a>) with an embedded data URL for downloading the CSV file.

    Example:
    '''python
    import pandas as pd

    # Create a Pandas DataFrame (df)
    data = {'Name': ['raju', 'ramu', 'vinayak'], 'Age': [25, 30, 22]}
    df = pd.DataFrame(data)

    # Generate a download link for the DataFrame
    link = get_csv_download_link(df, 'my_data.csv', 'Download CSV')

    # Use the link in your HTML or display it
    print(link)
    '''
    """
    
    csv = df.to_csv(index=False)

    ## bytes conversions
    b64 = base64.b64encode(csv.encode()).decode()      
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href








######################### Reads Pdf file and check_extractable ##########################

def pdf_reader(file):
    """
    Reads a PDF file and extracts text content.

    Parameters:
    - file (str): The path to the PDF file to be read.

    Returns:
    str: The extracted text content from the PDF file.

    Example:
    ```python
    # Read text from a sample PDF file
    pdf_file_path = 'path/to/sample.pdf'
    extracted_text = pdf_reader(pdf_file_path)
    print(extracted_text)
    ```
    """
    # Create PDF resource manager, fake file handle, and text converter
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    # Open the PDF file and process each page
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)

        # Get the extracted text from the fake file handle
        text = fake_file_handle.getvalue()

    # Close open handles
    converter.close()
    fake_file_handle.close()

    return text





##################################### SHOWING UPLOADED FILE PATH TO VIEW pdf_display ###################################
def show_pdf(file_path):
    
    """
    Displays a PDF file in the Streamlit app using an iframe.

    Parameters:
    - file_path (str): The path to the PDF file to be displayed.

    Example:
    ```python
    # Display a PDF file in the Streamlit app
    pdf_file_path = 'path/to/sample.pdf'
    show_pdf(pdf_file_path)
    ```
    """
    
    with open(file_path, "rb") as f:
        # Converting PDF file to base64 encoding
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Creating an HTML iframe to display the PDF
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    
    # Rendering the PDF display in the """Streamlit app"""
    st.markdown(pdf_display, unsafe_allow_html=True)










############################### course recommendations which has data already loaded from Courses.py #########################################################
def course_recommender(course_list):
    """
    Displays recommendations for courses and certificates.

    Parameters:
    - course_list (list): A list of tuples containing course names and links.

    Returns:
    - list: A list of recommended course names.

    Example:
    ```python
    # Provide a list of courses with names and links
    courses = [("Course 1", "https://www.example.com/course1"),
               ("Course 2", "https://www.example.com/course2"),
               ("Course 3", "https://www.example.com/course3")]

    # Display 5 course recommendations
    recommended_courses = course_recommender(courses)
    ```
    """
    st.subheader("**Courses & Certificates Recommendations 👨‍🎓**")
    c = 0
    rec_course = []

    # Slider to choose the number of course recommendations
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 5)
    
    # Shuffle the course list for randomness
    random.shuffle(course_list)
    
    # Display recommended courses
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    
    return rec_course





################################ DATA-BASE STUFFS #####################

######################## sql connector ##############################
connection = pymysql.connect(host='localhost', user='root', password='', db='cv')
cursor = connection.cursor()


# inserting miscellaneous data, fetched results, prediction and recommendation into user_data table
def insert_data(sec_token, ip_add, host_name, dev_user, os_name_ver, latlong, city, state, country, act_name, act_mail, act_mob, name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills, courses, pdf_name):
    """
    Inserts data into the 'user_data' table in the database.

    Parameters:
    - sec_token (str): Security token.
    - ip_add (str): IP address.
    - host_name (str): Host name.
    - dev_user (str): Device user.
    - os_name_ver (str): Operating system name and version.
    - latlong (str): Latitude and longitude.
    - city (str): City.
    - state (str): State.
    - country (str): Country.
    - act_name (str): Active user name.
    - act_mail (str): Active user email.
    - act_mob (str): Active user mobile.
    - name (str): User name.
    - email (str): User email.
    - res_score (str): Resume score.
    - timestamp (str): Timestamp of the data.
    - no_of_pages (str): Number of pages in the PDF.
    - reco_field (str): Recommended field.
    - cand_level (str): Candidate level.
    - skills (str): Skills.
    - recommended_skills (str): Recommended skills.
    - courses (str): Courses.
    - pdf_name (str): PDF file name.
    """
    DB_table_name = 'user_data'
    insert_sql = f"INSERT INTO {DB_table_name} VALUES (0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    rec_values = (str(sec_token), str(ip_add), host_name, dev_user, os_name_ver, str(latlong), city, state, country, act_name, act_mail, act_mob, name, email, str(res_score), timestamp, str(no_of_pages), reco_field, cand_level, skills, recommended_skills, courses, pdf_name)
    cursor.execute(insert_sql, rec_values)
    connection.commit()


# inserting feedback data into user_feedback table
def insertf_data(feed_name, feed_email, feed_score, comments):
    """
    Inserts feedback data into the 'user_feedback' table in the database.

    Parameters:
    - feed_name (str): Feedback provider's name.
    - feed_email (str): Feedback provider's email.
    - feed_score (str): Feedback score.
    - comments (str): Feedback comments.
    """
    DBf_table_name = 'user_feedback'
    insertfeed_sql = f"INSERT INTO {DBf_table_name} VALUES (0, %s, %s, %s, %s, %s)"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rec_values = (feed_name, feed_email, feed_score, comments, timestamp)
    cursor.execute(insertfeed_sql, rec_values)
    connection.commit()




###### Setting Page Configuration (favicon, Logo, Title) ######
"""
Sets the configuration for the Streamlit application page.
Configuration includes page title, favicon, and logo.
"""
# Set page title, favicon, and logo
st.set_page_config(
    page_title="Resume Analyzer",
    page_icon='./PATH/TO/LOGO/PHOTO', ########## Add logo!!!####
)



##### Main function ###### 


def Main():
    print("this is the dummy main method")