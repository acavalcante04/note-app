from backend.app import create_app  # Ajuste o caminho se estiver em 'backend'

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
