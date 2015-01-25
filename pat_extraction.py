"""Output tweets that match a given pattern/set of patterns.
Requires: POS-tagged corpus."""

from sys import argv
import cPickle
import re
from collections import defaultdict

"""
Detect patterns and write the matching tweets to separate file.
"""
def getTweetFiles(patList, tweets, outfile):
    patFile = open(outfile,'w')
    patFile.write('TWEET\n')
    ctr=0
    tweetLine = tweets.readline()
    while(tweetLine):
        # if tweet contains one of patterns, capture it
        for pattern in patList:
            if(pattern.search(tweetLine) is not None):
                # store all tweets in pat file
                patFile.write(tweetLine + '\n')
                # break out of pattern-matching loop after successful match
                continue
        ctr+=1
        if(ctr%10**6==0):
            print str(ctr)+'.'
            # output to file
            o.close()
            o = open(statFileName,'a')
            patFile.close()
            patFile = open(patFileName,'a')
        tweetLine = tweets.readline().rstrip()
    print 'done tabulating'
    tweets.close()
    print('done with pats = ' + 
          str(map(lambda x: x.pattern,patList)))
    patFile.close()

"""
Convert pattern to regex.
"""
def regexConvert(pattern):
    pattern = pattern.replace('_\\','\w+\\').replace('\\_','\\[A-Z~!@#$^&,]+')
    print 'split pattern = ' + str(pattern.split())
    finalPattern = [re.compile(pattern)]
    print "regex Pattern is <" + finalPattern.pattern + ">"
    return finalPattern

"""
argv[1] = POS-tagged file e.g. ptb_pos_jul-aug-sep-oct-nov-dec.normalized.noURL.tweets
argv[2] = .txt file containing all patterns separated by line
argv[3] = output file name
"""
if __name__=='__main__':
    tweetFile = argv[1]
    tweets = open(tweetFile,'r')
    print('loaded tweets')

    pats = map(lambda x: x.strip(),open(argv[2]).readlines())
    print 'pats from txt = ' + str(map(lambda x: x+'\n',pats))
    
    writeName = argv[3]
    print('writeName = ' + writeName)
    # list of patterns
    # e.g. negative concord => 'ain't nothing', 'ain't nobody', etc.
    patList = list()
    for pat in pats:
        patList.append(regexConvert(pat))

    getTweetFiles(patList,tweets,writeName)