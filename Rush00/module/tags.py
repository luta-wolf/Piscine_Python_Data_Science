from collections import Counter


class Tags:
    """
    Analyzing data from tags.csv
    """
    def __init__(self, path_to_the_file='data/tags.csv'):
        """
        Put here any fields that you think you will need.
        """
        self.content = []
        try:
            with open(path_to_the_file, 'r') as fl:
                for row in fl:
                    self.content += [row.split(',')[2]]
            self.content = self.content[1:]
        except OSError as os_err:
            print(os_err)

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
 where the keys are tags and the values are the number of words inside the tag.
 Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = {}
        for i in self.content:
            line = i.count('-')
            num = i.count(' ') + 1 - line
            big_tags[i] = num
        big_tags = dict(sorted(big_tags.items(), key=lambda x: -x[1])[:n])
        return big_tags

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = sorted(set(self.content), key=lambda x: len(x), reverse=True)[:n]
        return big_tags

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        big_tags = []
        m_v = self.most_words(n)
        longest = self.longest(n)
        for i, key in enumerate(m_v.keys()):
            if longest[i] == key:
                big_tags += [key]
        return big_tags

    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        big_tags = dict(Counter(self.content))
        big_tags = dict(sorted(big_tags.items(), key=lambda x: -x[1])[:n])
        return big_tags

    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        tags_with_word = []
        for i in self.content:
            if word.upper() in i.upper():
                tags_with_word += [i]
        tags_with_word = sorted(set(tags_with_word), key=lambda x: x.upper())
        return tags_with_word
