from setuptools import setup
import glob

execfile('concrete/version.py')

if __name__ == '__main__':
    setup(
        name="concrete",
        version=__version__,
        description="Python modules and scripts for working with Concrete",

        packages=[
            'concrete',

            # Python code generated by Thrift Compiler
            'concrete.access',
            'concrete.annotate',
            'concrete.audio',
            'concrete.clustering',
            'concrete.communication',
            'concrete.email',
            'concrete.entities',
            'concrete.exceptions',
            'concrete.language',
            'concrete.learn',
            'concrete.linking',
            'concrete.metadata',
            'concrete.nitf',
            'concrete.search',
            'concrete.services',
            'concrete.services.results',
            'concrete.situations',
            'concrete.spans',
            'concrete.structure',
            'concrete.twitter',
            'concrete.uuid',

            # Python code generated by people
            'concrete.util',
        ],

        scripts=glob.glob('scripts/*')
                  + glob.glob('concrete/services/*-remote'),

        setup_requires=['pytest-runner'],
        tests_require=['pytest', 'pytest-mock', 'pytest-cov', 'flake8'],

        install_requires=[
            'networkx',
            'testfixtures',
            'thrift>=1.0.0.dev0',
            'redis>=2.10.0',
            'pycountry==1.20',
            'requests',
        ],

        url="https://github.com/hltcoe/concrete-python",
        license="BSD",
    )
