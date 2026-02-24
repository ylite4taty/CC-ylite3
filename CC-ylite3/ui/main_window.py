import wx
from ui.loading_window import LoadingWindow
from ui.operator_menu import OperatorMenu

class MainWindow:
    def __init__(self):
        self.app = wx.App(False)

        # 1. Mostra a janela de loading
        self.loading = LoadingWindow()
        self.loading.simulate_loading()

        # 2. fecha o loading
        self.loading.Destroy()

        # 3. Abre menu do operador
        self.operator_menu = OperatorMenu()

        # 4. Looop principal
        self.app.MainLoop()

        """
        super(MainWindow, self).__init__(parent, title=title, size=(600 , 400))

        # Painel Principal
        panel = wx.Panel(self)

        # Layout vertical
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Título
        title_text = wx.StaticText(panel, label="CC-ylite3 Prototype")
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_text.SetFont(font)
        vbox.Add(title_text, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        # Dados simulados
        self.angle_label = wx.StaticText(panel, label="Ângulo de lança: 45º")
        self.weight_label = wx.StaticText(panel, label="Peso da carga: 1200 kg")
        self.wind_label = wx.StaticText(panel, label="Velocidade do vento: 15km/h")

        vbox.Add(self.angle_label, flag=wx.LEFT | wx.TOP, border=20)
        vbox.Add(self.weight_label, flag=wx.LEFT | wx.TOP, border=20)
        vbox.Add(self.wind_label, flag=wx.LEFT | wx.TOP, border=20)

        # Botão de Emergência
        emergency_btn = wx.Button(panel, label="Botão de Emergência")
        vbox.Add(emergency_btn, flag=wx.ALIGN_CENTER | wx.TOP, border=30)

        panel.SetSizer(vbox)

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow()
    app.MainLoop()

""" 