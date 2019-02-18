import unittest
from run import Comments, comments

class TestComments(unittest.TestCase):
  """
  Test case for comments class
  """

  def setUp(self):
    """
    set up to run before each test cases.
    """
    self.new_comment = Comments("Neville","This is a comment") 

  def tearDown(self):
    """
    method that cleans up after each test has run.
    """
    Comments.comments = []

  def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """

    self.assertEqual(self.new_comment.author,"Neville")
    self.assertEqual(self.new_comment.message,"This is a comment")

  def test_save_comment(self):
    """
    test save comment test case to test if the new account object is saved into the contact list
    """
    self.new_comment.new_comment()
    self.assertEqual(len(comments),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

