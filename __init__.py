from mycroft import MycroftSkill, intent_file_handler


class Affirmations(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('affirmations.intent')
    def handle_affirmations(self, message):
        self.speak_dialog('affirmations')


def create_skill():
    return Affirmations()

