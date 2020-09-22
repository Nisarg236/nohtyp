
#include <MPU6050_tockn.h>
#include <Wire.h>

MPU6050 mpu6050(Wire);
#include <Servo.h>

byte servoPin = 9;
Servo servo;

float initial;
float inal;
float prin;
float prp;
float integ;
float deriv;
float kp=0.01;
float ki=0.001;
float kd=0.001;
float error;
float time;
float timediff;
float ptime;
float pid;
int signal;
int throttle=1500;
void setup() {
  servo.attach(servoPin);

  servo.writeMicroseconds(1500);

  delay(7000); 
  Serial.begin(9600);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  mpu6050.update();
  initial=mpu6050.getAngleX();
}

void loop() {
  ptime=time;
  time=millis();
  timediff=time-ptime;
  mpu6050.update();
  inal=mpu6050.getAngleX();

  prin=initial-inal;

  Serial.print("angleX :");
  Serial.print(prin,0);
  Serial.print("  ");
  error=inal-initial;
  prp=kp*error;
  integ=(kd*timediff*error)+integ;
  deriv=kd*(error/timediff);
  pid=prp+integ+deriv;
  signal=throttle+pid;
  if(signal<=1100)
  {
    signal=1100;
  }
  if(signal>=1900)
  {
    signal=1900;
  }
 

  servo.writeMicroseconds(signal);
  Serial.print("pid=");
  Serial.print(pid);
  Serial.print("  ");
  Serial.println(signal);
}
