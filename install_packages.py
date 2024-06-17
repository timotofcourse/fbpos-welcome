#!/usr/bin/env python

import tkinter
import customtkinter
import usefull_functions

# Install packages UI

install_window = customtkinter.CTk()
install_window.geometry('500x700')
install_window.title('Install Packages')
install_window._set_appearance_mode('System')

install_packages_label = customtkinter.CTkLabel(install_window, text='Select the packages you need to install')
install_packages_label.pack(padx=20, pady=20)

# Old packages

install_nvidia_driver = customtkinter.CTkButton(install_window, text='Nvidia Driver', command=usefull_functions.install_nvidia_driver)
install_bumblebee = customtkinter.CTkButton(install_window, text='Nvidia Optimus', command=usefull_functions.install_nvidia_optimus)
install_game_launchers = customtkinter.CTkButton(install_window, text='Game Launchers (Steam, Heroic, ProtonUpQT, Lutris)', command=usefull_functions.install_games)
install_office = customtkinter.CTkButton(install_window, text='Office Suite (WPS Office)', command=usefull_functions.install_office_suite)
install_security_software = customtkinter.CTkButton(install_window, text='Security Software (Bitwarden and Authy)', command=usefull_functions.install_security_software)
install_virtuabox_guest_addons = customtkinter.CTkButton(install_window, text='VirtualBox Guest Addons', command=usefull_functions.install_virtualbox_addons)
install_vmware_guest_addons = customtkinter.CTkButton(install_window, text='Vmware Guest Addons', command=usefull_functions.install_vmware_guest_addons)

# New packages

install_firefox = customtkinter.CTkButton(install_window, text='Mozilla Firefox', command=usefull_functions.install_firefox)
install_chrome = customtkinter.CTkButton(install_window, text='Google Chrome', command=usefull_functions.install_chrome)
install_vivaldi = customtkinter.CTkButton(install_window, text='Vivaldi', command=usefull_functions.install_vivaldi)
install_brave = customtkinter.CTkButton(install_window, text='Brave Browser', command=usefull_functions.install_brave)
install_opera = customtkinter.CTkButton(install_window, text='Opera', command=usefull_functions.install_opera)
install_librewolf = customtkinter.CTkButton(install_window, text='Librewolf', command=usefull_functions.install_librewolf)

# Pack buttons on the UI

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

if __name__ == "__main__":
    install_window.mainloop()
