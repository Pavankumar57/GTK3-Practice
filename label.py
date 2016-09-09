import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Label(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Label')
        label = Gtk.Label(label="User Name",\
        angle=0, halign=Gtk.Align.CENTER)
        self.add(label)

win = Label()
win.connect("delete-event", Gtk.main_quit)
win.set_size_request(500,300)
win.show_all()
Gtk.main()