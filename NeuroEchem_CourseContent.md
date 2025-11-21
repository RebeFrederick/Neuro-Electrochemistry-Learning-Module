# Neuro-Electrochemistry Learning Module
by Rebecca A. Frederick, Ph.D. <br /> 
Last Updated 2025-NOV-21 <br /> 
***< Course Content (In Progress) >***

# A. Introduction
In working through this introduction, you will gain understanding of foundational content from multiple basic science topics required to get started in electrochemistry measurements and research projects related to neural engineering. 

## A1. Electronics and Circuits Basics

### A1a. Definitions
- Resistor:  
- Capacitor:  
- Inductor:  
- Current:  
- Voltage:  
- Impedance:  

### A1b. Current-Voltage Relationships
#### Resistors
#### Capacitors
#### Inductors


### A1c. Impedance Relationships
#### Resistors
#### Capacitors
#### Inductors


## A2. Neuroanatomy and Neurophysiology Basics
### A2a. Brain Overview
### A2b. Spinal Cord Overview
### A2c. Peripheral Nerves Overview
### A2d. Neurons
### A2e. Action Potentials
### A2f. Neurotransmitters
### A2g. Other Cell Types


## A3. Chemistry Basics

### A3a. Chemical Structures
### A3b. Chemical Reactions
### A3c. Reduction and Oxidation Reactions
### A3d. Fermi Level


## A4. Materials Science


## A5. Thermodynamics

### A5a. "Laws" of Thermodynamics

### A5b. Nernst Equation


# B. Neural Engineering

## B1. Electrochemistry
Reference:  LibreTexts&trade; Chemistry Library  >  Analytical Chemistry  >  Electrochemistry
[https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Supplemental_Modules_(Analytical_Chemistry)/Electrochemistry](https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Supplemental_Modules_(Analytical_Chemistry)/Electrochemistry)

