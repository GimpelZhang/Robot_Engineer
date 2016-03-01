# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from monstertruck_msgs/Pdout.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Pdout(genpy.Message):
  _md5sum = "fffcd293bef6bed7b184d4f3834f37f4"
  _type = "monstertruck_msgs/Pdout"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
bool approaching_goal_point
float32 dt
float32 e_position
float32 de_position_dt
float32 e_angle
float32 de_angle_dt
float32 speed
float32 speed_real
float32 z_twist
float32 z_twist_real
float32 z_twist_deg
float32 z_twist_deg_real

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
  __slots__ = ['header','approaching_goal_point','dt','e_position','de_position_dt','e_angle','de_angle_dt','speed','speed_real','z_twist','z_twist_real','z_twist_deg','z_twist_deg_real']
  _slot_types = ['std_msgs/Header','bool','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,approaching_goal_point,dt,e_position,de_position_dt,e_angle,de_angle_dt,speed,speed_real,z_twist,z_twist_real,z_twist_deg,z_twist_deg_real

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Pdout, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.approaching_goal_point is None:
        self.approaching_goal_point = False
      if self.dt is None:
        self.dt = 0.
      if self.e_position is None:
        self.e_position = 0.
      if self.de_position_dt is None:
        self.de_position_dt = 0.
      if self.e_angle is None:
        self.e_angle = 0.
      if self.de_angle_dt is None:
        self.de_angle_dt = 0.
      if self.speed is None:
        self.speed = 0.
      if self.speed_real is None:
        self.speed_real = 0.
      if self.z_twist is None:
        self.z_twist = 0.
      if self.z_twist_real is None:
        self.z_twist_real = 0.
      if self.z_twist_deg is None:
        self.z_twist_deg = 0.
      if self.z_twist_deg_real is None:
        self.z_twist_deg_real = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.approaching_goal_point = False
      self.dt = 0.
      self.e_position = 0.
      self.de_position_dt = 0.
      self.e_angle = 0.
      self.de_angle_dt = 0.
      self.speed = 0.
      self.speed_real = 0.
      self.z_twist = 0.
      self.z_twist_real = 0.
      self.z_twist_deg = 0.
      self.z_twist_deg_real = 0.

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
      buff.write(_struct_B11f.pack(_x.approaching_goal_point, _x.dt, _x.e_position, _x.de_position_dt, _x.e_angle, _x.de_angle_dt, _x.speed, _x.speed_real, _x.z_twist, _x.z_twist_real, _x.z_twist_deg, _x.z_twist_deg_real))
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
      end += 45
      (_x.approaching_goal_point, _x.dt, _x.e_position, _x.de_position_dt, _x.e_angle, _x.de_angle_dt, _x.speed, _x.speed_real, _x.z_twist, _x.z_twist_real, _x.z_twist_deg, _x.z_twist_deg_real,) = _struct_B11f.unpack(str[start:end])
      self.approaching_goal_point = bool(self.approaching_goal_point)
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
      buff.write(_struct_B11f.pack(_x.approaching_goal_point, _x.dt, _x.e_position, _x.de_position_dt, _x.e_angle, _x.de_angle_dt, _x.speed, _x.speed_real, _x.z_twist, _x.z_twist_real, _x.z_twist_deg, _x.z_twist_deg_real))
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
      end += 45
      (_x.approaching_goal_point, _x.dt, _x.e_position, _x.de_position_dt, _x.e_angle, _x.de_angle_dt, _x.speed, _x.speed_real, _x.z_twist, _x.z_twist_real, _x.z_twist_deg, _x.z_twist_deg_real,) = _struct_B11f.unpack(str[start:end])
      self.approaching_goal_point = bool(self.approaching_goal_point)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B11f = struct.Struct("<B11f")
