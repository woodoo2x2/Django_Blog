from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/index.html', context={
        'title' : 'Post Lists',
        'content' : 'Posts: '
    })
