import streamlit as st

from streamlit_option_menu import option_menu
import sqlite3

def home():
    st.title("Home")
    st.write("Welcome Karan to the Home page!")
def sign_in():
    st.title("Sign IN")
    st.write("Please enter your credentials to sign in.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign IN"):
        try:
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username, password))
            user = cur.fetchone()
            conn.close()
            if user:
                conn = sqlite3.connect('users.db')
                cur = conn.cursor()
                cur.execute("SELECT * FROM users")
                allUsers = cur.fetchall()
                conn.close()
                st.header("User List")
                st.dataframe(allUsers)
        except sqlite3.Error as e:
            st.error(f"An error occurred: {e}")
 

def sign_up():
    st.title("Sign UP")
    st.write("Create a new account.")
    username = st.text_input("Username")
    age = st.number_input("Age", min_value=0, max_value=120)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign UP"):
        try:
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT,age INTEGER,email TEXT,password TEXT)")
            cur.execute("INSERT INTO users (username, age, email, password) VALUES (?, ?, ?, ?)",
                        (username, age, email, password))
            conn.commit()
            conn.close()
            st.success("You have successfully signed up!")
        except sqlite3.Error as e:
            st.error(f"An error occurred: {e}")

def contact_us():
    st.title("Contact Us")
    st.write("Get in touch with us.")

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Sign IN','Sign UP','Contact Us'], 
        icons=['house', 'box-arrow-in-right','person-add','envelope'], menu_icon="cast", default_index=0)
if selected == 'Home':
    home()
elif selected == 'Sign IN':
    sign_in()
elif selected == 'Sign UP':
    sign_up()
elif selected == 'Contact Us':
    contact_us()