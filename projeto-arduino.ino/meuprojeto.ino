#include <Arduino.h>

class Led {
  private:
    int pin;
    bool status;

  public:
    Led(int p) {
      pin = p;
      status = false;
    }

    void setup() {
      pinMode(pin, OUTPUT);
      digitalWrite(pin, LOW);
    }

    void toggle() {
      status = !status;
      digitalWrite(pin, status ? HIGH : LOW);
    }

    bool check() {
      return status;
    }
};

Led debugLed(13);

void setup() {
  debugLed.setup();
  Serial.begin(9600);
}

void loop() {
  debugLed.toggle();
  
  if (debugLed.check()) {
    Serial.println("LIGADO");
  } else {
    Serial.println("DESLIGADO");
  }

  delay(1000);
}