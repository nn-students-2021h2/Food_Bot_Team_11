from setuptools import setup

setup(
    name='pretty_time_package',
    version='0.1',
    description='allows you to get unixtime in pretty format',
    url='http://github.com/name/package_name',
    author='Alex',
    author_email='AlexVE36@yandex.ru',
    license='MIT',
    packages=['get_pretty_time_package'],
    entry_points={
        'console_scripts': [
            'get_time=get_pretty_time_package.pretty_time:main',
        ]
    }
)