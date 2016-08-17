from setuptools import setup, find_packages

setup(
    name='nros-youpi2',
    setup_requires=['setuptools_scm'],
    use_scm_version={
        'write_to': 'src/nros/youpi2/__version__.py'
    },
    namespace_packages=['nros'],
    packages=find_packages("src"),
    package_dir={'': 'src'},
    url='',
    license='',
    author='Eric Pascual',
    author_email='eric@pobot.org',
    install_requires=['nros-core', 'pybot-youpi2'],
    download_url='https://github.com/Pobot/PyBot',
    description='Youpi2 arm nROS node',
    entry_points={
        'console_scripts': [
            'start-youpi2-node = nros.youpi2.nodes:start_node'
        ]
    }
)
