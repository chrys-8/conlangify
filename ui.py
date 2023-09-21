import wx

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        panel = wx.Panel(self)

        self.initMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Ready")

    def initMenuBar(self):
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, lambda _: self.Close(True), exitItem)

def runGUI():
    app = wx.App()
    frame = MainFrame(None, title = "Feature")
    frame.Show()
    app.MainLoop()
