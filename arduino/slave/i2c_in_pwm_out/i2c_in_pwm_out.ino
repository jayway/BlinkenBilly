/*
 Read 6 bytes over i2c, and write them to the PWM pins.
 
 */
 
#include <Wire.h>

void setup()  { 
  // declare pin 9 to be an output:
 
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(13, OUTPUT); // status LED
  // start i2c stuff 
  Wire.begin(7); // My address...hardwired for now
  Wire.onReceive(receiveEvent);
} 


void receiveEvent(int howmany){
  if(howmany==6) {
    digitalWrite(13,HIGH);
    analogWrite(3, Wire.read());
    analogWrite(5, Wire.read());
    analogWrite(6, Wire.read());
    analogWrite(9, Wire.read());
    analogWrite(10, Wire.read());
    analogWrite(11, Wire.read());
  } else {
    // Indicate error by blinking status LED faster
    for(int i =0; i<10; i++) {
      digitalWrite(13,HIGH);
      delay(200);
      digitalWrite(13,LOW);
      delay(200);
    }
  }
}

// Show signs of life by blinking status LED
void loop()  {
  digitalWrite(13, HIGH);
  delay(2000);  
  digitalWrite(13, LOW);
  delay(2000);
}

