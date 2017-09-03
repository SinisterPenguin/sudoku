from setuptools import setup

setup(name='sudoku',
      version='0.1',
      description='Generic SuDoku Solver',
      url='http://github.com/SinisterPenguin/sudoku',
      author='Ben Haytack',
      author_email='benhaytack@gmail.com',
      packages=['sudoku'],
      entry_points={
          'console_scripts': ['sd-display = sudoku.console:display_grid'],
      },
      zip_safe=False)