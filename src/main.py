#!/usr/bin/python2.6
import gtk

def main():
    builder = gtk.Builder()
    builder.add_from_file('res/gui.glade')
    window = builder.get_object('window')
    window.show()
    gtk.main()

if __name__ == '__main__':
    main()
