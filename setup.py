from setuptools import setup, find_packages

setup(
    name='cl_vx_config',
    version='v1.0',
    author='Reynold Tabuena',
    author_email='rynldtbuen@gmail.com',
    description=(
        '''
        A python script that simplify the configuration variables defined in
        master.yml and use it as a custom filter in
        https://github.com/rynldtbuen/cumulus-vxlan-evpn-ansible.git
        to load the simplified configuration variables to deploy
        Cumulus VXLAN EVPN
        '''
    ),
    url='https://github.com/rynldtbuen/cl_vx_config',
    download_url=(
        'https://github.com/rynldtbuen/cl_vx_config/archive/v0.1-beta.zip'
    ),
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'ansible==2.7.8',
        'napalm',
        'napalm-ansible',
        'napalm-vyos',
        'ruamel.yaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta'
    ],
)
