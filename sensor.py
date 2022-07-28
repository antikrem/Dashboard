from source import Source
from psutil import cpu_percent, virtual_memory
from format import progress_bar, four_character_percentage

class Sensor(Source):

    def name(self) :
        return "Sensor"

    def period(self) :
        return 1

    def update(self) :
        self._cpu_usage = cpu_percent(interval = None, percpu = True)
        self._mem_usage = virtual_memory()

    def render(self) :
        return ''.join(self.cpu_progress_parts())

    def cpu_progress_parts(self):
        
        yield '\nCPU\n'
        totalCPU = sum(self._cpu_usage) / (100 * len(self._cpu_usage))
        yield four_character_percentage(totalCPU)
        yield ' '
        yield progress_bar(115, totalCPU)
        yield '\n'

        for i, usage in enumerate(self._cpu_usage) :
            if (i % 2 == 0) :
                yield '\n'

            yield progress_bar(60, usage / 100)
        
        yield '\n\nMEM: '
        yield str(self._mem_usage.used)
        yield ' / '
        yield str(self._mem_usage.total)
        yield '\n'
        totalMem = self._mem_usage.used / (100 * self._mem_usage.total)
        yield four_character_percentage(totalMem)
        yield ' '
        yield progress_bar(115 , totalMem * 100)





