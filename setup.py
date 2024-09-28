from setuptools import setup, find_packages

setup(
    name='resize-image',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'resize-image=resize_image.cli:cli',
        ],
    },
    author='ShinChven',
    author_email='shinchven@gmail.com',
    description='A CLI tool to resize images while maintaining aspect ratio.',
    keywords='image resize CLI',
)
