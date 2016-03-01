// Generated by gencpp from file monstertruck_msgs/ServoPositions.msg
// DO NOT EDIT!


#ifndef MONSTERTRUCK_MSGS_MESSAGE_SERVOPOSITIONS_H
#define MONSTERTRUCK_MSGS_MESSAGE_SERVOPOSITIONS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <monstertruck_msgs/ServoPosition.h>

namespace monstertruck_msgs
{
template <class ContainerAllocator>
struct ServoPositions_
{
  typedef ServoPositions_<ContainerAllocator> Type;

  ServoPositions_()
    : servo()  {
    }
  ServoPositions_(const ContainerAllocator& _alloc)
    : servo(_alloc)  {
    }



   typedef std::vector< ::monstertruck_msgs::ServoPosition_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::monstertruck_msgs::ServoPosition_<ContainerAllocator> >::other >  _servo_type;
  _servo_type servo;




  typedef boost::shared_ptr< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> const> ConstPtr;

}; // struct ServoPositions_

typedef ::monstertruck_msgs::ServoPositions_<std::allocator<void> > ServoPositions;

typedef boost::shared_ptr< ::monstertruck_msgs::ServoPositions > ServoPositionsPtr;
typedef boost::shared_ptr< ::monstertruck_msgs::ServoPositions const> ServoPositionsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::monstertruck_msgs::ServoPositions_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace monstertruck_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'monstertruck_msgs': ['/home/somal/catkin_ws/src/monstertruck_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "58f4f4c70dfb67bb7c1c5f32abf2a35a";
  }

  static const char* value(const ::monstertruck_msgs::ServoPositions_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x58f4f4c70dfb67bbULL;
  static const uint64_t static_value2 = 0x7c1c5f32abf2a35aULL;
};

template<class ContainerAllocator>
struct DataType< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "monstertruck_msgs/ServoPositions";
  }

  static const char* value(const ::monstertruck_msgs::ServoPositions_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ServoPosition[] servo\n\
\n\
================================================================================\n\
MSG: monstertruck_msgs/ServoPosition\n\
uint8 id\n\
float32 position\n\
";
  }

  static const char* value(const ::monstertruck_msgs::ServoPositions_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.servo);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct ServoPositions_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::monstertruck_msgs::ServoPositions_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::monstertruck_msgs::ServoPositions_<ContainerAllocator>& v)
  {
    s << indent << "servo[]" << std::endl;
    for (size_t i = 0; i < v.servo.size(); ++i)
    {
      s << indent << "  servo[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::monstertruck_msgs::ServoPosition_<ContainerAllocator> >::stream(s, indent + "    ", v.servo[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MONSTERTRUCK_MSGS_MESSAGE_SERVOPOSITIONS_H
