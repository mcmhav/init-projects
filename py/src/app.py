
class App():
    def run(self, host=None, port=None, debug=None,
            load_dotenv=True, **options):
        print('an app')


def get_app(
        database_uri=None,
        exclude_tables=None,
        user_models=None,
        reflect_all=True,
        read_only=False,
        schema=None):
    app = App()

    return app
