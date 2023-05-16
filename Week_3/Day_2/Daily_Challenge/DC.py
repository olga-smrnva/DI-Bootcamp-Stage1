# 1. Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# 2. The Pagination class will accept 2 parameters:

# 	* items (default: None): It will contain a list of contents to paginate.
# 	* pageSize (default: 10): The amount of items to show in each page.
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

class Pagination():
	def __init__(self, items=None, page_size=10):
		self.items = items
		self.page_size = int(page_size)
		self.current_page = 1
		self.pages_data = {}
		self.number_of_pages = 0
		self._gen_pages_data()

	def _gen_pages_data(self):
		count = 0
		page = 1
		for item in self.items:
			if count < self.page_size:
				if count == 0:
					self.pages_data[page] = [item]
				else:
					self.pages_data[page].append(item)
			else:
				count = 0
				page+=1
				self.pages_data[page] = [item]
			count+=1
		self.number_of_pages = page

	def prev_page(self):
		if self.current_page != 1:
			self.current_page -= 1
		return self

	def next_page(self):
		if self.current_page != self.number_of_pages:
			self.current_page += 1
		return self
	
	def first_page(self):
		self.current_page = 1
		return self

	def last_page(self):
		self.current_page = self.number_of_pages
		return self

	def go_to_page(self, page_num):
		if(int(page_num) > 0 and int(page_num) <= self.number_of_pages):
			self.current_page = int(page_num)
		return self

	def get_visible_items(self):
		visible_items =  self.pages_data[self.current_page]
		print(visible_items)
		return self


p = Pagination(alphabetList, 4)
p.get_visible_items().next_page().get_visible_items().prev_page().get_visible_items().go_to_page(3).get_visible_items().first_page().get_visible_items().last_page().get_visible_items()