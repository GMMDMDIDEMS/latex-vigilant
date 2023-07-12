from dataclasses import dataclass, field
from typing import Tuple, Optional
from time import perf_counter
from datetime import datetime

import asyncio


@dataclass()
class Header:
    TITLECASE_EXCEPTIONS = ['a', 'abaft', 'about', 'above', 'afore', 'after', 'along', 'amid', 'among', 'an', 'apud',
                            'as', 'aside', 'at', 'atop', 'below', 'but', 'by', 'circa', 'down', 'for', 'from', 'given',
                            'in', 'into', 'lest', 'like', 'mid', 'midst', 'minus', 'near', 'next', 'of', 'off', 'on',
                            'onto', 'out', 'over', 'pace', 'past', 'per', 'plus', 'pro', 'qua', 'round', 'sans', 'save',
                            'since', 'than', 'thru', 'till', 'times', 'to', 'under', 'until', 'unto', 'up', 'upon',
                            'via', 'vice', 'with', 'worth', 'the', 'and', 'nor', 'or', 'yet', 'so']

    # level: str
    content: str
    # position: Tuple(int, int)
    # file: str

    def __post_init__(self):
        self.titlecase = self._get_titlecase()
        self.is_titlecase = self._is_titlecase()
        self.last_check = datetime.now()

    def _get_titlecase(self) -> str:
        modified_words = []
        word_list = self.content.lower().split()
        for word in word_list:
            if word not in self.TITLECASE_EXCEPTIONS:
                modified_words.append(word.capitalize())
            else:
                modified_words.append(word)
        titlecase_string = ' '.join(modified_words)
        return titlecase_string

    def _is_titlecase(self) -> bool:
        return self.content == self.titlecase


def main():
    header = Header("this is a basic TesT")
    print(header)
    print(header.content)
    print(header.titlecase)
    print(header.is_titlecase)
    print(header.last_check)
    print(header.__dict__)


if __name__ == "__main__":
    main()

    # is_titlecase: bool = False
    # titlecase: Optional[str]
    # last_check: Optional[datetime]

    # @property
    # def is_titlecase(self) -> bool:
    #     return self.is_titlecase
