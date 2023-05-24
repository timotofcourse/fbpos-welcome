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

def launch_timeshift():
    os.system('pkexec timeshift-gtk')


# Application Widgets

welcome_label = customtkinter.CTkLabel(welcome, text='Welcome to FBP OS. We will help you to configure your new system')
welcome_label.pack(padx=20, pady=10)

settings_button = customtkinter.CTkButton(welcome, text='Settings', command=system_settings)
settings_button.pack(padx=20, pady=10)

timeshift = customtkinter.CTkButton(welcome, text='Backup and restore', command=launch_timeshift)
timeshift.pack(padx=20, pady=10)

# Launch Application

welcome.mainloop()