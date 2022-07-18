from django.test import SimpleTestCase
from django.urls import reverse, resolve
from backend.views import *

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
        
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, UserRegisterView)  
            
    def test_login_url_is_resolved(self):
        url = reverse('loginPage')
        self.assertEquals(resolve(url).func, loginPage)