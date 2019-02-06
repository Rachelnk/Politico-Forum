import os

from Forum.app.__int__ import create_app

#config_name = os.getenv('APP_SETTINGS')
flask_app = create_app('development')

if __name__ == '__main__':
   flask_app.run()
