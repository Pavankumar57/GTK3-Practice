import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class listRowData(Gtk.ListBoxRow):
    def __init__(self,data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Labelk(data))


class list(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="List Layout")
        self.set_border_width(10)
    
        box_outer = Gtk.Box(orientation= Gtk.Orientation.VERTICAL,spacing=8)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox,True,True,0)
    
        row = Gtk.ListBoxRow()

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        row.add(hbox)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox,True,True,0)

        labelDT = Gtk.Label(label="Automatic Date and Time : ")
        #labelNet = Gtk.Label(label= "Require Internet Access : ")
        vbox.pack_start(labelDT,True,True,0)
        #vbox.pack_start(labelNet,True,True,0)

        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switch,False,True,1)
        
        listbox.add(row)

        row = Gtk.ListBoxRow()
   
        hbox = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL,spacing =10)
        row.add(hbox)
        label = Gtk.Label(label="Date Format")
        combo = Gtk.ComboBoxText()
        combo.insert(0,"0","24-hour")
        combo.insert(1,"1","AM/PM")
        hbox.pack_start(label,True,True,0)
        hbox.pack_start(combo,False,True,0)
   
        listbox.add(row)
        
        row = Gtk.ListBoxRow()
   
        hbox = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL,spacing =10)
        row.add(hbox)
        label = Gtk.Label(label="Enable Automatic Update")
        checkbox = Gtk.CheckButton()
        hbox.pack_start(label,True,True,0)
        hbox.pack_start(checkbox,False,True,0)
   
        listbox.add(row)
        


win = list()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()