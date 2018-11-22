int x;
#include <SoftwareSerial.h>
additional Genotronex(10, 11);
void setup() {
  // put your setup code here, to run once:
  additional.begin(9600);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  x=additional.read();
  if (x=='1'){
    digitalWrite(3,HIGH);
    
  }
  else if (x=='2'){
    digitalWrite(3,LOW);
  }
  else if (x=='3'){
    digitalWrite(4,HIGH); 
  }
 else if (x=='4'){
  digitalWrite(4,LOW);
 }
 else if (x=='5'){
  digitalWrite(5,HIGH);
 }
 else if (x=='6'){
  digitalWrite(5,LOW);
 }
 else if (x=='7'){
  digitalWrite(6,HIGH);
 }
 else if(x=='8'){
  digitalWrite(6,LOW);
 }  
 delay(10);
}
