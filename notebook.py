import gi
from gi.repository import Gtk
#notebook comprises of Pages 
#pages are added to the notebook with their custom titles

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Notebook")
        self.set_border_width(10)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        

        #first page

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label("Here is the stuff that is in the main area"))
        self.notebook.append_page(self.page1, Gtk.Label("First tab"))

        #second page
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label(" stuff tpage 2 page 2 page 2"))
        icon = Gtk.Image.new_from_icon_name("gnome-dev-cdrom-audio",Gtk.IconSize.MENU)


        self.notebook.append_page(self.page2, icon)



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
