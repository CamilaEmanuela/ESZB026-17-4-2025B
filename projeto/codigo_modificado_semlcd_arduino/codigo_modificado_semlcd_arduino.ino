#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"

MAX30105 particleSensor;

const byte RATE_SIZE = 4;
byte rates[RATE_SIZE];
byte rateSpot = 0;
long lastBeat = 0;
float beatsPerMinute;
int beatAvg;

long ultimoenvio;

void setup() {
    Serial.begin(115200); // Inicializa a comunicação serial
    Serial.println("Começando...");
    bool encontrou = particleSensor.begin(Wire, I2C_SPEED_FAST);
    Serial.println("testou...");
    
    while (!encontrou) {
        Serial.println("Sensor nao encontrado");
        delay(1000);
        encontrou = particleSensor.begin(Wire, I2C_SPEED_FAST);
        //while(1);
    }
    Serial.println("Coloque seu dedo");
    delay(1000);
    particleSensor.setup();
    particleSensor.setPulseAmplitudeRed(0x0A);
    particleSensor.setPulseAmplitudeGreen(0);

    ultimoenvio = millis();
}

void loop() {
    long irValue = particleSensor.getIR();

    if (checkForBeat(irValue) == true) {
        long delta = millis() - lastBeat;
        lastBeat = millis();

        beatsPerMinute = 60 / (delta / 1000.0);

        if (beatsPerMinute < 255 && beatsPerMinute > 20) {
            rates[rateSpot++] = (byte)beatsPerMinute;
            rateSpot %= RATE_SIZE;

            beatAvg = 0;
            for (byte x = 0; x < RATE_SIZE; x++)
                beatAvg += rates[x];
            beatAvg /= RATE_SIZE;
        }
    }


    long deltaenvio = millis() - ultimoenvio;
    if (deltaenvio >= 1000){
      ultimoenvio = millis();
      // Envia os dados via Serial no formato CSV: IR,BPM
      if (irValue < 50000) {
        // Não tem dedo...
          //Serial.println(String(irValue) + ",0"); // 0 para BPM indica "sem dedo"
          Serial.println(0);
      } else {
        // tem dedo...
          //Serial.println(String(irValue) + "," + String(beatsPerMinute, 1));
          Serial.println(beatsPerMinute);
      }
    }

    //Serial.println(irValue);

    //delay(1); // ajuste delay para não sobrecarregar serial
}
