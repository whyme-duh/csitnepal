from django.test import TestCase
from blog.models import Blog


class BlogListViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		no_of_blogs= 20
		for blog in no_of_blogs:
			Blog.objects.create(title="Testing One To Three", content="This is just a testing", sub_title = "Python Django Testing", author ="ritik")


	def test_url_exists(self):
		response = self.client.get('"/blogs')
		self.assertEqual(response.status_code, 200)

