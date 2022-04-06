import os
inputs = [
    ['test_0', 'example0.csv', 'ECV', 'WIW', '0', True],
    # ['test_1', 'example1.csv', 'NIZ', 'DHE', ''],
    # ['test_2', 'example2.csv', 'YOT', 'IUT', ''],
    # ['test_3', 'example3.csv', 'EZO', 'JBN', ''],


    # ['test_missing_entry_1', '', 'NIZ', 'DHE', ''],
    # ['test_missing_entry_2', 'example2.csv', '', 'IUT', ''],
    # ['test_missing_entry_3', 'example3.csv', 'EZO', '', ''],

    # ['test_incorrect_entry_1', 'example2', 'NIZ', 'DHE', ''],
    # ['test_incorrect_entry_2', 'example2.csv', 'NIZNIZ', 'IUT', ''],
    # ['test_incorrect_entry_3', 'example3.csv', 'EZO', 'asfb', ''],

]

for input in inputs:
    print()
    print('test_case: ', input[0])
    print('--------------------------------------------------')
    command = f"python -m solution {input[1]} {input[2]} {input[3]}" 
    print(command)
    os.system(command)
