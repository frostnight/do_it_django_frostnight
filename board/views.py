from django.views.generic import ListView

from board.models import Board


class BoardList(ListView):
    model = Board
    ordering = '-pk'
