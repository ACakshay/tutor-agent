from google.adk.cli.fast_api import get_fast_api_app
import logging

logging.basicConfig(level=logging.DEBUG)

try:
    app = get_fast_api_app(agents_dir=".", web=True)
except Exception as e:
    print(repr(e))
