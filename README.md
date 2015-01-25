Code to help you with short-range syntax detection in tweets.

Basic usage
===========

This is meant as a add-on package to the fantastic POS Twitter taggers developed by CMU's TweetNLP team (info at http://www.ark.cs.cmu.edu/TweetNLP/#pos_down).

(0) Collect your data! I'm working on a real simple Python Twitter miner but for now you should check out (https://github.com/tweepy/tweepy) to get going.

(1) To get started, pull the package from https://github.com/brendano/ark-tweet-nlp/. Once you've got that and your raw data, modify runTagger.sh to have your tweet file as its input and a new file name as its output. It will look like this:

"#!/bin/bash
set -eu

# Run the tagger (and tokenizer).
java -XX:ParallelGCThreads=2 -Xmx500m -jar $(dirname $0)/ark-tweet-nlp-0.3.2.jar "$@" --model model.ritter_ptb_alldata_fixed.20130723 sampleTweets.txt > sampleTweetsTagged.txt"

The long model name (model.ritter...) specifies which kind of POS tags you want: the "standard" PTB stuff (https://mlnl.net/jg/software/pac/ptb_pos.html) or the custom tags which are simpler and Twitter-specific (http://www.ark.cs.cmu.edu/TweetNLP/annot_guidelines.pdf). I included sampleTweets.txt, sample

(2) Next step: run the tagger! It may take a few hours for bigger (>10 G) files. You'll notice the output file has funky formatting, and I wrote tabCleanup.py to convert the formatting to a more parseable word\POS format. This format does get rid of tag probabilities but makes life easier for rule-based syntax detection. So after running the tagger, run tabCleanup.py with the arguments (1) tagged tweets file (2) output file name.

(3) Write some regular expressions to extract syntax patterns! Save them in a txt file to access later. You can find the ones I used for my AAE research in syntaxPatterns/. Use the '|' operator to do "OR" statements, like "don't" OR "couldn't" would be "(don't)|(couldn't)". And use "_" as a wildcard, i.e. any word or POS expression. If you're totally lost, check out Python's regex documentation at https://docs.python.org/2/howto/regex.html to get started. It's easy, I promise. Just make sure that each pattern in the file is separated by a return character.

Caveat: all the patterns within a file have to use the same tag set. So no PTB/custom-tag mashups like "we\\O be\\V chillin\\VBG". Sorry, it was too complicated to do it that way.

(4) Extract those tweets! Run pat_extraction.py with the arguments (1) tweet file (2) pattern file (3) output file name (ex. "habitual_be.tweets"). MAKE SURE that the tweet file has the same tagset as your patterns. pat_extraction.py is a pretty verbose program, so you may want to manually kill the print statements if you get fed up with the feedback. It also shouldn't take more than a few minutes to chug through even >10G files.

(5) Check your errors in the output file and keep modifying your regexes until you've reached a sufficient accuracy. 

Information
===========

I'm going to be adding more of my code to show how I connected tweets to demographic data in order to do studies like this: http://www.aclweb.org/anthology/E/E14/E14-3.pdf#page=41

The POS tagging models I used are described in the following two papers, available at TweetNLP website.
Please cite these if you write a research paper using this software.

Part-of-Speech Tagging for Twitter: Annotation, Features, and Experiments
Kevin Gimpel, Nathan Schneider, Brendan O'Connor, Dipanjan Das, Daniel Mills,
  Jacob Eisenstein, Michael Heilman, Dani Yogatama, Jeffrey Flanigan, and 
  Noah A. Smith
In Proceedings of the Annual Meeting of the Association
  for Computational Linguistics, companion volume, Portland, OR, June 2011.
http://www.ark.cs.cmu.edu/TweetNLP/gimpel+etal.acl11.pdf

Part-of-Speech Tagging for Twitter: Word Clusters and Other Advances
Olutobi Owoputi, Brendan O'Connor, Chris Dyer, Kevin Gimpel, and
  Nathan Schneider.
Technical Report, Machine Learning Department. CMU-ML-12-107. September 2012.

Contact
=======

Please contact Ian Stewart (ian.b.stewart.14@alum.dartmouth.org) if you encounter any problems or if I did something bad.