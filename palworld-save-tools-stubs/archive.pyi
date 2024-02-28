# pyright: reportArgumentType=false

import io
from io import TextIOWrapper, BytesIO
import os
import uuid
from typing import Any, Callable, Literal, Optional, Sequence, Union


# Alias stdlib types to avoid name conflicts
_float = float
_bool = bool
_bytes = bytes
_double = float
_int64 = int
_uint64 = int
_uint = int
_int16 = int
_uint16 = int


class UUID:
    __slots__: tuple[Literal["raw_bytes"], Literal["parsed_uuid"], Literal["parsed_str"]]
    raw_bytes: bytes
    parsed_uuid: Optional[uuid.UUID]
    parsed_str: Optional[str]

    def __init__(self, raw_bytes: bytes) -> None: ...

    @staticmethod
    def from_str(s: str) -> "UUID": ...

    def __str__(self) -> str: ...

    def UUID(self) -> uuid.UUID: ...

    def __eq__(self, __value: object) -> bool: ...

    def __ne__(self, __value: object) -> bool: ...

    def __repr__(self) -> str: ...

    def __hash__(self) -> int: ...


# Specify a type for JSON-serializable objects
JSON = Union[None, bool, int, float, str, list["JSON"], dict[str, "JSON"], UUID, uuid.UUID]


def instance_id_reader(reader: "FArchiveReader") -> dict[str, UUID]: ...


def uuid_reader(reader: "FArchiveReader") -> UUID: ...


class FArchiveReader:
    data: BytesIO
    size: int
    type_hints: dict[str, str]
    custom_properties: dict[str, tuple[Callable[..., Any], Callable[..., Any]]]
    debug: bool

    def __init__(
        self,
        data: BytesIO,
        type_hints: dict[str, str] = {},
        custom_properties: dict[str, tuple[Callable[..., Any], Callable[..., Any]]] = {},
        debug: bool = os.environ.get("DEBUG", "0") == "1",
        allow_nan: bool = True,
    ) -> None: ...

    def __enter__(self) -> "FArchiveReader": ...

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

    def internal_copy(self, data: BytesIO, debug: bool) -> "FArchiveReader": ...

    def get_type_or(self, path: str, default: str) -> str: ...

    def eof(self) -> bool: ...

    def read(self, size: int) -> bytes: ...

    def read_to_end(self) -> bytes: ...

    def bool(self) -> bool: ...

    def fstring(self) -> str: ...

    unpack_i16: tuple[_int16, ...]

    def i16(self) -> int: ...

    unpack_u16: tuple[_uint16, ...]

    def u16(self) -> int: ...

    unpack_i32: tuple[int, ...]

    def i32(self) -> int: ...

    unpack_u32: tuple[_uint, ...]

    def u32(self) -> int: ...

    unpack_i64: tuple[_int64, ...]

    def i64(self) -> int: ...

    unpack_u64: tuple[_uint64, ...]

    def u64(self) -> int: ...

    unpack_float: tuple[_float, ...]

    def float(self) -> Optional[_float]: ...

    unpack_double: tuple[_double, ...]

    def double(self) -> Optional[_float]: ...

    unpack_byte: tuple[_bytes, ...]

    def byte(self) -> int: ...

    def byte_list(self, size: int) -> Sequence[int]: ...

    def skip(self, size: int) -> None: ...

    def guid(self) -> UUID: ...

    def optional_guid(self) -> Optional[UUID]: ...

    def tarray(self, type_reader: Callable[["FArchiveReader"], Any]) -> list[Any]: ...

    def properties_until_end(self, path: str = "") -> dict[str, Any]: ...

    def property(
        self, type_name: str, size: int, path: str, nested_caller_path: str = ""
    ) -> dict[str, Any]: ...

    def prop_value(self, type_name: str, struct_type_name: str,
                   path: str) -> JSON: ...

    def struct(self, path: str) -> dict[str, Any]: ...

    def struct_value(self, struct_type: str, path: str = "") -> JSON: ...

    def array_property(self, array_type: str, size: int, path: str) -> JSON: ...

    def array_value(self, array_type: str, count: int, size: int, path: str) -> JSON: ...

    def compressed_short_rotator(self) -> tuple[_float, _float, _float]: ...

    def serializeint(self, component_bit_count: int) -> int: ...

    def packed_vector(
        self, scale_factor: int
    ) -> tuple[Optional[_float], Optional[_float], Optional[_float]]: ...

    def vector(self) -> tuple[Optional[_float], Optional[_float], Optional[_float]]: ...

    def vector_dict(self) -> dict[str, Optional[_float]]: ...

    def quat(
        self,
    ) -> tuple[Optional[_float], Optional[_float], Optional[_float], Optional[_float]]: ...

    def quat_dict(self) -> dict[str, Optional[_float]]: ...

    def ftransform(self) -> dict[str, dict[str, Optional[_float]]]: ...


