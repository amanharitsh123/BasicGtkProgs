from gi.repository import Gtk 
import sys

class MyApplication(Gtk.Application):
    
    def do_activate(self): 
        #creating a Gtk Window belonging to the application intself
        window = Gtk.Window(application = self)
        #set the title 
        window.set_default_size(800, 600)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set
        window.set_title("Welcome to MyApp1")
        #Display Window 
        window.show_all()

#Starting the application
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

