from blog.models import Post
from django.utils import timezone
from django.shortcuts import render

# Create your views here.
def index(request):
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'blog/index.html', {'posts': posts})



