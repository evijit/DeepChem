# DeepChem

Using Deep Learning to predict properties of Chemicals. 
[![Join the chat at https://gitter.im/Deep-Chem/Lobby](https://badges.gitter.im/Deep-Chem/Lobby.svg)](https://gitter.im/Deep-Chem/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


## About DeepChem

This is a personal research project, but I opened it up for KWoC 2017 since I could really use some help! 

## Objective: 

To Predict a difficult to obtain property of a compound using **only** the 3D structure.
The property that I have selected for the initial proof-of-concept is *Solubility*. 

## Methodology:

Part 1 of the project will consist of data collection. For this, we will be generating a huge database of 3D structures vs Solubility.

For this purpose, there is a [Handbook of solubility](http://chemistry-chemists.com/chemister/Spravochniki/handbook-of-aqueous-solubility-data-2010.pdf) which the student will be using to obtain the solubility. The 3D structure will be parsed from SDF files, which can be obtained from NIST: [Benzene SDF](http://webbook.nist.gov/cgi/cbook.cgi?Str3File=C71432)

Part 2 of the project will be to try and use the 3D structure to predict the solubility. For this, I aim to apply Vector Models to convert the 3D SDF to a high dimensional vector, and then build a Deep Neural Network to predict the solubility. 



### *© 2017 Avijit Ghosh for the Department of Chemical Engineering, IIT Kharagpur.*
