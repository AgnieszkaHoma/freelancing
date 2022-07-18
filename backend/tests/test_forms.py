from django.test import SimpleTestCase
from backend.forms import ContactForm, NewJobForm, CommentForm

class TestForms(SimpleTestCase):
    
    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'email' : 'test@example.com',
            'title' : 'test title', 
            'message' : 'test message',
            
        })
        
        self.assertTrue(form.is_valid())
        
    def test_contact_form_no_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        
    def test_new_job_form_valid_data(self):
        form = NewJobForm(data={
            'title' : 'test@example.com',
            'category' : 'Backend', 
            'proglanguage' : 'Python',
            'description' : 'testowy opis',
            'price' : '300',         
        })
        
        self.assertTrue(form.is_valid())
        
    def test_new_job_form_no_data(self):
        form = NewJobForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
        
        
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'name' : 'Agnes',
            'body' : 'Test comment',       
        })
        
        self.assertTrue(form.is_valid())
        
    def test_comment_form_no_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)