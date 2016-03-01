# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from motion_editor_core/ExecuteMotionRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ExecuteMotionRequest(genpy.Message):
  _md5sum = "baea61f0df386139ca78eeafc991b967"
  _type = "motion_editor_core/ExecuteMotionRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
string motion_name


float32 time_factor

"""
  __slots__ = ['motion_name','time_factor']
  _slot_types = ['string','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       motion_name,time_factor

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ExecuteMotionRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.motion_name is None:
        self.motion_name = ''
      if self.time_factor is None:
        self.time_factor = 0.
    else:
      self.motion_name = ''
      self.time_factor = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.motion_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_f.pack(self.time_factor))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motion_name = str[start:end].decode('utf-8')
      else:
        self.motion_name = str[start:end]
      start = end
      end += 4
      (self.time_factor,) = _struct_f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.motion_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_f.pack(self.time_factor))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motion_name = str[start:end].decode('utf-8')
      else:
        self.motion_name = str[start:end]
      start = end
      end += 4
      (self.time_factor,) = _struct_f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f = struct.Struct("<f")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from motion_editor_core/ExecuteMotionResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import std_msgs.msg

class ExecuteMotionResponse(genpy.Message):
  _md5sum = "bc46ec169a534a83d0df8dab4f9cea97"
  _type = "motion_editor_core/ExecuteMotionResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
bool ok

std_msgs/Time finish_time


================================================================================
MSG: std_msgs/Time
time data

"""
  __slots__ = ['ok','finish_time']
  _slot_types = ['bool','std_msgs/Time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ok,finish_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ExecuteMotionResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.ok is None:
        self.ok = False
      if self.finish_time is None:
        self.finish_time = std_msgs.msg.Time()
    else:
      self.ok = False
      self.finish_time = std_msgs.msg.Time()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_B2I.pack(_x.ok, _x.finish_time.data.secs, _x.finish_time.data.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.finish_time is None:
        self.finish_time = std_msgs.msg.Time()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.ok, _x.finish_time.data.secs, _x.finish_time.data.nsecs,) = _struct_B2I.unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_B2I.pack(_x.ok, _x.finish_time.data.secs, _x.finish_time.data.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.finish_time is None:
        self.finish_time = std_msgs.msg.Time()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.ok, _x.finish_time.data.secs, _x.finish_time.data.nsecs,) = _struct_B2I.unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B2I = struct.Struct("<B2I")
class ExecuteMotion(object):
  _type          = 'motion_editor_core/ExecuteMotion'
  _md5sum = 'df0966c07354a91b75525ffbd3ff4e08'
  _request_class  = ExecuteMotionRequest
  _response_class = ExecuteMotionResponse
