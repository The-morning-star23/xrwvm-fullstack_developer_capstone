"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from djangoapp import views

urlpatterns = [
    path("register/", TemplateView.as_view(template_name="index.html")),
    path("login/", TemplateView.as_view(template_name="index.html")),
    path("contact/", TemplateView.as_view(template_name="Contact.html")),
    path("about/", TemplateView.as_view(template_name="About.html")),
    path("admin/", admin.site.urls),
    path("djangoapp/", include("djangoapp.urls")),
    path("", TemplateView.as_view(template_name="Home.html")),
    path("dealers/", TemplateView.as_view(template_name="index.html")),
    path(
        "dealer/<int:dealer_id>",
        TemplateView.as_view(template_name="index.html")
    ),
    path(
        "reviews/dealer/<int:dealer_id>/",
        views.get_dealer_reviews,
        name="get_dealer_reviews",
    ),
    path(
        "postreview/<int:dealer_id>",
        TemplateView.as_view(template_name="index.html")
    ),
    path(
        "searchcars/<int:dealer_id>",
        TemplateView.as_view(template_name="index.html")
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    # Add this line to serve manifest.json
    # directly from the React build folder
    urlpatterns += [
        path(
            "manifest.json",
            TemplateView.as_view(
                template_name="manifest.json", content_type="application/json"
            ),
        ),
    ]
