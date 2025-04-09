from setuptools import setup, find_packages

setup(
    name="autoq",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["qiskit==0.43.0"],
    author="xAI Team",
    author_email="support@xai.com",
    description="AutoQ Framework: Automated quantum circuit optimization",
    long_description="The AutoQ Framework is a tool for automated quantum circuit optimization, designed to increase processing speed (gates per µs). It integrates transpilation, parallelism, and QEC into a unified pipeline.",
    long_description_content_type="text/plain",
    url="https://github.com/Ronaldoengenhariadacomputacao/autoq-framework.git",
    license="MIT"
)
