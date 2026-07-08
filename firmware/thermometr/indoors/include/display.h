#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setDisplay(int size, uint16_t color){
    display.clearDisplay();
    display.setTextSize(size);
    display.setTextColor(color);
}

void printRow(int x, int y, String text){
    display.setCursor(x, y);
    display.print(text);
}