Reference: Standard Operating Procedures for Cyclic Voltammetry by Daniel Graham [https://sop4cv.com/](https://sop4cv.com/)
### B1a. Definitions:
- **Cathode**:  the electrode within a cell that gains electrons, i.e. the electrode that is reduced. <br/>
  Note: In a **galvanic** cell (see B1b below), the potential of the cathode vs. reference will be **positive***, because the spontaneous reaction within the electrolyte polarizes the electrode to be positive and attract electrons to move away from the anode through the connected electrical circuit. In an **electrolytic** cell (see B1b below), the potential of the cathode vs. reference will be **negative**, because the connected electrical circuit is used to move electrons away from the anode and into the cathode to drive reactions within the electrolyte.
- **Anode**:  the electrode within a cell that looses electrons, i.e. the electrode that is oxidized. <br/>
  Note: In a **galvanic** cell (see B1b below), the potential of the anode vs. reference will be **negative**, because the spontaneous reaction within the electrolyte polarizes the electrode to be positive and attract electrons to move away from the anode through the connected electrical circuit. In an **electrolytic** cell (see B1b below), the potential of the anode vs. reference will be **positive**, because the connected electrical circuit is used to move electrons away from the anode and into the cathode to drive reactions within the electrolyte.
- **Cation**:  A cation is a positively charged ion, i.e. an ion containing fewer electrons than protons. 
- **Anion**:  An anion is a negatively charged ion, i.e. an ion containing more electrons than protons.
- **Cathodic or Cathodal (Electrical Current)**:  the flow of electrons *away from* an electrode. In an electrolytic cell, the flow of electrons *from* the power source *to* the cathode and then *from* the cathode *to* a species in the electrolyte solution. By International Union of Pure and Applied Chemistry (IUPAC) definition, cathodic current amplitude is defined as negative.
- **Anodic or Anodal (Electrical Current)**:  the flow of electrons *into* an electrode. In an electrolytic cell, the flow of electrons *from* a species in the electrolyte solution *to* the anode and then *from* the anode back *to* the power source. By International Union of Pure and Applied Chemistry (IUPAC) definition, anodic current amplitude is defined as positive.
- **Cathodic (Chemical Reaction)**:  a reduction reaction; gain of electrons.
- **Anodic (Chemical Reaction)**:  an oxidation reaction; loss of electrons.

### B1b. Electrochemical Cells
There are different types of cells in electrochemistry. <br/>
- In a Galvanic Cell, energy released by a spontaneous redox reaction is converted to electrical energy.
- In an Electrolytic Cell, electrical energy is used to drive redox reactions that (typically) do not occur spontaneously.
- **Most measurement methods and hardware systems in neural engineering employ electrolytic cells.**
### B1c. Chemical Equilibrium vs. Electrochemical Equilibrium
- Electrochemical Equilibrium $\Delta E_{r}$ is measured using a high input resistance voltmeter, without any current flow.
- Chemical Equilibrium is a special case of electrochemical equilibrium, where $\Delta E_{r}=0V$

### B1d. Open Circuit Potential


### B1e. Hardware Considerations
- Gamry Application Notes:  https://www.gamry.com/resources-2/application-notes/
	- Faraday Cage: What Is It? How Does It Work?  https://www.gamry.com/application-notes/instrumentation/faraday-cage/
	- Potentiostat Fundamentals  https://www.gamry.com/application-notes/instrumentation/potentiostat-fundamentals/
	- Instrument Grounding and Guide for the Right Setup  https://www.gamry.com/application-notes/instrumentation/instrument-grounding-right-setup/
	- Understanding the Specifications of your Potentiostat  https://www.gamry.com/application-notes/instrumentation/understanding-specs-of-potentiostat/
	- Calibration of Your Potentiostat  https://www.gamry.com/application-notes/instrumentation/why-calibrate-potentiostats/
	- Cable-Capacitance Correction  https://www.gamry.com/application-notes/instrumentation/cable-capacitance-correction/
	- Risks of Using Additional Cabling  https://www.gamry.com/application-notes/instrumentation/additional-cabling/
	- Understanding iR Compensation  https://www.gamry.com/application-notes/instrumentation/understanding-ir-compensation/
	- Measuring Surface Related Currents using Digital Staircase Voltammetry  https://www.gamry.com/application-notes/physechem/cyclic-voltammetry-measuring-surface-related-currents/
	- Square-wave Voltammetry  https://www.gamry.com/application-notes/physechem/square-wave-voltammetry/
	- Measuring pA-level current flowing across artificial Ion channels and Nanopores Using a Reference 620 potentiostat  https://www.gamry.com/application-notes/physechem/measuring-pa-level-current/
	- Two, Three and Four Electrode Experiments  https://www.gamry.com/application-notes/instrumentation/two-three-four-electrode-experiments/
	- Measurement of Small Electrochemical Signals  https://www.gamry.com/application-notes/instrumentation/measurement-of-small-electrochemical-signals/
	- Reference Electrodes  https://www.gamry.com/application-notes/instrumentation/reference-electrodes/
	- Measuring the Impedance of Your Reference Electrode  https://www.gamry.com/application-notes/instrumentation/measuring-the-impedance-of-your-reference-electrode/
	- Rapid Biphasic Pulsing  https://www.gamry.com/application-notes/instrumentation/rapid-biphasic-pulsing/
		- Tips and Techniques for Improving Potentiostat Stability  https://www.gamry.com/application-notes/instrumentation/potentiostat-stability-tips-techniques/
		- Changing Potentiostat Speed Settings  https://www.gamry.com/application-notes/instrumentation/changing-potentiostat-speed-settings/
- Gamry White Papers:  https://www.gamry.com/resources-2/white-papers/
	- Basics of Electrochemical Impedance Spectroscopy - Part 1  https://www.gamry.com/assets/Uploads/resources/The-Basics-of-EIS.pdf
	- Basics of Electrochemical Impedance Spectroscopy - Part 2  https://www.gamry.com/assets/Uploads/resources/The-Basics-of-EIS-Part-2.pdf
	- Basics of Electrochemical Impedance Spectroscopy - Part 3  https://www.gamry.com/assets/Uploads/resources/The-Basics-of-EIS-Part-3.pdf
	- Basics of Electrochemical Impedance Spectroscopy - Part 4  https://www.gamry.com/assets/Uploads/resources/The-Basics-of-EIS-Part-4.pdf
- "Limitations in the electrochemical analysis of voltage transients" by Alexander Harris  https://doi.org/10.1088/1741-2552/ad1e23
- "On the use of drift correction for electrochemical impedance spectroscopy measurements: by Mark Orazem, Burak Ulgut  https://doi.org/10.1016/j.electacta.2023.141959

## B2. Electrophysiology
### B2a. Definitions
### B2b. Patch Clamp Recording and Stimulation (Intracellular)
### B2c. Neural Recording (Extracellular)
### B2d. Neural Stimulation (Extracellular)
Reference: J. T. Mortimer and N. Bhadra, “Applied Neural Control,” Applied Neural Control. Accessed: Apr. 29, 2024. Available: [https://case.edu/groups/ANCL/ANCL.htm](https://case.edu/groups/ANCL/ANCL.htm)
#### Electrode Configurations
##### Reference Electrodes
##### Counter/Ground Electrodes
##### Working/Stimulation Electrodes
- Monopolar
- Bipolar
- Tripolar
- Other Configurations
#### Stimulation Waveforms
##### Stimulation Control/Method
- Voltage
- Current
- Mixed Methods
##### Stimulation Waveform
- Square
- Triangle
- Sinusoidal
##### Square Waveform: Phase
- Monophasic
- Biphasic
- Triphasic or Multi-phasic
##### Square Waveform: Symmetry
- Symmetric
- Asymmetric
##### Example and Parameter Definitions
- Amplitude
- Phase Width (Pulse Width)
- Inter-phase Delay
- Period
- Frequency
- Inter-pulse period


# C. Advanced Topics

## C1. Electrochemistry
- The Electrochemistry Video Lectures series from the University of Oregon Electrochemistry Department provides in-depth lectures and instruction in fundamental electrochemistry principles covering thermodynamics, kinetics, mass transfer, transport, and other topics. This is an advanced lecture series requiring background knowledge in chemistry and thermodynamics beyond the content presented in this module's introduction (section A). <br/>
  [https://electrochemistry.uoregon.edu/education/electrochemistry-video-lectures/](https://electrochemistry.uoregon.edu/education/electrochemistry-video-lectures/)
- LibreTexts&trade; Chemistry Library  >  Analytical Chemistry  >  Electrochemistry
  [https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Supplemental_Modules_(Analytical_Chemistry)/Electrochemistry](https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Supplemental_Modules_(Analytical_Chemistry)/Electrochemistry)
- LibreTexts&trade; Chemistry Library  >  Reference Tables  >  Electrochemistry Tables
  [https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Electrochemistry_Tables](https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Electrochemistry_Tables)
	- [Standard Reduction Potentials by Element](https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Electrochemistry_Tables/P1%3A_Standard_Reduction_Potentials_by_Element)
	- [Standard Reduction Potentials by Value](https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Electrochemistry_Tables/P2%3A_Standard_Reduction_Potentials_by_Value)
	- [Activity Series of Metals](https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Electrochemistry_Tables/P3%3A_Activity_Series_of_Metals)
	- [Polarographic Half-Wave Potentials](https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Electrochemistry_Tables/P4%3A_Polarographic_Half-Wave_Potentials)
- "What is CV? A comprehensive guide to Cyclic Voltammetry" from Biologic
  https://www.biologic.net/topics/what-is-cv-a-comprehensive-guide-to-cyclic-voltammetry/
- Application Notes from Gamry
  https://www.gamry.com/application-notes/

## C2. Neurotransmitter Detection



# D. Summary



