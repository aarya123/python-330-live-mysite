# noinspection PyUnresolvedReferences,PyPackageRequirements
from blogging.models import Post
from django.http import HttpResponse, Http404
from django.shortcuts import render


def stub_view(request, *args, **kwargs):
    body = 'Stub View\n\n'
    if args:
        body += 'Args:\n'
        body += '\n'.join([f'\t{a}' for a in args])
    if kwargs:
        body += 'Kwargs:\n'
        body += '\n'.join([f'\t{a}' for a in kwargs.items()])
    return HttpResponse(body, content_type='text/plain')


def list_view(request):
    published = Post.objects.exclude(published_at__exact=None)
    posts = published.order_by('-published_at')
    context = {'posts': posts}
    '''
    template = loader.get_template('blogging/list.html')
    body = template.render(context)
    return HttpResponse(body, content_type='text/html')
    '''
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_at__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404()
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
