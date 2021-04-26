from mycroft import MycroftSkill, intent_handler


class TestPadatiousEntityFiles(MycroftSkill):
    def intialize(self):
        self.register_entity_file('type.entity')

    @intent_handler("test.intent")
    def handle_padatious_entity_test(self, message):
        self.log.info(repr(message.data))
        entity = message.data.get("type")
        self.speak_dialog("test", {"type": entity})


def create_skill():
    return TestPadatiousEntityFiles()
