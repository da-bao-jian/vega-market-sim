# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/assets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11vega/assets.proto\x12\x04vega"8\n\x05\x41sset\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x12.vega.AssetDetails"\xba\x01\n\x0c\x41ssetDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x14\n\x0ctotal_supply\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x04 \x01(\x04\x12\x0f\n\x07quantum\x18\x05 \x01(\t\x12+\n\rbuiltin_asset\x18\x65 \x01(\x0b\x32\x12.vega.BuiltinAssetH\x00\x12\x1c\n\x05\x65rc20\x18\x66 \x01(\x0b\x32\x0b.vega.ERC20H\x00\x42\x08\n\x06source".\n\x0c\x42uiltinAsset\x12\x1e\n\x16max_faucet_amount_mint\x18\x01 \x01(\t"U\n\x05\x45RC20\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\x12\x16\n\x0elifetime_limit\x18\x02 \x01(\t\x12\x1a\n\x12withdraw_threshold\x18\x03 \x01(\tB"Z code.vegaprotocol.io/protos/vegab\x06proto3'
)


_ASSET = DESCRIPTOR.message_types_by_name["Asset"]
_ASSETDETAILS = DESCRIPTOR.message_types_by_name["AssetDetails"]
_BUILTINASSET = DESCRIPTOR.message_types_by_name["BuiltinAsset"]
_ERC20 = DESCRIPTOR.message_types_by_name["ERC20"]
Asset = _reflection.GeneratedProtocolMessageType(
    "Asset",
    (_message.Message,),
    {
        "DESCRIPTOR": _ASSET,
        "__module__": "vega.assets_pb2"
        # @@protoc_insertion_point(class_scope:vega.Asset)
    },
)
_sym_db.RegisterMessage(Asset)

AssetDetails = _reflection.GeneratedProtocolMessageType(
    "AssetDetails",
    (_message.Message,),
    {
        "DESCRIPTOR": _ASSETDETAILS,
        "__module__": "vega.assets_pb2"
        # @@protoc_insertion_point(class_scope:vega.AssetDetails)
    },
)
_sym_db.RegisterMessage(AssetDetails)

BuiltinAsset = _reflection.GeneratedProtocolMessageType(
    "BuiltinAsset",
    (_message.Message,),
    {
        "DESCRIPTOR": _BUILTINASSET,
        "__module__": "vega.assets_pb2"
        # @@protoc_insertion_point(class_scope:vega.BuiltinAsset)
    },
)
_sym_db.RegisterMessage(BuiltinAsset)

ERC20 = _reflection.GeneratedProtocolMessageType(
    "ERC20",
    (_message.Message,),
    {
        "DESCRIPTOR": _ERC20,
        "__module__": "vega.assets_pb2"
        # @@protoc_insertion_point(class_scope:vega.ERC20)
    },
)
_sym_db.RegisterMessage(ERC20)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z code.vegaprotocol.io/protos/vega"
    _ASSET._serialized_start = 27
    _ASSET._serialized_end = 83
    _ASSETDETAILS._serialized_start = 86
    _ASSETDETAILS._serialized_end = 272
    _BUILTINASSET._serialized_start = 274
    _BUILTINASSET._serialized_end = 320
    _ERC20._serialized_start = 322
    _ERC20._serialized_end = 407
# @@protoc_insertion_point(module_scope)