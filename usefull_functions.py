#!/usr/bin/env python

import sys
import os
import tkinter
import customtkinter
import platform
import find_binaries

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
    if find_binaries.discover:
        os.system('plasma-discover')
    elif find_binaries.software:
        os.system('gnome-software')
    elif find_binaries.mint:
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

def remote_control_software():
    os.system('pkexec pacman -S rustdesk')
    os.system('zenity --info --text="Remote Control Set Installed"')

def install_vmware_guest_addons():
    os.system('pkexec pacman -S open-vm-tools')
    os.system('systemctl enable --now vmtoolsd.service vmware-vmblock-fuse.service')
    os.system('zenity --info --text="Vmware guest addons installed. It\'s recommend that you restart your pc.')

def install_virtualbox_addons():
    os.system('pkexec pacman -S virtualbox-guest-utils xf86-video-vmware virtualbox-guest-utils-nox')
    os.system('systemctl enable --now vboxservice.service')
    os.system('systemctl enable --now systemd-modules-load.service')
    os.system('zenity --info --text="Virtualbox guest addons installed. It\'s recommend that you restart your pc.')

def fix_pacman():
    os.system('pkexec pacman-key --init')
    os.system('pkexec pacman-key --populate archlinux')
    os.system('yes | pkexec pacman -Sy archlinux-keyring')

def install_firefox():
    os.system('pkexec pacman -S firefox')
    os.system('zenity --info --text="Mozilla Firefox Installed"')

def install_chrome():
    os.system('pkexec pacman -S google-chrome')
    os.system('zenity --info --text="Google Chrome Installed"')

def install_opera():
    os.system('pkexec pacman -S opera')
    os.system('zenity --info --text="Opera Installed"')

def install_vivaldi():
    os.system('pkexec pacman -S vivaldi')
    os.system('zenity --info --text="Vivaldi Installed"')

def install_brave():
    os.system('pkexec pacman -S brave')
    os.system('zenity --info --text="Brave Installed"')

def install_librewolf():
    os.system('pkexec pacman -S librewolf')
    os.system('zenity --info --text="Librewolf Installed"')
