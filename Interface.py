#!/usr/bin/python

import argparse
from gi.repository import Gtk, Gio
from os import path
from os import chdir
import subprocess
from subprocess import Popen
from os import chdir
import glob
import re
from gi.repository.GdkPixbuf import Pixbuf

class Handler:

    def on_mainWindow_quit(self, *args):
        Gtk.main_quit(*args)
        



def main():

    builder = Gtk.Builder()
    builder.add_from_file("ui.glade")
    builder.connect_signals(Handler())
    
    grid = builder.get_object("grid")
    window = builder.get_object("mainWindow")


    #pi = Pixbuf.new_from_file_at_size("/home/belette/Images/5gk6sd.jpg", 100, 100)
    #image = Gtk.Image.new_from_pixbuf(pi)
    #grid.pack_start(image, False, False, False)
    grid.set_row_spacing(15)    
    grid.set_column_spacing(15)

    i=0;
    j=0;
    
    for filename in glob.glob(path.expanduser("~/Images/" + "*")):
        if path.isfile(filename):
            pi = Pixbuf.new_from_file_at_size(filename, 150, 150)
            image = Gtk.Image.new_from_pixbuf(pi)
            grid.attach(image, i, j, 1 ,1)
            if (i == 2):
                i=0
                j+=1
            else:
                i+=1

    #pi = Pixbuf.new_from_file_at_size("/home/belette/Images/5gk6sd.jpg", 150, 150)
    #image = Gtk.Image.new_from_pixbuf(pi)
    #grid.attach(image, 0, 0, 1, 1)

    
    print(window.get_size())
    window.show_all()

    Gtk.main()


    

if  __name__ =='__main__':
    main()
