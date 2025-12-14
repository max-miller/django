from django.db import models

# Create your models here.
class annual_reviews(models.Model):
    title= models.TextField()
    author = models.TextField()
    cover_img_link = models.TextField()
    review = models.TextField()
    edition_number = models.IntegerField()

    def paragraph_split(self):
        return self.review.split('<p>')