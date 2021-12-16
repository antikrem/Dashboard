from packges import Packages
from clock import Clock

from runner import Runner


if __name__ == '__main__' :
    runner = Runner(
        Clock(),
        Packages("ephemeralex", "typesharpgen", "typesharpgenlauncher")
    )
    runner.start()
    runner.loop()