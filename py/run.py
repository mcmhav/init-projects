from src import get_app

app = get_app()


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
