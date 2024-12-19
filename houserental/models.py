from django.db import models
from django.db import models
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile

class data(models.Model):
    photo=models.ImageField(upload_to='uploads/') 
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    BHK=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    rent=models.CharField(max_length=20)

def save(self, *args, **kwargs):
        # Open the uploaded image
        img = PilImage.open(self.poster)

        # Convert to JPEG format (or any other format you need)
        if img.format != 'JPEG':
            img = img.convert('RGB')
            img_io = BytesIO()
            img.save(img_io, format='JPEG', quality=85)  # Set quality as needed
            img_file = ContentFile(img_io.getvalue(), name=self.poster.name.split('.')[0] + '.jpg')

            # Update the poster field with the new JPEG file
            self.poster.save(img_file.name, img_file, save=False)

        # Call the original save method
        super().save(*args, **kwargs)