from source import Source
from os import system
from multiprocessing import Process, Queue
from datetime import datetime
from time import sleep


class RunningSource() :
    def __init__(self, source: Source) :
        self._source = source
        self._queue = Queue()
        self._last = ''

    def _loop(q: Queue, source: Source) :
        while True :
            start = datetime.now()
            
            source.update()
            output = source.render()
            q.put(output)
            
            taken = datetime.now() - start
            sleep(source.period() - taken.microseconds / 1000000.0)

    def start_process(self) :
        self._process = Process(target=RunningSource._loop, args=(self._queue, self._source))
        self._process.start()

    def poll(self) :
        try :
            self._last = self._queue.get(False)
        except :
            pass

        return self._last

class Runner() :
    def __init__(self, *args : Source) :
        self._sources = [RunningSource(source) for source in args]

    def _render(self) :
        view ='\n'.join(source.poll() for source in self._sources)
        system('clear')
        print(view)

    def start(self) :
        for source in self._sources :
            source.start_process()

    def loop(self) :
        while True :
            sleep(1)
            self._render()