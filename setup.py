from setuptools import setup

package_name = 'pikabot'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
# data_files.append(('share/' + package_name + '/worlds', ['worlds/my_world.wbt']))
data_files.append(('share/' + package_name + '/worlds/PIKABOT/worlds', ['worlds/PIKABOT/worlds/pikabot.wbt']))
data_files.append(('share/' + package_name + '/worlds/PIKABOT/models', ['worlds/PIKABOT/models/pika.mtl.obj']))
data_files.append(('share/' + package_name + '/worlds/PIKABOT/models', ['worlds/PIKABOT/models/pika.mtl.mtl']))
data_files.append(('share/' + package_name + '/worlds/PIKABOT/models', ['worlds/PIKABOT/models/hover_board_wheel.obj']))
data_files.append(('share/' + package_name + '/worlds/PIKABOT/models', ['worlds/PIKABOT/models/hover_board_wheel.mtl']))
data_files.append(('share/' + package_name + '/resource', ['resource/pikabot.urdf']))
data_files.append(('share/' + package_name + '/resource', ['resource/ros2control.yml']))
data_files.append(('share/' + package_name + '/resource', ['resource/pikabot.rviz']))
data_files.append(('share/' + package_name + '/resource', ['resource/pikabot_model.xacro']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rjrobotics2',
    maintainer_email='rjrobotics2@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_robot_driver = pikabot.my_robot_driver:main'
        ],
    },
)
