from app.v1.models.models import User,Admin
import unittest
  class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.test_comment = {
            'author':'Linet',
            'comment_id':'1',
            'comments':'How are you'
        }
  
  
  
    def test_admin_edit(self):
         self.assertEqual(['Message'],'You are not an admin')

    def test_admin_delete(self):
         self.assertEqual(['Message'],'You are not an admin')
