from mycroft import MycroftSkill, intent_file_handler


class Polihint(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('polihint.intent')
    def handle_polihint(self, message):
        self.speak_dialog('polihint')


def create_skill():
    return Polihint()

