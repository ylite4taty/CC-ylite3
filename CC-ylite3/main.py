import wx
from ui.main_window import MainWindow

def main():
    #Dá um start na aplicação com a lib wxPython
    app = wx.App(False)

    # Cria a Janela principal do Crane Controller
    frame = MainWindow()
    frame.Show()

    # Loop principal da aplicação
    app.MainLoop()

if __name__ == "__main__":
    main()