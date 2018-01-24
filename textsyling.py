import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self  ,title ="Label Example")
        self.set_border_width(20)
        self.set_default_size(500 , 300)

		#boxes

        hbox  = Gtk.Box(spacing = 20)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation = Gtk.Orientation.VERTICAL , spacing = 22)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation = Gtk.Orientation.VERTICAL , spacing = 22)
        vbox_right.set_homogeneous(False)


        #pack the two columns 
        hbox.pack_start(vbox_left,True,True,0)
        hbox.pack_start(vbox_right,True,True,0)
        #Normal
        label = Gtk.Label("this is a plain label")
        vbox_left.pack_start(label, True,True,0)
        
        #left align

        label = Gtk.Label()
        label.set_text("This \n")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True,True,0)

        #RIght aligned
        label = Gtk.Label()
        label.set_text("This is aligned text.\n")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True,True,0)
        self.add(hbox)






window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
