import time
from decimal import Decimal
# import PIL
from selenium import webdriver
from selenium.webdriver.remote import command
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from PIL import Image, ImageTk
import PySimpleGUI as sg

def click():
    
    #Image
    #Window Setup
    window = Tk()
    window.title("CAB BOT")
    window.configure(background="black")
    window.geometry("560x500")
    #Set columns
    Label(window, text=".", bg="black", fg="black", width=20).grid(row=0, column=1)
    #Labels
    Label (window, text="CAB Bot", bg="black", font="Times 20 bold").grid(row = 0, column=2, sticky=N, pady=10)
    #Brown Username entry
    Label(window, text = "Brown Username:", bg="black", font= "Times 14 bold").grid(row=1, column=2, sticky=W, pady=5)
    brownUsernameEntry = Entry(window, width=20)
    brownUsernameEntry.grid(row=2, column=2, sticky=W, pady=5, ipady=2, ipadx=2)
    #image
    hidePass = PhotoImage(file="showpassword.png")
    hidePass = hidePass.subsample(10)
    #Brown Password entry
    Label(window, text="Brown Password:", bg="black", font="Times 14 bold").grid(row=3, column=2, sticky=W, pady=5)
    brownPasswordEntry = Entry(window, width=20, show="*")
    brownPasswordEntry.grid(row=4, column=2, sticky=W, pady=5, ipady=2, ipadx=2)
    #Show password button
    showPassword = Button(image=hidePass, highlightbackground="black")
    showPassword.grid(row = 4, column=3, sticky=W, ipady=2, ipadx=2)
    #Advising Pin Entry
    Label(window, text="Advising Pin:", bg="black", font="Times 14 bold").grid(row=5, column=2, sticky=W, pady=5)
    advisingPin = Entry(window, width=20)
    advisingPin.grid(row=6, column=2, sticky=W, pady=5, ipady=2, ipadx=2)
    #Number of Courses:
    Label(window, text="Number of Courses:", bg="black", font="Times 14 bold").grid(row=7, column=2, sticky=W, pady=5)
    numberOfCourses = Entry(window, width=20)
    numberOfCourses.grid(row=8, column=2, sticky=W, pady=5, ipady=2, ipadx=2)
    #Enter Button
    enterbutton = Button(window, borderwidth=2,  highlightbackground="black",font="Times 14 bold", text="Register For Courses", width=15, command=click).grid(row=9, column=2, sticky=N, pady=5)
    window.mainloop()

    #Person's username, password, advising
    cab_password = brownPasswordEntry.get()
    cab_username = brownUsernameEntry.get()
    advisingpin = advisingPin.get()
    number_classes = numberOfCourses.get()

    if(cab_password == None or cab_username == None or advisingpin == None or number_classes == None):
        enterbutton.set("Please enter ")

      #Initiate the browser
    browser  = webdriver.Chrome(ChromeDriverManager().install())
    #Open CAB
    browser.get("https://cab.brown.edu")

    #Click sign in
    browser.find_element_by_class_name('anon-only').click()
    #Get new page url
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    newURl = browser.window_handles[-1]
    browser.switch_to.window(newURl)
    #Input username and password
    browser.find_element_by_id("username").send_keys(cab_username)
    browser.find_element_by_id("password").send_keys(cab_password)
    #Click login
    browser.find_element_by_name("_eventId_proceed").click()

    time.sleep(30)

    #Switch back to original window
    window_after = browser.window_handles[0]
    browser.switch_to.window(window_after)
    newURl = browser.window_handles[-1]
    browser.switch_to.window(newURl)
    browser.find_element_by_id("primary-cart-button").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/main/div[2]/div/div[4]/div/button").click()

    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    newURl = browser.window_handles[-1]
    browser.switch_to.window(newURl)
    browser.find_element_by_name("raltpin").send_keys(advisingpin)


    