//char serialData;
//int pin=13;



void setup() {

  Serial.begin(9600);
//  pinMode(pin,OUTPUT);
  
}

void loop() {
//  if(Serial.available() > 0)
//  serialData = Serial.read();
//  Serial.println(serialData);

  Serial.println("Hello from arduino!");
  


//  if(serialData == '1'){
//  digitalWrite(pin,HIGH);
//  }
//
//  else if(serialData == '0'){
//  digitalWrite(pin,LOW);
//  }

  delay(1000);
  
}
