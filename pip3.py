"""KEy points about wxPython:"""
"""1.open source python GUI network"""
"""2.provides native look and feel on all operating systems"""
"""3.requires installation"""
"""4. every wxPython program has:"""
"""Application(wx.app)-starts th GUI"""
"""Frame(wx.Frame)-the main window"""
"""Panel(wx.Panel)-a container for widgets"""
"""Controls(widgets)-ex:Button,TextBox,CheckBox"""
"""Button(wx.Button)-a clickable control used to trigger actions"""
"""Event Loop(MainLoop)-keeps the app running"""
import wx
#app=wx.App()
#frame=wx.Frame(None,title="Basic Window",size=(400,300))
#frame.Show()
#app.MainLoop()
#app=wx.App(False)
#frame=wx.Frame(None,title="Panel Example",size=(300,200))
#panel=wx.Panel(frame)
#panel.SetBackgroundColour("light blue")
#frame.Show()
#app.MainLoop()
"""buttons:"""
"""nomal buttons(wx.Button(parent,id,label,pos,size,style))-Standard text buttons"""
"""toggle button(wx.ToggleButton(...))-two state button (on/off)"""
"""bitmap button(wx.BitmapButton(...))-button with image/icon"""
"""SetLabel()-change button text, GetLabel()-get current text, SetDefault()-makes button default, GetValue()-returns toggle state, SetValue()-set state programmatically"""
app=wx.App()
#def on_click(event):
#    wx.MessageBox("Hii asshole!!","Info")
#def change_label(event):
#    btn.SetLabel("Hii what's up?")
def on_text_change(event):
    print("Text changed to:",event.GetString())
frame=wx.Frame(None,title="Button Example",size=(300,200))
panel=wx.Panel(frame)
panel.SetBackgroundColour("light blue")
#btn=wx.Button(panel,label="Click me",pos=(20,20),size=(100,25))
#btn.Bind(wx.EVT_BUTTON,on_click)
#btn.Bind(wx.EVT_BUTTON,change_label)
#text=wx.TextCtrl(panel,value="",pos=(20,70),size=(200,25))
text_box=wx.TextCtrl(panel,pos=(20,20))
text_box.Bind(wx.EVT_TEXT,on_text_change)
frame.Show()
app.MainLoop()
