from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    #create a window
    
    def __init__(self,app):
        Gtk.Window.__init__(self , title = "Welcome to GNOME" , application = app)
        self.set_default_size(300,300)
        
        image = Gtk.Image()
        image.set_from_file("/home/amanharitsh/Downloads/giphy.gif")
        self.add(image)
         
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)
    
    def do_activate(self):
        win = MyWindow(self)
        win.show_all()
    
    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
        