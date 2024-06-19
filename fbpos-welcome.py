#!/usr/bin/env python

import sys
import os
import tkinter # Just in case
from CTkMessagebox import CTkMessagebox
import customtkinter
import platform

# Messagebox i'll use on this script

def show_error(title, message):
    
    CTkMessagebox(title=title, message=message, icon="cancel")


def show_info(title, message):
    
    CTkMessagebox(title=title, message=message)


# Application Properties

settings_app = ''
store_app = ''
packages_to_look_for = ['plasma-discover', 'gnome-software', 'mintinstall', 'yay']
where_to_look_for_packages = '/usr/bin/'

welcome = customtkinter.CTk()
welcome.geometry('450x900')
welcome.title('FBP OS Welcome')
welcome._set_appearance_mode('System')

running_on = platform.platform()

if running_on.startswith('Win') or running_on.startswith('Darwin'):

    show_error(title='Error', message='This tool does not work on this platform')
    sys.exit()

# Look for packages

packages_found = []

for item in packages_to_look_for:
    
    complete_path_for_binary = where_to_look_for_packages + item
    
    if os.path.exists(complete_path_for_binary):
        
        packages_found.append(item)
        print(packages_found)

yay = 'yay'
discover = 'plasma-discover'
gnome_software = 'gnome-software'
mintinstall = 'mintinstall'


if yay not in packages_found:
    os.system('pkexec pacman -S yay')

if discover in packages_found:

    store_app = discover
    settings_app = 'systemsettings'

elif gnome_software in packages_found:

    store_app = gnome_software
    settings_app = 'gnome-control-center'

elif mintinstall in packages_found:

    store_app = mintinstall
    settings_app = 'mintsettings'

# Functions for the ui to work

def settings():

    os.system(settings_app)

def timeshift_launch():

    os.system('timeshift-gtk')

def store():
    
    os.system(store_app)

def fix_pacman_keys_function():

    fix_commands = ['pkexec pacman-key --init', 'pkexec pacman-key --populate archlinux', 'yes | pkexec pacman -Sy archlinux-keyring', 'pkexec pacman -Syyu --no-confirm']

    for item in fix_commands:
       
        os.system(item)
    
    show_info(title='Fixed Pacman Keys', message='The Pacman Keys are fixed, you can now install packages with this tool or with pacman directly')

# Install packages with pacman

def install_packages_with_pacman(packages):

    os.system('pkexec pacman -S ' + packages + '--no-confirm')
    show_info(title='Packages Installed', text=f'The packages: {packages} have been installed with pacman')

# install packages with yay

def install_packages_with_yay(packages):
        
    os.system('yay -S ' + packages + '--no-confirm')
    show_info(title='Packages Installed', text=f'This packages: {packages} have been installed with yay')

# Install packages with flatpak

def install_packages_with_flatpak(packages):

    os.system('flatpak install ' + packages)
    show_info(title='Packages Installed', text=f'This packages: {packages} have been installed with flatpak')

# Enable services with systemd

def enable_services(services):

    os.system('systemctl enable --now' + services)
    show_info(title='Services Enabled', text=f'This services: {services} have been enabled and started')

# functions for the buttons to install things

def install_nvidia_optimus():

    install_packages_with_pacman(packages='')
    install_packages_with_yay(packages='')
    show_info(title='Nvidia Optimus Installed', text='Everything needed for nvidia optimus to work is installed')

def install_vm_driver(vendor):

    if vendor == 'virtualbox':

        install_packages_with_pacman(packages='virtualbox-guest-utils xf86-video-vmware virtualbox-guest-utils-nox')
        enable_services(services='vboxservice.service systemd-modules-load.service')
        
    elif vendor == 'vmware':

        install_packages_with_pacman(packages='open-vm-tools')
        enable_services(services='vmtoolsd.service vmware-vmblock-fuse.service')

    show_info(title='VM Driver Installed', text=f'The correct video drivers for {vendor} has been installed sucessfully, it\' recommended to restart your system')


# Install packages window


# Buttons to install things

install_nvidia_driver = customtkinter.CTkButton(welcome, text='Install Nvidia Driver', command=lambda:install_packages_with_pacman('nvidia nvidia-utils nvidia-settings'))
install_bumblebee = customtkinter.CTkButton(welcome, text='Install Nvidia Optimus', command=install_nvidia_optimus)
install_game_launchers = customtkinter.CTkButton(welcome, text='Install Game Launchers (Steam, Heroic, ProtonUpQT, Lutris)', command=lambda:install_packages_with_pacman('steam heroic-games-launcher pcsx2 minecraft-launcher'))
install_office = customtkinter.CTkButton(welcome, text='Install Office Suite (WPS Office)', command=lambda:install_packages_with_pacman('wps-office'))
install_security_software = customtkinter.CTkButton(welcome, text='Install Security Software (Bitwarden)', command=lambda:install_packages_with_pacman('bitwarden'))
install_virtuabox_guest_addons = customtkinter.CTkButton(welcome, text='Install VirtualBox Guest Addons', command=lambda:install_vm_driver('virtualbox'))
install_vmware_guest_addons = customtkinter.CTkButton(welcome, text='Install Vmware Guest Addons', command=lambda:install_vm_driver('vmware'))
install_firefox = customtkinter.CTkButton(welcome, text='Install Mozilla Firefox', command=lambda:install_packages_with_pacman('firefox'))
install_chrome = customtkinter.CTkButton(welcome, text='Install Google Chrome', command=lambda:install_packages_with_pacman('google-chrome'))
install_vivaldi = customtkinter.CTkButton(welcome, text='Install Vivaldi', command=lambda:install_packages_with_pacman('vivaldi'))
install_brave = customtkinter.CTkButton(welcome, text='Install Brave Browser', command=lambda:install_packages_with_pacman('brave'))
install_opera = customtkinter.CTkButton(welcome, text='Install Opera', command=lambda:install_packages_with_pacman('opera'))
install_librewolf = customtkinter.CTkButton(welcome, text='Install Librewolf', command=lambda:install_packages_with_pacman('librewolf'))


# Application Widgets

welcome_label = customtkinter.CTkLabel(welcome, text='Welcome to FBP OS. We will help you to configure your new system')
welcome_label.pack(padx=20, pady=10)

install_brave.pack(padx=20, pady=10)
install_chrome.pack(padx=20, pady=10)
install_firefox.pack(padx=20, pady=10)
install_vivaldi.pack(padx=20, pady=10)
install_opera.pack(padx=20, pady=10)
install_librewolf.pack(padx=20, pady=10)
install_nvidia_driver.pack(padx=20, pady=10)
install_bumblebee.pack(padx=20, pady=10)
install_game_launchers.pack(padx=20, pady=10)
install_office.pack(padx=20, pady=10)
install_security_software.pack(padx=20, pady=10)
install_virtuabox_guest_addons.pack(padx=20, pady=10)
install_vmware_guest_addons.pack(padx=20, pady=10)

settings_button = customtkinter.CTkButton(welcome, text='Settings')
settings_button.pack(padx=20, pady=10)

fix_pacman_keys = customtkinter.CTkButton(welcome, text='Fix Pacman Keys')
fix_pacman_keys.pack(padx=20, pady=10)

timeshift = customtkinter.CTkButton(welcome, text='Backup and restore')
timeshift.pack(padx=20, pady=10)

software_center = customtkinter.CTkButton(welcome, text='Software Center')
software_center.pack(padx=20, pady=10)

if __name__ == '__main__':

    # Launch Application

    welcome.mainloop()
