import random
import time
import uuid

class Base_page:

    def __init__(self, browser) -> None:
        self._browser = browser


    def screen_shot_exception(self ):
        number = uuid.uuid4()
        screen_name = 'screenshot' + '_' + str(number) + '_' + '.png'
        self._browser.save_screenshot('screen_shot/' + screen_name)

