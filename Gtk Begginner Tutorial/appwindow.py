#This is a Application Window which can Support GMenu
from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    #Window Constructor 
    def __init__(self , app):
        Gtk.Window.__init__(self, title = "Application Window", application = app)
        
class MyApplication(Gtk.Application):
    #constructor of the Gtk Application
    
    def __init__(self):
        Gtk.Application.__init__(self)
    def do_activate(self):
        win = MyWindow(self)
        #show the created window
        win.show_all()
        
    #starting up the application
    
    def do_startup(self):
        Gtk.Application.do_startup(self)
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
    