# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lab2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nlab2.proto\x12\x04lab2\"\x16\n\x05\x41rray\x12\r\n\x05value\x18\x01 \x03(\x02\"\x1b\n\x08Response\x12\x0f\n\x07reponse\x18\x01 \x01(\t2:\n\x04Lab2\x12\x32\n\x11LessGreaterNumber\x12\x0b.lab2.Array\x1a\x0e.lab2.Response\"\x00\x62\x06proto3')



_ARRAY = DESCRIPTOR.message_types_by_name['Array']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
Array = _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), {
  'DESCRIPTOR' : _ARRAY,
  '__module__' : 'lab2_pb2'
  # @@protoc_insertion_point(class_scope:lab2.Array)
  })
_sym_db.RegisterMessage(Array)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'lab2_pb2'
  # @@protoc_insertion_point(class_scope:lab2.Response)
  })
_sym_db.RegisterMessage(Response)

_LAB2 = DESCRIPTOR.services_by_name['Lab2']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ARRAY._serialized_start=20
  _ARRAY._serialized_end=42
  _RESPONSE._serialized_start=44
  _RESPONSE._serialized_end=71
  _LAB2._serialized_start=73
  _LAB2._serialized_end=131
# @@protoc_insertion_point(module_scope)