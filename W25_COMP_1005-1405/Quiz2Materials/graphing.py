def adj_matrix():
    return [
        [0, 1, 0],
        [1, 0, 1],
        [0, 0, 1]
    ]

def adj_list():
    return [
        [1, 2],
        [],
        [0]
    ]

# MATRIX FUNCTIONS
matrix = adj_matrix()

def m_is_connected(a, b):
    return (matrix[a][b] == 1)

def m_connect(a, b):
    if (matrix[a][b] == 0): # Check if NOT connected
        matrix[a][b] = 1    # Connect
    
def m_disconnect(a, b):
    if (matrix[a][b] == 1): # Check if connected
        matrix[a][b] = 0    # Disconnect

def m_check_bidirection(a, b):
    return (matrix[a][b] == 1 and matrix[b][a] == 1)
        
# TIP : matrix[a][b] means "node a is connected to node b"

# LIST FUNCTIONS
a_list = adj_list()

def l_is_connected(a, b):
    return (b in a_list[a])

def l_connect(a, b):
    if (not (b in a_list[a])):
        a_list[a].append(b)
    
def l_disconnect(a, b):
     if (b in a_list[a]):
        a_list[a].remove(b)

def l_check_bidirection(a, b):
    return (b in a_list[a] and a in a_list[b])
        
    
