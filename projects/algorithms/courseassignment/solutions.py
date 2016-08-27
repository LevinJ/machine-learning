import numpy as np

"""

#####################################Solution for question 1######################################

"""
"""
Helper function for question1, determine if a and b is anagram
"""
def question1_isanagram(a, b):
    if (len(a) != len(b)):
        raise 'a and b should have equal length'
    for letter_a in a:
        letter_find = False
        for i in range(len(b)):
            if letter_a == b[i]:
                letter_find = True
                #remove the letter tht has been found so that we do not have to search it next time
                b = b[:i] + b[i+1:]
                break
        if not letter_find:
            return False
    return True
def question1(s, t):
    s_lenght = len(s)
    t_length = len(t)
    
    if t_length <= 1:
        return False
    if s_lenght < t_length:
        return False
    s = s.lower()
    t = t.lower()
    for i in range(s_lenght):
        start = i
        end = start + t_length
        if (end > s_lenght):
            break
        if (question1_isanagram(s[start:end], t)):
            return True
    return False


print "Test case for Question 1"     
#True
print question1('This is Madam Curie, she is cool', 'Radium came')

#False, edge case
print question1('l', 'l')

#False, edge case
print question1('', 'silent')


"""

#####################################Solution for question 2######################################

"""

"""
Helper function for question2,  determine if string s is a Palindrome
return a tuple (bispalindrome, palindrome_length)
bispalindrome: if s is a palindrome
palindrome_length: the lenght of palindrome, excluding punctuation, and word dividers.
"""
def question2_ispalindrome(s):
    s = s.lower()
    letter_to_remvoe = [',', ' ','!','?']
    for letter in letter_to_remvoe:
        s = s.replace(letter, '')

    s_length = len(s)
    if s_length < 3:
        return False, 0
    start = 0
    end = s_length - 1
    while start < end:
        if s[start] != s[end]:
            return False, 0
        start =start + 1
        end   = end -1 
    return True, len(s)
def question2(a):
    a_length = len(a)
    largest_palindrome_length = 0
    largetst_palindrome_string = ""
    for start in range(a_length):
        end = a_length
        while end >= start + 2:
            sub_string = a[start:end]
            bispalindrome, palindrome_length = question2_ispalindrome(sub_string)
    
            #update largest palindrome if neccessary
            if bispalindrome:
                if palindrome_length >= largest_palindrome_length:
                    # largest_palindrome_length is updated even when it's equal to palindrome_length
                    # this is because we want to display the resultant palindrome string without chararacters like  [',', ' ','!','?']
                    largest_palindrome_length = palindrome_length
                    largetst_palindrome_string = sub_string
            #move the end pointer forward
            end = end -1
        
    return largetst_palindrome_string
# print question2_ispalindrome("Eva, can I stab bats in a 1cave?")
print "Test case for Question 2"    
#A man, a plan, a canal, Panama
print question2("three palindromes in all, A man, a plan, a canal, Panama!, stressed, put it up, find the longest one")

# "", edge case, expect to see a blank line in the console
print question2("")

# "", edge case, expect to see a blank line in the console
print question2("no Palindrome")


"""

#####################################Solution for question 3######################################

"""

class quetion3_helper(object):
    def get_initial_mstree(self, G):
        # selct a random node into the minimum spanning tee
        return {G.keys()[0]:[]}
    """
    get all  edges in the graph
    """
    def get_all_edges(self, G):
        res = {}
        for node, edges in G.iteritems():
            for edge in edges:
                node2= edge[0]
                edge_value = edge[1]
                if node+node2 not in res:
                    res[node+ node2] = edge_value
                    
        return res
    """
    get all outgoing edges of current minimum spannding tree
    """
    def get_outgoing_edges(self, alledges, mstree):
        res = {}
        nodes_in_mstree = mstree.keys()
        for edge_name, edge_value in alledges.iteritems():
            if (edge_name[0] in nodes_in_mstree) and (not edge_name[1] in nodes_in_mstree):
                #put the node in mstree as first letter
                res[edge_name[0] + edge_name[1]] = edge_value
                continue
            if (not edge_name[0] in nodes_in_mstree) and ( edge_name[1] in nodes_in_mstree):
                #put the node in mstree as first letter
                res[edge_name[1] + edge_name[0]] = edge_value     
        return res
    """
    find minimum edge out of all outging edges
    """
    def find_minimum_outgoing_edge(self, outgoing_edges):
        min_edge_value = None
        min_edge_name = None
        for edge_name,edge_value  in outgoing_edges.iteritems():
            if min_edge_value is None or  edge_value < min_edge_value:
                min_edge_value = edge_value
                min_edge_name = edge_name
        return min_edge_name, min_edge_value
    """
    update mstree, add the new node into the mstree
    """
    def update_mstree(self, mstree, min_edge_name, min_edge_value):
        existing_node_name = min_edge_name[0]
        new_node_name = min_edge_name[1]
        #insert the new edge 
        mstree[existing_node_name].append((new_node_name, min_edge_value))
        #insert the new node and new edge
        mstree[new_node_name] = [(existing_node_name, min_edge_value)]
        return
    def question3(self, G):
        if G is None:
            return None
        nodes_num = len(G) #number of nodes in the graph
        alledges = self.get_all_edges(G)
        mstree = self.get_initial_mstree(G)
        while len(mstree) < nodes_num:
            outgoing_edges = self.get_outgoing_edges(alledges, mstree)
            min_edge_name, min_edge_value = self.find_minimum_outgoing_edge(outgoing_edges)
            self.update_mstree(mstree, min_edge_name, min_edge_value)
        return mstree

