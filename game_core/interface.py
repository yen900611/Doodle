import abc


class Mediator(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def send_info(self, sender,commands):
        '''
        :param sender:colleague which send message for other.
        :param commands:
        :return: None
        '''
        pass

class ConcreateMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)
        pass

    def set_colleague(self,colleague):
        pass

    def del_colleague(self,colleague):
        pass

    def send_info(self,sender, commands):
        pass


class Colleague(abc.ABC):
    def __init__(self,mediator):
        self.m_mediator = mediator

    @abc.abstractmethod
    def request(self,game_info):
        pass

