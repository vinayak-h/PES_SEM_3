# import streamlit as st
# import mysql.connector
# import hashlib
# import time  # Import the time module for page refresh
# from streamlit_option_menu import option_menu

# # Connect to MySQL database
# conn = mysql.connector.connect(
#     host="localhost",
#     user="vinayak",
#     password="root",
#     database="user_data"
# )
# cursor = conn.cursor()

# # Create users table if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         username VARCHAR(255),
#         password VARCHAR(255)
#     )
# ''')
# conn.commit()

# def register_user(username, password):
#     # Hash the password before storing it
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     # Insert user data into the database
#     cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
#     conn.commit()

# def login_user(username, password):
#     # Hash the password for comparison
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     # Check if the user exists in the database
#     cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
#     return cursor.fetchone() is not None

# def resume_analyzer(username):
#     st.title(f"Welcome to Resume Analyzer, {username}!")

# def main():
#     st.set_page_config(page_title="Resume Analyzer", page_icon=":rocket:", layout="wide")

#     st.title("RESUME-ANALYZER")

#     # Use session_state for login/logout
#     if 'user' not in st.session_state:
#         st.session_state.user = None

#     st.sidebar.title("Navigation")

#     # Always show the wide screen button
#     st.markdown("""
#         <style>
#             .css-17eq0hr {
#                 width: 100%;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     menu_options = ["Home"]

#     # Display Login and Resume Analyzer options if user is not logged in
#     if not st.session_state.user:
#         menu_options.extend(["Login", "Register"])

#     # Display Logout, Register, and Resume Analyzer options only if user is logged in
#     if st.session_state.user:
#         st.sidebar.title("Logged In")
#         menu_options.extend(["Logout", "Register", "Resume Analyzer"])

#     selected_option = option_menu(
#         menu_title="Select Option",
#         options=menu_options,
#         default_index=0,
#         orientation="horizontal",
#     )

#     if selected_option == "Home":
#         st.subheader("Home")
#         st.write("Welcome to the Login and Registration Page.")
#         st.markdown('<i class="bi-house-door-fill"></i> Home', unsafe_allow_html=True)

#     elif selected_option == "Login":
#         st.subheader("Login")

#         # Check for the query parameter indicating successful registration
#         register_success = st.experimental_get_query_params().get('register_success', False)
#         if register_success:
#             st.success("Registration successful. You can now log in.")
#             # Clear the query parameter to avoid unnecessary redirections
#             st.experimental_set_query_params()

#         with st.form("login_form"):
#             username = st.text_input("Username")
#             password = st.text_input("Password", type="password")
#             submit_button = st.form_submit_button("Login")

#         if submit_button:
#             print(f"Attempting login with username: {username} and password: {password}")
#             if login_user(username, password):
#                 st.session_state.user = username  # Store the logged-in user in session_state
#                 st.success(f"Welcome, {username}! Login successful.")
#                 time.sleep(0.2)  # Wait for 2 seconds to simulate a page refresh
#                 st.experimental_rerun()  # Trigger a page refresh after login
#             else:
#                 st.error("Invalid username or password. Please try again.")
#         st.markdown('<i class="bi-box-arrow-in-right"></i> Login', unsafe_allow_html=True)

#     elif selected_option == "Logout":
#         st.subheader("Logout")
#         # Add your logout logic here
#         if st.button("Logout"):
#             st.session_state.user = None  # Clear the user in session_state to simulate logout
#             st.success("Logout successful.")
#             time.sleep(0.2)  # Wait for 2 seconds to simulate a page refresh
#             st.experimental_rerun()  # Trigger a page refresh after logout
#         st.markdown('<i class="bi-box-arrow-left"></i> Logout', unsafe_allow_html=True)

#     elif selected_option == "Register":
#         st.subheader("Register")
#         with st.form("register_form"):
#             new_username = st.text_input("New Username")
#             new_password = st.text_input("New Password", type="password")
#             confirm_password = st.text_input("Confirm Password", type="password")
#             submit_button = st.form_submit_button("Register")

#         if submit_button:
#             if new_password == confirm_password:
#                 register_user(new_username, new_password)
#                 st.success("Registration successful. Redirecting to login page...")
#                 # Set query parameters to redirect to the login page after registration
#                 st.experimental_set_query_params(register_success=True)
#                 time.sleep(0.2)  # Wait for 2 seconds to simulate a page refresh
#                 st.experimental_rerun()  # Trigger a page refresh after registration
#             else:
#                 st.error("Passwords do not match. Please try again.")
#         st.markdown('<i class="bi-box-arrow-in-left"></i> Register', unsafe_allow_html=True)

