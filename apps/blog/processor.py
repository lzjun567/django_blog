from .models import Tag
def tag_list(request):
    tags = Tag.objects.all()
    ctx = {'tag1s': tags[0:len(tags)/2],
           'tag2s': tags[len(tags)/2:]
    }
    return ctx 

