from libs.data import get_relevant_information
import random
import sys
import libs.cmds


class RandomLines(object):
    def __init__(self, main):
        self.threshold = 20
        self.counter = 0
        self.main = main

        self.generate_threshold()

    def generate_threshold(self, lower=5, upper=20):
        self.threshold = random.randrange(lower, upper)

    def increment(self):
        self.counter += 1
        if self.counter == self.threshold:
            self.send_message()

    def send_message(self):
        data = get_relevant_information("lines")
        random_line = random.randrange(0, len(data))
        try:
            line = data[random_line]["text"]
        except KeyError:
            for module in sys.modules:
                if data[random_line]["cmd"] in module:
                    line = getattr(sys.modules[module], module.title().lower().replace("libs.cmds.", ""))("", "")
        finally:
            self.main.send_message(line)
