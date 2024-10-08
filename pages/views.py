from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context= {
        "inventory_list": ["Widget 1","Widget 2", "Widget 3"], 
        "greeting": "Thank you FOR VIsiting"
    }
    return render(request,"home.html",context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main street"
        context["phone_number"] = "123-456-7890"
        return context
class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["product_1"] = "Cast iron pan"
        context["product_2"] = "Chefs knife"
        context["product_3"] = "cutting board"
        context['product_4'] = "plates"
        return context
