"""
Advent of Code Day One Challege One
"""

import pandas as pd

from pathlib import Path

_INPUT_FILE_LOCATION = Path(r"H:\advent_of_code_inputs\DayOne\ChallengeOne.txt")

def main():
    raw_data = pd.read_csv(_INPUT_FILE_LOCATION, 
                           header=None,
                           names=['frequency']
                           )
    total_frequency = sum(raw_data['frequency'])
    print(total_frequency)

    return 0

if __name__ == '__main__':
    RETURN_CODE = main()
    
    print('Return Code: {}'.format(RETURN_CODE))
