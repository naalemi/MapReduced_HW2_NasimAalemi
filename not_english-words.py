#Date_of_birth 11/07/1990

from spellchecker import SpellChecker
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRNonEnglishWordCount(MRJob):

    def mapper(self, _, line):
        spell = SpellChecker()
        words = line.lower().split()
        for word in words:
            if word not in spell:  # If the word is not recognized
                yield (word, 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                    reducer=self.reducer)
        ]

if __name__ == '__main__':
    MRNonEnglishWordCount.run()
