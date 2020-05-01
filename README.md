# nela_features

NELA (News Landscape) Features are groups of hand-crafted, text-based features for news veracity detection. These features have been used on multiple news veracity studies, although they can also be used more generically. 

## Features

The features can be broken down into 6 groups:

* Style -
* Complexity -
* Bias - 
* Affect -
* Moral - 
* Event - 

## Installation

The easiest way to install is using pip

`pip install nela_features`

## Example package use

**Input**: text as a string

**Output**: feature vector, names of features in vector, both as Python lists

```python
from nela_features.nela_features import NELAFeatureExtractor

newsarticle = "Breaking News: Ireland Expected To Become World's First Country To Divest From Fossil Fuels ..." 

nela = NELAFeatureExtractor()

# Extract all feature groups at once
feature_vector, feature_names = nela.extract_all(newsarticle)

# Extract each feature group independently
feature_vector, feature_names = nela.extract_style(newsarticle) 
feature_vector, feature_names = nela.extract_complexity(newsarticle) 
feature_vector, feature_names = nela.extract_bias(newsarticle)
feature_vector, feature_names = nela.extract_affect(newsarticle) 
feature_vector, feature_names = nela.extract_moral(newsarticle) 
feature_vector, feature_names = nela.extract_event(newsarticle)

```

## Whats different between old and new NELA features?

If you have used the old version of these features: , you will notice a few changes. 1. The subjectivity feature was removed. 2. The event group of features has been added. 

## Papers
The updated features are described in:

@article{horne2019robust,
  title={Robust Fake News Detection Over Time and Attack},
  author={Horne, Benjamin D and N{\o}rregaard, Jeppe and Adali, Sibel},
  journal={ACM Transactions on Intelligent Systems and Technology (TIST)},
  volume={11},
  number={1},
  pages={1--23},
  year={2019},
  publisher={ACM New York, NY, USA}
}

The original features were release in:

@inproceedings{horne2018assessing,
  title={Assessing the news landscape: A multi-module toolkit for evaluating the credibility of news},
  author={Horne, Benjamin D and Dron, William and Khedr, Sara and Adali, Sibel},
  booktitle={Companion Proceedings of the The Web Conference 2018},
  pages={235--238},
  year={2018}
}

Please cite one of the papers if the features are used in publication. 

