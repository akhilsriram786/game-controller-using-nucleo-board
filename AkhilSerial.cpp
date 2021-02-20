#include "mbed.h" //importing the header files

DigitalIn button1_press(PC_13); //Digitalin object for button

Serial pc(USBTX, USBRX); //serial object 

int button2_press=1; 
int button3_press=1;



int main()
        {
          button1_press.mode(PullUp);//configure the button with pull up resitor as  by default the the pins have to be configured as inputs with internal pull-up resistor.
          while(1)//infinite loop
          { 
           //buttons are active low which means when button is pressed the logic will be zero and when button is rleased the logic will be one 
           button2_press=button1_press; //assigning the value of digitalout buton to our variable akhilbutton1
           
           if(button2_press==0 && button3_press==1) //checking whether the value of akhilbutton2 is zero and akhilbutton3 is one
           {
            pc.printf("1");  //if both the operand are true it would return true and this statement will be executed i.e. i is printed on pc using serial communication which proves button is pressed
           }
           
           else if(button2_press==1 && button3_press==0)  // checking whether the value of akhilbutton2 is one and akhilbutton3 is zero
           {
            pc.printf("0");// if both the operands are true the button is released
           }
           button3_press=button2_press; //assigning the value 
           
           wait_ms (1); //wait for one millisecond
          }
        }   
          