from django.views.generic import ListView, DetailView

from board.models import Board


class BoardList(ListView):
    model = Board
    ordering = '-pk'

class BoardDetail(DetailView):
    model = Board
