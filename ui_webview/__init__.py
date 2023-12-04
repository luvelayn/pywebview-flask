import webview

from ui_webview.flask_file import flask_app


def app():
    webview.create_window('Unit Converter', flask_app)
    webview.start()
