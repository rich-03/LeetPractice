class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direc_U = moves.count('U')
        direc_D = moves.count('D')
        direc_L = moves.count('L')
        direc_R = moves.count('R')
        if direc_U == direc_D and direc_L == direc_R:
            return True

        return False
