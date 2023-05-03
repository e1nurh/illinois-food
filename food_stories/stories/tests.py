from django.test import TestCase
from .models import Story
from django.contrib.auth.models import User
import time

class TestStoryModel(TestCase):
    def setUp(self) -> None:

        self.user = User.objects.create_user(username='akif', password="asd123")

        self.story1 = Story.objects.create(
            title = "Test story 1",
            description = "Test description",
            author = self.user
        )
    
    def test_title(self):
        time.sleep(20)
        self.assertEqual('Test story 1', self.story1.title)
    
    def test_user(self):
        self.assertIsInstance(self.user, User)