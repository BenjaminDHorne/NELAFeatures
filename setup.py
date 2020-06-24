import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='nela_features',
     packages=['nela_features'],
     install_requires=['nltk', 'vaderSentiment', 'datefinder', 'numpy'],
     version='2.0.6',
     author="Benjamin D. Horne",
     author_email="benjamindhorne314@gmail.com",
     description="A package to compute text features for news veracity.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/BenjaminDHorne/NELAFeatures",
     #packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

import nltk
nltk.download('stopwords')
nltk.download('words')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')
