from . import models


def menu_link(request):
    links = models.Categoria.objects.all()
    return dict(links=links)