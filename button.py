import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class HelloWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title = "Hello")
        #self.set_default_size()
#Gtk.Window.maximize
        button = Gtk.Button(label = "Click Here")
        button.connect("clicked",self.onClick,"pavan")
        self.add(button)
    def onClick(self, widget,string):
        print("hello World "+ string)
win = HelloWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()