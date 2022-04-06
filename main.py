from queen import NQueens


def main():
    print('N-Queens Problem :')
    size = int(input('Please enter the size of board: '))
    print_solutions = input(
        'Do you want the solutions to be printed (Y/N): ').lower() == 'y'
    n_queens = NQueens(size)
    dfs_solutions = n_queens.solve_dfs()
    if print_solutions:
        for i, solution in enumerate(dfs_solutions):
            print('DFS Solution %d:' % (i + 1))
            n_queens.print(solution)
    print('Total BFS solutions: %d' % len(dfs_solutions))


if __name__ == '__main__':
    main()
