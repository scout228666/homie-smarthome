#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
#include <config.h>

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

bool readSensor(float &temp, float &humidity){
    temp = dht.readTemperature();
    humidity = dht.readHumidity();

    if(isnan(temp) || isnan(humidity)){
        return false;
    }
    return true;
}

void connectWiFi(){
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    while(WiFi.status() != WL_CONNECTED){
        delay(500);
    }
}

int postData(float &temp, float &humidity){
    if(!readSensor(temp, humidity)) return 1;

    if(WiFi.status() == WL_CONNECTED){
        HTTPClient http;
        http.begin(SERVER_URL_POST);
        http.addHeader("Content-Type", "application/json");

        String body = "{\"temperature\":" + String(temp) + 
                      ",\"humidity\":" + String(humidity) + "}";

        int code = http.POST(body);
        if(code <= 0) return 2;
        Serial.println("Response: " + String(code));
        http.end();
  }
  else return 2;
  return 0;
}