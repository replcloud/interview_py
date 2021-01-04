def solution(S, K):
    # write your code in Python 3.6
    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    pos = DAYS.index(S)
    new_pos = (pos + K) % 7
    return DAYS[new_pos]


def solution2(N):
    negative = True if N < 0 else False
    str_N = str(N)
    if negative:
        for i in range(1, len(str_N)):
            if int(str_N[i]) > 5:
                if i == 1:
                    return -(5 * pow(10, len(str_N) - i) + int(str_N[i:]))
                else:
                    return -(int(str_N[1:i])) * pow(10, len(str_N) - i + 1) - 5 * pow(10, len(str_N) - i) - int(str_N[i:])
        return N * 10 - 5
    else:  # positive
        for i in range(len(str_N)):
            if int(str_N[i]) < 5:
                if i == 0:
                    return 5 * pow(10, len(str_N) - i) + int(str_N[i:])
                else:
                    return int(str_N[:i]) * int(pow(10, len(str_N) - i + 1)) + 5 * int(pow(10, len(str_N) - i) + int(str_N[i:]))

        return N * 10 + 5


if __name__ == '__main__':
    print(solution2(-268))
"""
# Enum for Color

# I will use observer pattern. 
# Class Tic-tac-toe
# has 2 Players which are givein at the initializaion. 
# During initialization, 1 players plays first.
# contains 2D arrays to represent game board
# Private method to determine the winner. Count the straight line and give the Color.
# play method which notify the player it's their turn 
# contains 2D arrays to represent game board, denoted by Color

# Class Player 
# contains members such as name
# Play method to choose the position (x, y)

# Queue of Players
# Use a queue and use random number to enter player in pairs. The first Player of Color 1 and the second Player of Color 2
# if the quque is empty add more players 

# Leader board
# Track winner

# high level implementation here

Enum Colr {} // Color Enum

Class LeaderBoard {}

Class Player {
    public void Player(String name);
    Position getPosition();
}

Class TicTacToe {
    Color[][] = board; //Initialize
    Player first, second;
    Player next;
    public void TicTacToe(Player p1, Player p2) {
        next = first;
    }

    private boolean hasWinner() {
        # Handle tie no winner situtation
    }

    private terminate() {
        # when there is a winner to not possible to continue to play
    }

    private updateLeaderBoard(LeaderBoard b) {} // Lead the implementation to be decided by LeaderBoard class. One way of decoupling if future design changes. 

    private Player winner() {} // return winner

    private play() {
        // Set timeout
        while wait {
            next.getPosition();
            next = (next == first) ? second : first;
        }
    }
}
"""