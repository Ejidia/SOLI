from abc import ABC, abstractmethod

# Base Notifier class
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Email implementation
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Email: {message}")

# SMS implementation
class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

# New notifier (e.g., Slack) can be added without modifying existing code
class SlackNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Slack message: {message}")

# Usage
def notify_users(notifier: Notifier, message: str):
    notifier.send(message)

# Example calls
notify_users(EmailNotifier(), "Welcome!")
notify_users(SMSNotifier(), "Your OTP is 1234")
notify_users(SlackNotifier(), "Team meeting at 3 PM")
