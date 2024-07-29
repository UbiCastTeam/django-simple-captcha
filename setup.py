from setuptools import find_packages, setup

from captcha import get_version as get_captcha_version


install_requires = [
    "Django >= 4.2",
    "Pillow >=6.2.0",
    "django-ranged-response == 0.2.0",
]
EXTRAS_REQUIRE = {"test": ("testfixtures",)}


with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name="django-simple-captcha",
    version=get_captcha_version(),
    description="A very simple, yet powerful, Django captcha application",
    long_description=long_description,
    author="Marco Bonetti",
    author_email="mbonetti@gmail.com",
    url="https://github.com/mbi/django-simple-captcha",
    license="MIT",
    packages=find_packages(exclude=["testproject", "testproject.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Framework :: Django",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require=EXTRAS_REQUIRE,
    tests_require=["tox>=4.31", "tox-uv>=1.23"],
)
