from setuptools import setup, find_packages

setup(
    name='database_client',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python>=8.0',
        'python-dotenv>=1.0'
    ],
    author='Vinicius Costa',
    description='Cliente simples para conectar e executar queries em MySQL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
