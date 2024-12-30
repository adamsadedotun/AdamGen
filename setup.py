from setuptools import find_packages,setup

setup(
    name='AdamGen',
    version='0.0.1',
    author='Adedotun Adams',
    author_email='adamsadedotun95@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
