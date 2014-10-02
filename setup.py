from setuptools import setup

setup(
    name='getout',
    version='0.1.0.dev1',
    author='Bin Wang', 
    author_email='binwang.cu@gmail.com',
    license='MIT',
    install_requires=['beautifulsoup4'],
    entry_points={
        'console_scripts':['getout=getout.command_line:main'],
    },
)
