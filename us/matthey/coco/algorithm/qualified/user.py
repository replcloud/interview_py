
import datetime

class User:
    """
    Base User class
    """

    """
    args: 
      name: name of the user
    """
    def __init__(self, name):
        self.name = name
        self.is_logged_in_status = False
        self.last_logged_in_at = None

    """
    Return user's name
    """
    def name(self):
        return self.name

    """
    Update user's name
    args:
      value: user's new name
    """
    def name(self, value):
        if value:
            self.name = value

    """
    Return True when the user is logged in
    """
    def is_logged_in(self):
        return self.is_logged_in_status

    """
    Return user's last login timstamp. If the user is currently logged in, return the current time.
    """
    # TODO: check the specification
    def last_logged_in_at(self):
        if self.is_logged_in_status:
            return self.last_logged_in_at
        else:  # The user us currently logged in
            return datetime.datetime.now()

    def log_in(self):
        self.last_logged_in_at = datetime.datetime.now()
        self.is_logged_in_status = True

    def log_out(self):
        self.last_seen_at = datetime.datetime.now()
        self.is_logged_in_status = False

    def can_edit(self, comment):
        if not comment:
            raise 'comment cannot be None'
        if comment.author.name == self.name:
            return True
        else:
            return False

    def can_delete(self, comment):
        return False

    def __str__(self):
        return self.name()


class Moderator(User):
    # Use super
    #     def __init__(self, name):
    #         pass
    def can_delete(self, comment):
        return True


class Admin(Moderator):
    # Use super
    #     def __init__(self, name):
    #         pass
    def can_edit(self, comment):
        return True

    def can_delete(self, comment):
        return True


class Comment:
    def __init__(self, author, message, replied_to=None):
        self.author = author
        self.message = message
        self.replied_to = replied_to
        self.created_at = datetime.datetime.now()

    def author(self, value):
        self.author = author

    def message(self):
        return self.message

    def message(self, value):
        # TODO: Check permission
        self.message = value

    def created_at(self):
        return self.created_at

    def replied_to(self, value):
        self.replied_to = value

    def __str__(self):
        if self.replied_to:
            return self.message + " by " + self.author.name + " (replied to " + self.replied_to.author.name + ")"
        else:
            return self.message + " by " + self.author.name

