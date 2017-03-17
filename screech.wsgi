import sys, os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from screech.app import create_app

application = create_app()
