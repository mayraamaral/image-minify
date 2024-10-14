from setuptools import setup, find_packages

setup(
    name='image_optimizer',
    version='0.1',
    description='A simple image compression and resizing library',
    author='Mayra Amaral',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'image-optimizer=optimizer:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
