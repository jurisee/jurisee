import sys
import logging
from app import app

logging.basicConfig(level=logging.Debug, filename='/var/www/html/jurisee/logs/jurisee.log',format='%(asctime)s %(message)s')
sys.path.insert(0, 'var/www/html/jurisee')
sys.path.insert(0, '/var/www/html/jurisee/environments/jurisee/lib/python3.10/site-packages')

from jurisee.app import app as application

if __name__ == "__main__":
    app = create_app()
    app.run()