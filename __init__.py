from mycroft import MycroftSkill, intent_file_handler


class TestPadatiousEntityFiles(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('files.entity.padatious.test.intent')
    def handle_files_entity_padatious_test(self, message):
        type = message.data.get('type')

        self.speak_dialog('files.entity.padatious.test', data={
            'type': type
        })


def create_skill():
    return TestPadatiousEntityFiles()

