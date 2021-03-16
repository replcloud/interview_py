import unittest

from us.matthey.coco.algorithm.qualified.user import User, Moderator, Admin, Comment


class Test(unittest.TestCase):
    def setUp(self):
        self.user1 = User('User 1')
        self.user2 = User('User 2')
        self.mod = Moderator('Moderator')
        self.admin1 = Admin('Admin')
        self.user1_comment = Comment(self.user1, 'hello')
        self.user2_comment = Comment(self.user2, 'hi', self.user1_comment)
        self.mod_comment = Comment(self.mod, 'moderator', self.user2_comment)

    def test_instantiation(self):
        """ test instantiation """
        self.assertEqual(self.user1.name, 'User 1', 'User name is set correctly')
        self.assertEqual(self.user2.name, 'User 2', 'User name is set correctly')
        self.assertIsInstance(self.user1_comment.created_at, datetime.datetime)
        self.assertEqual(self.user1_comment.author, self.user1, 'User was set on comment creation')
        self.assertEqual(self.user2_comment.author, self.user2, 'User was set on comment creation')
        self.assertEqual(self.mod_comment.author, self.mod, 'User was set on comment creation')

    def test_login_methods(self):
        """ test login methods """
        self.assertEqual(self.user1.is_logged_in(), False, 'User is logged out by default')
        self.assertEqual(self.user1.last_logged_in_at, None, 'Last logged in date is not set by default')
        self.user1.log_in()
        self.assertEqual(self.user1.is_logged_in(), True, 'User can be logged in')
        self.assertIsInstance(self.user1.last_logged_in_at, datetime.datetime, 'Last logged in date is set')
        last_logged_in_at = self.user1.last_logged_in_at
        self.user1.log_out()
        self.assertEqual(self.user1.is_logged_in(), False, 'User can be logged out')
        self.assertEqual(self.user1.last_logged_in_at, last_logged_in_at, 'Last logged in date stays the same')

    def test_inheritance(self):
        """ test inheritance """
        self.assertIsInstance(self.user1, User, 'User is a User')
        self.assertNotIsInstance(self.user1, Moderator, 'User is not a Moderator')
        self.assertNotIsInstance(self.user1, Admin, 'User is not an Admin')
        self.assertIsInstance(self.mod, User, 'Moderator is a User')
        self.assertIsInstance(self.mod, Moderator, 'Moderator is a Moderator')
        self.assertNotIsInstance(self.mod, Admin, 'Moderator is not an Admin')
        self.assertIsInstance(self.admin1, User, 'Admin is a User')
        self.assertIsInstance(self.admin1, Moderator, 'Admin is a Moderator')
        self.assertIsInstance(self.admin1, Admin, 'Admin is an Admin')

    def test_method_overriding(self):
        """ test method overriding """
        self.assertEqual(self.user1.can_edit(self.user1_comment), True, 'User can edit their own comment')
        self.assertEqual(self.user1.can_edit(self.user2_comment), False, 'User cannot edit other comments')
        self.assertEqual(self.user1.can_delete(self.user1_comment), False, 'User cannot delete their own comment')
        self.assertEqual(self.user1.can_delete(self.user1_comment), False, 'User cannot delete other comment')
        self.assertEqual(self.mod.can_edit(self.mod_comment), True, 'Moderator can edit their own comment')
        self.assertEqual(self.mod.can_edit(self.user1_comment), False, 'Moderator cannot edit other comments')
        self.assertEqual(self.mod.can_delete(self.mod_comment), True, 'Moderator can delete their own comment')
        self.assertEqual(self.mod.can_delete(self.user1_comment), True, 'Moderator can delete other comments')
        self.assertEqual(self.admin1.can_edit(self.user1_comment), True, 'Admin can edit other comments')
        self.assertEqual(self.admin1.can_delete(self.user1_comment), True, 'Admin can delete other comments')

    def test_function_overloading(self):
        """ test function overloading """
        self.assertEqual(self.user1_comment.replied_to, None, 'Comment was created without a reply')
        self.assertEqual(self.user2_comment.replied_to, self.user1_comment, 'Comment was created with a rep')

    def test_updating_users(self):
        """ test updating users """
        user1 = User('User 1')
        self.assertEqual(user1.name, 'User 1', 'User name was set')
        user1.name = 'User 1 Updated'
        self.assertEqual(user1.name, 'User 1 Updated', 'User name can be updated')

    def test_updating_comments(self):
        """ test updating comments """
        user1 = User('User 1')
        user1_comment = Comment(user1, 'hello')
        self.assertEqual(user1_comment.message, 'hello', 'Comment message was set')
        user1_comment.message = 'howdy'
        self.assertEqual(user1_comment.message, 'howdy', 'Comment message can be updated')

    def test_handle_str(self):
        """ test handle str """
        user1 = User('User 1')
        user2 = User('User 2')
        user1_comment = Comment(user1, 'hello')
        user2_comment = Comment(user2, 'hi', user1_comment)
        self.assertEqual(str(user1_comment), 'hello by User 1',
                         'The toString method should return the correct hierarchy (no reply)')
        self.assertEqual(str(user2_comment), 'hi by User 2 (replied to User 1)',
                         'The toString method should return the correct hierarchy (reply)')
        self.assertEqual(str(self.mod_comment), 'moderator by Moderator (replied to User 2)',
                         'The toString method should return the correct hierarchy (nested reply)')
        user1.name = 'User One'
        user2.name = 'User Two'
        self.assertEqual(str(user1_comment), 'hello by User One',
                         'The toString method should reflect reference changes')
        self.assertEqual(str(user2_comment), 'hi by User Two (replied to User One)',
                         'The toString method should reflect reference changes')