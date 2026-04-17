from django.urls import path
from .views import (
    ContactCreateView, CareerApplicationCreateView, PropertyListCreateView, 
    InquiryCreateView, InvestedProjectListCreateView, NewsletterCreateView
)

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    path('careers/', CareerApplicationCreateView.as_view(), name='career-create'),
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('inquiries/', InquiryCreateView.as_view(), name='inquiry-create'),
    path('invested-projects/', InvestedProjectListCreateView.as_view(), name='invested-project-list'),
    path('newsletter/', NewsletterCreateView.as_view(), name='newsletter-subscribe'),
]
