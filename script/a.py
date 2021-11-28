match 1:
    case 'Actor':
        print('Actor')
    case int():
        print('int')
    case str():
        print('str')
    case unexpected:
        raise TypeError(f'unexpected type: {unexpected}')
