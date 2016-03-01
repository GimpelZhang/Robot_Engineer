// Generated by gencpp from file monstertruck_msgs/Compass.msg
// DO NOT EDIT!


#ifndef MONSTERTRUCK_MSGS_MESSAGE_COMPASS_H
#define MONSTERTRUCK_MSGS_MESSAGE_COMPASS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace monstertruck_msgs
{
template <class ContainerAllocator>
struct Compass_
{
  typedef Compass_<ContainerAllocator> Type;

  Compass_()
    : header()
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , heading(0.0)
    , declination(0.0)  {
    }
  Compass_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , heading(0.0)
    , declination(0.0)  {
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _z_type;
  _z_type z;

   typedef float _heading_type;
  _heading_type heading;

   typedef float _declination_type;
  _declination_type declination;




  typedef boost::shared_ptr< ::monstertruck_msgs::Compass_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::monstertruck_msgs::Compass_<ContainerAllocator> const> ConstPtr;

}; // struct Compass_

typedef ::monstertruck_msgs::Compass_<std::allocator<void> > Compass;

typedef boost::shared_ptr< ::monstertruck_msgs::Compass > CompassPtr;
typedef boost::shared_ptr< ::monstertruck_msgs::Compass const> CompassConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::monstertruck_msgs::Compass_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::monstertruck_msgs::Compass_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace monstertruck_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'monstertruck_msgs': ['/home/somal/catkin_ws/src/monstertruck_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::monstertruck_msgs::Compass_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::monstertruck_msgs::Compass_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::monstertruck_msgs::Compass_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::monstertruck_msgs::Compass_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::monstertruck_msgs::Compass_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::monstertruck_msgs::Compass_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::monstertruck_msgs::Compass_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d008232f5b940b5db5ffc0e8b711366b";
  }

  static const char* value(const ::monstertruck_msgs::Compass_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd008232f5b940b5dULL;
  static const uint64_t static_value2 = 0xb5ffc0e8b711366bULL;
};

template<class ContainerAllocator>
struct DataType< ::monstertruck_msgs::Compass_<ContainerAllocator> >
{
  static const char* value()
  {
    return "monstertruck_msgs/Compass";
  }

  static const char* value(const ::monstertruck_msgs::Compass_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::monstertruck_msgs::Compass_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
float32 x\n\
float32 y\n\
float32 z\n\
float32 heading\n\
float32 declination\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::monstertruck_msgs::Compass_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::monstertruck_msgs::Compass_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.heading);
      stream.next(m.declination);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct Compass_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::monstertruck_msgs::Compass_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::monstertruck_msgs::Compass_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<float>::stream(s, indent + "  ", v.z);
    s << indent << "heading: ";
    Printer<float>::stream(s, indent + "  ", v.heading);
    s << indent << "declination: ";
    Printer<float>::stream(s, indent + "  ", v.declination);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MONSTERTRUCK_MSGS_MESSAGE_COMPASS_H
