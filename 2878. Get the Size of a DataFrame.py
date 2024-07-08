"""
447 ms runtime beats 0%
65.93 MB memory beats 0%
"""
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]