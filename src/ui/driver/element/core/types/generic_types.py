from typing import TypeVar

from ..interface.collection_element import CollectionElement
from ..interface.input import Input
from ..interface.select import Select
from ..interface.element import Element
from ..interface.error import Error

TElement = TypeVar('TElement', bound=Element)
TError = TypeVar("TError", bound=Error)
TInput = TypeVar('TInput', bound=Input)
TSelect = TypeVar("TSelect", bound=Select)
TCollection = TypeVar("TCollection", bound=CollectionElement)
