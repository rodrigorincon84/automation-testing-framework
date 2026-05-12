from core.interface.collection_element import (
    CollectionElement, CollectionElmntAction, CollectionElmntFilter, CollectionElmntShould
)


class CollectionElementShould(CollectionElmntShould):

    def __init__(self, collection: CollectionElement):
        self._collection: CollectionElement = collection

    def filter(self) -> CollectionElmntFilter:
        return self._collection.filter()

    def action(self) -> CollectionElmntAction:
        return self._collection.action()

    def have_size(self, comparator, amount):
        raise NotImplementedError
        return self
