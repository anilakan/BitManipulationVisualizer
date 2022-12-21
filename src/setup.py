from setuptools import setup

setup(
    name="bit_visualize",
    version="0.0.2",
    description="bit visualizer",
    maintainer="Nish Nilakantan",
    maintainer_email="anilakan@andrew.cmu.edu",
    license="GPL",
    packages=["bit_visualize"],
    scripts=[
        "bit_visualize/visualizer.py",
        "bit_visualize/bit_ops.py",
        "bit_visualize/variables.py",
    ],
    setup_requires=[],
    data_files=["LICENSE"],
    include_package_data=False,
    install_requires=["importlib_resources"],
)
