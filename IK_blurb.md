
The goal of the project was to assemble an afforable quadraped robot resembling a dinosaur of our choosing (we chose to go with an ankylosaurus). In order to accomplish this, we decided to base our design on boston dynamics mini. For the leg configuration, we went with a 5 bar linkage system powered by two servo motors allowing. 

<img width="2560" height="1050" alt="image" src="https://github.com/user-attachments/assets/d274e875-c86d-4281-b567-3048727c61d6" />

In order to to find the necceary angle/postion of the servo motors at each postion of the walking gait, inverse kinematic equations needed to be derived. These equations will then implemented into a python script and used to program to final animatronic (which will be complete by the end of april 2026, stay tuned). This is a very brief and high level explination of the inverse kinamatic equations used, more details can be found in the python script located in this repository. 

<img width="1957" height="1100" alt="Screenshot 2026-03-07 at 2 52 42 PM" src="https://github.com/user-attachments/assets/befd911c-956b-4b85-a4f6-00d5c0c2468c" />

This diagram now presents a high level overiew of that python script

![4MathFunctions](https://github.com/user-attachments/assets/8374171a-105b-447a-8faf-97ef3029f9f7)

This script was designed to help us analyize the walking gait and verify our inverse kinamatic equations, thus we used our calculated values to make an animation of the leg to ensure no erratic motion or linkage resizing was taking place. Final version of the code will out put andgles or positions for the motors. 

This is the output of animation of the script

<img width="385" height="399" alt="image" src="https://github.com/user-attachments/assets/7f424f66-fc07-4534-8f34-043945d76193" />

We also programed another verion in which the knee is facing bacwards in order to ensure the ability to fully resemble the ankylosaurus, whoose knees foaward and hind knees faced each other. 

<img width="372" height="399" alt="image" src="https://github.com/user-attachments/assets/2556e077-9b10-4f94-bef4-098d49e2643e" />

<img width="1600" height="800" alt="image" src="https://github.com/user-attachments/assets/01d14e40-9377-4f74-bd8d-a48926ccc480" />

Further analysis of the walking gait will be conducted once parts are ordered and delivered and a version one of the final product (in this case final prototype as the scope of the project only goes as far as proving the capability of making a budget friendly walkng quardraped) is built. Comparison between the legs physical actions and expected actions will be compared in order to further adjust and improve the python script.
