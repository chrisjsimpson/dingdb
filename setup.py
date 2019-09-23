import setuptools

setuptools.setup(
    name='dingdb',
    version="0.0.1",
    author="Chris Simpson",
    author_email="chris@karmacomputing.co.uk",
    desciption="Dingdb is a Python api for thingdb like storage and retrieval",
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=[('dingdb/migrations', ['dingdb/migrations/1-create-dingdb-schema.py'])],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ),
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
    ''',
)
