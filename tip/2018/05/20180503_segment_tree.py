# 
class SegmentTreeNode:
	def __init__(self, start, end, segment_tree):
		self.range = (start, end)
		self.parent_tree = segment_tree
		self.range_value = None
		self.values = {}
		self.left = None
		self.right = None
		if start == end:
			self._sync()
			return
			
		self.left = SegmentTreeNode(start, start+(end-start)//2, segment_tree)
		self.right = SegmentTreeNode(start+(end-start)//2 + 1, end, segment_tree)
		self._sync()
	
	def _sync(self):
		if self.range[0] == self.range[1]:
			current_value = self.parent_tree.arr[self.range[0]]
			if self.range_value is not None:
				current_value = self.range_value
			
			self.values = sum([current_value])
		else:
			result = sum([self.left.values, self.right.values])
			if self.range_value is not None:
				bound_length = self.range[1] - self.range[0]
				f = lambda x, y : x*y
				result = f(self.range_value, bound_length)
				
			self.values = result
		
class SegmentTree:

	def __init__(self, arr):
		self.arr = arr
		self.root = SegmentTreeNode(0, len(arr)-1, self)

if __name__ == '__main__':
	A = [5, 1, 4, 3, 4, 2]
	seg = SegmentTree(A)
	from IPython import embed
	embed()