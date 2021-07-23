"""Maze solver algorithm test script

This script allows the user to load an maze from text, execute the maze solver and
visualize the maze and solution path using tkinter
"""
from tkinter import Tk
import argparse
import threading
import os
import sys
import timeit

import SusannaAStarAlgo
import Teams.ReferenceSolutionAStarCPP.build.astar as astarcpp
import Teams.ReferenceSolutionAStar.MazeSolverAlgoAStar
import Teams.ReferenceSolutionBreadthFirst.MazeSolverAlgoBreadthFirst
import Framework.Visualizer.maze_visualize


sys.path.append("../..")


def on_closing():
    """ Callback function if Visualizer Window is closed
    """
    os._exit(0)


apptk = Tk()
apptk.protocol("WM_DELETE_WINDOW", on_closing)
apptk.title("MazeRunner")
apptk.geometry("700x700")
apptk.resizable(True, True)

alg = SusannaAStarAlgo.SusannaAStarAlgo()
alg3 = Teams.ReferenceSolutionBreadthFirst.MazeSolverAlgoBreadthFirst.MazeSolverAlgoBreadthFirst()
alg4 = Teams.ReferenceSolutionAStar.MazeSolverAlgoAStar.MazeSolverAlgoAStar()
alg2 = astarcpp.AStar("Test")

vis = Framework.Visualizer.maze_visualize.MazeVisualizer(apptk)


def main():
    """[summary]
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="The maze as text file"
    )
    args = parser.parse_args()

    if not alg2.loadMaze(args.input_file):
        exit(1)

    if not alg.loadMaze(args.input_file):
        exit(1)
    vis.prepareVisualization(alg.dimRows, alg.dimCols,
                             alg.startRow, alg.startCol, alg.endRow, alg.endCol)

    for row in range(alg.dimRows):
        for col in range(alg.dimCols):
            if alg.grid[row][col] == alg.OBSTACLE:
                vis.setBlocked(row, col)

    vis.endMaze()

    t = threading.Thread(target=mainloop)
    t.start()
    apptk.mainloop()


def mainloop():
    """[summary]
    """
    starttime = timeit.default_timer()
    alg.solveMaze()
    print("The time difference is :", timeit.default_timer() - starttime)

    starttime = timeit.default_timer()
    alg2.solveMaze()
    print("The time difference is :", timeit.default_timer() - starttime)

    for move in alg2.came_from:
        if isinstance(move) == str:
            a_list = move.split(',')
            map_object = map(int, a_list)
            move = list(map_object)
        vis.addSolutionStep(move[0], move[1])
    vis.plot_route()

    for move in alg.getResultPath():
        vis.addSolutionStepFin(move[0], move[1])

    print(
        f'Steps necessary {len(alg.came_from)} - Optimal path needs:{len(alg.getResultPath())}')


if __name__ == "__main__":
    main()
