from setuptools import setup, find_packages


def setup_package():
    setup(
        name='IntellectFinanceAPI',
        packages=find_packages(exclude=('test',)),
        description='An open-sourced Python package to access the intellect.finance API (https://www.intellect.finance/API_Document).',
        author='intellect.finance',
        author_email='customer-obsession@intellect.finance',
        scripts=[],
        zip_safe=False,
        include_package_data=True
    )


if __name__ == "__main__":
    setup_package()
