from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='body/images/%Y/%m/%d/', blank=True)
    # file_upload = models.FileField(upload_to='body/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    # tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'[{self.pk}] {self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/body/{self.pk}'

    # def get_file_name(self):
    #     return os.path.basename(self.file_upload.name)