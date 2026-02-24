import wx
from data.sensors import check_operator_status

class OperatorMenu(wx.Frame):
    def __init__(self, parent=None, title="Login Operador - CC-ylite3"):
        super(OperatorMenu, self).__init__(parent, title=title, size=(400, 300))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        wx.StaticText(panel, label="Digite seu nome de operador:")
        self.input_name = wx.TextCtrl(panel)
        vbox.Add(self.input_name, flag=wx.EXPAND | wx.ALL, border=10)

        login_btn = wx.Button(panel, label="Entrar")
        login_btn.Bind(wx.EVT_BUTTON, self.on_login)
        vbox.Add(self.result_label, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        self.result_label = wx.StaticText(panel, label="")
        vbox.Add(self.result_label, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        panel.SetSizer(vbox)
        self.Show()

    def on_login(self, event): 
        name = self.input_name.GetValue() 
        status = check_operator_status(name) # consulta camada data 
        if status == "authorized": 
            self.result_label.SetLabel(f"Bem-vindo {name}, autorizado para manobras.") 
        elif status == "suspended": 
            self.result_label.SetLabel(f"Operador {name} está suspenso!") 
        else: 
            self.result_label.SetLabel(f"Operador {name} não encontrado.")