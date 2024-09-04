from os import system
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

class Btn(Gtk.Button):
    def __init__(self, icon:str, cmd:str):
        super().__init__()
        self.connect("clicked", lambda b: system(cmd))
        liststore = Gtk.ListStore(Pixbuf, str)
        iconview = Gtk.IconView.new()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
        liststore.append([pixbuf, icon])
        self.add(iconview)

class Gexit(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gexit")
        btn1=Btn("shutdown", "poweroff")
        btn2=Btn("reboot", "reboot")
        btn3=Btn("exit", "gksu killall lightdm")
        btn4=Btn("suspend", "systemctl suspend")
        
        grid = Gtk.Grid()
        grid.add(btn1)
        grid.attach_next_to(btn2, btn1, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(btn3, btn1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(btn4, btn2, Gtk.PositionType.BOTTOM, 1, 1)
        self.add(grid)

win = Gexit()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
