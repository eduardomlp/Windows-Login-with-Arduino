#include <MFRC522.h>
#include <SPI.h>

//Configuracoes de pinos do sensor RFID
#define SS_PIN 10
#define RST_PIN 9
MFRC522 rfidSensor(SS_PIN, RST_PIN);

void setup(){
  Serial.begin(9600);
  SPI.begin();
  rfidSensor.PCD_Init();
}

void loop(){
  if(!rfidSensor.PICC_IsNewCardPresent()){
    return;
  }

  if(!rfidSensor.PICC_ReadCardSerial()){
    return;
  }

  String conteudo = "";

  for(byte i = 0; i < rfidSensor.uid.size; i++){
    conteudo.concat(String(rfidSensor.uid.uidByte[i] < 0x10 ? " 0" : " "));
    conteudo.concat(String(rfidSensor.uid.uidByte[i], HEX));
  }

  conteudo.toUpperCase();

  //Hexadecimal abaixo eh o codigo do chaveiro
  if(conteudo == " A4 81 18 EB" || conteudo == " FB 03 F1 03"){
    Serial.println("True");
  }
  else{
    Serial.println("False");
  }
}


