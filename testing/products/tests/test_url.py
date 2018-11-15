from django.urls import reverse,resolve

class TestUrls:
	def test_detail(self):
		path=reverse('detail',kwargs={'pk':1})
		assert resolve(path).view_name=='detail'