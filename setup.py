import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="html-to-docx",
    version="0.1.3",
    author="Example Author",
    author_email="author@example.com",
    description=(
        "A tool which allows to convert HTML parsed as a string "
        "into docx content."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fr0mhell/html_docx",
    packages=['html_to_docx', 'html_to_docx.tag_dispatchers', ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "lxml==4.4.1",
        "python-docx==0.8.7",
    ],
)
