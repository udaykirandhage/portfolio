import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image


st.set_page_config(page_title="Portfolio",layout="wide")

def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
selectedNavbar=option_menu(menu_title="My Portfolio",options=["About","Skills","projects","Contact"],orientation="horizontal",default_index=0,styles={
            "container": {"padding": "3!important","width":"100%"},
            "icon": {"color": "orange", "font-size": "15px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#E9DCCF","backgroundcolor":"transparent"}},)

if(selectedNavbar == "About"):
    st.write()
    col1,col2=st.columns(2)
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.header("Hi , Iam  MD UdayKiran ")
        for i in range(7):
            st.write("")
    
        
        
        st.write("""An Aspiring Student currently pursuing my Bachelors Degree (Btech) in Malla Reddy Engineering College-MREC",
                in Information Technology - IT Branch , Iam eager to bring my passion towards building applications into a 
                career by working with a reputed organisation and gain more Knowledge.
                Iam Mostly Interested In Web Development I have built many Small applications Using Front End Technologies
                such as HTML CSS JS BOOTSTRAP ..
                I progress slowly because I would like to do hands on every topic that I learn so that I would be 
                Mastering the Technology.

                
                """)
        st.write("")
        st.write("""If your Looking for a motivated and passionate,skilled Developer Then Your at The Right Position
                    I would Love to Interact with you 😊 """)
    with col2:
        lottie_About=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_au98facn.json")
        st_lottie(lottie_About,key="about")
if (selectedNavbar == "Skills"):
     
     st.header("My skills and Certifications")
     st.markdown("___________________________")
     col1,col2=st.columns(2)
     with col2:
          
          
          for i in range(9):
               st.write("")
          lottie_skills=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_tno6cg2w.json")
          st_lottie(lottie_skills,key="skills")
     with col1:
          st.header("Technical & Non Technical Skills")
          st.write("")
          st.write("")
        
          
          
          for i in range(7):
               st.write("")
          langs=["Python","HTML","CSS","BOOTSTRAP","JAVA SCRIPT","Communication"]
          for i in langs:
               st.header(" "*3+i)
     st.write("")
     st.write("")
     st.write("_________________________________")
     
     st.header("My Certifications!")
     st.write(" ")
     st.write("I love learning New Technologies so Take up Online courses and make use of it to Build new applications!")
     st.write("1. Build Your Own Static Webpages , Nxt Wave"+" "+"  "+  "[View](https://certificates.ccbp.in/academy/static-website?id=OXALQLJBVC)")
     st.write("2. Build Your Own Responsive Webpages , Nxt Wave"+" "+"  "+  "[View](https://certificates.ccbp.in/academy/build-your-own-responsive-website?id=QSQLRFNRWO)")
     st.write("3. Build Your Own Dynamic Webpages , Nxt Wave"+" "+"  "+  "[View](https://certificates.ccbp.in/academy/build-your-own-responsive-website?id=QSQLRFNRWO)")
     st.write("4. Programming Foundations Python , Nxt Wave"+" "+"  "+  "[View](https://certificates.ccbp.in/academy/programming-foundations-with-python?id=VFHDGSUSXQ)")
     st.write("5. Xpm 4.0 Fundamentals , Nxt Wave"+" "+"  "+  "[View](https://certificates.ccbp.in/academy/xpm-4-0-fundamentals?id=KWNSQHOTTO)")
     st.write("6. Python Zero To Hero , Udemy"+" "+"  "+  "[View](https://www.udemy.com/certificate/UC-7b2573cb-845d-4c4b-a224-6f624dda2efb/)")
     st.write("7. MTA ,Microsoft Technology"+" "+"  "+  "[View](https://www.credly.com/badges/2084a451-c4c6-40ec-aa50-5e726d47b285/linked_in_profile)")
     st.write("8. Python , Hacker rank"+" "+"  "+  "[View](https://www.hackerrank.com/certificates/8c72e766f85a)")

if selectedNavbar =="Contact":
        st.header(":mailbox: Mail me !")
        st.write("Lets Get Connected!")
        with st.sidebar:
             st.header("Contact Me")
             lottie_contactus=load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_qmaetdpn.json")
             st.write("____________________________________________")
             st.write("Fill Out This Mail and lets Get connected !!!")
             st_lottie(lottie_contactus)
        contact_form="""
        <form action="https://formsubmit.co/udaykirandhage@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name"  placeholder="Your Name"required>
            <input type="email" name="email" placeholder="Your Gmail" required>
            <input type="text" name="number" placeholder="Your Number" required>
            <textarea name="Address" placeholder=" write Your message"></textarea>
            <button type="submit">Send</button>
        </form> """
        st.markdown(contact_form,unsafe_allow_html=True)

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        local_css("style.css")
if selectedNavbar =="projects":
     st.write()
     st.header("Projects")
     col1,col2=st.columns(2)
     with col2:
        lottie_pro=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yCjSOH1fA9.json")
        st_lottie(lottie_pro,key="pro")
     with col1:
        for i in range(12):
           st.write("")
        st.write("""As a student Building  projects makes me feel confident that I Have gained some knowledge
                        over that topic so I try to do hands on them in my free time and would love to depoly and share them to Family 
                              and friends .This certainly Makes me feel confident and helps me getting feedback and suggestions to improve my website      """)
     st.write("_________________________________________")
     st.header("Here are my few projects List ,CheckOut!")
     for i in range(3):
        st.write("")
     col1,col2=st.columns(2)
     with col1:
        st.header("[1.SunriseAvenue](https://roombook.ccbp.tech/)")
        st.video("vid1.mp4")
        st.write("")
        st.write("")
     st.write("""This is a static web app for Mobile phone users
                     it is usefull for the user to know the available flats near to them 
                     and here we try to pass the user details to the brokers and we would call back them based on the details given by them
                                                                                                           """)
     st.write("* **Technologies used**  :- HTML  , CSS , PYTHON , BOOTSTRAP , JAVASCRIPT")
     st.write("* **Credntials** ph_no:-9390483324 , username:-uday_29  ")

     st.write("** *View This project SunRise Avenue Here [View  Here!](https://roombook.ccbp.tech/)** *")

     for i in range(3):
        st.write("")
     col1,col2=st.columns(2)
     with col1:
        st.header("[2.Crypto web app](https://cryptro-webapp29.onrender.com)")
        st.video("vid1.mp4")
        st.write("")
        st.write("")
     st.write("""This is a Data science application ,This app serves as Information center to check the current
                        market Trends of the crypto currencies.This application is a dynamic application and  user friendly
                        The data is  webscrapped from the coinmarketcap website and the rhe user interacts is a
                        real time data .Here My main aim is to do handson on Data Visualizations of what I have learnt Till date 
                                                                                                           """)
     st.write("* **Technologies used**  : Streamlit Python CSS")
     

     st.write("** *View This project Crypto web app Here [View  Here!](https://cryptro-webapp29.onrender.com)** *")
            

