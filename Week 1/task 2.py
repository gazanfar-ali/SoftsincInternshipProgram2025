class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def __str__(self):
        return f"User: {self._username}, Email: {self._email}"

    def send_message(self, message):
        return f"{self._username} sends: {message}"


class Intern(User):
    def __init__(self, username, email, internship_domain):
        super().__init__(username, email)
        self.internship_domain = internship_domain

    def __str__(self):
        return f"Intern: {self._username}, Domain: {self.internship_domain}"

    def daily_task(self):
        return f"{self._username} is working on {self.internship_domain} tasks."


class Mentor(User):
    def __init__(self, username, email, expertise):
        super().__init__(username, email)
        self.expertise = expertise

    def __str__(self):
        return f"Mentor: {self._username}, Expertise: {self.expertise}"

    def review_task(self, intern_name):
        return f"{self._username} is reviewing {intern_name}'s work."


# Challenge: Simulated Chat App
class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"{self.sender._username}: {self.content}"


class Manager(User):
    def __init__(self, username, email, team):
        super().__init__(username, email)
        self.team = team  # list of Users

    def broadcast(self, content):
        return [Message(self, content) for _ in self.team]


# Example Usage
if __name__ == "__main__":
    intern = Intern("ali123", "ali@example.com", "Machine Learning")
    mentor = Mentor("sanaM", "sana@example.com", "AI/ML")
    manager = Manager("zafarM", "zafar@example.com", [intern, mentor])

    print(intern)
    print(mentor)
    print(manager)
    print(intern.daily_task())
    print(mentor.review_task(intern._username))
    
    msg = Message(intern, "Hello, I submitted today's task.")
    print(msg)

    for broadcast_msg in manager.broadcast("Please attend the meeting at 4 PM."):
        print(broadcast_msg)
