from src.models.app import App

import locale
import warnings

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
warnings.filterwarnings("ignore")

def main():
    app = App()
    app.create_app()

if __name__ == '__main__':
    main()