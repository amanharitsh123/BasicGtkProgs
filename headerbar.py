import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk ,Gio

class MainWindow(Gtk.Window): 
    def __init__(self):
        Gtk.Window.__init__(self, title = "Header")
        self.set_border_width(10)
        self.set_default_size(500,400)
        
        #header bar

        headerbar = Gtk.HeaderBar()
        headerbar.set_show_close_button(True)#setting default close maximize and full screeen button
        headerbar.props.title = "Rippin Music Player"
        self.set_titlebar(headerbar)#replacing our headerbar in place of default title bar
        #audio button ion right

        audio_button = Gtk.Button()
        cd_icon = Gio.ThemedIcon(name="gnome-dev-cdrom-audio")
        image = Gtk.Image.new_from_gicon(cd_icon, Gtk.IconSize.BUTTON)
        audio_button.add(image)
        headerbar.pack_end(audio_button) #sending audio icon button to the right


        #Create box of linked items

        box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(),"linked")

        #left arrow

        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT,Gtk.ShadowType.NONE))
        box.add(left_arrow)
 

        #right arrow

        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT,Gtk.ShadowType.NONE))
        box.add(right_arrow)
       
        headerbar.pack_start(box)
        self.add(Gtk.TextView())




window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
