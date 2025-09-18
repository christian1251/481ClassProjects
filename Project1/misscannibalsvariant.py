from search import *

class MissCannibalsVariant(Problem):
    """ The problem of Missionaries and Cannibals. 
    N1 and N2 are the total number of missionaries and cannibals starting from the left bank.
    A state is represented as a 3-tuple, two numbers and a boolean:
    state[0] is the number of missionaries on the left bank (note: the number of missionaries on the right bank is N1-m)
    state[1] is the number of cannibals on the left bank (note: the number of cannibals on the right bank is N2-c)
    state[2] is true if boat is at the left bank, false if at the right bank """

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)
        
    
    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal
        
    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        m_count = action.count('M')
        c_count = action.count('C')
        
        if (state[2]):
            new_m = state[0] - m_count
            new_c = state[1] - c_count
            boat = False
        else:
            new_m = state[0] + m_count
            new_c = state[1] + c_count
            boat = True
            
        return (new_m, new_c, boat)
    
    def actions(self, state):
        """ Return the actions that can be executed in the given state."""
        
        actions = []
        
        if(state[2]):
            # generate possible actions from left side 
            m_available = state[0]
            c_available = state[1]
        
            for m_count in range(m_available + 1):
              for c_count in range(c_available + 1):
                  if 1 <= m_count + c_count <= 3:
                      # make string based on m and c count
                      action = "M" * m_count + "C" * c_count
                      new_state = self.result(state, action)
                      if self.is_valid_state(new_state):
                          actions.append(action)
                      
                           
        else:
            # generate possible actions from right side 
            m_available = self.N1 - state[0]
            c_available = self.N2 - state[1]
            
              
            for m_count in range(m_available + 1):
              for c_count in range(c_available + 1):
                  if 1 <= m_count + c_count <= 3:
                      # make string based on m and c count
                      action = "M" * m_count + "C" * c_count
                      new_state = self.result(state, action)
                      if self.is_valid_state(new_state):
                          actions.append(action)
            
        return actions
        
if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    print(mc.actions((3, 3, True))) # Test your code as you develop! This should return  ['MC', 'MMM']

    # path = depth_first_graph_search(mc).solution()
    # print(path)
    # path = breadth_first_graph_search(mc).solution()
    # print(path)

