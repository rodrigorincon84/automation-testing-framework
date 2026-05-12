from core.interface.collection_element import (
    CollectionElement, CollectionElmntAction, CollectionElmntFilter, CollectionElmntShould
)
from core.types.generic_types import TElement


class CollectionElementAction(CollectionElmntAction):

    def __init__(self, collection: CollectionElement):
        self._collection: CollectionElement = collection

    def should_(self) -> CollectionElmntShould:
        return self._collection.should_()

    def filter(self) -> CollectionElmntFilter:
        return self._collection.filter()

    def get_elements(self) -> list[TElement]:
        collection = self._collection.get_underlying_collection()
        ui_elements: list[TElement] = []

        for e in collection:
            element = self._collection.get_parameter("driver").Element().from_wrapped(e).build()
            ui_elements.append(element)

        return ui_elements
