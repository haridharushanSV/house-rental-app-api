from django.db import models
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile

class data(models.Model):
    photo1=models.ImageField(upload_to='uploads/') 
    photo2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    photo3=models.ImageField(upload_to='uploads/', blank=True, null=True) 
    photo4=models.ImageField(upload_to='uploads/', blank=True, null=True) 
    photo5=models.ImageField(upload_to='uploads/', blank=True, null=True) 
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=2000)
    BHK_CHOICES = (
        ('0' , ' '),
        ('1','1BHK' ),
        ('2','2BHK'),
        ('3','3BHK'),
        ('4','4BHK'),
        ('5','5BHK'),
        ('6','6BHK'),
        ('7','7BHK'),
    )
    BHK=models.CharField(max_length=1, choices=BHK_CHOICES)
    bachelor_CHOICES= (
        ('0' , ' '),
        ('1','YES' ),
        ('2','NO' ),
        )
    bachelor=models.CharField(max_length=1, choices=bachelor_CHOICES)
    location=models.CharField(max_length=20)
    city_CHOICES = (
    ('0' , ' '),
    ('1', 'Ambur'),
    ('2', 'Ariyalur'),
    ('3', 'Chennai'),
    ('4', 'Coimbatore'),
    ('5', 'Cuddalore'),
    ('6', 'Dharmapuri'),
    ('7', 'Dindigul'),
    ('8', 'Erode'),
    ('9', 'Kanchipuram'),
    ('10', 'Kanyakumari'),
    ('11', 'Karur'),
    ('12', 'Krishnagiri'),
    ('13', 'Madurai'),
    ('14', 'Nagapattinam'),
    ('15', 'Namakkal'),
    ('16', 'Perambalur'),
    ('17', 'Pudukkottai'),
    ('18', 'Ramanathapuram'),
    ('19', 'Salem'),
    ('20', 'Sivaganga'),
    ('21', 'Tenkasi'),
    ('22', 'Thanjavur'),
    ('23', 'Theni'),
    ('24', 'Thoothukudi'),
    ('25', 'Tiruchirappalli'),
    ('26', 'Tirunelveli'),
    ('27', 'Tiruppur'),
    ('28', 'Tiruvallur'),
    ('29', 'Tiruvannamalai'),
    ('30', 'Tiruvarur'),
    ('31', 'Vellore'),
    ('32', 'Viluppuram'),
    ('33', 'Virudhunagar') 
    )
    city=models.CharField(max_length=20, choices=city_CHOICES)
    rent=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)

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