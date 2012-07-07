from django.views.generic.detail import DetailView
from models import Partner

class PartnerDetailView(DetailView):
    model = Partner
