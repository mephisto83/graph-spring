from GraphSpring import Vector, Point, Spring, Edge, Data, Node, Graph


def test_Vector():
    v = Vector(1, 1)
    if v.x != 1:
        raise Exception("vector initialized incorrectly")
    return True

def test_Vector_random():
    v = Vector.random()
    if not v:
        raise Exception("no vector created")
    return True

def test_Vector_Add():
    v = Vector(1, 1)
    v2 = Vector(2, 2)
    v3 = v2.add(v)
    if v3.x != 3 or v3.y != 3:
        raise Exception("vector value added incorrectly")


def test_Vector_Subtract():
    v = Vector(1, 1)
    v2 = Vector(2, 2)
    v3 = v2.subtract(v)
    if v3.x != 1 or v3.y != 1:
        raise Exception("vector value subtracted incorrectly")

        
def test_Vector_Divide():
    v2 = Vector(1, 1)
    v3 = v2.divide(1)
    if v3.x != 1 or v3.y != 1:
        raise Exception("vector value divided incorrectly")

def test_Vector_Magnitude():
    v2 = Vector(4, 0)
    v3 = v2.magnitude()
    if v3 != 4:
        raise Exception("vector value magnitude incorrectly")

def test_Point_create():
    p = Point(Vector(0,0), 10)
    if not p:
        raise Exception ("point not created")

def test_Point_applyForce():
    p = Point(Vector(0,0), 1)
    p.applyForce(Vector(1,1))
    if not p.a:
        raise Exception("applying force to point failed")

def test_Spring_create():
    spring = Spring(Point(Vector(0,0), 1), Point(Vector(1,1), 1), 10, 1)
    if not spring:
        raise Exception("failed to create spring")

def test_Data_create():
    data = Data(label="label")
    if not data or data.label != "label":
        raise Exception("Data did not create correctly")

def test_Edge_create():
    edge = Edge("id", "source", "target", Data(label="asdf"))
    if not edge:
        raise Exception("Edge was not created")

def test_Node_create():
    node = Node("id", Data(label="asdf"))
    if not node:
        raise Exception("Node was not created")

def test_Graph_create():
    graph = Graph()
    if not graph:
        raise Exception("Graph was not created")

def test_Graph_addGraphListener():
    graph = Graph()
    graph.addGraphListener({})
    if len(graph.eventListeners) != 1:
        raise Exception("missing event listener")
    print("added listener")

def test_Graph_addNode():
    graph = Graph()
    graph.addNode(Node("id", Data(label="asdf")))
    if len(graph.nodes) != 1:
        raise Exception("wrong number of nodes in graph")
    if not graph.nodeSet["id"]:
        raise Exception("node set doesnt have expected node")

tests = [
    test_Vector,
    test_Vector_random,
    test_Vector_Add,
    test_Vector_Subtract,
    test_Graph_addGraphListener,
    test_Vector_Magnitude,
    test_Vector_Divide,
    test_Point_create,
    test_Point_applyForce,
    test_Spring_create,
    test_Edge_create,
    test_Node_create,
    test_Graph_addNode,
    test_Data_create,
    test_Graph_create
]



failed = 0
success = 0
for test in tests:
    try:
        test()
        success = success + 1
    except Exception as e:
        failed = failed + 1
        print(e)

print("Success " + str(success) + ", failed : " + str(failed))