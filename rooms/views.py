from django.utils import timezone
from django.views.generic import ListView
from . import models


class HomeView(ListView):
    """ Home View Define"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 6
    ordering = "created"
    context_object_name = "rooms"  # object_list 대신 rooms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now

        return context  # context는 템플릿으로 가는 변수
