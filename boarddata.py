class BoardData:
    '''
    default_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    '''

    easy_board = [
        [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0], 
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3], 
        [4, 0, 0, 8, 0, 3, 0, 0, 1], 
        [7, 0, 0, 0, 2, 0, 0, 0, 6], 
        [0, 6, 0, 0, 0, 0, 2, 8, 0], 
        [0, 0, 0, 4, 1, 9, 0, 0, 5], 
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ], 
        [
        [0, 5, 7, 9, 4, 0, 8, 0, 0],
        [2, 0, 4, 0, 0, 0, 1, 9, 6],
        [3, 9, 0, 1, 0, 0, 0, 0, 5],
        [0, 3, 1, 0, 0, 0, 2, 0, 0],
        [6, 0, 2, 3, 5, 0, 9, 8, 0],
        [5, 0, 0, 2, 0, 7, 0, 0, 0],
        [0, 0, 5, 6, 0, 2, 0, 0, 8],
        [7, 6, 0, 0, 1, 5, 0, 0, 9],
        [0, 0, 8, 7, 3, 0, 0, 0, 0]
        ], 
        [
        [0, 2, 0, 0, 0, 0, 0, 3, 1],
        [7, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 1, 4, 0, 2, 9, 0],
        [0, 5, 2, 7, 6, 4, 0, 1, 8],
        [0, 6, 3, 0, 1, 2, 7, 5, 9],
        [0, 7, 8, 0, 0, 0, 4, 0, 0],
        [2, 0, 0, 3, 7, 0, 0, 0, 5],
        [0, 1, 0, 0, 0, 0, 9, 0, 0],
        [5, 4, 0, 0, 8, 1, 0, 0, 0]
        ]
    ]

    medium_board = [
        [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 2, 1, 0, 0, 4, 0],
        [1, 0, 0, 7, 0, 0, 0, 8, 9],
        [0, 4, 5, 9, 0, 0, 0, 1, 7],
        [7, 2, 6, 0, 0, 0, 3, 0, 4],
        [0, 0, 1, 4, 7, 0, 2, 0, 0],
        [0, 1, 3, 0, 6, 8, 0, 0, 0],
        [6, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 7, 0, 0, 0]
        ], 
        [
        [0, 0, 0, 0, 1, 3, 0, 6, 8],
        [0, 0, 9, 6, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 5, 4, 0, 0, 7],
        [1, 0, 0, 0, 4, 0, 0, 0, 6],
        [0, 0, 0, 0, 2, 6, 0, 5, 0],
        [0, 5, 2, 0, 0, 0, 0, 7, 0],
        [2, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 9, 5, 1, 6, 0, 0, 3, 0],
        [4, 0, 7, 0, 0, 0, 2, 1, 0]
        ]
    ]


    hard_board = [
        [
        [0, 3, 4, 5, 0, 6, 9, 0, 0],
        [0, 0, 5, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 1, 0],
        [0, 0, 0, 8, 2, 3, 0, 0, 7],
        [1, 0, 8, 7, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 7, 2],
        [4, 0, 9, 0, 0, 0, 0, 0, 0]
        ], 
        [
        [0, 6, 0, 0, 1, 0, 5, 0, 0],
        [1, 0, 0, 0, 0, 5, 0, 7, 0],
        [0, 9, 8, 0, 0, 4, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 3, 0, 9, 1],
        [9, 0, 0, 3, 0, 2, 0, 0, 0],
        [0, 0, 7, 5, 0, 8, 0, 0, 3],
        [0, 0, 0, 1, 0, 0, 2, 0, 4]
        ]
    ]

    expert_board = [
        [
        [0, 4, 6, 0, 0, 7, 8, 0, 0],
        [0, 0, 8, 9, 0, 0, 7, 0, 0],
        [5, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 2, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 5, 0, 0, 1, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 1, 5, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 8, 0, 6, 0]
        ], 
        [
        [7, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 5, 0, 2, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [5, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 8, 6, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 0, 0, 0, 9, 0, 2, 0, 0],
        [4, 0, 3, 0, 0, 5, 0, 0, 1]
        ]
    ]


    evil_board = [
        [
        [0, 0, 7, 0, 0, 0, 0, 0, 3], 
        [0, 0, 9, 0, 6, 0, 0, 0, 0], 
        [3, 6, 0, 0, 0, 8, 2, 0, 0], 
        [0, 0, 6, 0, 0, 0, 0, 0, 0], 
        [5, 1, 0, 0, 8, 0, 0, 0, 9], 
        [0, 0, 0, 0, 0, 2, 0, 4, 0], 
        [0, 0, 0, 5, 0, 0, 9, 0, 0], 
        [8, 3, 0, 0, 1, 0, 0, 0, 5], 
        [7, 0, 0, 0, 0, 0, 0, 0, 0]
        ], 
        [
        [1, 0, 3, 0, 0, 4, 0, 0, 7],
        [0, 0, 0, 9, 0, 0, 0, 6, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [5, 0, 7, 0, 0, 3, 0, 0, 1],
        [0, 0, 0, 0, 4, 0, 3, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 8],
        [8, 0, 5, 0, 6, 0, 0, 7, 0],
        [0, 2, 0, 0, 0, 5, 0, 0, 0]
        ], 
    ]

    boards = list([easy_board, medium_board, hard_board, expert_board, evil_board])
