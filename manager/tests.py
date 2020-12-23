from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from slugify import slugify

from manager.models import Book


class TestMyAppPlease(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test_user")
        self.user1 = User.objects.create_user("test_user1")
        self.user2 = User.objects.create_user("test_user2")

    def test_add_book(self):
        self.client.force_login(self.user)
        url = reverse("add-book")
        data = {
            'title': "test title",
            'text': "test text"
        }
        responce = self.client.post(url, data)
        self.assertEqual(responce.status_code, 302, msg="is not redirected")
        self.assertTrue(Book.objects.exists(), msg="book is not created")
        book = Book.objects.first()
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.text, data['text'])
        self.assertEqual(book.slug, slugify(data['title']))
        self.assertEqual(book.authors.first(), self.user)
        self.client.logout()
        data = {
            'title': "test title2",
            'text': "test text"
        }
        responce = self.client.post(url, data)
        self.assertEqual(responce.status_code, 302, msg="is not redirected")
        self.assertEqual(Book.objects.count(), 1, msg="created book without author")


    def test_update_book(self):
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title="test_title1")
        self.book1.authors.add(self.user)
        self.book1.save()
        self.book2 = Book.objects.create(title="test_title2")
        self.assertEqual(Book.objects.count(), 2)
        data = {
            'title': "test title2",
            'text': "test text"
        }
        url = reverse('update-book', kwargs=dict(slug=self.book1.slug))
        responce = self.client.post(url, data)
        self.assertEqual(responce.status_code, 302)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, data['title'], msg="book1 is not refreshed")
        self.assertEqual(self.book1.text, data['text'], msg="book1 is not refreshed" )
        self.assertEqual(self.book1.authors.first(), self.user)
        self.client.logout()
        url = reverse('update-book', kwargs=dict(slug=self.book2.slug))
        responce = self.client.post(url, data)
        self.assertEqual(responce.status_code, 302)
        self.book2.refresh_from_db()
        self.assertNotEqual(self.book2.title, data['title'])
        self.assertNotEqual(self.book2.text, data['text'])


    def test_rate_book(self):
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title="test_title1")
        url = reverse("add-rate", kwargs=dict(slug=self.book1.slug, rate=3))
        self.client.get(url)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.rate, 3)
        # second user
        self.client.force_login(self.user1)
        url = reverse("add-rate", kwargs=dict(slug=self.book1.slug, rate=4))
        self.client.get(url)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.rate, 3.5)
        # three user
        self.client.force_login(self.user2)
        url = reverse("add-rate", kwargs=dict(slug=self.book1.slug, rate=5))
        self.client.get(url)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.rate, 4)
        # #first user
        # url = reverse("add-rate", kwargs=dict(slug=self.book1.slug, rate=5))
        # self.client.force_login(self.user)
        # self.client.get(url)
        # self.book1.refresh_from_db()
        # self.assertNotEqual(self.book1.rate, 4)
        #


    def test_delete_book(self):
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title="test_title")
        self.book1.authors.add(self.user)
        self.book1.save()
        self.book2 = Book.objects.create(title="test_title2")
        self.assertEqual(Book.objects.count(), 2)
        url = reverse("delete-book", kwargs=dict(slug=self.book1.slug))
        self.client.get(url)
        self.assertEqual(Book.objects.count(), 1)
        url = reverse("delete-book", kwargs=dict(slug=self.book2.slug))
        self.client.get(url)
        self.assertEqual(Book.objects.count(), 1)
        self.client.logout()
        self.client.get(url)
        self.assertEqual(Book.objects.count(), 1)