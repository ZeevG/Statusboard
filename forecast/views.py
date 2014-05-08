# views.py
from rest_framework_proxy.views import ProxyView


class ItemListProxy(ProxyView):
    """
    List of items
    """
    source = 'items/'


class ProxyDetailView(ProxyView):
    """
    Item detail
    """
    source = 'forecast/%(pk)s'
