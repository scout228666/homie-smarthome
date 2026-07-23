#include <Arduino.h>
#include <dht_sensor.h>


void setup() {
  Serial.begin(115200);
  dht.begin();

  connectWiFi();
}

void loop() {
   float temp, humidity;
  int code = postData(temp, humidity);

  if(code == 1){ 
    Serial.println("DHT read failed");
    delay(500);
  }
  else if(code == 2){
     Serial.println("POST-request failed");
     delay(500);
  }

  Serial.println("Temp: " + String(temp));
  Serial.println("Hum: " + String(humidity));
  
  delay(10000);
}