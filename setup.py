from setuptools import setup

package_name = 'ros2caret'

setup(
    name=package_name,
    version='0.2.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['ros2cli'],
    zip_safe=True,
    maintainer='hsgwa',
    maintainer_email='hasegawa@isp.co.jp',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'ros2cli.command': [
            'caret = ros2caret.command.caret:CaretCommand',
        ],
        'ros2cli.extension_point': [
            'ros2caret.verb = ros2caret.verb:VerbExtension'
        ],
        'ros2caret.verb': [
            'check_caret_rclcpp = \
                    ros2caret.verb.check_caret_rclcpp:CheckCaretRclcppVerb',
            'check_ctf = ros2caret.verb.check_ctf:CheckCTFVerb',
            'trace_point_summary = \
                    ros2caret.verb.trace_point_summary:TracePointSummaryVerb',
            'topic_summary = ros2caret.verb.topic_summary:TopicSummaryVerb',
            'node_summary = ros2caret.verb.node_summary:NodeSummaryVerb',
            'create_architecture_file = \
                    ros2caret.verb.create_architecture:CreateArchitectureVerb',
            'verify_paths = \
                    ros2caret.verb.verify_paths:VerifyPathsVerb',
            'record = \
                    ros2caret.verb.record:RecordVerb',
            # 'callback_graph = \
            #       ros2caret.verb.callback_graph:CallbackGraphVerb',
            # 'chain_latency = ros2caret.verb.chain_latency:ChainLatencyVerb',
            # 'message_flow = ros2caret.verb.message_flow:MessageFlowVerb',
        ]
    },
)
