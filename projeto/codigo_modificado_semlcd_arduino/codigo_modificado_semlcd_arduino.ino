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

void piscaum(int tempo){
  digitalWrite(LED_BUILTIN, HIGH);
  delay(int(tempo/2));
  digitalWrite(LED_BUILTIN, LOW);
  delay(int(tempo/2));
}

void piscaN(int N, int tempo){
  for (int i =0; i < N; i++) piscaum(tempo);
}

void setup() {
    Serial.begin(115200); // Inicializa a comunicação serial

    // configura led do arduino
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
    piscaN(5,100); // pisca 5 vezes para sabe que configurou o led

    bool encontrou = false;
    while (!encontrou) {
        
        delay(500);
        encontrou = particleSensor.begin(Wire);
        piscaN(1,500);
        if (!encontrou) piscaN(1,500);
    }
    //Serial.println("Coloque seu dedo");
    piscaN(10,100);

    delay(1000);
    particleSensor.setup();
    particleSensor.setPulseAmplitudeRed(0x0A);
    particleSensor.setPulseAmplitudeGreen(0);

    lastBeat = millis();
    ultimoenvio = millis();
    //Serial.println("Começando a monitorar...");
    piscaN(3,500);
}

void loop() {
    long irValue = particleSensor.getIR();

    //Serial.print("irValue = ");
    //Serial.println(irValue);

    if (checkForBeat(irValue) == true) {
        long delta = millis() - lastBeat;
        lastBeat = millis();

        piscaN(1,100);

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
    if (deltaenvio >= 500){
      ultimoenvio = millis();
      // Envia os dados via Serial no formato CSV: IR,BPM
      if (irValue < 50000) {
        // Não tem dedo...
          Serial.println(0);
      } else {
        // tem dedo...
          Serial.println(beatAvg);
      }
    }

    //Serial.println(irValue);

    //delay(1); // ajuste delay para não sobrecarregar serial
}
