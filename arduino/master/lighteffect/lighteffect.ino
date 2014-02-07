#include <Wire.h>

#define LED_PIN 13 
byte x = 0; 

// ====================================================== 

void setup() 
{ 
Wire.begin(); // Start I2C Bus as Master 
pinMode(LED_PIN, OUTPUT); 
digitalWrite(LED_PIN, LOW); 
Serial.begin(9600);
} 

// ====================================================== 

void loop() 
{ 
//  //code to determine order  
//  for (int tennis = 0; tennis < 6; tennis++) {
//    turnOnShelf(tennis, 7);
//    delay(3000);
//  }
  int lamp = 0;
  
  
  while (true) {
    turnOffAll(7);
    delay(300);
    sendLightEffectUp(lamp, 7, 1000);  
    sendLightEffectDown(lamp, 7, 1000);
    lamp ++;
    lamp = lamp % 6;
    delay(1000);
  }
  digitalWrite(LED_PIN, HIGH);
  
  Serial.write("\nyes\n");
  
  //delay(1000);
  digitalWrite(LED_PIN, LOW);
  
  
  
} 

void sendLightEffectUp(int shelf, int billy, int duration) {
  
  int intensity = 0;
  int i = 0;
  do {
    Wire.beginTransmission(billy);
    Serial.print("\n");
    for (i = 0; i < 6; i++) {
      int distance = abs (shelf - i);
      int atten = min((distance * 60), 255);
      int value = max((intensity - atten), 0);
      Wire.write(value);
      Serial.print(value);
      Serial.print("\n");
    }
    intensity += 5;
    Wire.endTransmission(); 
  } while (intensity < 255);
}

void sendLightEffectDown(int shelf, int billy, int duration) {
  
  int intensity = 255;
  int i = 0;
  do {
    Wire.beginTransmission(billy);
    Serial.print("\n");
    for (i = 0; i < 6; i++) {
      if (shelf == i) {
        Wire.write(255);
      } else {
        int distance = abs (shelf - i);
        int atten = min((distance * 60), 255);
        int value = max((intensity - atten), 0);
        Wire.write(value);
        Serial.print(value);
        Serial.print("\n");
      }
    }
    intensity -= 5;
    Wire.endTransmission(); 
  } while (intensity > 0);
}


void turnOffAll(int billy) {
  Wire.beginTransmission(billy);
  for (int i = 0; i < 6; i++) {
    Wire.write(0);      
  } 
  Wire.endTransmission(); 
}

void turnOnShelf(int j, int billy) {
  Wire.beginTransmission(billy);
  for (int i = 0; i < 6; i++) {
    if (i == j) {
      Wire.write(0);    
    } else {
      Wire.write(255);
    }  
  } 
  Wire.endTransmission(); 
}
