#!/usr/bin/env python

import sys
import os
import tkinter
import customtkinter

# Application Properties

welcome = customtkinter.CTk()
welcome.geometry('500x500')
welcome.title('FBP OS Welcome')
welcome._set_appearance_mode('System')

# Functions

def system_settings():
    os.system('systemsettings')



# Application Widgets

welcome_label = customtkinter.CTkLabel(welcome, text='Welcome to FBP OS. We will help you to configure your new system')
welcome_label.pack()

settings_button = customtkinter.CTkButton(welcome, text='Settings', command=system_settings)
settings_button.pack()

# Launch Application

welcome.mainloop()