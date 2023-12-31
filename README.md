# Production of UV photosensor and current readout circuit
The project focuses mainly on the production of a UV photosensor and current readout circuit containing a transimpedance amplifier on a single glass substrate using a semiconductor production process in a clean room at the Institute of Large Area Microelectronics, University of Stuttgart.

# Various steps involved in the project
- Creation of layout and production of photosensors using Chromium-Gold and Molybdenum Tantalum-Indium Tin Oxide as its electrode
- Creation of layout and production of current readout circuit for the photosensor containing transimpedance amplifier on the same substrate
- Optimization of production steps by reusing the existing layer and also reducing the number of layers required
- Electrical characterization of all the components after their production using the Keithley instruments and the Python scripts
- Detailed description of the project is mentioned in the report: [Production of UV photosensor and current readout circuit](https://drive.google.com/file/d/1Ng5pi7pYeUGtu5qTg4N3Vx0-dnfdbjn2/view?usp=sharing)

# How to read the files
The codes are organized batch-wise for better clarity. Each batch is the set of measurements done on substrates after each production step.
- Batch 1 contains the electrical characterization of UV photosensors produced using Chromium-Gold as its electrode. The photosensor I-V characteristics are measured and plotted using the Keithley instrument and Python scripts. The response time (rise and fall time) of this photosensor is evaluated using different Python scripts.
- Batch 2 contains the electrical characterization of UV photosensors, thin film transistor characteristics, operational amplifier in the form of transimpedance amplifier and the putput from the combination of both photosensor and the current readout circuit. Various Python scripts are used to analyse these data.
- Batch 3 contains the electrical characterization of UV photosensors produced using Molybdenum Tantalum-Indium Tin Oxide as its electrode. This was done to reuse the material from thin film transistors to optimize the production in the next batch.
- Batch 4 contains the electrical characterization of components similar to batch 2 but here the production process was optimized by reusing the existing materials and eliminating the layers.

# How to run the code
- The data could not be updated due to non-disclosure agreement signed with the Institute of Large Area Microelectronics, Uni Stuttgart.
- The packages and their versions used mentioned in the file "requirements.txt" and the command console'''pip install -r requirements.txt''' could be used to install all the packages that is required to recreate the same environment.
