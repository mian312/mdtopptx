from setuptools import setup, find_packages

def read_requirements():
    try:
        with open('requirements.txt', 'r', encoding='utf-8-sig') as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")
        return []
    
with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='mdtopptx',
    version='0.0.3',
    packages=find_packages(),
    install_requires=read_requirements(),
    description='Converts markdown files to PowerPoint presentations',
    long_description=description,
    long_description_content_type = 'text/markdown',
)