from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
# noinspection PyUnresolvedReferences,PyPackageRequirements
from polling.models import Poll


class CustomListView:
    model = None
    template_name = None

    def as_view(self):
        return self.get

    def get(self, request):
        model_list_name = self.model.__name__.lower() + '_list'
        context = {model_list_name: self.model.objects.all()}
        return render(request, self.template_name, context)


class CustomPollListView(CustomListView):
    model = Poll
    template_name = 'polling/list.html'


# class CustomPostListView(CustomListView):
#     model = Post
#     template_name = 'blogging/list.html'

class PollListView(ListView):
    model = Poll
    template_name = 'polling/list.html'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()
        if request.POST.get('vote') == 'Yes':
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
        context = {'object': poll}
        return render(request, self.template_name, context)


def list_view(request):
    context = {'polls': Poll.objects.all}
    return render(request, 'polling/list.html', context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        if request.POST.get('vote') == 'Yes':
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)
