<<<<<<< HEAD
#!/usr/bin/env python

import sys
import os
import tkinter
import customtkinter
import CTkMessagebox
import platform
import shutil

# Application Properties

welcome = customtkinter.CTk()
welcome.geometry('500x800')
welcome.title('FBP OS Welcome')
welcome._set_appearance_mode('System')

settings_frame = customtkinter.CTkFrame(welcome)
settings_label = customtkinter.CTkLabel(settings_frame, text='Tweak settings')
settings_label.pack(padx=20, pady=10)

drivers_frame = customtkinter.CTkFrame(welcome)
drivers_label = customtkinter.CTkLabel(drivers_frame, text="Install Drivers")
drivers_label.pack(padx=20, pady=10)

software_frame = customtkinter.CTkFrame(welcome)
software_label = customtkinter.CTkLabel(software_frame, text='Install software packs')
software_label.pack(padx=20, pady=10)

# Software stores

discover = shutil.which('discover')
software = shutil.which('gnome-software')
mint = shutil.which('mintinstall')

# AUR Helper

yay_bin = shutil.which('yay')

# Distro ID

distro_id = ''

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
    os.system('yay -S steam heroic-games-launcher-bin pcsx2 minecraft-launcher')
    infobox(text="Game Set Installed")

# Install office suite

def install_office_suite():
    os.system('yay -S wps-office')
    infobox(text="Office Suite Installed")

# Install Authy and Bitwarden

def install_security_software():
    os.system('yay -S authy bitwarden')
    infobox(text="Security Set Installed")

# Install Rustdesk for remote control (not working on wayland)

def remote_control_software():
    os.system('yay -S rustdesk')
    infobox(text="Remote Control Set Installed")

# Install Virtual Machine Guest Drivers

def install_vmware_guest_addons():
    os.system('yay -S open-vm-tools')
    os.system('systemctl enable --now vmtoolsd.service vmware-vmblock-fuse.service')
    infobox(text="Vmware guest addons installed. It\'s recommend that you restart your pc.")

def install_virtualbox_addons():
    os.system('yay -S virtualbox-guest-utils xf86-video-vmware virtualbox-guest-utils-nox')
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

# Frame Stacking

settings_frame.pack(padx=20, pady=10)
drivers_frame.pack(padx=20, pady=10)
software_frame.pack(padx=20, pady=10)


settings_button = customtkinter.CTkButton(settings_frame, text='Settings', command=system_settings)
settings_button.pack(padx=20, pady=10)

fix_pacman_keys = customtkinter.CTkButton(settings_frame, text='Fix Pacman Keys', command=fix_pacman)
fix_pacman_keys.pack(padx=20, pady=10)

timeshift = customtkinter.CTkButton(settings_frame, text='Backup and restore', command=launch_timeshift)
timeshift.pack(padx=20, pady=10)

nvidia_driver = customtkinter.CTkButton(drivers_frame, text='Install Nvidia Driver (nvidia users only)', command=sure_install_nvidia_driver)
nvidia_driver.pack(padx=20, pady=10)

bumblebee = customtkinter.CTkButton(drivers_frame, text='Install Nvidia Optimus (Hybrid graphics only)', command=sure_install_hybrid)
bumblebee.pack(padx=20, pady=10)

software_center = customtkinter.CTkButton(settings_frame, text='Software Center', command=launch_software_center)
software_center.pack(padx=20, pady=10)

install_game_launchers = customtkinter.CTkButton(software_frame, text='Install some game launchers', command=install_games)
install_game_launchers.pack(padx=20, pady=10)

office_suite = customtkinter.CTkButton(software_frame, text='Install Office Suite', command=install_office_suite)
office_suite.pack(padx=20, pady=10)

security_software = customtkinter.CTkButton(software_frame, text='Install Account Security Software', command=install_security_software)
security_software.pack(padx=20, pady=10)

rustdesk = customtkinter.CTkButton(software_frame, text='Install Remote Control Software', command=remote_control_software)
rustdesk.pack(padx=20, pady=10)

vmware_addons = customtkinter.CTkButton(drivers_frame, text='Install Vmware Addons (Vmware virtual machines only)', command=install_vmware_guest_addons)
vmware_addons.pack(padx=20, pady=10)

virtualbox_addons = customtkinter.CTkButton(drivers_frame, text='Install Virtualbox Addons (Virtualbox virtual machines only)', command=install_virtualbox_addons)
virtualbox_addons.pack(padx=20, pady=10)

# Launch Application

welcome.mainloop()
=======
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

show_info(title='Linux', message='Everything, ok')

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
    show_info(title='Packages Installed', text=f'This packages have been installed')

# install packages with yay

def install_packages_with_yay(packages):
        
    os.system('yay -S ' + packages + '--no-confirm')
    show_info(title='Packages Installed', text=f'This packages: {packages} have been installed')

# Install packages with flatpak

def install_packages_with_flatpak(packages):

    os.system('flatpak install ' + packages)
    show_info(title='Packages Installed', text=f'This packages: {packages} have been installed')

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

# Launch Application

welcome.mainloop()
>>>>>>> e38f9db (Separated some functions in separate files)
