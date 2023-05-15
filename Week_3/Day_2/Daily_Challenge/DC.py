# 1. Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# 2. The Pagination class will accept 2 parameters:

# 	* items (default: None): It will contain a list of contents to paginate.
# 	* pageSize (default: 10): The amount of items to show in each page.
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

class Pagination():
	def __init__(self, items=None, pageSize=10):
		self.items = items
		self.pageSize = pageSize
	
# 3. The Pagination class will have a few methods:
# 	* getVisibleItems() : returns a list of items visible depending on the pageSize

	def getVisibleItems(self):
		visible_items =  self.items[0 : self.pageSize]
		print(visible_items)
			
# 	* You will have to implement various methods to go through the pages such as:
		# prevPage()
		# nextPage()
		# firstPage()
		# lastPage()
		# goToPage(pageNum)

p = Pagination(alphabetList, 4)
p.getVisibleItems() 