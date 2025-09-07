try:
    with open('Assignment_4/sample.txt') as f: ## By default it's take 'r' mode.
        print(f'Reading file content: ')
        print(f'Line: {f.readline()}')
        print(f'Line: {f.readline()}')
except FileNotFoundError:
    print('Error: Thr \'sample.txt\' was not found.')

