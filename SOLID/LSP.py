from abc import ABC, abstractmethod



class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Contact:
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email
        self.phone = phone 


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification
    
    def send(self, message):
        self.notification.notify(message)


class Email(Notification):
    def __init__(self, email) -> None:
        self.email = email
    
    def notify(self, message):
        print(f"Send message : {message} to email : {self.email}")


class SMS(Notification):
    def __init__(self, phone) -> None:
        self.number = phone 
    
    def notify(self, message):
        print(f"Send message : {message} to email : {self.number}")



if __name__ == '__main__':
    c1 = Contact("Aron Talcha", "aron@talcha.com", "9814356151")
    sms_notification = SMS(phone = c1.phone)
    email_notification = Email(email = c1.email)
    notification_manager_SMS = NotificationManager(sms_notification)
    notification_manager_SMS.send(" Hello Aron")
    notification_manager_EMAIL = NotificationManager(email_notification)
    notification_manager_EMAIL.send(" Hello Ashesh")