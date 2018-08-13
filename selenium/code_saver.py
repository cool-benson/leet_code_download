
SAVE_DIR = "/Users/benson/Documents/leet_code_download/code"
class CodeSaver:
    def __init__(self):
        self.saved_topic = {}
        self.extension = {"python":".py",
                          "c":".c"}
    def saveInstance(self, data):
        problem = data['problem_name'].replace(" ","_")
        if not problem in self.saved_topic:
            self.saved_topic[problem] = 1
            file_name = SAVE_DIR + "/" + problem + self.extension[data['language']]
            fp = open(file_name,"w")
            fp.write(data['code'])
            fp.close()
            




