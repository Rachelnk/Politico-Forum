import os

from app.__int__ import create_app

flask_app = create_app('development')

if __name__ == '__main__':
   flask_app.run()
