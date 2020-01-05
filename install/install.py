#!/usr/bin/python
import subprocess
from shutil import copyfile
from distutils.dir_util import copy_tree
import os

subprocess.run(["sudo", "pacman", "-Syyu", "--noconfirm"])
subprocess.run(["sudo", "pacman", "-S", 
    "i3-gaps",
    "xorg",
    "cmake",
    "code",
    "vim",
    "dhcpcd",
    "fakeroot",
    "fish",
    "gcc",
    "git",
    "make",
    "termite",
    "ranger",
    "nvidia",
    "nitrogen",
    "firefox",
    "htop",
    "alsa-utils",
    "pulseaudio",
    "pavucontrol",
    "ttf-dejavu",
    "discord",
    "--noconfirm"])

path = os.path.dirname(os.path.abspath(__file__))
copyfile(path + "/.files/i3/config", "/home/" + os.getlogin() + "/.config/i3/config")
copyfile(path + "/.files/termite/config", "/home/" + os.getlogin() + "/.config/termite/config")
copy_tree(path + "/.files/fish", "/home/" + os.getlogin() + "/.config/fish")

subprocess.run(["sudo", "cp", "-i", path + "/.files/i3status/i3status.conf", "/etc/i3status.conf"])

xinitrc = open("/home/" + os.getlogin() + "/.xinitrc", "w")
xinitrc.write("exec i3\n")

subprocess.run(["sudo", "chsh", "--shell", "/usr/bin/fish", os.getlogin()])

subprocess.run(["git", "clone", "https://aur.archlinux.org/yay.git"])
os.chdir(path + "/yay")
subprocess.run(["makepkg", "-si"])
subprocess.run(["yay", "-S", "spotify", "--noconfirm"])
