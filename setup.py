from setuptools import setup

setup(
    name='Coinex_api_client',
    version='0.7',
    description='An easy API client for the Coinex trading platform',
    url='https://github.com/Dan-Ilie/Coinex_api_client',
    author='Daniel Ilie',
    author_email='daniel.ilie.gl@gmail.com',
    license='LGPL',
    packages=['Coinex_api_client'],
    package_data={'Coinex_api_client': ['API/*.py',
                                        'API/AccountAPI/*.py',
                                        'API/CommonAPI/*.py',
                                        'API/ContractAPI/*.py',
                                        'API/MarginAPI/*.py',
                                        'API/MarketAPI/*.py',
                                        'API/TradingAPI/*.py',
                                        'tools/*.py']},
    install_requires=['requests>=2.0'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
    ],
)
