# logger.py
from datetime import datetime

class Logger:
    @staticmethod
    def log(message, filename='general.log'):
        with open(filename, 'a') as file:
            file.write(f"[{datetime.now()}] {message}\n")


# roles.py
class Role:
    def perform_action(self):
        pass

class Admin(Role):
    def perform_action(self):
        return "Managing system settings"

class HR(Role):
    def perform_action(self):
        return "Managing recruitment process"

class Intern(Role):
    def perform_action(self):
        return "Completing assigned tasks"

class Mentor(Role):
    def perform_action(self):
        return "Reviewing intern work"

class User:
    def __init__(self, name, role: Role):
        self.name = name
        self.role = role

    def act(self):
        action = self.role.perform_action()
        Logger.log(f"{self.name}: {action}", filename=f"{self.role.__class__.__name__.lower()}.log")
        return action


# file_utils.py
def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()

def write_file(filepath, data):
    with open(filepath, 'w') as file:
        file.writelines(data)
