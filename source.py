from abc import ABC, abstractmethod


class Source(ABC) :
    
    @abstractmethod
    def name(self) -> str :
        pass
    
    @abstractmethod
    def period(self) -> int :
        '''
        Returns number of seconds to run the update
        '''
        pass

    @abstractmethod
    def update(self) -> None :
        pass

    @abstractmethod
    def render(self) -> str :
        pass