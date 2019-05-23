# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/services/paid_organic_search_term_view_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.resources import paid_organic_search_term_view_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_paid__organic__search__term__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/services/paid_organic_search_term_view_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v1.servicesB%PaidOrganicSearchTermViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services'),
  serialized_pb=_b('\nRgoogle/ads/googleads_v1/proto/services/paid_organic_search_term_view_service.proto\x12 google.ads.googleads.v1.services\x1aKgoogle/ads/googleads_v1/proto/resources/paid_organic_search_term_view.proto\x1a\x1cgoogle/api/annotations.proto\"<\n#GetPaidOrganicSearchTermViewRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x8e\x02\n PaidOrganicSearchTermViewService\x12\xe9\x01\n\x1cGetPaidOrganicSearchTermView\x12\x45.google.ads.googleads.v1.services.GetPaidOrganicSearchTermViewRequest\x1a<.google.ads.googleads.v1.resources.PaidOrganicSearchTermView\"D\x82\xd3\xe4\x93\x02>\x12</v1/{resource_name=customers/*/paidOrganicSearchTermViews/*}B\x8c\x02\n$com.google.ads.googleads.v1.servicesB%PaidOrganicSearchTermViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_paid__organic__search__term__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETPAIDORGANICSEARCHTERMVIEWREQUEST = _descriptor.Descriptor(
  name='GetPaidOrganicSearchTermViewRequest',
  full_name='google.ads.googleads.v1.services.GetPaidOrganicSearchTermViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetPaidOrganicSearchTermViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=287,
)

DESCRIPTOR.message_types_by_name['GetPaidOrganicSearchTermViewRequest'] = _GETPAIDORGANICSEARCHTERMVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPaidOrganicSearchTermViewRequest = _reflection.GeneratedProtocolMessageType('GetPaidOrganicSearchTermViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPAIDORGANICSEARCHTERMVIEWREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.paid_organic_search_term_view_service_pb2'
  ,
  __doc__ = """Request message for
  [PaidOrganicSearchTermViewService.GetPaidOrganicSearchTermView][google.ads.googleads.v1.services.PaidOrganicSearchTermViewService.GetPaidOrganicSearchTermView].
  
  
  Attributes:
      resource_name:
          The resource name of the paid organic search term view to
          fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetPaidOrganicSearchTermViewRequest)
  ))
_sym_db.RegisterMessage(GetPaidOrganicSearchTermViewRequest)


DESCRIPTOR._options = None

_PAIDORGANICSEARCHTERMVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='PaidOrganicSearchTermViewService',
  full_name='google.ads.googleads.v1.services.PaidOrganicSearchTermViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=290,
  serialized_end=560,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPaidOrganicSearchTermView',
    full_name='google.ads.googleads.v1.services.PaidOrganicSearchTermViewService.GetPaidOrganicSearchTermView',
    index=0,
    containing_service=None,
    input_type=_GETPAIDORGANICSEARCHTERMVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_paid__organic__search__term__view__pb2._PAIDORGANICSEARCHTERMVIEW,
    serialized_options=_b('\202\323\344\223\002>\022</v1/{resource_name=customers/*/paidOrganicSearchTermViews/*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_PAIDORGANICSEARCHTERMVIEWSERVICE)

DESCRIPTOR.services_by_name['PaidOrganicSearchTermViewService'] = _PAIDORGANICSEARCHTERMVIEWSERVICE

# @@protoc_insertion_point(module_scope)