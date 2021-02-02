from pandas._typing import AggregationFunction, GeneralDuplicatesKeepStrategy
from pandas.core import algorithms as algorithms
from pandas.core.accessor import DirNamesMixin as DirNamesMixin
from pandas.core.algorithms import duplicated as duplicated, unique1d as unique1d, value_counts as value_counts
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.construction import create_series_with_explicit_dtype as create_series_with_explicit_dtype
from pandas.core.dtypes.cast import is_nested_object as is_nested_object

from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, Optional

class PandasObject(DirNamesMixin):
    def __sizeof__(self) -> Any: ...

class NoNewAttributesMixin:
    def __setattr__(self, key: Any, value: Any) -> None: ...

class GroupByError(Exception): ...
class DataError(GroupByError): ...
class SpecificationError(GroupByError): ...

class SelectionMixin:
    def ndim(self) -> int: ...
    def __getitem__(self, key: Any) -> Any: ...
    def aggregate(self, func: AggregationFunction, *args: Any, **kwargs: Any) -> Any: ...
    def agg(self, func: AggregationFunction, *args: Any, **kwargs: Any) -> Any: ...

class ShallowMixin: ...

class IndexOpsMixin:
    T: Any = ...
    to_list: Any = ...
    is_monotonic_increasing: Any = ...
    __array_priority__: int = ...
    def __iter__(self) -> Any: ...
    def transpose(self, *args: Any, **kwargs: Any) -> Any: ...
    @property
    def shape(self) -> Any: ...
    @property
    def ndim(self) -> int: ...
    def item(self) -> Any: ...
    @property
    def nbytes(self) -> Any: ...
    @property
    def size(self) -> Any: ...
    @property
    def array(self) -> ExtensionArray: ...
    def to_numpy(self, dtype: Optional[Any] = ..., copy: bool = ..., na_value: Any = ..., **kwargs: Any) -> Any: ...
    @property
    def empty(self) -> Any: ...
    def max(self, axis: Optional[Any] = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    def argmax(self, axis: Optional[Any] = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    def min(self, axis: Optional[Any] = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    def argmin(self, axis: Optional[Any] = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    def tolist(self) -> Any: ...
    def hasnans(self) -> Any: ...
    def value_counts(self, normalize: bool = ..., sort: bool = ..., ascending: bool = ..., bins: Optional[Any] = ..., dropna: bool = ...) -> Any: ...
    def unique(self) -> Any: ...
    def nunique(self, dropna: bool = ...) -> Any: ...
    @property
    def is_unique(self) -> Any: ...
    @property
    def is_monotonic(self) -> Any: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def memory_usage(self, deep: bool = ...) -> Any: ...
    def factorize(self, sort: bool = ..., na_sentinel: int = ...) -> Any: ...
    def searchsorted(self, value: Any, side: str = ..., sorter: Optional[Any] = ...) -> Any: ...
    def drop_duplicates(self, keep: GeneralDuplicatesKeepStrategy = ..., inplace: bool = ...) -> Any: ...
    def duplicated(self, keep: GeneralDuplicatesKeepStrategy = ...) -> Any: ...
