import abc

class Mediator(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def send_message(self,colleague,message):
        pass

class Colleague(abc.ABC):
    def __init__(self,mediator):
        self.m_mediator = mediator

    @abc.abstractmethod
    def request(self,message):
        pass

class ConcreateColleague1(Colleague):
    def __init__(self,mediator):
        Colleague.__init__(self,mediator)

    def action(self):
        self.m_mediator.send_message(self,"ConcreateColleague1發出通知")

    def request(self,message):
        print("ConcreateColleague1.request " + message)

class ConcreateColleague2(Colleague):
    def __init__(self,mediator):
        Colleague.__init__(self,mediator)
        pass

    def action(self):
        self.m_mediator.send_message(self,"ConcreateColleague2發出通知")

    def request(self,message):
        print("ConcreateColleague2.request " + message)

class ConcreateMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)
        self.concreateColleague1 = None
        self.concreateColleague2 = None

    def set_colleague1(self,colleague):
        self.concreateColleague1 = colleague

    def set_colleague2(self,colleague):
        self.concreateColleague2 = colleague


    def send_message(self,colleague,message):
        if colleague == self.concreateColleague1:
            self.concreateColleague2.request(message)
        if colleague == self.concreateColleague2:
            self.concreateColleague1.request(message)

def test_mediator():
    concreateMediator = ConcreateMediator()
    colleague1 = ConcreateColleague1(concreateMediator)
    colleague2 = ConcreateColleague2(concreateMediator)

    concreateMediator.set_colleague1(colleague1)
    concreateMediator.set_colleague2(colleague2)

    colleague1.action()
    colleague2.action()

if __name__ == "__main__":
    test_mediator()