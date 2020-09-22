
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
int kp=1;
int ki=1;
int kd=1;
float error;
float time;
float timediff;
float ptime;
float pid;
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

  prin=initial-inal

  serial.print("angleX :");
  serial.print(prin);
  error=inal-initial;
  prp=kp*error;
  integ=kd*timediff*error;
  deriv=kd*(error/timediff);
  pid=prp+integ+deriv;

    int signal =pid;

  servo.writeMicroseconds(pid);
}
