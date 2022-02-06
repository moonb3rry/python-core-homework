class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __gt__(self, other):
        if self.name == 'Rock':
            return other.name == 'Scissors'
        if self.name == 'Paper':
            return other.name == 'Rock'
        if self.name == 'Scissors':
            return other.name == 'Paper'

    def __eq__(self, other):
        return isinstance(self, type(other))

    def __hash__(self):
        return hash(self.name)


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')
