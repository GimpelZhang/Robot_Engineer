# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from monstertruck_msgs/RawOdometry.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class RawOdometry(genpy.Message):
  _md5sum = "16be9e146c33fd79f2291a429164cfb3"
  _type = "monstertruck_msgs/RawOdometry"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
uint32 tics_fl
uint32 tics_fr
uint32 tics_rl
uint32 tics_rr
float32 v_fl
float32 v_fr
float32 v_rl
float32 v_rr
float32 speed
float32 yawRate

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','tics_fl','tics_fr','tics_rl','tics_rr','v_fl','v_fr','v_rl','v_rr','speed','yawRate']
  _slot_types = ['std_msgs/Header','uint32','uint32','uint32','uint32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,tics_fl,tics_fr,tics_rl,tics_rr,v_fl,v_fr,v_rl,v_rr,speed,yawRate

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RawOdometry, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.tics_fl is None:
        self.tics_fl = 0
      if self.tics_fr is None:
        self.tics_fr = 0
      if self.tics_rl is None:
        self.tics_rl = 0
      if self.tics_rr is None:
        self.tics_rr = 0
      if self.v_fl is None:
        self.v_fl = 0.
      if self.v_fr is None:
        self.v_fr = 0.
      if self.v_rl is None:
        self.v_rl = 0.
      if self.v_rr is None:
        self.v_rr = 0.
      if self.speed is None:
        self.speed = 0.
      if self.yawRate is None:
        self.yawRate = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.tics_fl = 0
      self.tics_fr = 0
      self.tics_rl = 0
      self.tics_rr = 0
      self.v_fl = 0.
      self.v_fr = 0.
      self.v_rl = 0.
      self.v_rr = 0.
      self.speed = 0.
      self.yawRate = 0.

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4I6f.pack(_x.tics_fl, _x.tics_fr, _x.tics_rl, _x.tics_rr, _x.v_fl, _x.v_fr, _x.v_rl, _x.v_rr, _x.speed, _x.yawRate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.tics_fl, _x.tics_fr, _x.tics_rl, _x.tics_rr, _x.v_fl, _x.v_fr, _x.v_rl, _x.v_rr, _x.speed, _x.yawRate,) = _struct_4I6f.unpack(str[start:end])
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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4I6f.pack(_x.tics_fl, _x.tics_fr, _x.tics_rl, _x.tics_rr, _x.v_fl, _x.v_fr, _x.v_rl, _x.v_rr, _x.speed, _x.yawRate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.tics_fl, _x.tics_fr, _x.tics_rl, _x.tics_rr, _x.v_fl, _x.v_fr, _x.v_rl, _x.v_rr, _x.speed, _x.yawRate,) = _struct_4I6f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4I6f = struct.Struct("<4I6f")
_struct_3I = struct.Struct("<3I")
