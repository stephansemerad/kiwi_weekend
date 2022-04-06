import os
commands = [
    ['test_0', 'example0.csv', '', '', ''],
    ['test_1', 'example1.csv', '', '', ''],
    ['test_2', 'example2.csv', '', '', ''],
    ['test_3', 'example3.csv', '', '', ''],
    ['test_4', 'example0.csv', '', '', ''],
    ['test_5', 'example1.csv', '', '', ''],
    ['test_6', 'example2.csv', '', '', ''],
    ['test_7', 'example3.csv', '', '', ''],
    ['test_8', 'example0.csv', '', '', ''],
]

for command in commands:
    commans = f'python -m solution --file --from --to'
    print(command)
    os.system(command)
