#!/usr/bin/python3
"""
    Last question
"""
from sys import argv, exit


class Solution:
    """
        Creates class called solutions
    """

    def solve(self, n):
        """
            Args:
                n: size of chess board
            Return:
                list of positions
        """
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        """
           
            Args:
                state: positions of the queen
            Returns
                True if a valid solution
        """
        return len(state) == n

    def get_candidates(self, state, n):
        """
            Finds the position the queen can occupy
            Args:
                state: current position of the queen
                n: size of the chessboard
            Returns:
                the indexes of the position the queen can occupy
        """
        if not state:  
            return range(n)

        position = len(state)
        candidates = set(range(n))

        for row, col in enumerate(state):
            candidates.discard(col)
            distance = position - row 
            candidates.discard(col + distance)  # diagonal right
            candidates.discard(col - distance)  # diagonal left
        return candidates

    def search(self, state, solutions, n):
        """
            See if queen can stay at current postion without being attached
	    by another queen,
            Args:
                state: position of queen 
                solutions: 2D list containing positions queen can stay
                n: size of chessboard
        """

        if self.is_valid_state(state, n):
            state_list = self.state_to_list(state)
            solutions.append(state_list)
            return

        for candidate in self.get_candidates(state, n):
            
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()  

    def state_to_list(self, state):
        """
            changes state indexes to coordinate list
            Args:
                state: position queen occupies
         
        """
        res = []
        for row, col in enumerate(state):
            coordinate = []
            coordinate.append(row)
            coordinate.append(col)
            res.append(coordinate)
        return res


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solution = Solution()
    list_of_sol = solution.solve(N)

    for res in list_of_sol:
        print(res)
