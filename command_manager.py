import sys
import libs.cmds


class CommandManager(object):
    def __init__(self):
        self.cmd_list = []

    def get_all_callables(self):
        self.cmd_list = []
        for module in sys.modules:
            if module.startswith("libs.cmds"):
                if "callables" in dir(sys.modules[module]):
                    self.cmd_list.append([sys.modules[module], module.title().lower().replace("libs.cmds.", ""), sys.modules[module].callables()])

    def process_cmd(self, user, message):
        cmd = message.split(" ")[0]
        for command in self.cmd_list:
            if cmd in command[2]:
                resp = getattr(command[0], command[1])(user, message)
                return resp

        else:
            return None