def uuid_writer(writer: TextIOWrapper, s: Union[str, uuid.UUID, UUID]) -> None: ...


def instance_id_writer(writer: TextIOWrapper, d: dict[str, Any]) -> None: ...


class FArchiveWriter:
    data: io.BytesIO
    size: int
    custom_properties: dict[str, tuple[Callable[..., Any], Callable[..., Any]]]
    debug: bool

    def __init__(
        self,
        custom_properties: dict[str, tuple[Callable[..., Any], Callable[..., Any]]] = {},
        debug: bool = os.environ.get("DEBUG", "0") == "1",
    ) -> None: ...

    def __enter__(self) -> "FArchiveWriter": ...

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

    def copy(self) -> "FArchiveWriter": ...

    def bytes(self) -> bytes: ...

    def write(self, data: _bytes) -> None: ...

    def bool(self, bool: bool) -> None: ...

    def fstring(self, string: str) -> int: ...

    def i16(self, i: int) -> None: ...

    def u16(self, i: int) -> None: ...

    def i32(self, i: int) -> None: ...

    def u32(self, i: int) -> None: ...

    def i64(self, i: int) -> None: ...

    def u64(self, i: int) -> None: ...

    def float(self, i: Optional[float]) -> None: ...

    def double(self, i: Optional[_float]) -> None: ...

    def byte(self, b: int) -> None: ...

    def u(self, b: int) -> None: ...

    def guid(self, u: Union[str, uuid.UUID, UUID]) -> None: ...

    def optional_guid(self, u: Optional[Union[str, uuid.UUID, UUID]]) -> None: ...

    def tarray(
        self, type_writer: Callable[["FArchiveWriter", Any], None], array: list[Any]
    ) -> None: ...

    def properties(self, properties: dict[str, Any]) -> None: ...

    def property(self, property: dict[str, Any]) -> None: ...

    def property_inner(self, property_type: str, property: dict[str, Any]) -> int: ...

    def struct(self, property: dict[str, Any]) -> int: ...

    def struct_value(self, struct_type: str, value: Union[dict[str, Union[_float, None]], int, str, uuid.UUID, UUID, _float]) -> None: ...

    def prop_value(self, type_name: str, struct_type_name: str, value: Union[dict[str, Union[_float, None]], int, str, uuid.UUID, UUID, _float, _bool]) -> None: ...

    def array_property(self, array_type: str, value: dict[str, Any]) -> None: ...

    def array_value(self, array_type: str, count: int, values: list[Any]) -> None: ...

    def compressed_short_rotator(self, pitch: _float, yaw: _float, roll: _float) -> None: ...

    @staticmethod
    def unreal_round_float_to_int(value: _float) -> int: ...

    @staticmethod
    def unreal_get_bits_needed(value: int) -> int: ...

    @staticmethod
    def count_leading_zeroes(value: int) -> int: ...

    def serializeint(self, component_bit_count: int, value: int) -> None: ...

    def packed_vector(self, scale_factor: int, x: _float, y: _float, z: _float) -> None: ...

    def vector(self, x: Optional[_float], y: Optional[_float], z: Optional[_float]) -> None: ...

    def vector_dict(self, value: dict[str, Optional[_float]]) -> None: ...

    def quat(
        self,
        x: Optional[_float],
        y: Optional[_float],
        z: Optional[_float],
        w: Optional[_float],
    ) -> None: ...

    def quat_dict(self, value: dict[str, Optional[_float]]) -> None: ...

    def ftransform(self, value: dict[str, dict[str, Optional[_float]]]) -> None: ...
