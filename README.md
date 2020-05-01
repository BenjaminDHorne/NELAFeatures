# nela_features

NELA (News Landscape) Features are groups of hand-crafted, text-based features for news veracity detection. These features have been used on multiple news veracity studies, although they can also be used more generically. 

## Features

The features can be broken down into 6 groups:

* Style - This feature group captures the style and structure of the article. It includes POS (part of speech) tags and simple linguistic features such as number of quotes, punctuation, and all capitalized words.
* Complexity - This feature group captures how complex the writing in the article is. It includes lexical diversity (type-token ratio), multiple reading difficulty metrics, length of words, and length of sentences.
* Bias - This feature group captures the overall bias and subjectivity in the writing. This feature group is strongly based on Recasens et al. work [1] on detecting bias language.It includes the number of hedges, factives, assertives, implicatives, and opinion words.
* Affect - This feature group captures sentiment and emotion used in the text. It includes LIWC emotion features such as anger, anxiety, and swear words [2]. It also includes positive and negative sentiment measures using VADER sentiment [3].
* Moral - This feature group is based on Moral Foundation Theory [4] and lexicons used in [5]
* Event - This feature group captures two concepts: time and location. This group contains 3 features: the number of locations in the article, the number of dates or times in the article, and the number of time related words in an article.
 

## Installation

The easiest way to install is using pip. This will install all Python dependencies and NLTK downloads needed. 

`pip install nela_features`

You can also download the *nela_features* folder and manually import the package and install dependencies. 

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

If you have used the old version of these features: https://github.com/BenjaminDHorne/Language-Features-for-News, you will notice a few changes: 1. The subjectivity classifier features (previous called NBsubj and NBobj) have been removed. 2. The event group of features has been added. You will also notice the feature names have been better normalized and grouped. 

## Papers to cite when using
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

### References

[1] Marta Recasens, Cristian Danescu-Niculescu-Mizil, and Dan Jurafsky. 2013. Linguistic models for analyzing and de-tecting biased language. In Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics(Volume 1: Long Papers), Vol. 1. 1650–1659.

[2] Yla R. Tausczik and James W. Pennebaker. 2010. The psychological meaning of words: LIWC and computerized textanalysis methods. J. Lang. Soc. Psychol. 29, 1 (2010), 24–54.

[3] Clayton J. Hutto and Eric Gilbert. 2014. Vader: A parsimonious rule-based model for sentiment analysis of socialmedia text. In Proceedings of the 8th International AAAI Conference on Weblogs and Social Media.

[4] Jesse Graham, Jonathan Haidt, Sena Koleva, Matt Motyl, Ravi Iyer, Sean P. Wojcik, and Peter H. Ditto. 2013. Moralfoundations theory: The pragmatic validity of moral pluralism. In Advances in Experimental Social Psychology. Vol. 47.Elsevier, 55–130.

[5] Ying Lin, Joe Hoover, Gwenyth Portillo-Wightman, Christina Park, Morteza Dehghani, and Heng Ji. 2018. Acquiringbackground knowledge to improve moral value prediction. In Proceedings of the IEEE/ACM International Conferenceon Advances in Social Networks Analysis and Mining (ASONAM’18). IEEE, 552–559.
