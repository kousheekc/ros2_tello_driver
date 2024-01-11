from setuptools import find_packages, setup

package_name = 'tello_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kousheek',
    maintainer_email='kousheekc@gmail.com',
    description='ROS2 driver package to control dji tello drone',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tello_driver = tello_driver.tello_driver_node:main'
        ],
    },
)
