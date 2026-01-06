import webbrowser
import urllib.parse

def ouvrir_gmail(email, objet, message):
    base_url = "https://mail.google.com/mail/?view=cm&fs=1"

    url = (
        base_url
        + "&to=" + urllib.parse.quote(email)
        + "&su=" + urllib.parse.quote(objet)
        + "&body=" + urllib.parse.quote(message)
    )

    webbrowser.open(url)