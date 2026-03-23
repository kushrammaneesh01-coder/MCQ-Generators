from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Maneesh Kushram',
    author_email='kushrammaneesh01@gmail.com',
    install_requires=["openai","langchain","langchain-openai","langchain-community","streamlit","python-dotenv","PyPDF2"],
    package_dir={"mcqgenrator": "src/mcqgenerator"},
    packages=["mcqgenrator"],
)