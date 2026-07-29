from setuptools import setup

package_name = 'arm_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thejaskm',
    maintainer_email='thejaskm@todo.todo',
    description='Arm control package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_control = arm_control.joint_control:main',
        ],
    },
)
