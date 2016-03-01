; Auto-generated. Do not edit!


(cl:in-package motion_editor_core-msg)


;//! \htmlinclude ExecuteMotionCommand.msg.html

(cl:defclass <ExecuteMotionCommand> (roslisp-msg-protocol:ros-message)
  ((motion_name
    :reader motion_name
    :initarg :motion_name
    :type cl:string
    :initform "")
   (time_factor
    :reader time_factor
    :initarg :time_factor
    :type cl:float
    :initform 0.0))
)

(cl:defclass ExecuteMotionCommand (<ExecuteMotionCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecuteMotionCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecuteMotionCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name motion_editor_core-msg:<ExecuteMotionCommand> is deprecated: use motion_editor_core-msg:ExecuteMotionCommand instead.")))

(cl:ensure-generic-function 'motion_name-val :lambda-list '(m))
(cl:defmethod motion_name-val ((m <ExecuteMotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motion_editor_core-msg:motion_name-val is deprecated.  Use motion_editor_core-msg:motion_name instead.")
  (motion_name m))

(cl:ensure-generic-function 'time_factor-val :lambda-list '(m))
(cl:defmethod time_factor-val ((m <ExecuteMotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motion_editor_core-msg:time_factor-val is deprecated.  Use motion_editor_core-msg:time_factor instead.")
  (time_factor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecuteMotionCommand>) ostream)
  "Serializes a message object of type '<ExecuteMotionCommand>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'motion_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'motion_name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'time_factor))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecuteMotionCommand>) istream)
  "Deserializes a message object of type '<ExecuteMotionCommand>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motion_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'motion_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'time_factor) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecuteMotionCommand>)))
  "Returns string type for a message object of type '<ExecuteMotionCommand>"
  "motion_editor_core/ExecuteMotionCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteMotionCommand)))
  "Returns string type for a message object of type 'ExecuteMotionCommand"
  "motion_editor_core/ExecuteMotionCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecuteMotionCommand>)))
  "Returns md5sum for a message object of type '<ExecuteMotionCommand>"
  "baea61f0df386139ca78eeafc991b967")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecuteMotionCommand)))
  "Returns md5sum for a message object of type 'ExecuteMotionCommand"
  "baea61f0df386139ca78eeafc991b967")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecuteMotionCommand>)))
  "Returns full string definition for message of type '<ExecuteMotionCommand>"
  (cl:format cl:nil "# Execute motion via topic	~%string  motion_name	~%float32 time_factor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecuteMotionCommand)))
  "Returns full string definition for message of type 'ExecuteMotionCommand"
  (cl:format cl:nil "# Execute motion via topic	~%string  motion_name	~%float32 time_factor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecuteMotionCommand>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'motion_name))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecuteMotionCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecuteMotionCommand
    (cl:cons ':motion_name (motion_name msg))
    (cl:cons ':time_factor (time_factor msg))
))
