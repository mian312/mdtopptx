from setuptools import setup, find_packages

def read_requirements():
    try:
        with open('requirements.txt', 'r', encoding='utf-8-sig') as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")
        return []

setup(
    name='mdtopptx',
    version='0.0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    long_description_content_type = 'text/x-rst'
)