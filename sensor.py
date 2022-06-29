from source import Source
from psutil import cpu_percent
from format import progress_bar, four_character_percentage

class Sensor(Source):

    def name(self) :
        return "Sensor"

    def period(self) :
        return 1

    def update(self) :
        self._cpu_usage = cpu_percent(interval = None, percpu = True)

    def render(self) :
        return ''.join(self.cpu_progress_parts())

    def cpu_progress_parts(self):
        total = sum(self._cpu_usage) / (100 * len(self._cpu_usage))
        yield four_character_percentage(total)
        yield ' '
        yield progress_bar(115, total)
        yield '\n'

        for i, usage in enumerate(self._cpu_usage) :
            if (i % 2 == 0) :
                yield '\n'

            yield progress_bar(60, usage / 100)

