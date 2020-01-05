from checkio import api
from checkio.signals import ON_CONNECT
from checkio.referees.io import CheckiOReferee

from tests import TESTS


# The interest here is that undecorated checker is the same
# that the one in python initial code.
def manage_asserts(func):
    def wrapper(*args):
        try:
            func(*args)
        except AssertionError as error:
            return False, error.args[0]
        return True, 'Great!'
    return wrapper


@manage_asserts
def checker(grid, result):
    try:
        result = list(result)
    except TypeError:
        raise AssertionError('You must return an iterable/list/tuple.')
    assert all(isinstance(row, str) for row in result), \
        'Must return an iterable of strings.'
    nb_rows, nb_cols = len(grid), len(grid[0])
    assert len(result) == nb_rows and \
        all(len(row) == nb_cols for row in result), 'Wrong size.'
    forbidden_chars = ''.join(set.union(*map(set, result)) - set('WB.'))
    assert not forbidden_chars, \
        f'Only the chars "WB." are allowed, not {forbidden_chars!r}.'
    forbidden_changes = [(y, x) for y, (r1, r2) in enumerate(zip(grid, result))
                         for x, (c1, c2) in enumerate(zip(r1, r2)) if c1 != '.' and c1 != c2]
    assert not forbidden_changes, \
        [f'You changed {len(forbidden_changes)} cells given at the start.',
         'cell', forbidden_changes]

    miss = sum(row.count('.') for row in result)
    # if miss:
    #     print('You can look what is missing here:')
    #     print('https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/'
    #           f'unruly.html#{grid2spec(result)}')
    #     print('You just need to open a new webpage with that url.')
    assert not miss, [f'{miss} cells are still empty.',
                      'empty', []]
    columns = map(''.join, zip(*result))
    for _type, lines in (('row', result), ('column', columns)):
        for n, line in enumerate(lines):
            Ws, Bs = map(line.count, 'WB')
            assert Ws == Bs, [f'{Ws} W & {Bs} B in {_type} {n} {line!r}.',
                              _type, n]
            for item in 'WB':
                assert item * 3 not in line, \
                    [f'{item * 3} found in {_type} {n} {line!r}.',
                     _type, n]


cover_tuple = '''
def cover(func, grid):
    return func(tuple(grid))
'''

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        checker=checker,
        function_name={
            'python': 'unruly',
            # 'js': 'unruly',
        },
        cover_code={
            'python-3': cover_tuple,
            # 'js-node':
        },
    ).on_ready,
)
