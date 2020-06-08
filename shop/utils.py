import random
import string
from django.utils.text import slugify


def random_string_generator(size=15, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# def translitirate_chars()

def slug_generator(obj, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(obj.title, allow_unicode=True)

    
    Klass = obj.__class__
    queryset_exsists = Klass.objects.filter(slug=slug).exists()#true false
    if queryset_exsists:
        slug = slug
        randomstring = random_string_generator()
        new_slug = f'{slug}-{randomstring}'
        return slug_generator(obj, new_slug=new_slug)
    else:
        return slug
        