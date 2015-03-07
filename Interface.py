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
        
    def on_mainWindow_resize(self, iconview):
        size = iconview.get_toplevel().get_size()

        iconview.set_columns(size[0]/150)
        print(size)
        

def main():

    builder = Gtk.Builder()
    builder.add_from_file("ui.glade")
    builder.connect_signals(Handler())
    
    grid = builder.get_object("grid")
    window = builder.get_object("mainWindow")

    liststore = Gtk.ListStore(Pixbuf, str)
    iconview = builder.get_object("iconview")
    iconview.set_model(liststore)    
    iconview.set_pixbuf_column(0)
    iconview.set_item_orientation(Gtk.Orientation.VERTICAL)
    
    for filename in glob.glob(path.expanduser("~/Images/" + "*")):
        if path.isfile(filename):
            pi = Pixbuf.new_from_file_at_size(filename, 150, 150)
            liststore.append([pi, filename])
           
    
    print(iconview.get_row_spacing())
    print(iconview.get_column_spacing())
    print(iconview.get_item_padding())
    print(iconview.get_item_width())
    print(iconview.get_margin())
    window.show_all()

    Gtk.main()


    

if  __name__ =='__main__':
    main()
