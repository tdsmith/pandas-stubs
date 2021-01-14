from StringIO import StringIO

import numpy as np
from pandas.core.frame import DataFrame

from pandas._typing import Renamer, Axis, FrameOrSeries, Function, AxisOption, Frequency, Scalar, Dtype, NoneNumpyCompatible, Level, \
    GroupByObject, GeneralDuplicatesKeepStrategy, Label, ArrayLike, InterpolationMethod, CorrelationMethod, SearchSide
from pandas.core import base, generic
from pandas.core.arrays import ExtensionArray
from pandas.core.groupby import generic as groupby_generic
from typing import Any, Callable, Hashable, IO, Optional, Iterable, Union, Mapping, Sequence

from pandas.core.indexes.base import Index


class Series(base.IndexOpsMixin, generic.NDFrame):
    hasnans: Any = ...
    div: Callable[[Series, Any], Series]
    rdiv: Callable[[Series, Any], Series]
    def __init__(self, data: Optional[Any] = ..., index: Optional[Any] = ..., dtype: Optional[Dtype] = ..., name: Optional[Any] = ..., copy: bool = ..., fastpath: bool = ...) -> None: ...
    @property
    def dtype(self) -> Dtype: ...
    @property
    def dtypes(self) -> Dtype: ...
    @property
    def name(self) -> Optional[Hashable]: ...
    @name.setter
    def name(self, value: Optional[Hashable]) -> None: ...
    @property
    def values(self) -> Any: ...
    @property
    def array(self) -> ExtensionArray: ...
    def ravel(self, order: str = ...) -> Any: ...
    def __len__(self) -> int: ...
    def view(self, dtype: Optional[Dtype] = ...) -> Any: ...
    def __array_ufunc__(self, ufunc: Function, method: str, *inputs: Any, **kwargs: Any) -> Any: ...
    def __array__(self, dtype: Any = ...) -> np.ndarray: ...
    __float__: Any = ...
    __long__: Any = ...
    __int__: Any = ...
    @property
    def axes(self) -> Any: ...
    def take(self, indices: Union[Iterable[int], np.ndarray[np.int_]], axis: AxisOption = ..., is_copy: bool = ..., **kwargs: Any) -> Series: ...
    def __getitem__(self, key: Any) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def repeat(self, repeats: Union[int, Iterable[int]], axis: Optional[NoneNumpyCompatible] = ...) -> Series: ...
    index: Any = ...
    def reset_index(self, level: Optional[Level] = ..., drop: bool = ..., name: Optional[Any] = ..., inplace: bool = ...) -> FrameOrSeries: ...
    def to_string(self, buf: Optional[StringIO] = ..., na_rep: Optional[str] = ..., float_format: Optional[Callable[[Any], Any]] = ..., header: bool = ..., index: bool = ..., length: bool = ..., dtype: bool = ..., name: bool = ..., max_rows: Optional[int] = ..., min_rows: Optional[int] = ...) -> Union[str, None]: ...
    def to_markdown(self, buf: Optional[IO[str]]=..., mode: Optional[str]=..., **kwargs: Any) -> Optional[str]: ...
    def items(self) -> Iterable[Any]: ...
    def iteritems(self) -> Iterable[Any]: ...
    def keys(self) -> Index: ...
    def to_dict(self, into: Mapping = ...) -> Mapping[Any, Any]: ...
    def to_frame(self, name: Optional[Any] = ...) -> DataFrame: ...
    def groupby(self, by: Optional[GroupByObject] = ..., axis: AxisOption = ..., level: Sequence[Level] = ..., as_index: bool=..., sort: bool=..., group_keys: bool=..., squeeze: bool=..., observed: bool=...) -> groupby_generic.SeriesGroupBy: ...
    def count(self, level: Optional[Level] = ...) -> Union[int, Series]: ...
    def mode(self, dropna: bool = ...) -> Series: ...
    def unique(self) -> ArrayLike: ...
    def drop_duplicates(self, keep: GeneralDuplicatesKeepStrategy = ..., inplace: bool = ...) -> Optional[Series]: ...
    def duplicated(self, keep: GeneralDuplicatesKeepStrategy = ...) -> Series: ...
    def idxmin(self, axis: int = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Label: ...
    def idxmax(self, axis: int = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Label: ...
    def round(self, decimals: int = ..., *args: Any, **kwargs: Any) -> Series: ...
    def quantile(self, q: Union[float, ArrayLike] = ..., interpolation: InterpolationMethod = ...) -> Union[float, Series]: ...
    def corr(self, other: Series, method: CorrelationMethod = ..., min_periods: Optional[int] = ...) -> float: ...
    def cov(self, other: Series, min_periods: Optional[int] = ...) -> float: ...
    def diff(self, periods: int = ...) -> Series: ...
    def autocorr(self, lag: int = ...) -> float: ...
    DotOther = Union['Series', DataFrame, ArrayLike]
    DotResult = Union[Scalar, 'Series', ArrayLike]
    def dot(self, other: DotOther) -> DotResult: ...
    def __matmul__(self, other: DotOther) -> DotResult: ...
    def __rmatmul__(self, other: DotOther) -> DotResult: ...
    def searchsorted(self, value: ArrayLike, side: SearchSide = ..., sorter: Optional[ArrayLike] = ...) -> Sequence[int]: ...
    def append(self, to_append: Union[Series, Iterable[Series]], ignore_index: bool = ..., verify_integrity: bool = ...) -> Series: ...
    def combine(self, other: Any, func: Any, fill_value: Optional[Any] = ...) -> Any: ...
    def combine_first(self, other: Any) -> Any: ...
    def update(self, other: Any) -> None: ...
    def sort_values(self, axis: int = ..., ascending: bool = ..., inplace: bool = ..., kind: str = ..., na_position: str = ..., ignore_index: bool = ...) -> Any: ...   # type: ignore[override]
    def sort_index(self, axis: Any = ..., level: Any = ..., ascending: Any = ..., inplace: Any = ..., kind: Any = ..., na_position: Any = ..., sort_remaining: Any = ..., ignore_index: bool=...) -> Any: ...
    def argsort(self, axis: int = ..., kind: str = ..., order: Optional[Any] = ...) -> Any: ...
    def nlargest(self, n: int = ..., keep: str = ...) -> Any: ...
    def nsmallest(self, n: int = ..., keep: str = ...) -> Any: ...
    def swaplevel(self, i: int = ..., j: int = ..., copy: bool = ...) -> Any: ...
    def reorder_levels(self, order: Any) -> Any: ...
    def explode(self) -> Series: ...
    def unstack(self, level: int = ..., fill_value: Optional[Any] = ...) -> Any: ...
    def map(self, arg: Any, na_action: Optional[Any] = ...) -> Any: ...
    def aggregate(self, func: Any, axis: int = ..., *args: Any, **kwargs: Any) -> Any: ...
    agg: Any = ...
    def transform(self, func: Any, axis: int = ..., *args: Any, **kwargs: Any) -> Any: ...
    def apply(self, func: Any, convert_dtype: bool = ..., args: Any = ..., **kwds: Any) -> Any: ...
    def align(self, other: Any, join: str = ..., axis: Optional[Any] = ..., level: Optional[Any] = ..., copy: bool = ..., fill_value: Optional[Any] = ..., method: Optional[Any] = ..., limit: Optional[Any] = ..., fill_axis: int = ..., broadcast_axis: Optional[Any] = ...) -> Any: ...
    def rename(self, index: Optional[Renamer] = ..., *, axis: Optional[Axis] = ..., copy: bool = ..., inplace: bool = ..., level: Optional[int] = ..., errors: str = ...) -> Optional[Series]: ...   # type: ignore[override]
    def reindex(self, index: Optional[Any] = ..., **kwargs: Any) -> FrameOrSeries: ... # type: ignore[override]
    def drop(self, labels: Optional[Any] = ..., axis: int = ..., index: Optional[Any] = ..., columns: Optional[Any] = ..., level: Optional[Any] = ..., inplace: bool = ..., errors: str = ...) -> Any: ...
    def fillna(self, value: Any = ..., method: Any = ..., axis: Any = ..., inplace: Any = ..., limit: Any = ..., downcast: Any = ...) -> Optional[Series]: ...
    def replace(self, to_replace: Optional[Any] = ..., value: Optional[Any] = ..., inplace: bool = ..., limit: Optional[Any] = ..., regex: bool = ..., method: str = ...) -> Any: ...
    def shift(self, periods: int = ..., freq: Optional[Frequency] = ..., axis: AxisOption = ..., fill_value: Scalar = ...) -> Series: ...
    def memory_usage(self, index: bool = ..., deep: bool = ...) -> int: ... # type: ignore[override]
    def isin(self, values: Any) -> Any: ...
    def between(self, left: Any, right: Any, inclusive: bool = ...) -> Any: ...
    def isna(self) -> Any: ...
    def isnull(self) -> Any: ...
    def notna(self) -> Any: ...
    def notnull(self) -> Any: ...
    def dropna(self, axis: int = ..., inplace: bool = ..., how: Optional[Any] = ...) -> Any: ...
    def to_timestamp(self, freq: Optional[Any] = ..., how: str = ..., copy: bool = ...) -> Any: ...
    def to_period(self, freq: Optional[Any] = ..., copy: bool = ...) -> Any: ...
    str: Any = ...
    dt: Any = ...
    cat: Any = ...
    plot: Any = ...
    sparse: Any = ...
    hist: Any = ...
