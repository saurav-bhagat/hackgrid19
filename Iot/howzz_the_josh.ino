#include "ThingSpeak.h"
#include <ESP8266WiFi.h>
const char* ssid     = "Tyrion";
const char* password = "motherfucker";
 
unsigned long channel = 725175;
 

unsigned int led1 = 1;
unsigned int led2 = 2;
 
WiFiClient  client;
 
 
void setup() {
  Serial.begin(115200);
  delay(100);
  
  pinMode(D0, OUTPUT);
  pinMode(D2, OUTPUT);
  digitalWrite(D0, 0);
  digitalWrite(D2, 0);
 
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Netmask: ");
  Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());
  ThingSpeak.begin(client);
 
}

 
void loop() {

  int led_1 = ThingSpeak.readFloatField(channel, led1);
  int led_2 = ThingSpeak.readFloatField(channel, led2);

  if(led_1 == 1){
    digitalWrite(D0, 1);
    Serial.println("D0 is On..!");
  }
  else if(led_1 == 0){
    digitalWrite(D0, 0);
    Serial.println("D0 is Off..!");
  }

  if(led_2 == 1){
    digitalWrite(D2, 1);
    Serial.println("D2 is On..!");
  }
  else if(led_2 == 0){
    digitalWrite(D2, 0);
    Serial.println("D2 is Off..!");
  }

  Serial.println(led_1);
  Serial.println(led_2);
  delay(5000);

}

