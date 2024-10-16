#include <Wire.h> //I2C tvåtrådskommunikationen
#include <VL53L0X.h> //Hämtar bibliotek till avståndssensor VL53L0X
// importerar adafruit
#include <Adafruit_GFX.h> 
#include <Adafruit_SSD1306.h> 
 
VL53L0X sensor; //skapar en instans av klassen
Adafruit_SSD1306 display(128, 64, &Wire, -1, 400000UL, 100000UL); // definierar displayen.
 
#define InputPin D5 //definierar IO13 som InputPin, kopplad till pinne D7
 
bool ButtonState; //definierar tryckknappen som bool,
int SensorDistance; //Talar om att variabeln SensorDistance är en heltalsvärde
byte LastSpeed = 0; //Första hastigheten
byte MotorSpeed = 5; //Definerar variabel för motorns hastighet och kopplar den till pinne 5
byte MotorDir = 0; //Definerar variabel för motorns riktning och kopplar den till pinne 0
 
typedef enum States //Definerar olika tillstånd 
{
  Init,
  Stopp,
  Fram,
  Back,
};
 
States State, LastState; //Olika lägen för tillstånden
 
// definierar displayDistance så att den kan användas senare. PGA att koden ska veta vad displayDistance är måste den vara definierad tidigare i koden.
void displayDistance(String StateStr, bool isForward = false);
 
void setup() { //körs en gång i början av programmet
  Serial.begin(9600); //Kommunikation med serial monitor
  Wire.begin(D7, D6); //IO 14 = pinne D5 till SDA, IO 12 = pinne D6 kopplas till SCL
  delay(2000); //Väntar 2 sekunder
  display.begin(SSD1306_SWITCHCAPVCC, 0X3C); //0x3C är adressen
  delay(3000);//väntar 3 sek
  display.clearDisplay(); //tar bort gammalt skräp
  display.setTextColor(WHITE);//displayen är på/tänd
  display.setCursor(0, 8); // sätter cursorn, där något ska skrivas till kordinaten (0,8)
  delay(1000); // väntar 1 sek
 
  State = Init; // Läget är init i början
  LastState = Init; // Det senaste läget är lika med init
 
  pinMode(MotorSpeed, OUTPUT);//MotorSpeed är en digitalutgång
  pinMode(MotorDir, OUTPUT);//MotorDir är en digitalutgång
 
 
  analogWrite(MotorSpeed, 0); //Motorn börjar med värdet 0 dvs av.
 
  sensor.setTimeout(500); // väntar 500 millisekunder
  if (!sensor.init()) { // om sensorn inte finns och inte är definierad körs detta
    Serial.println("Failed to detect and initialize sensor!"); // skrivs att sensorn inte finns
    while (1) {} // fastnar i evig while loop
  }
  sensor.startContinuous();
}
 
void loop() { //upprepar händelsen
  ButtonState = digitalRead(InputPin); //läser av signalen, noll eller ett, på input pin
  // Debugging: Visa knappens status
  Serial.print("ButtonState: ");
  Serial.println(ButtonState);
  switch (State) { //switch byter mellan olika case, kan inte köra flera samtidigt
    case Init: //startläge, väntar på knapptryck för att starta
      display.clearDisplay(); //rensar skärmen
      display.setTextSize(2); // Större fontstorlek, du kan öka om du vill ha större
      display.setCursor(35, 24); // Centrera texten på skärmen (ungefär)
      display.println("Start?"); // Visa "Start?"
      display.display(); //visar det som finns i minnet
      display.setTextSize(1); // Sätt tillbaka till normal storlek efteråt
      if (ButtonState) { // Knappen nedtryckt (LOW på grund av pull-up resistor)
        State = Stopp;
        Serial.println("Knappen tryckt, gå till Stopp-läge!");
      }
      break; //avslutar case init
 
    case Stopp: //Stannar motorn
      display.clearDisplay(); //rensar
      display.display(); //visar
      getDistance(); //hämtar avstånd
      displayDistance("Stopp"); //Visar avstånd
      delay(500); //väntar en halv sekund
      Motor_1(0, 1); 
      delay(500);//vänta 0,5s
      if (SensorDistance > 320 && SensorDistance < 2000) { // interval för att den ska börja köra framåt igen. 
        State = Fram; // sätt läge till fram.
      }
      if (SensorDistance < 280) { // interval för backande.
        State = Back; // sätt läge till back.
      }
      break;
 
    case Fram: //kör motorn framåt
      display.clearDisplay(); // tömmer displayen från gammalt skräp
      display.display(); // visar
      getDistance(); //hämtar och visar avstånd
      displayDistance("Kor framat", true); //Visar pil nedåt
      Motor_1(100, 10); // kör motorn
      delay(500);
      if (!(SensorDistance > 320)) { // interval stop från fram.
        State = Stopp;
      }
      break;
    case Back: //backar motorn
      display.clearDisplay();
      display.display();
      getDistance(); //hämtar avstånd
      displayDistance("Backar", false); //Visar avstånd och pil uppåt
      Motor_1(100, 10); // kör motorn.
      delay(500);
      if (!(SensorDistance < 280)) { // interval stop från back
        State = Stopp;
      }
      break;
  }
}
 
void getDistance() { // få distansen så den är definierad. Skriver även ut den till Serial display för debugging.
  SensorDistance = (sensor.readRangeContinuousMillimeters()) ; 
  Serial.print("Distance: ");
  Serial.println(SensorDistance); 
}
 
void displayDistance(String StateStr, bool isForward) { 
  display.clearDisplay(); // töm gammalt skräp från display
  display.print("Avstand: ");  // skriv avstånd
  display.println(SensorDistance); // därefter hur långt den har kommit
  display.println(StateStr); // läget den är i.
  display.setCursor(0, 8); 
  // Beroende på riktningen visas en pil upp eller ner eller en stoppskylt
  if (StateStr == "Stopp") { // Om den stannar
    display.drawRect(110, 0, 18, 18, WHITE); // Ritar en stoppskylt
    display.setCursor(113, 5); 
    display.print("S");
  } else if (isForward) { // om den kör framåt:
    display.fillTriangle(100, 20, 110, 40, 120, 20, WHITE); // Pilen pekar ned (fram)
  } else { // om den inte kör framåt:
    display.fillTriangle(100, 40, 110, 20, 120, 40, WHITE); // Pilen pekar up (bak)
  }
  display.display (); // visa
}
 
void Motor_1(byte NewSpeed, long Step ) {
  if (State != LastState) { // om statet har ändrats. För att se till att motorn skripten inte körs flera gånger.
    NewSpeed = map(NewSpeed, 0, 100, 0, 255); // definierar nya hastigheten
    LastState = State; // sätter statesen till samma för att stoppa körning igen.
    switch (State) {  // går igenom state en efter en.
      case Init:
        break;
      case Stopp: // om stopp
        for (byte Speed = LastSpeed + 1 ; Speed <= NewSpeed; Speed -= 1) {
          analogWrite(MotorSpeed, Speed);
          delay(Step);
        }
        break;
      case Fram: // om fram
        digitalWrite(MotorDir, HIGH);
        for (short Speed = LastSpeed; Speed <= NewSpeed; Speed += 1) {
          analogWrite(MotorSpeed, Speed);
          delay(Step);
        }
        break;
      case Back: // om back
        digitalWrite(MotorDir, LOW);
        for (short Speed = LastSpeed; Speed <= NewSpeed; Speed += 1) {
          analogWrite(MotorSpeed, Speed);
          delay(Step);
        }
        break;
    }
    LastSpeed = NewSpeed; // inkrementerar den nya hastigheten. 
  }
}