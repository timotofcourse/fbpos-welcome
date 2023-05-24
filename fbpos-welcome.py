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

discover = os.path.exists('usr/bin/plasma-discover')
software = os.path.exists('usr/bin/gnome-software')
mint = os.path.exists('mintinstall')

# Functions

def system_settings():
    os.system('systemsettings')

def launch_timeshift():
    os.system('pkexec timeshift-gtk')

def install_nvidia_driver():
    os.system('pkexec pacman -S nvidia nvidia-utils nvidia-settings')
    os.system('zenity --info --text="Nvidia Driver Installed')

def install_nvidia_optimus():
    os.system('pkexec pacman -S bumblebee')
    os.system('yay -S envycontrol optimus-manager optimus-manager-qt-kde')
    os.system('zenity --info --text="Nvidia Optimus Installed')

def launch_software_center():
    if discover:
        os.system('plasma-discover')
    elif software:
        os.system('gnome-software')
    elif mint:
        os.system('mintinstall')
    else:
        os.system('zenity --info --text="No software center found"')


def install_games():
    os.system('pkexec pacaman -S steam heroic-games-launcher-beta pcsx2 minecraft-launcher')
    os.system('zenity --info --text="Game Set Installed"')

def install_office_suite():
    os.system('pkexec pacman -S wps-office')
    os.system('zenity --info --text="Office Suite Installed"')

def install_security_software():
    os.system('pkexec pacman -S authy bitwarden')
    os.system('zenity --info --text="Security Set Installed"')

# Application Widgets

welcome_label = customtkinter.CTkLabel(welcome, text='Welcome to FBP OS. We will help you to configure your new system')
welcome_label.pack(padx=20, pady=10)

settings_button = customtkinter.CTkButton(welcome, text='Settings', command=system_settings)
settings_button.pack(padx=20, pady=10)

timeshift = customtkinter.CTkButton(welcome, text='Backup and restore', command=launch_timeshift)
timeshift.pack(padx=20, pady=10)

nvidia_driver = customtkinter.CTkButton(welcome, text='Install Nvidia Driver (nvidia users only)', command=install_nvidia_driver)
nvidia_driver.pack(padx=20, pady=10)

bumblebee = customtkinter.CTkButton(welcome, text='Install Nvidia Optimus (Hybrid graphics only)', command=install_nvidia_optimus)
bumblebee.pack(padx=20, pady=10)

software_center = customtkinter.CTkButton(welcome, text='Software Center', command=launch_software_center)
software_center.pack(padx=20, pady=10)

install_game_launchers = customtkinter.CTkButton(welcome, text='Install some game launchers', command=install_games)
install_game_launchers.pack(padx=20, pady=10)

office_suite = customtkinter.CTkButton(welcome, text='Install Office Suite', command=install_office_suite)
office_suite.pack(padx=20, pady=10)

security_software = customtkinter.CTkButton(welcome, text='Install Account Security Software', command=install_security_software)
security_software.pack(padx=20, pady=10)

# Launch Application

welcome.mainloop()