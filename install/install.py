#!/usr/bin/python
import subprocess
from shutil import copyfile
from distutils.dir_util import copy_tree
import os

subprocess.run(["pacman", "-Syyu", "--noconfirm"])
subprocess.run(["pacman", "-S", 
    "i3-gaps",
    "xorg",
    "cmake",
    "code",
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
    "--noconfirm"])

path = os.path.dirname(os.path.abspath(__file__))
copyfile(path + "/.files/i3/config", "/home/" + os.getlogin() + "/.config/i3/config")
copyfile(path + "/.files/termite/config", "/home/" + os.getlogin() + "/.config/termite/config")
copyfile(path + "/.files/i3status/i3status.conf", "/etc/i3status.conf")
copy_tree(path + "/.files/fish", "/home/" + os.getlogin() + "/.config/fish")

xinitrc = open("/home/william/test.txt", "w")
xinitrc.write("exec i3\n")

subprocess.run(["chsh", "--shell", "/usr/bin/fish", os.getlogin()])
