import unittest
from datetime import datetime
from app_python.current_time import get_current_time
import pytz

class CurrentTimeTest(unittest.TestCase):
    def test_get_current_time(self):
       timeZ_Moscow = pytz.timezone('Europe/Moscow')
       dt_Moscow = datetime.now(timeZ_Moscow)
       self.assertEqual(dt_Moscow.strftime('%Y-%m-%d %H:%M:%S %Z %z'), get_current_time())


