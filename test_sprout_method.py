from abc import ABC, abstractmethod
from typing import List


class Entry(ABC):

    @abstractmethod
    def post_date(self) -> None:
        raise NotImplementedError


class TransactionGate:

    @staticmethod
    def post_entries(entries: List[Entry]):
        for entry in entries:
            entry.post_date()
        transaction_bundle.get_ListManager().add(entries)


# TODO: We need to add code to verify that none of the new entries are already in
# transactionBundle before we post their dates and add them




# Sprout Method
class TransactionGateWithSproutedMethod:

    def post_entries(self, entries: List[Entry]):
        entries_to_add = self.unique_entries(entries)
        for entry in entries:
            entry.post_date()
        transaction_bundle.get_ListManager().add(entries_to_add)

    @staticmethod
    def unique_entries(entries: List[Entry]) -> List[Entry]:
        # let's imagine that there's more complex logic for removing dupes
        return list(set(entries))


"""
Disadvantages:
when you use it, in effect you essentially are saying that you are giving up on the
source method and its class for the moment. You aren’t going to get it under
test, and you aren’t going to make it better—you are just going to add some
new functionality in a new method. Giving up on a method or a class is the
practical choice sometimes, but it still is kind of sad. It leaves your code in
limbo. The source method might contain a lot of complicated code and a single
sprout of a new method. Sometimes it isn’t clear why only that work is happen-
ing someplace else, and it leaves the source method in an odd state. But at least
that points to some additional work that you can do when you get the source
class under test later.

Advantages:
* you are clearly separating new code from old code
* Even if you can’t get the old code under test immediately, 
    you can at least see your changes separately and have a clean interface between 
    the new code and the old code. 
* You see all of the variables affected, and this can make it easier to determine 
    whether the code is right in context.
"""
