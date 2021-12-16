from datetime import datetime
from source import Source

class Clock(Source):

    def name(self) :
        return "Clock"

    def period(self) :
        return 1

    def update(self) :
        pass

    def render(self) :
        return str(datetime.now().time())
