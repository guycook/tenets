# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='api',
  syntax='proto3',
  serialized_pb=_b('\n\tapi.proto\x12\x03\x61pi\"\x05\n\x03Nil\"#\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05lines\x18\x02 \x03(\x03\"\xa3\x02\n\x05Issue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x08position\x18\x02 \x01(\x0b\x32\x0f.api.IssueRange\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x11\n\tctxBefore\x18\x04 \x01(\t\x12\x10\n\x08lineText\x18\x05 \x01(\t\x12\x10\n\x08\x63txAfter\x18\x06 \x01(\t\x12(\n\x07metrics\x18\x07 \x03(\x0b\x32\x17.api.Issue.MetricsEntry\x12\x0c\n\x04tags\x18\x08 \x03(\t\x12\x0c\n\x04link\x18\t \x01(\t\x12\x0f\n\x07newCode\x18\n \x01(\x08\x12\r\n\x05patch\x18\x0b \x01(\t\x12\x0b\n\x03\x65rr\x18\x0c \x01(\t\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\nIssueRange\x12\x1c\n\x05start\x18\x01 \x01(\x0b\x32\r.api.Position\x12\x1a\n\x03\x65nd\x18\x02 \x01(\x0b\x32\r.api.Position\"J\n\x08Position\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06Offset\x18\x02 \x01(\x03\x12\x0c\n\x04Line\x18\x03 \x01(\x03\x12\x0e\n\x06\x43olumn\x18\x04 \x01(\x03\"&\n\x06\x43onfig\x12\x1c\n\x07options\x18\x01 \x03(\x0b\x32\x0b.api.Option\"4\n\x06Option\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05usage\x18\x03 \x01(\t\"\x98\x01\n\x04Info\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05usage\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x0c\n\x04tags\x18\x05 \x03(\t\x12\x0f\n\x07metrics\x18\x06 \x03(\t\x12\x10\n\x08language\x18\x07 \x01(\t\x12\x1c\n\x07options\x18\x08 \x03(\x0b\x32\x0b.api.Option\"$\n\rSchemaVersion\"\x13\n\x07version\x12\x08\n\x04V000\x10\x00\x32\xa4\x01\n\x05Tenet\x12%\n\x06Review\x12\t.api.File\x1a\n.api.Issue\"\x00(\x01\x30\x01\x12 \n\x07GetInfo\x12\x08.api.Nil\x1a\t.api.Info\"\x00\x12,\n\nAPIVersion\x12\x08.api.Nil\x1a\x12.api.SchemaVersion\"\x00\x12$\n\tConfigure\x12\x0b.api.Config\x1a\x08.api.Nil\"\x00\x42\x18\n\x10io.grpc.examples\xa2\x02\x03HLWb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SCHEMAVERSION_VERSION = _descriptor.EnumDescriptor(
  name='version',
  full_name='api.SchemaVersion.version',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V000', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=770,
  serialized_end=789,
)
_sym_db.RegisterEnumDescriptor(_SCHEMAVERSION_VERSION)


_NIL = _descriptor.Descriptor(
  name='Nil',
  full_name='api.Nil',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=23,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='api.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.File.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lines', full_name='api.File.lines', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=60,
)


_ISSUE_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='api.Issue.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Issue.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.Issue.MetricsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=354,
)

_ISSUE = _descriptor.Descriptor(
  name='Issue',
  full_name='api.Issue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Issue.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='api.Issue.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comment', full_name='api.Issue.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ctxBefore', full_name='api.Issue.ctxBefore', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lineText', full_name='api.Issue.lineText', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ctxAfter', full_name='api.Issue.ctxAfter', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='api.Issue.metrics', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='api.Issue.tags', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link', full_name='api.Issue.link', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newCode', full_name='api.Issue.newCode', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patch', full_name='api.Issue.patch', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='api.Issue.err', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ISSUE_METRICSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=354,
)


_ISSUERANGE = _descriptor.Descriptor(
  name='IssueRange',
  full_name='api.IssueRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='api.IssueRange.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='api.IssueRange.end', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=426,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='api.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='api.Position.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Offset', full_name='api.Position.Offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Line', full_name='api.Position.Line', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Column', full_name='api.Position.Column', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=502,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='api.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='api.Config.options', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=504,
  serialized_end=542,
)


_OPTION = _descriptor.Descriptor(
  name='Option',
  full_name='api.Option',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Option.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.Option.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usage', full_name='api.Option.usage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=596,
)


_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='api.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Info.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usage', full_name='api.Info.usage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='api.Info.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='api.Info.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='api.Info.tags', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='api.Info.metrics', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='api.Info.language', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='api.Info.options', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=751,
)


_SCHEMAVERSION = _descriptor.Descriptor(
  name='SchemaVersion',
  full_name='api.SchemaVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCHEMAVERSION_VERSION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=753,
  serialized_end=789,
)

_ISSUE_METRICSENTRY.containing_type = _ISSUE
_ISSUE.fields_by_name['position'].message_type = _ISSUERANGE
_ISSUE.fields_by_name['metrics'].message_type = _ISSUE_METRICSENTRY
_ISSUERANGE.fields_by_name['start'].message_type = _POSITION
_ISSUERANGE.fields_by_name['end'].message_type = _POSITION
_CONFIG.fields_by_name['options'].message_type = _OPTION
_INFO.fields_by_name['options'].message_type = _OPTION
_SCHEMAVERSION_VERSION.containing_type = _SCHEMAVERSION
DESCRIPTOR.message_types_by_name['Nil'] = _NIL
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Issue'] = _ISSUE
DESCRIPTOR.message_types_by_name['IssueRange'] = _ISSUERANGE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Option'] = _OPTION
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['SchemaVersion'] = _SCHEMAVERSION

Nil = _reflection.GeneratedProtocolMessageType('Nil', (_message.Message,), dict(
  DESCRIPTOR = _NIL,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Nil)
  ))
_sym_db.RegisterMessage(Nil)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.File)
  ))
_sym_db.RegisterMessage(File)

Issue = _reflection.GeneratedProtocolMessageType('Issue', (_message.Message,), dict(

  MetricsEntry = _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ISSUE_METRICSENTRY,
    __module__ = 'api_pb2'
    # @@protoc_insertion_point(class_scope:api.Issue.MetricsEntry)
    ))
  ,
  DESCRIPTOR = _ISSUE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Issue)
  ))
_sym_db.RegisterMessage(Issue)
_sym_db.RegisterMessage(Issue.MetricsEntry)

IssueRange = _reflection.GeneratedProtocolMessageType('IssueRange', (_message.Message,), dict(
  DESCRIPTOR = _ISSUERANGE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.IssueRange)
  ))
_sym_db.RegisterMessage(IssueRange)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Position)
  ))
_sym_db.RegisterMessage(Position)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Config)
  ))
_sym_db.RegisterMessage(Config)

Option = _reflection.GeneratedProtocolMessageType('Option', (_message.Message,), dict(
  DESCRIPTOR = _OPTION,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Option)
  ))
_sym_db.RegisterMessage(Option)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), dict(
  DESCRIPTOR = _INFO,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Info)
  ))
_sym_db.RegisterMessage(Info)

SchemaVersion = _reflection.GeneratedProtocolMessageType('SchemaVersion', (_message.Message,), dict(
  DESCRIPTOR = _SCHEMAVERSION,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.SchemaVersion)
  ))
_sym_db.RegisterMessage(SchemaVersion)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020io.grpc.examples\242\002\003HLW'))
_ISSUE_METRICSENTRY.has_options = True
_ISSUE_METRICSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)