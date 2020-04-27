import unittest

import random

from graphs import DiGraph

class TestGraph(unittest.TestCase):
    def test_init(self):
        g = DiGraph()
        
        self.assertIsInstance(g._edges, dict)
        
    def test_add_vertex(self):
        g = DiGraph()
        
        g.add_vertex("a")
        
        self.assertIn("a", g._edges)
        self.assertIsInstance(g._edges["a"], set)
        self.assertTrue(g.vertex_exists("a"))
        self.assertEqual(g.count_vertices(), 1)
        self.assertEqual(g.count_edges(), 0)
        
        g.add_vertex("b")
        
        self.assertIn("b", g._edges)
        self.assertIsInstance(g._edges["b"], set)
        self.assertTrue(g.vertex_exists("b"))
        self.assertEqual(g.count_vertices(), 2)
        self.assertEqual(g.count_edges(), 0)
        
    def test_add_edge(self):
        g = DiGraph()
        
        g.add_edge("a", "b")
        
        self.assertIn("a", g._edges)
        self.assertIn("b", g._edges)
        self.assertIsInstance(g._edges["a"], set)
        self.assertIsInstance(g._edges["b"], set)
        self.assertIn("b", g._edges["a"])
        self.assertNotIn("a", g._edges["b"])
        self.assertTrue(g.vertex_exists("a"))
        self.assertTrue(g.vertex_exists("b"))
        self.assertTrue(g.edge_exists("a", "b"))
        self.assertFalse(g.edge_exists("b", "a"))
        self.assertEqual(g.count_vertices(), 2)
        self.assertEqual(g.count_edges(), 1)
        
        # check that re-adding a vertex
        # doesn't erase edge information
        g.add_vertex("a")
        self.assertIn("b", g._edges["a"])
        self.assertEqual(g.count_vertices(), 2)
        self.assertEqual(g.count_edges(), 1)
        
        # validate that edges are directed
        g.add_edge("b", "a")
        self.assertIn("a", g._edges["b"])
        self.assertEqual(g.count_vertices(), 2)
        self.assertEqual(g.count_edges(), 2)
        self.assertTrue(g.edge_exists("a", "b"))
        self.assertTrue(g.edge_exists("b", "a"))
        
        self.assertFalse(g.edge_exists("b", "c"))
        self.assertFalse(g.edge_exists("c", "d"))
        
        neighbors_a = g.get_outgoing_edges("a")
        self.assertSetEqual(neighbors_a, set(["b"]))
        
    def test_vertex_exsts(self):
        g = DiGraph()
        
        g.add_vertex("a")
        
        self.assertTrue(g.vertex_exists("a"))
        self.assertFalse(g.vertex_exists("none_existent"))


if __name__ == "__main__":
    unittest.main()
