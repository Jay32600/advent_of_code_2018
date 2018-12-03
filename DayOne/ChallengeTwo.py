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
    
    values = []
    current_value = 0
    first_repeat = None
    
    while first_repeat == None:
        for index, row in raw_data.iterrows():
            current_value += row['frequency']
            if current_value in values:
                first_repeat = current_value
                break
            values.append(current_value)

    print(first_repeat)

    return 0

if __name__ == '__main__':
    RETURN_CODE = main()
    
    print('Return Code: {}'.format(RETURN_CODE))
