from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "name"], name="tag of username")
        ]

    def __str__(self):
        return f"{self.name}"


class Note(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name}"


# # Extending User Model Using a One-To-One Link
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(default="default_avatar.png", upload_to="profile_images")

#     def __str__(self):
#         return self.user.username

#     # resizing images
#     def save(self, *args, **kwargs):
#         super().save()

#         img = Image.open(self.avatar.path)

#         if img.height > 250 or img.width > 250:
#             new_img = (250, 250)
#             img.thumbnail(new_img)
#             img.save(self.avatar.path)
