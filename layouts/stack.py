import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class stack(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Stack")
        self.set_border_width(10)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        chk_btn = Gtk.CheckButton("click Me")
        stack.add_titled(chk_btn,"check","Check Button")

        label = Gtk.Label()
        label.set_markup("<big>A Fancy Label</big>")
        stack.add_titled(label,"label", "A Label")

        stk_switcher = Gtk.StackSwitcher()
        stk_switcher.set_stack(stack)
        vbox.pack_start(stk_switcher, True,True,0)
        vbox.pack_start(stack,True,True,0)

win = stack()
win.connect("delete-event",Gtk.main_quit)
win.set_size_request(500,400)
win.show_all()
Gtk.main()