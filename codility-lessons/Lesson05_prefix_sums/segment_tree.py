# Segment tree using python
from collections import defaultdict

__author__ = 'rrbb014'


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
			self.values['sum'] = sum([current_value])
		else:
			result = sum([self.left.values['sum'], self.right.values['sum']])
			if self.range_value is not None:
				bound_length = self.range[1] - self.range[0] + 1
				sum_f = lambda x, y: x * y 
				result = sum_f(self.range_value, bound_length)
			self.values['sum'] = result
		
	def _query(self, start, end):
		if end < self.range[0] or start > self.range[1]:
			return None
		if start <= self.range[0] and self.range[1] <= end:
			return self.values['sum']
		self._push()
		left_res = self.left._query(start, end) if self.left else None
		right_res = self.right._query(start, end) if self.right else None
		
		if left_res is None:
			return right_res
		if right_res is None:
			return left_res
		return sum([left_res, right_res])
		
		
	def _push(self):
		if self.range_value is None:
			return 
		if self.left:
			self.left.range_value = self.range_value
			self.right.range_value = self.range_value
			self.left._sync()
			self.right._sync()
			self.range_value = None
	
	def _update_range(self, start, end, value):
		if end < self.range[0] or start > self.range[1]:
			return 
		if start <= self.range[0] and self.range[1] <= end:
			self.range_value = value
			self._sync()
			return
		self._push()
		self.left._update_range(start, end, value)
		self.right._update_range(start, end, value)
		self._sync()

class SegmentTree:
	def __init__(self, arr):
		self.arr = arr
		self.root = SegmentTreeNode(0, len(arr)-1, self)
	
	def __repr__(self):
		return self.root.__repr__()
	
	def query(self, start, end):
		return self.root._query(start, end)
		
if __name__ == '__main__':
	# input test-case
	T1 = [1, 2, 3, 4, 5]
	A1 = 15 # sum of all 
	A2 = 9 # sum of 1:3

	# segment tree
	st = SegmentTree(T1)
	# compare answer
	assert st.query(0, len(T1)-1) == A1
	assert st.query(1, 3) == A2
