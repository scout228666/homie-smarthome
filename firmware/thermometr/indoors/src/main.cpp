#include <Arduino.h>
#include <config.h>
#include <dht_sensor.h>
#include <display.h>
#include <ArduinoJson.h>
#include <HTTPClient.h> 

int getData(float &outside_temp, float &outside_humidity){
    outside_humidity = 0.0, outside_temp = 0.0;
    if(WiFi.status() == WL_CONNECTED){
      HTTPClient http_get;
      http_get.begin(SERVER_URL_GET);
      int response_code = http_get.GET();
    

      if(response_code > 0){
        String response = http_get.getString();
        JsonDocument doc;
        deserializeJson(doc, response);
        outside_temp = doc["temperature"];
        outside_humidity = doc["humidity"];
      }
      else return 2;
  }
  else return 1;
  return 0;
}
 
void isValid(int code){
  if(code == 1){ 
    Serial.println("DHT read failed");
    delay(500);
  }
  else if(code == 2){
     Serial.println("POST-request failed");
     delay(500);
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  connectWiFi();

  if(!display.begin(SSD1306_SWITCHAPVCC, 0x3C)){
    for(;;);
  }
  setDisplay(1, WHITE);
}

void loop() {

  float inside_temp, inside_humidity;
  int code = postData(inside_temp, inside_humidity);
  isValid(code);

  float outside_temp, outside_humidity;
  code = getData(outside_temp, outside_humidity);
  isValid(code);

  printRow(0, 0, "Inside: " + String(inside_temp, 1) + (char)247 + "C");
  printRow(0, 12, "Outside: " + String(outside_temp, 1) + (char)247 + "C");
  printRow(0, 24, "Humidity: " + String(outside_humidity, 0) + "%");
  display.display();

  delay(300000); // 5 minutes
}