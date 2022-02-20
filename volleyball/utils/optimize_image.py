""" Optimize image for better compression """

# Django
from django.core.files.uploadedfile import InMemoryUploadedFile

# Utilities
from PIL import Image
from io import BytesIO
import sys



class OptimizeImage:
    """ Optimize image for better compression """

    def __init__(self, image):
        """ Initialize the class. """

        self.image = image

    def optimize(self):
        """ Optimize the image. """

        imageTemproary = Image.open(self.image)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()

        w, h = imageTemproary.size

        if w > 2000:
            w = int(w/4)
            h = int(h/4)

        elif h > 2000:
            w = int(w/4)
            h = int(h/4)

        elif w > 1400:
            w = int(w/3)
            h = int(h/3)

        elif h > 1400:
            w = int(w/3)
            h = int(h/3)

        elif w > 800:
            w = int(w/2)
            h = int(h/2)

        elif h > 800:
            w = int(w/2)
            h = int(h/2)

        imageTemproary = imageTemproary.resize((w, h))
        imageTemproary.save(
            outputIoStream, 
            format='JPEG', 
            optimize=True, 
            quality=150
        )

        outputIoStream.seek(0)

        self.image = InMemoryUploadedFile(
            outputIoStream, 
            'ImageField', "%s.jpg" %self.image.name.split('.')[0], 
            'image/jpeg',
            sys.getsizeof(outputIoStream),
            None
        )

        return self.image