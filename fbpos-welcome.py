#!/usr/bin/env python

import sys
import os
import tkinter
import customtkinter
import CTkMessagebox
import platform

# Application Properties

welcome = customtkinter.CTk()
welcome.geometry('500x600')
welcome.title('FBP OS Welcome')
welcome._set_appearance_mode('System')

# Software stores

discover = os.path.exists('usr/bin/plasma-discover')
software = os.path.exists('usr/bin/gnome-software')
mint = os.path.exists('usr/bin/mintinstall')

# AUR Helper

yay_bin = '/usr/bin/yay'

# Distro ID

distro_id = ''

# Check for yay and install if it's not installed

if not os.path.exists(yay_bin):
    print('yay not found')
    print('Checking if you are running FBP OS or Arch Linux')
    if distro_id == 'fbpos':
        print('Installing yay on FBP OS...')
        os.system('pkexec pacman -S yay')
    elif distro_id == 'arch':
        print('Installing yay on Arch Linux')
        os.system('pkexec pacman -S go base-devel pacman-contrib git')
        os.system('git clone https://aur.archlinux.org/yay.git')
        os.system('cd ./yay/')
        os.system('updpkgsums')
        os.system('makepkg --install')
    else:
        print('Not on FBP OS or Arch Linux')

    

# Custom messagebox function

def infobox(text):
    CTkMessagebox.CTkMessagebox(title="Info", message=text)


# Open settings

def system_settings():
    os.system('systemsettings')

# Open timeshift

def launch_timeshift():
    os.system('pkexec timeshift-gtk')

# Open software store

def launch_software_center():
    if discover:
        os.system('plasma-discover')
    elif software:
        os.system('gnome-software')
    elif mint:
        os.system('mintinstall')
    else:
        infobox(text="No software center found")
        
# Install a game meta-package

def install_games():
    os.system('pkexec pacaman -S steam heroic-games-launcher-beta pcsx2 minecraft-launcher')
    infobox(text="Game Set Installed")

# Install office suite

def install_office_suite():
    os.system('pkexec pacman -S wps-office')
    infobox(text="Office Suite Installed")

# Install Authy and Bitwarden

def install_security_software():
    os.system('pkexec pacman -S authy bitwarden')
    infobox(text="Security Set Installed")

# Install Rustdesk for remote control (not working on wayland)

def remote_control_software():
    os.system('pkexec pacman -S rustdesk')
    infobox(text="Remote Control Set Installed")

# Install Virtual Machine Guest Drivers

def install_vmware_guest_addons():
    os.system('pkexec pacman -S open-vm-tools')
    os.system('systemctl enable --now vmtoolsd.service vmware-vmblock-fuse.service')
    infobox(text="Vmware guest addons installed. It\'s recommend that you restart your pc.")

def install_virtualbox_addons():
    os.system('pkexec pacman -S virtualbox-guest-utils xf86-video-vmware virtualbox-guest-utils-nox')
    os.system('systemctl enable --now vboxservice.service')
    os.system('systemctl enable --now systemd-modules-load.service')
    infobox(text="Virtualbox guest addons installed. It's recommend that you restart your pc.")

# Fix pacman keys

def fix_pacman():
    os.system('fix-pacman-keyring')
    fixed_pacman_keys()
    
def fixed_pacman_keys():
    CTkMessagebox.CTkMessagebox(message="Pacman keys fixed.",
                  icon="check", option_1="OK")

# Install Proprietary nvidia driver

def sure_install_nvidia_driver():

    nvidiamsg = CTkMessagebox.CTkMessagebox(title="Are you sure?", message="Are you sure you want to install nvidia driver?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    nvidiaresponse = nvidiamsg.get()
    
    if nvidiaresponse=="Yes":
        os.system('pkexec pacman -S nvidia nvidia-utils nvidia-settings')
        infobox(text="Nvidia Driver Installed")
    else:
        pass

# Install nvidia tools for hybrid graphics

def sure_install_hybrid():

    optimusmsg = CTkMessagebox.CTkMessagebox(title="Are you sure?", message="Are you sure you want to install nvidia otimus? This is only for hybrid graphic cards",
                        icon="warning", option_1="Cancel", option_2="No", option_3="Yes")
    optimusresponse = optimusmsg.get()
    
    if optimusresponse=="Yes":
        os.system('pkexec pacman -S bumblebee')
        os.system('yay -S envycontrol optimus-manager optimus-manager-qt-kde')
        infobox(text="Nvidia Optimus Installed")     
    else:
        pass


# Application Widgets

welcome_label = customtkinter.CTkLabel(welcome, text='Welcome to FBP OS. We will help you to configure your new system')
welcome_label.pack(padx=20, pady=10)

settings_button = customtkinter.CTkButton(welcome, text='Settings', command=system_settings)
settings_button.pack(padx=20, pady=10)

fix_pacman_keys = customtkinter.CTkButton(welcome, text='Fix Pacman Keys', command=fix_pacman)
fix_pacman_keys.pack(padx=20, pady=10)

timeshift = customtkinter.CTkButton(welcome, text='Backup and restore', command=launch_timeshift)
timeshift.pack(padx=20, pady=10)

nvidia_driver = customtkinter.CTkButton(welcome, text='Install Nvidia Driver (nvidia users only)', command=sure_install_nvidia_driver)
nvidia_driver.pack(padx=20, pady=10)

bumblebee = customtkinter.CTkButton(welcome, text='Install Nvidia Optimus (Hybrid graphics only)', command=sure_install_hybrid)
bumblebee.pack(padx=20, pady=10)

software_center = customtkinter.CTkButton(welcome, text='Software Center', command=launch_software_center)
software_center.pack(padx=20, pady=10)

install_game_launchers = customtkinter.CTkButton(welcome, text='Install some game launchers', command=install_games)
install_game_launchers.pack(padx=20, pady=10)

office_suite = customtkinter.CTkButton(welcome, text='Install Office Suite', command=install_office_suite)
office_suite.pack(padx=20, pady=10)

security_software = customtkinter.CTkButton(welcome, text='Install Account Security Software', command=install_security_software)
security_software.pack(padx=20, pady=10)

rustdesk = customtkinter.CTkButton(welcome, text='Install Remote Control Software', command=remote_control_software)
rustdesk.pack(padx=20, pady=10)

vmware_addons = customtkinter.CTkButton(welcome, text='Install Vmware Addons (Vmware virtual machines only)', command=install_vmware_guest_addons)
vmware_addons.pack(padx=20, pady=10)

virtualbox_addons = customtkinter.CTkButton(welcome, text='Install Virtualbox Addons (Virtualbox virtual machines only)', command=install_virtualbox_addons)
virtualbox_addons.pack(padx=20, pady=10)

# Launch Application

welcome.mainloop()