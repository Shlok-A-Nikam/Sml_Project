from setuptools import setup, find_packages



def read_requirements(path: str = 'requirements.txt'):
    requirements = []
    with open (path, 'r', encoding='utf-8') as f:
        for line in f:
            line= line.strip()
            if not line or line.startswith("#"):
                continue
            if line == '-e .':
                continue
            requirements.append(line)
    return requirements

setup(
    name = "v1-app",
    version="0.0.1",
    packages=find_packages(),
    install_requires=read_requirements(),
    description='A sample pyhton aplication',
    author="Shlok Nikam",
    author_email='shlokanikam@gmail.com',
    url='https://github.com/Shlok-A-Nikam/Sml_Project/tree/main')