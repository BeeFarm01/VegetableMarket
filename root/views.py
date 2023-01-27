from django.views.generic import TemplateView
from vegetables.models import VegTitle, VegList
from about.models import About
from customers.models import CustomerTitle, CustomerList
from footer.models import Footer1, Footer2
from home.models import HomeImage, HomeContent
from contact.models import Contact


class IndexPage(TemplateView):
     template_name = 'index.html'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context["vet_title"] = VegTitle.objects.last()
          context["vet_list"] = VegList.objects.all()
          context["about"] = About.objects.last()
          context["customer_title"] = CustomerTitle.objects.last()
          context["customer_list"] = CustomerList.objects.all()
          context["footer_one"] = Footer1.objects.last()
          context["footer_two"] = Footer2.objects.last()
          context["home_image"] = HomeImage.objects.last()
          context["home_content"] = HomeContent.objects.all()
          context["contact"] = Contact()



          return context