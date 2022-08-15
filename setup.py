# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='youtube_dl_server',
    version='0.5',
    description='An API server based on yt-dlp',
    long_description='Get the videos from different sites using a server running yt-dlp',
    author='zasdevs',
    author_email='zasdevs@gmail.com',
    url='https://github.com/zasdevs/yt-dlp-api-server.git',
    packages=['youtube_dl_server'],
    entry_points={
        'console_scripts': [
            'youtube-dl-server = youtube_dl_server.server:main',
        ],
    },

    install_requires=[
        'Flask',
        'yt-dlp >= 2022.08.14',
    ],

    classifiers=[
        'Topic :: Multimedia :: Video',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
