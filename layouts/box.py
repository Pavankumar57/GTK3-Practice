import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class box(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title=\
             "Layout Box")
        self.box = Gtk.Box(spacing = 6)
        self.add(self.box)
        name = Gtk.Label(label="Username", angle =0)
        self.box.pack_start(name,True,False,0)
        pwd = Gtk.Label(label="Username", angle =0)
        self.box.pack_start(pwd,True,True,0)

win = box()
win.connect("delete-event",Gtk.main_quit)
win.set_size_request(500,400)
win.show_all()
Gtk.main()