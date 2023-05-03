from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class StoryImage(models.Model):
    image = models.ImageField(upload_to="story_images")
    story = models.ForeignKey('stories.Story', on_delete=models.CASCADE, related_name="images")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.story.title

class Category(models.Model):
    name = models.CharField(max_length=20)
    background_image = models.ImageField(upload_to="category_images")
    
    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    read_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")    
    text = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")

    created_at = models.DateTimeField(auto_now_add=True)


    