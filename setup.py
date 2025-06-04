from setuptools import setup
from glob import glob
import os

package_name = 'turtlebot_explorer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Example Maintainer',
    maintainer_email='user@example.com',
    description='Simple TurtleBot exploration package.',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'explorer = turtlebot_explorer.explorer_node:main',
        ],
    },
)