#     elif selected_option == "Resume Analyzer":
#         # Add your Resume Analyzer logic here
#         resume_analyzer(st.session_state.user)  # Assuming you want to pass the logged-in user to the Resume Analyzer
#         st.markdown('<i class="bi-file-earmark-text"></i> Here you go!', unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()



































import streamlit as st
import mysql.connector
import hashlib
import time  # Import the time module for page refresh
from streamlit_option_menu import option_menu

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="vinayak",
    password="root",
    database="user_data"
)
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255)
    )
''')
conn.commit()

def register_user(username, password):
    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Insert user data into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()

def login_user(username, password):
    # Hash the password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Check if the user exists in the database
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    return cursor.fetchone() is not None

def resume_analyzer(username):
    st.title(f"Welcome to Resume Analyzer, {username}!")

def main():
    st.set_page_config(page_title="Resume Analyzer", page_icon=":rocket:", layout="wide")

    st.title("RESUME-ANALYZER")

    # Use session_state for login/logout
    if 'user' not in st.session_state:
        st.session_state.user = None

    # Always show the wide screen button
    st.markdown("""
        <style>
            .css-17eq0hr {
                width: 100%;
            }
        </style>
    """, unsafe_allow_html=True)

    menu_options = ["Home"]

    # Display Login and Resume Analyzer options if user is not logged in
    if not st.session_state.user:
        menu_options.extend(["Login", "Register"])

    # Display Logout, Register, and Resume Analyzer options only if user is logged in
    if st.session_state.user:
        menu_options.extend(["Logout", "Register", "Resume Analyzer"])

    selected_option = option_menu(
        menu_title="Select Option",
        options=menu_options,
        default_index=0,
        orientation="horizontal",
    )

    if selected_option == "Home":
        st.subheader("Home")
        st.write("Welcome to the Login and Registration Page.")
        st.markdown('<i class="bi-house-door-fill"></i> Home', unsafe_allow_html=True)

    elif selected_option == "Login":
        st.subheader("Login")

        # Check for the query parameter indicating successful registration
        register_success = st.experimental_get_query_params().get('register_success', False)
        if register_success:
            st.success("Registration successful. You can now log in.")
            # Clear the query parameter to avoid unnecessary redirections
            st.experimental_set_query_params()

        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button("Login")

        if submit_button:
            print(f"Attempting login with username: {username} and password: {password}")
            if login_user(username, password):
                st.session_state.user = username  # Store the logged-in user in session_state
                st.success(f"Welcome, {username}! Login successful.")
                time.sleep(0.2)  # Wait for 2 seconds to simulate a page refresh
                st.experimental_rerun()  # Trigger a page refresh after login
            else:
                st.error("Invalid username or password. Please try again.")
        st.markdown('<i class="bi-box-arrow-in-right"></i> Login', unsafe_allow_html=True)

    elif selected_option == "Logout":
        st.subheader("Logout")
        # Add your logout logic here
        if st.button("Logout"):
            st.session_state.user = None  # Clear the user in session_state to simulate logout
            st.success("Logout successful.")
            time.sleep(0.2)  # Wait for 2 seconds to simulate a page refresh
            st.experimental_rerun()  # Trigger a page refresh after logout
        st.markdown('<i class="bi-box-arrow-left"></i> Logout', unsafe_allow_html=True)

    elif selected_option == "Register":
        st.subheader("Register")
        with st.form("register_form"):
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit_button = st.form_submit_button("Register")

        if submit_button:
        # Basic validation
            if not new_username:
                st.error("Username cannot be empty. Please enter a username.")
            elif not new_password:
                st.error("Password cannot be empty. Please enter a password.")
            elif new_password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            else:
            # Additional validation or checks can be added here
                register_user(new_username, new_password)
                st.success("Registration successful. Redirecting to login page...")
            # Set query parameters to redirect to the login page after registration
                st.experimental_set_query_params(register_success=True)
                time.sleep(0.2)  # Wait for 2 seconds to simulate a page refresh
                st.experimental_rerun()  # Trigger a page refresh after registration
        st.markdown('<i class="bi-box-arrow-in-left"></i> Register', unsafe_allow_html=True)

    elif selected_option == "Resume Analyzer":
        # Add your Resume Analyzer logic here
        resume_analyzer(st.session_state.user)  # Assuming you want to pass the logged-in user to the Resume Analyzer
        st.markdown('<i class="bi-file-earmark-text"></i> Here you go!', unsafe_allow_html=True)

if __name__ == "__main__":
    main()








