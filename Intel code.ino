#include <Wire.h>
#include "rgb_lcd.h"
#define len 5

char out[len];
rgb_lcd lcd;

int notifier_pin = 9;
FILE *fromarduino;

int wheel[len] = {6, 5, 4, 8, 2}; // IR reflective sensors attached to these pins
int inverted[len] = {1, 1, 1, 0, 1}; // On default position, does the sensor led glow? (depends on the way you have labelled the characters
int button = 7;
int wheel_state[len];
int wheel_state_prev[len];
int letter_code[len];

int speakerPin = 3;

void setup() {
  for (int i = 0; i < len; i++)
  {
    pinMode(wheel[i], INPUT);
    wheel_state[i] = digitalRead(wheel[i]);
    wheel_state_prev[i] = wheel_state[i];
    letter_code[len] = 0;
  }
  pinMode(button, INPUT);
  pinMode(speakerPin, OUTPUT);
  pinMode(notifier_pin, OUTPUT); //Notification pin trigger

  lcd.begin(16, 2);
  lcd.print("**hello world!**");

  //Serial.begin(115200);
}

void loop() {
  check_position(); // checks if there is any motion and updates the array letter_code
  if (digitalRead(button))
  {
    output();
    delay(100);
  }
  //dumb_check();
}

void check_position()
{
  for (int i = 0; i < len; i++)
  {
    wheel_state_prev[i] = wheel_state[i];
    wheel_state[i] = !digitalRead(wheel[i]);
  }
  for (int i = 0; i < len; i++)
  {
    if (wheel_state[i] == !inverted[i] && wheel_state_prev[i] == inverted[i])
    {
      letter_code[i]++;
      output();
      playNote('g', 50);
    }
    while (letter_code[i] > 26) //27 chars
    {
      letter_code[i] -= 27;
    }
  }
}

// Push the characters to Serial, LCD and a text-file for later processing
void output()
{
  for (int i = 0; i < len; i++)
  {
    if (letter_code[i] == 0)
    {
      out[i] = ' ';
    }
    else
    {
      out[i] = (char)letter_code[i] + (char)96;
    }
  }

  lcd.clear();
  lcd.print("*****");
  for (int i = 0; i < len; i++)
  {
    Serial.print(out[i]);
    lcd.write(out[i]);
  }
  lcd.print("******");
  Serial.println();
  publishData();
  notifyWorld();
  playNote('cgh', 150);
}

void dumb_check()
{
  for (int i = 0; i < len; i++)
  {
    if (inverted[i])
      Serial.print(!digitalRead(wheel[i]));
    else
      Serial.print(digitalRead(wheel[i]));
  }
  Serial.println();
}

void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(char note, int duration) {
  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };

  // play the tone corresponding to the note name
  for (int i = 0; i < 8; i++) {
    if (names[i] == note) {
      playTone(tones[i], duration);
    }
  }
}

void publishData()
{
  fromarduino = fopen ("/arduino_notification_out.txt", "w+");
  for (int i = 0; i < len; i++)
  {
    fprintf(fromarduino, "%c", out[i]);
  }
  fclose(fromarduino);
}

//Nofity any body connected to this interrupt, so that they can
void notifyWorld()
{
  digitalWrite(notifier_pin, HIGH);
  delay(200);
  digitalWrite(notifier_pin, LOW);
}
