# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/tts/v3/tts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n yandex/cloud/ai/tts/v3/tts.proto\x12\x10speechkit.tts.v3\"j\n\x0c\x41udioContent\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12\x38\n\naudio_spec\x18\x02 \x01(\x0b\x32$.speechkit.tts.v3.AudioFormatOptionsB\r\n\x0b\x41udioSource\"\x91\x01\n\x12\x41udioFormatOptions\x12/\n\traw_audio\x18\x01 \x01(\x0b\x32\x1a.speechkit.tts.v3.RawAudioH\x00\x12;\n\x0f\x63ontainer_audio\x18\x02 \x01(\x0b\x32 .speechkit.tts.v3.ContainerAudioH\x00\x42\r\n\x0b\x41udioFormat\"\xaa\x01\n\x08RawAudio\x12@\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32(.speechkit.tts.v3.RawAudio.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x03\"A\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x10\n\x0cLINEAR16_PCM\x10\x01\"\xbf\x01\n\x0e\x43ontainerAudio\x12Q\n\x14\x63ontainer_audio_type\x18\x01 \x01(\x0e\x32\x33.speechkit.tts.v3.ContainerAudio.ContainerAudioType\"Z\n\x12\x43ontainerAudioType\x12$\n CONTAINER_AUDIO_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03WAV\x10\x01\x12\x0c\n\x08OGG_OPUS\x10\x02\x12\x07\n\x03MP3\x10\x03\"=\n\x0cTextVariable\x12\x15\n\rvariable_name\x18\x01 \x01(\t\x12\x16\n\x0evariable_value\x18\x02 \x01(\t\"]\n\rAudioVariable\x12\x15\n\rvariable_name\x18\x01 \x01(\t\x12\x19\n\x11variable_start_ms\x18\x02 \x01(\x03\x12\x1a\n\x12variable_length_ms\x18\x03 \x01(\x03\"O\n\x1aUtteranceSynthesisResponse\x12\x31\n\x0b\x61udio_chunk\x18\x01 \x01(\x0b\x32\x1c.speechkit.tts.v3.AudioChunk\"\xa9\x01\n\rAudioTemplate\x12-\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x1e.speechkit.tts.v3.AudioContent\x12\x35\n\rtext_template\x18\x02 \x01(\x0b\x32\x1e.speechkit.tts.v3.TextTemplate\x12\x32\n\tvariables\x18\x03 \x03(\x0b\x32\x1f.speechkit.tts.v3.AudioVariable\"\x1a\n\nAudioChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"X\n\x0cTextTemplate\x12\x15\n\rtext_template\x18\x01 \x01(\t\x12\x31\n\tvariables\x18\x02 \x03(\x0b\x32\x1e.speechkit.tts.v3.TextVariable\"\xa5\x01\n\x05Hints\x12\x0f\n\x05voice\x18\x01 \x01(\tH\x00\x12\x39\n\x0e\x61udio_template\x18\x02 \x01(\x0b\x32\x1f.speechkit.tts.v3.AudioTemplateH\x00\x12\x0f\n\x05speed\x18\x03 \x01(\x01H\x00\x12\x10\n\x06volume\x18\x04 \x01(\x01H\x00\x12\x0e\n\x04role\x18\x05 \x01(\tH\x00\x12\x15\n\x0bpitch_shift\x18\x06 \x01(\x01H\x00\x42\x06\n\x04Hint\"\xcc\x03\n\x19UtteranceSynthesisRequest\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12\x37\n\rtext_template\x18\x03 \x01(\x0b\x32\x1e.speechkit.tts.v3.TextTemplateH\x00\x12&\n\x05hints\x18\x04 \x03(\x0b\x32\x17.speechkit.tts.v3.Hints\x12?\n\x11output_audio_spec\x18\x05 \x01(\x0b\x32$.speechkit.tts.v3.AudioFormatOptions\x12j\n\x1bloudness_normalization_type\x18\x06 \x01(\x0e\x32\x45.speechkit.tts.v3.UtteranceSynthesisRequest.LoudnessNormalizationType\x12\x13\n\x0bunsafe_mode\x18\x07 \x01(\x08\"`\n\x19LoudnessNormalizationType\x12+\n\'LOUDNESS_NORMALIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08MAX_PEAK\x10\x01\x12\x08\n\x04LUFS\x10\x02\x42\x0b\n\tUtteranceB\\\n\x1ayandex.cloud.api.ai.tts.v3Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/tts/v3;ttsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.tts.v3.tts_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032yandex.cloud.api.ai.tts.v3Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/tts/v3;tts'
  _globals['_AUDIOCONTENT']._serialized_start=54
  _globals['_AUDIOCONTENT']._serialized_end=160
  _globals['_AUDIOFORMATOPTIONS']._serialized_start=163
  _globals['_AUDIOFORMATOPTIONS']._serialized_end=308
  _globals['_RAWAUDIO']._serialized_start=311
  _globals['_RAWAUDIO']._serialized_end=481
  _globals['_RAWAUDIO_AUDIOENCODING']._serialized_start=416
  _globals['_RAWAUDIO_AUDIOENCODING']._serialized_end=481
  _globals['_CONTAINERAUDIO']._serialized_start=484
  _globals['_CONTAINERAUDIO']._serialized_end=675
  _globals['_CONTAINERAUDIO_CONTAINERAUDIOTYPE']._serialized_start=585
  _globals['_CONTAINERAUDIO_CONTAINERAUDIOTYPE']._serialized_end=675
  _globals['_TEXTVARIABLE']._serialized_start=677
  _globals['_TEXTVARIABLE']._serialized_end=738
  _globals['_AUDIOVARIABLE']._serialized_start=740
  _globals['_AUDIOVARIABLE']._serialized_end=833
  _globals['_UTTERANCESYNTHESISRESPONSE']._serialized_start=835
  _globals['_UTTERANCESYNTHESISRESPONSE']._serialized_end=914
  _globals['_AUDIOTEMPLATE']._serialized_start=917
  _globals['_AUDIOTEMPLATE']._serialized_end=1086
  _globals['_AUDIOCHUNK']._serialized_start=1088
  _globals['_AUDIOCHUNK']._serialized_end=1114
  _globals['_TEXTTEMPLATE']._serialized_start=1116
  _globals['_TEXTTEMPLATE']._serialized_end=1204
  _globals['_HINTS']._serialized_start=1207
  _globals['_HINTS']._serialized_end=1372
  _globals['_UTTERANCESYNTHESISREQUEST']._serialized_start=1375
  _globals['_UTTERANCESYNTHESISREQUEST']._serialized_end=1835
  _globals['_UTTERANCESYNTHESISREQUEST_LOUDNESSNORMALIZATIONTYPE']._serialized_start=1726
  _globals['_UTTERANCESYNTHESISREQUEST_LOUDNESSNORMALIZATIONTYPE']._serialized_end=1822
# @@protoc_insertion_point(module_scope)
