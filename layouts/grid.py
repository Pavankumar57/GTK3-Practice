import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class grid(Gtk.Window):
    def __init__(self):

        Gtk.Window.__init__(self,title="Grid")
        grid = Gtk.Grid()
        self.add(grid)
        self.user = Gtk.Label(label="User Name: ")
        self.pwd = Gtk.Label(label="password")
        self.tf_user = Gtk.Label(label="User Name: ")
        self.tf_pwd = Gtk.Label(label="password")
        self.sbt = Gtk.Button(label="Submit")
        grid.add(self.user)
        grid.attach(self.tf_user,1,0,1,1)
        grid.attach_next_to(self.pwd,self.user,\
        Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(self.tf_pwd,self.tf_user,\
        Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(self.sbt,self.tf_pwd,\
        Gtk.PositionType.BOTTOM,1,1)
win = grid()
win.connect("delete-event", Gtk.main_quit)
win.set_size_request(500,400)
win.show_all()
Gtk.main()
