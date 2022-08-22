int ledPin = 12;




void setup() {

  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin,LOW);

  Serial.begin(9600); 
}

void loop() {

  char readData = 0;

  if(Serial.available()){
    readData = Serial.read();


    switch(readData){

      case 'A': digitalWrite(ledPin,HIGH);
//                delay(1000);
                break;

      case 'B': digitalWrite(ledPin,LOW);
//                delay(1000);
                break;

      default:
                break;
    }
  }
}
