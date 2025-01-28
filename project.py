""" ----------------------------------------------------------------------------
******** Search Code for DFS  and other search methods
******** (expanding front only)
"""

import copy

import sys 
  
sys.setrecursionlimit(10**6) 

# ******** Operators

  
def go_to_floor1(state , floor_num):
    if state[-1] < 8 and state[floor_num] > 0:
        if state[floor_num] > 8 - state[-1]:
            new_state = state[:floor_num] + [state[floor_num] + state[-1] - 8] + state[floor_num+1:-1] + [8]
        else:
            new_state = state[:floor_num] + [0] + state[floor_num+1:-1] + [state[floor_num] + state[-1]]
        new_state[0] = floor_num
        return new_state
    return None
'''
Descendant finding function of the current state
'''
def find_children(state):
    children = []
    if state[-1]==8:
        floor_state = copy.deepcopy(state)
        floor_state[0]=5
        floor_state[5]=0
        children.append(floor_state)
    else:
        for floor in range(1, 5):
            floor_state = copy.deepcopy(state)
            floor_child = go_to_floor1(floor_state, floor)
            if floor_child is not None:
                children.append(floor_child)
    
    return children



""" ----------------------------------------------------------------------------
**** Front Management
"""

""" ----------------------------------------------------------------------------
** initialization of front
"""

def make_front(state):
    return [state]
    
""" ----------------------------------------------------------------------------
**** expanding front  
"""

def expand_front(front, method):  
    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)
    
    elif method=='BFS':
        print("Front:")
        print(front)
        node=front.pop(0)
        for child in find_children(node):     
            front.append(child)
            
    elif method=='BestFS':
        print("Front:")
        print(front)
        node=front.pop(0)
        for child in find_children(node):     
            front.append(child)
            front.sort()
    #else: "other methods to be added"        
    
    return front


""" ----------------------------------------------------------------------------
**** QUEUE
"""

""" ----------------------------------------------------------------------------
** initialization of queue
"""

def make_queue(state):
    return [[state]]

""" ----------------------------------------------------------------------------
**** expanding queue
"""

def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)
    
    elif method=='BFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
    
    elif method=='BestFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
            queue_copy.sort()
    #else: "other methods to be added" 
    
    return queue_copy



""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
"""

def find_solution(front, queue, closed, goal, method):
#def find_solution(front, queue, closed, method):
       
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)
        #find_solution(new_front, new_queue, closed, method)
    
    #elif is_goal_state(front[0]):
    elif front[0]==goal:
        print('_GOAL_FOUND_')
        #print(front[0])
        print(queue[0])
        
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)
        #find_solution(front_children, queue_children, closed_copy, method)
        
        
        
"""" ----------------------------------------------------------------------------
** Executing the code
"""
           
def main():
    
    initial_state = [0, 9, 4, 12, 7, 0]
    goal = [5, 0, 0, 0, 0, 0]
    method='BestFS'
    
#BestFS DFS BFS    
    
    """ ----------------------------------------------------------------------------
    **** starting search
    """
    
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], goal, method)
    #find_solution(make_front(initial_state), make_queue(initial_state), [], method)
    
    
if __name__ == "__main__":
    main()
