import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Switcher")
        self.set_border_width(10)
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        self.add(box)

        #stack
        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(2000)

        #checkbox
        check_button = Gtk.CheckButton("check")
        main_area.add_titled(check_button , "check_name", "check_box")

        #label

        label = Gtk.Label()
        label.set_markup("<big>Huge Text</big>")
        main_area.add_titled(label, "label_name", "Big label")

        #button
        button = Gtk.Button(label = "hi")
        main_area.add_titled(button , "b1","b2")


        #stackSwitcher

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)
        

        box.pack_start(stack_switcher,True,True,0)
        box.pack_start(main_area, True, True , 0)





window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()


