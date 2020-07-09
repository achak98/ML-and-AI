"""
Water jug Problem solution using BFS on state space search.

-Abhirup Chakravarty, 17BCE7055
"""

import copy

class found(Exception):
	pass

class jug(object):

	def __init__(self, cap):
		self.cap = cap
		self.amt = 0
	
	def fill_it(self):
		self.amt = self.cap
		
	def empty(self):
		self.amt = 0
		
	def transfer(self, jug):
		remainder = jug._fill(self.amt)
		self.amt = remainder
		
	def _fill(self, amt):
		self.amt += amt
		if self.amt > self.cap:
			remainder = self.amt - self.cap
			self.amt -= remainder
			return remainder
		else:
			return 0
		
	def __repr__(self):
		
		return "jug: %i/%i" % (self.amt, self.cap)

class jState(object):

	def __init__(self, jugs):
		self.jugs = [copy.copy(j) for j in jugs]
		self.next_states = []
		self.parent = None
		self.goal_flag = False
		
	def add_state(self, jugs_state):
		self.next_states.append(jugs_state)
		jugs_state.parent = self
		
	def is_same(self, state):
		
		for i, j in enumerate(self.jugs):
			if j.cap == state.jugs[i].cap and j.amt != state.jugs[i].amt:
				return False
			
		return True
	
	def is_full(self, amt):
	
		for j in self.jugs:
			if j.amt == amt:
				return True
			
		return False
		
class j_graph(object):
	
	def __init__(self, jugs, goal):
		self.start = jState(jugs)
		self.goal = goal
		self.graphed = False 
		
	def state_exists(self, state):
	
		def fn1(self_state):
			these_states = [state.is_same(s) for s in self_state.next_states]
			child_states = [fn1(s) for s in self_state.next_states]
			
			exists = False
			for ts in these_states:
				exists = exists or ts
			for cs in child_states:
				exists = exists or cs
			
			return exists
		
		this_state = state.is_same(self.start)
		child_states = fn1(self.start)
		return this_state or child_states
	
	def build_graph(self):
	
		def fn1(curr_st):
			try:
				
				for i,j in enumerate(curr_st.jugs):
					
					fill_state = jState(curr_st.jugs)
					fill_state.jugs[i].fill_it()
					
					if not self.state_exists(fill_state):
						curr_st.add_state(fill_state)
					
					if fill_state.is_full(self.goal):
						fill_state.goal_flag = True
						raise found()
						
					
					empty_state = jState(curr_st.jugs)
					empty_state.jugs[i].empty()
					
					if not self.state_exists(empty_state):
						curr_st.add_state(empty_state)

					if empty_state.is_full(self.goal):
						empty_state.goal_flag = True
						raise found()
						

					for k in range(len(curr_st.jugs)):
						if i == k:
							continue
						intermittent_st = jState(curr_st.jugs)
						intermittent_st.jugs[i].transfer(intermittent_st.jugs[k])

						if not self.state_exists(intermittent_st):
							curr_st.add_state(intermittent_st)

						if intermittent_st.is_full(self.goal):
							intermittent_st.goal_flag = True
							raise found()
						
				for s in curr_st.next_states:
					if s.goal_flag:
						raise found()
					fn1(s)
			except found:
				pass
			
		self.graphed = True
		fn1(self.start)

	def print_solutions(self):

		self.solution_number = 0
		self.solutions = []

		def trav_st(curr_st):
			if curr_st.goal_flag:
				self.solution_number += 1
				print("Solution %i" % self.solution_number)

				state_list = get_path(curr_st)
				for s in state_list:
					print(s.jugs)
				print("%i steps" % len(state_list))
				self.solutions.append({
					"steps": len(state_list),
					"list": state_list
				})
			else:
				for s in curr_st.next_states:
					trav_st(s)

		def get_path(curr_st, curr_path = []):
			curr_path = [curr_st] + curr_path
			if curr_st.parent:
				return get_path(curr_st.parent, curr_path)
			else:
				return curr_path

		if self.graphed:
			trav_st(self.start)
			if self.solution_number == 0:
				print("No solution found.")
			else:
				print("\nBest solution found:")
				min_steps = 9999999999
				solution = None
				for s in self.solutions:
					if s["steps"] < min_steps:
						min_steps = s["steps"]
						solution = s
				for s in solution["list"]:
					print(s.jugs)
				print("%i steps" % solution["steps"])

		else:
			
			print("Didn't build graph.")
		
	def __repr__(self):
		def fn1(states, prefix = "-"):
			string = ""
			for s in states:
				string += prefix + str(s.jugs)
				if s.goal_flag:
					string += " <----"
				string += "\n"
				string += fn1(s.next_states, "-" + prefix)
			return string
				
		string = str(self.start.jugs)
		if self.start.goal_flag:
			string += " <----"
		string += "\n"
		string += fn1(self.start.next_states)
		
		return string

def main():
	jugs = input("Input each jug size, separated by space, then press enter.\n")
	goal = input("Input target amt: ")
	jugs = [jug(int(x)) for x in jugs.split()]
	goal = int(goal)

	graph = j_graph(jugs, goal)
	graph.build_graph()
	print(graph)

	graph.print_solutions()

if __name__ == '__main__':
	main()