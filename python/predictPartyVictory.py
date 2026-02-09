# https://leetcode.com/problems/dota2-senate/

from collections import deque
from typing import Deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Predict the winner of the Dota2 Senate game given the initial arrangement
        of senators. The game proceeds in rounds where each senator can ban one
        opposing senator for all future rounds. The process continues until a
        senator sees that the other party has no more senators left.

        Complexity:
        - Time: O(n) since a senator can only be banned once and processed twice
        - Space: O(n)
        """
        radq: Deque[int] = deque()
        dirq: Deque[int] = deque()
        n = len(senate)

        # Populate the queues
        for i, ch in enumerate(senate):
            if ch == "R":
                radq.append(i)
            else:
                dirq.append(i)

        # Now we play the actual game
        while radq and dirq:
            if radq[0] < dirq[0]:
                # Remove closest Dire member
                dirq.popleft()
                # Move current Radiant member to the back
                radq.append(radq.popleft() + n)
            else:
                # Remove closest Radiant member
                radq.popleft()
                # Move current Dire member to the back
                dirq.append(dirq.popleft() + n)

        return "Radiant" if radq else "Dire"
