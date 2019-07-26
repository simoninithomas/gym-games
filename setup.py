from setuptools import setup

setup(name='gym_games',
      version='0.0.2',
      description='This is a gym version of various games for reinforcenment learning.',
      install_requires=[
            'gym',
            'MinAtar',
            'pygame'
            ],
      author='qlan3',
      url='https://github.com/qlan3/gym-games',
      email='qlan3@ualberta.ca',
      keywords = ['AI', 'Reinforcement Learning', 'Games', 'Pygame', 'MinAtar']
)