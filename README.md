# DeepChem 

Using Deep Learning to predict properties of Chemicals. This is one of the projects in [KWoC 2017!](http://kwoc.kossiitkgp.in)


Discussion:

[![Join the chat at https://gitter.im/Deep-Chem/Lobby](https://badges.gitter.im/Deep-Chem/Lobby.svg)](https://gitter.im/Deep-Chem/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Registered Research Project :

![Fig1](https://zenodo.org/badge/DOI/10.5281/zenodo.1059147.svg)


<!--- ## About DeepChem

This is an exploratory personal research project in the Department of Chemical Engineering, IIT Kharagpur. 

[Working report](https://drive.google.com/open?id=1mxxSkFWa3xcFPXJB3WE8U7Q6wdRsVd_f). The work that I have done till now, // however, uses a very small dataset. The dataset needs to be rebuilt completely, which is where I require help from the 
opensource community. Yay [KWoC 2017!](http://kwoc.kossiitkgp.in) --->

## Objective: 

To Predict a difficult to obtain property of a compound using **only** the 3D structure.
The property that I have selected for the initial proof-of-concept is *Solubility*. 

## Methodology:

The first phase of the project will consist of data collection. For this, we will be generating a huge database of 3D structures vs Solubility.

For this purpose, there is a [Handbook of solubility](http://chemistry-chemists.com/chemister/Spravochniki/handbook-of-aqueous-solubility-data-2010.pdf) which the student will be using to obtain the solubility. The 3D structure will be parsed from SDF files, which can be obtained from NIST: [Benzene SDF](http://webbook.nist.gov/cgi/cbook.cgi?Str3File=C71432)

The second phase of the project will be to try and use the 3D structure to predict the solubility. For this, I aim to apply Vector Models to convert the 3D SDF to a high dimensional vector, and then build a Deep Neural Network to predict the solubility. 



### *© 2017 Avijit Ghosh for the Department of Chemical Engineering, IIT Kharagpur.*
