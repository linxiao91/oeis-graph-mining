from Digraph import *
from BFS import *
from OEIS import *
import sys

if __name__ == '__main__':
    oeis = OEIS(sys.argv[1], sys.argv[2])
    graph = oeis.graph
    vertices = [127892 - 1, 181085 - 1]
    bfs = BFS(graph, vertices[0])
    path = bfs.pathTo(vertices[1])
    print "longest path", [ele + 1 for ele in path]
    bfsSeq = BFS(graph, path)
    while True:
        sink = int(raw_input()) - 1
        if bfsSeq.hasPathTo(sink):
            for v in bfs.pathTo(sink):
                print "%d %s" % (v + 1, oeis.getTitle(v))
        else:
            print "Not connected"
