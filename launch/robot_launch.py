import os
import pathlib
import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.utils import controller_url_prefix
from webots_ros2_driver.webots_controller import WebotsController
from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration
import xacro

def generate_launch_description():
    package_name = 'pikabot'
    package_dir = os.path.join(get_package_share_directory(package_name))
    robot_description = pathlib.Path(os.path.join(package_dir, 'resource', 'pikabot.urdf')).read_text()
    # model_path = os.path.join(package_dir, 'resource', 'pikabot_model.urdf')

    ros2_control_params = os.path.join(package_dir, 'resource', 'ros2control.yml')
    use_sim_time = LaunchConfiguration('use_sim_time', default=False)
    # use_rviz = LaunchConfiguration('rviz', default=False)

    xacro_file = os.path.join(package_dir,'resource','pikabot_model.xacro')
    robot_description_config = xacro.process_file(xacro_file)

    controller_manager_timeout = ['--controller-manager-timeout', '50']
    controller_manager_prefix = 'python.exe' if os.name == 'nt' else ''

    use_deprecated_spawner_py = 'ROS_DISTRO' in os.environ and os.environ['ROS_DISTRO'] == 'foxy'


    diffdrive_controller_spawner = Node(
        package='controller_manager',
        executable='spawner' if not use_deprecated_spawner_py else 'spawner.py',
        output='screen',
        prefix=controller_manager_prefix,
        arguments=['diffdrive_controller'] + controller_manager_timeout,
        # parameters=[{'use_sim_time': use_sim_time}]
    )

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner' if not use_deprecated_spawner_py else 'spawner.py',
        output='screen',
        prefix=controller_manager_prefix,
        arguments=['joint_state_broadcaster'] + controller_manager_timeout,
        # parameters=[{'use_sim_time': use_sim_time}]
    )

    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'PIKABOT', 'worlds', 'pikabot.wbt')
    )

    mappings = [('/diffdrive_controller/cmd_vel_unstamped', '/cmd_vel'), ('/diffdrive_controller/odom', '/odom')]
    
    
    # if 'ROS_DISTRO' in os.environ and os.environ['ROS_DISTRO'] in ['humble', 'rolling']:
    #     mappings.append(('/diffdrive_controller/odom', '/odom'))
    #     mappings.append(('/pikabot/LDS_01','/scan'))

    my_robot_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'pikabot'},
        parameters=[
            {'robot_description': robot_description,
             'use_sim_time': use_sim_time,
             'set_robot_state_publisher': False
            },
             ros2_control_params
        ],
        remappings=mappings
    )


    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        # parameters=[{
        #     'robot_description': '<robot name=""><link name=""/></robot>'
        # }]
        parameters=[params]
    )

    base_link_to_laser = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments = ['0', '0', '0.01', '0', '0', '0', 'base_link', "LDS-01"],
        parameters=[{'use_sim_time': use_sim_time}]
        
    )

    footprint_publisher = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'],
    )

    rviz_config = os.path.join(get_package_share_directory(package_name), 'resource', 'pikabot.rviz')
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['--display-config=' + rviz_config],
        parameters=[{'use_sim_time': use_sim_time}]
    )
    return LaunchDescription([
        webots,
        base_link_to_laser,
        footprint_publisher,
        rviz,
        robot_state_publisher,
        joint_state_broadcaster_spawner,
        diffdrive_controller_spawner,
        my_robot_driver,
        # footprint_publisher,
        
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])