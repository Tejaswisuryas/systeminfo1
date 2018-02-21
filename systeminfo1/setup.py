from setuptools import setup
setup(name="systeminfo1",
      version="0.1",
      description="Basic system infromation for comp30670",
      url="",
      author="Tejaswi Suryas",
      author_email="tejaswi.suryas@ucdconnect.ie",
      license="GPL3",
      packages=['systeminfo1'],
      entry_points={
          'console_scripts':['comp30670_systeminfo1=systeminfo1.main:main']
          }
    )