# Cad Design

### Cycloidal Drive / Gearbox

Our originial designs were inspired by other quadrapedal robots we found online from the likes of [Aaed Musa](https://www.youtube.com/watch?v=8s9TjRz01fo&t=389s) and [James Bruton](https://www.youtube.com/watch?v=yXA_KeuYpCY&t=652s). These quadrepeds were pretty big and used very robust motors. Our plans were to immitate this style of quadreped with stepper motors and a custom gear box assembly, however we were later advised (and rightfully so) to scale the design back as the stepper motors added a significant amount of weight not only by themselves, but also in the controllers neccesary to run them and the big batterys needed to power them. We then pivoted to sizing the robot down to only about a foot in length and standing height, and using servo motors. Non the less, i felt that my original gear box prototype was worthy of an inclusion here. 

![Dimensioned mini cyclodial drawing](https://github.com/user-attachments/assets/740f0745-6404-4880-96f8-17650750c524)

In order to design these disks I made a crude function in JAVA to derive the parametric equations defining the shape of the disks. It also calculated the necessary hole diameter based on the size of the disk and the size of the output shafts. The full JAVA script will be included in this repository. The calculations were based on information provided by [StepByStep Robotics](https://stepbystep-robotics.com/hp/robots/cycloidal-drive/)  and [tec science](https://www.tec-science.com/mechanical-power-transmission/planetary-gear/construction-of-the-cycloidal-disc/)


<img width="1392" height="1056" alt="Screenshot 2026-03-09 at 11 43 53 AM" src="https://github.com/user-attachments/assets/8067dbb2-c63e-4eff-8b99-7bf89edc2b1b" />

These calculations were then inputed into solid works (becuase it was more convinent that dealing with fusion plug ins) and exported out and into the fusion file where the output shaft holes were cut.

<img width="1902" height="1130" alt="image" src="https://github.com/user-attachments/assets/99e75163-90b3-4667-9ad1-df43fc9c5ebd" />

I then printed out a couple of components to ensure sizing and fit with motor and bearing. Upon printing concerns were raised about the strength of the eccentric cam as certain portion proved too small for g code to compute. This resulted in portions of it not printing, however the cam did fit and output shaft of the motor and worked for sizing purposes. The strength of the guiding pins and output pins were also a cuase for concern as they had been printed vertically resulting in perpendicular print layers susceptible to shear faliures. I planed to aleviate the shear stress in at the base of these pins by filetting the edges resulting in more surface areas in theses regions and lowering shrear stress, however the gearbox solution was scraped before more iterations could be made. 

<img width="1207" height="930" alt="IMG_3646 jpeg" src="https://github.com/user-attachments/assets/c5b956dd-715e-4909-a99f-709176224be8" />
<img width="1736" height="1049" alt="IMG_3644 jpeg" src="https://github.com/user-attachments/assets/4e22edf7-7327-413f-83c0-1f61540b2404" />

![IMG_3645](https://github.com/user-attachments/assets/767527dd-118c-41e6-9ee1-c5f52c6858e8)

![IMG_3643](https://github.com/user-attachments/assets/3624ccdf-f43e-4925-9f96-af229087f961)

![IMG_3647](https://github.com/user-attachments/assets/1245d605-3aaf-4163-9513-163fc60c274a)

From these experience I had become very comforatable with the fusion workflow and my bambu lab slicer. These skill would cary foward into the next iteration of our animatronic's design. 

### 5 Bar linkage system 

When we pitvoted to the smaller size, I decided that the easiest course of action was to attach the motors dirctly to the joints of the new leg design. Our first design and prototype was promising after printing

![OG paw linkage](https://github.com/user-attachments/assets/894c5463-939d-45d6-a9b7-54351a2d3dbc)

![IMG_3618](https://github.com/user-attachments/assets/ab64c9ba-8fd9-4577-9754-b3b919c6394d)
![IMG_3617](https://github.com/user-attachments/assets/58bb5a38-e2d5-432b-b903-c49bbd98d8d6)

Note that the input shafts were still being design for stepper motors as that is what we had on hand to test with. More on the inverse kinamatics of the project and how we will control the movements in the IK.md sectino of this repository.

The next steps taken and where we are now is FEA analysis of out leg component. After inital tests showed stress build concentration in the skinny up link component and hip area of the leg these were then thicken until FEA stress, strain, and displacement results were within an acceptable range.

![Right Side leg Drawing v1](https://github.com/user-attachments/assets/bf4fcbc5-e8ba-4f62-82c3-3f159fa46d61)


<img width="1512" height="982" alt="Screenshot 2026-02-27 at 6 16 29 PM" src="https://github.com/user-attachments/assets/f708ca9e-8001-4188-bbd5-414a391d3445" />

<img width="1512" height="982" alt="Screenshot 2026-02-27 at 6 16 34 PM" src="https://github.com/user-attachments/assets/432ca581-f5c0-4425-8110-911ff1aff2ed" />

<img width="1512" height="982" alt="Screenshot 2026-02-27 at 6 16 56 PM" src="https://github.com/user-attachments/assets/7290768c-4c93-4b4b-b650-7adbf79858c4" />

While I do belive that these results are indicative of a strong leg becasue of the loading being done at the hip joint 

![ASMB_3 0 servo Drawing v1](https://github.com/user-attachments/assets/928f2daa-c845-4c98-b00e-bc1b507ec135)

