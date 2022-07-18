from django.test import TestCase, Client
from django.urls import reverse
from backend.models import JobAdvert, Freelancer, Comment, Contact
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.freelancers_url = reverse('freelancers')
            
    def test_freelancers_GET(self):
        response = self.client.get(self.freelancers_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend/freelancers.html')