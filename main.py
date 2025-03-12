import streamlit as st

# Page Configuration for SEO, this is going to be the title which will be displayed on tab bar along with the icon of key which represents the passsword here.
st.set_page_config(
    page_title="Password Strength Meter | Muhammad Shariq", page_icon="🔑",  
)

st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #FFB200;
        }
        .sub-title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #1ABC9C;
        }
        .date {
            text-align: center;
            color: gray;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# The above code is used to set the styles of some elements for better UI of the App. And the classes are used below.

# Main Heading
st.markdown("<div class='title'>GIAIC - Password Strength Meter App</div>", unsafe_allow_html=True) # for the main title
st.markdown("<div class='sub-title'>Created By Muhammad Shariq</div>", unsafe_allow_html=True) # for a sub titile
st.markdown("<div class='date'>Dated: 12 | 3 | 2025</div>", unsafe_allow_html=True)
st.divider() # for showing the completion date of assignment.
# --------------------------------------------------------------------------------

# Making the password input for user to enter password and checks its password strength!

password = st.text_input("Enter Your Password to Check its Strength: ", type="password")

# storing user input in a variable named password this will help us to check its characters and keys in the password for the strength meter.

# -------------------------------------------------------------------------

progress = 0
# Defining the progress variable this will help us in progress bar.

# --------------------------------------------------------------------------

if password:
    if any(char.islower() for char in password):
        progress += 0.2
    if any(char.isupper() for char in password):
        progress += 0.2
    if any(char.isdigit() for char in password):
        progress += 0.2
    if any(char in "!@#$%^&*_-+=|\/.,<>~" for char in password):
        progress += 0.2
    if len(password) > 10:
        progress += 0.2
        
# if password is used to check that the user has surely enter some value in input other vise it will not run. 

# ---------------------------------------------------------------------------

# any(char.islower()) this is used to check if there is any character in lower case.

# for char in password, this will loop through each character in password to check if any character is in lower case. and if any is in lower case so the prograss variable value will increase by 0.2 .

# --------------------------------------------------------------------------

# any(char.isupper()) this is used to check if there is any character in upper case.

# for char in password, works the same but this time checks the upper case. and if any is in upper case so the prograss variable value will increase by 0.2 .

# -----------------------------------------------------------------------------

# any(char.isdigit()) this is used to check if there is any digit in user input (from 0 to 9 only).

# for char in password, works the same but this time checks the digits. and if any digit is in password so the prograss variable value will increase by 0.2 .

# ----------------------------------------------------------------------------

# any(char in "!@#$%^&*_-+=|\/.,<>~"), this is used to check these special characters in the user input.

# for char in password, works the same but this time checks the special characters. and if any special character is in password so the prograss variable value will increase by 0.2 .

# -------------------------------------------------------------------------------

# len(password) > 10) this is used to check the length of password in characters and if it is greater than 10 characters the progress variable value will increase by 0.2 .

# -------------------------------------------------------------------------------

# else , if none of the above conditions is available the else makes sure progress variable value is 0.

# -----------------------------------------------------------------------------

st.progress(progress)

# This is used to define a progress bar with a parameter (progress) so the value of the prograss bar updates with the corresponding value of the variable progress.

# -------------------------------------------------------------------------------

if st.button("Check the strength of the password"):
    if progress == 0:
        st.error("Please Enter a Password")
    elif progress < 0.3:
        st.error("Very Weak Password")
    elif progress < 0.5:
        st.warning("Weak Password")
    elif progress < 0.7:
        st.warning("Medium Password")
    elif progress < 0.9:
        st.warning("Normal Password")
    else:
        st.success("Strong Password")

        

# if st.button makes sure the button is clicked.
# st.button("Check the strength of the password") the value in button is going to be the text which will be displayed on the button.

# if else if and else statements verify the progress value and runs the outpout as per conditions. Else returns error if there is no progress variable value.

# -------------------------------------------------------------------------------

st.markdown("##### Password Strength Guide")
st.info("Use at least 10 characters, mix letters, numbers, and symbols.")


# --------------------------------------------------------------------------

# Footer for copyright section and enhanced UI
st.markdown("<p style='text-align: center; font-size: 14px; color: gray;'>© 2025 Muhammad Shariq - All Rights Reserved</p>", unsafe_allow_html=True)
