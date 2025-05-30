from google.adk.cli.fast_api import get_fast_api_app

try:
    app = get_fast_api_app(agents_dir=".", web=True)
except Exception as e:
    print(repr(e))
