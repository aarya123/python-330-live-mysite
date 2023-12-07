from django.urls import path

# noinspection PyUnresolvedReferences,PyPackageRequirements
from polling.views import list_view, detail_view, PollListView, PollDetailView

urlpatterns = [
    path("", PollListView.as_view(), name="poll_index"),
    path("<int:pk>", PollDetailView.as_view(), name="poll_detail"),
]
