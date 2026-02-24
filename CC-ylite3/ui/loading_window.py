import wx
import time

class LoadingWindow(wx.Frame):
    def __init__(self, parent=None, title="Carregando CC-ylite3"):
        super(LoadingWindow, self).__init__(parent, title=title, size=(400, 200))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(panel, label="Carregando recursos...")
        vbox.Add(self.label, flag=wx.ALIGN_CENTER | wx.TOP, border=40)

        self.progress = wx.Gauge(panel, range=100, size=(300, 25))
        vbox.Add(self.progress, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        panel.SetSizer(vbox)
        self.Show()

    def simulate_loading(self):
        for i in range(101):
            time.sleep(0.02) # simula tempo de carregamento
            self.progress.SetValue(i)
            wx.Yield() # Atualiza interface