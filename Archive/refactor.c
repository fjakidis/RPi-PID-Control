#include <stdio.h>

#define COUNTER		100		// in milliseconds
#define CYCLE		0.7

// Input pins for Hall sensors 
#define HALL_1  	2		
#define HALL_2  	4
#define HALL_3  	5	

// Numerical constants
#define A 		1
#define B 		2
#define C 		3

int main(){
   return 0;
}

void setup(){

   // Setup output pins
   // (?) Why is there four outputs and not 3?

   pinMode( 6, OUTPUT);
   pinMode( 9, OUTPUT);
   pinMode(10, OUTPUT);
   pinMode(11, OUTPUT);

   // Setup input pins
   pinMode(HALL_1, INPUT);
   pinMode(HALL_2, INPUT);
   pinMode(HALL_3, INPUT)

}

void loop(){}

void isr(){}

void motor(){}

void readingHull(){}