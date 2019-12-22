import unittest
import pytest
import os,sys,inspect
import logging
import tempfile
from shutil import copyfile, rmtree, copy, copytree, move
import numpy 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from MazeSolverAlgoAStar import MazeSolverAlgoAStar

# Line Coverage
# branch Coverage
# Condition covera
# Boundarycheck

class LoadMazeTest(unittest.TestCase):
    def testLoadMaze(self):
        example_load=os.path.join(parentdir,"..","..","MazeExamples","maze1.txt")
        astar = MazeSolverAlgoAStar()
        astar.loadMaze(example_load)
        result = numpy.array([[0,0,0,0,2],[0,1,1,1,1],[0,1,0,1,3],[0,1,0,0,0],[0,0,0,1,0]])
        #self.assertTrue(astar.grid == result)
        numpy.testing.assert_array_equal(astar.grid, result)

if __name__ == '__main__':
    unittest.main()