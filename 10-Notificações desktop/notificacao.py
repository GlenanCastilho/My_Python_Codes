from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast(
    "Notificação",
    "Teste de mensagem",
    threaded=True,
    icon_path=None,
    duration=3
)