def question3(G):
    obj = quetion3_helper()
    return obj.question3(G)

print "Test case for Question 3"
G= {'S':[('A', 7), ('C',8)],
    'A':[('S', 7), ('C',3),('B',6)],
    'B':[('A', 6),  ('C', 4), ('D', 2),('T', 5)],
    'C':[('S', 8), ('A', 3), ('B', 4), ('C',3)],
    'D':[('C', 3), ('B', 2), ('T', 2)],
    'T':[('D',2),('B', 5)]}
#{'A': [('C', 3), ('S', 7)], 'C': [('A', 3), ('D', 3)], 'B': [('D', 2)], 'D': [('C', 3), ('B', 2), ('T', 2)], 'S': [('A', 7)], 'T': [('D', 2)]}
print question3(G)

#None, edge case, input is empty graph
print question3(None)

G={'A': [('C', 3), ('S', 7)], 'C': [('A', 3), ('D', 3)], 'B': [('D', 2)], 'D': [('C', 3), ('B', 2), ('T', 2)], 'S': [('A', 7)], 'T': [('D', 2)]}
#{'A': [('C', 3), ('S', 7)], 'C': [('A', 3), ('D', 3)], 'B': [('D', 2)], 'D': [('C', 3), ('B', 2), ('T', 2)], 'S': [('A', 7)], 'T': [('D', 2)]}, edge cases, input is a tree
print question3(G)



"""

#####################################Solution for question 4######################################

"""

class Question4_helper:
    """
    find the parent path of a node, all the way up to root node
    T: the tree
    r: root node of the three
    n: the node
    parents_path: the resultant parent path of node n
    """
    def find_parents_path(self, T, r, n, parents_path):
        if (r == n):
            return
        #the column of the matrix that contains node n's parent
        potential_parent = np.array(T)[:,n]
        for i in range(len(potential_parent)):
            if (potential_parent[i] == 1):
                parent = i
                parents_path.insert(0, parent)
                break
        self.find_parents_path(T, r, parent, parents_path)
        return
    def find_least_common_ancestor(self, T, r, n1, n2):
        parents_path_n1 = [n1]
        self.find_parents_path(T, r, n1, parents_path_n1)
        parents_path_n2 = [n2]
        self.find_parents_path(T, r, n2, parents_path_n2)
        max_length = min([len(parents_path_n1), len(parents_path_n2)])
        common_ancestor = None
        for i in range(max_length):
            if (parents_path_n1[i] == parents_path_n2[i]):
                common_ancestor = parents_path_n1[i]
            else:
                break
        return common_ancestor
    
def question4(T, r, n1, n2):
    helper = Question4_helper()
    return helper.find_least_common_ancestor(T, r, n1, n2)
print "Test case for Question 4"
#3
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)

#1, edge case both nodes refer to the same nodes
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,1)

#0, edge case, the two nodes are already parent/child relationship
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,0,1)


"""

#####################################Solution for question 5######################################

"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        return

def initiate_list(linked_list):   
    for i in np.arange(2, 6,1):
        tail  = linked_list
        while tail.next is not None:
            tail = tail.next
        tail.next  = Node(i)
    return
"""
Helper function that transform the linked list to an array, for easier access via index later on
"""
def question5_tranforminto_array(linked_list):
    arr = []
    current_node = linked_list
    while current_node is not None:
        arr.append(current_node)
        current_node = current_node.next
    return arr
def question5(linked_list, m):
    if m < 1:
        return None
    arr = question5_tranforminto_array(linked_list)
    arr_length = len(arr)
    index = arr_length -m
    if index < 0:
        return None
    return arr[arr_length -m ].data

print "Test case for Question 5"
linked_list = Node(1) 
initiate_list(linked_list)
#3
print question5(linked_list, 3)

# None, edge case, passed the root node
print question5(linked_list, 10)

#None, edge case, invalid input
print question5(linked_list, -1)
