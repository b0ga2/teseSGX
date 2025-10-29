Google Scholar query:

WiFi-based presence detection OR occupancy detection in indoor environments
- https://www.sciencedirect.com/science/article/abs/pii/S0360132321003401
  - Method : using Wi-Fi connection data as a proxy to understand building occupancy in an academic setting.
  - Goal : Energy efficiency
  - The article addresses privacy by avoiding the collection of sensitive data. It explicitly states: "Privacy concerns are limited in this data collection approach since it only relies on the aggregated device counts (i.e., no personally identifying information is being collected or used)".
  - The article uses K-means clustering and Poisson regression as its main analysis methods.

- https://ieeexplore.ieee.org/abstract/document/9266493
  - Method: Using Passive Wi-Fi Radar (PWR) to analyze disturbances in existing Wi-Fi signals. It processes signal reflections into Doppler spectrograms to detect human motion.
  - Goal: Occupancy detection and people counting
  - Privacy: The article states this Wi-Fi sensing approach can "preserve the privacy of individuals" and avoids the "privacy issues" associated with camera-based systems. The method is device-free and analyzes anonymous signal patterns rather than personal device data
  - The article uses Cross Ambiguity Function (CAF) processing , a CLEAN algorithm to remove signal interference , and a Convolutional Neural Network (CNN) for classification.

- https://www.sciencedirect.com/science/article/abs/pii/S0360132319300794
  - Method: Using device-based Wi-Fi data (MAC address and RSS) to solve the problem of discontinuous communication caused by smartphone battery-saving modes. It maintains a list of "inside" devices (an "inside MAC list") which is only updated when an "entering" or "exiting" event is detected.
  - Goal: To enable demand-driven control of HVAC and lighting systems for energy saving.
  - Privacy: The article notes that camera-based methods suffer from "privacy intrusiveness". It acknowledges that the MAC address data it uses is sensitive and "should be protected to preserve privacy," suggesting that "dynamic MAC masks or data encryption should be used"
  - Analysis Methods: The system uses two filters: a non-human MAC address filter (based on heuristics like appearance frequency and stable RSS) and a location filter (based on a calibrated RSS threshold to distinguish "inside" from "outside" devices). The core algorithm is an event-triggered updating method that modifies an "inside MAC list" based on detected "entering" and "exiting" events

- https://dro.deakin.edu.au/articles/journal_contribution/Effectiveness_of_using_WiFi_technologies_to_detect_and_predict_building_occupancy/20790145/1/files/37042060.pdf
  - Method: Using the hourly count of Wi-Fi connections from existing university Access Points (APs) as a direct proxy for the number of occupants in a classroom. The study simultaneously collected manual occupancy counts and CO2​ sensor data to compare their effectiveness.
  - Goal: To demonstrate that Wi-Fi connection counts are a more accurate and lower-cost indicator of building occupancy than CO2​ sensors, with the end goal of enabling demand-controlled HVAC systems for energy savings.
  - Privacy: The article explicitly acknowledges privacy concerns with Wi-Fi tracking, noting that methods like triangulation "raise privacy concerns since it requires identifying each device and its associated MAC address". In this study, "Specific MAC addresses were not provided due to security and privacy concerns", meaning the analysis was performed on pre-aggregated counts provided by the IT department.
  - Analysis Methods: The study uses Pearson's product-moment correlation to prove the strong, positive relationship between Wi-Fi counts and the actual number of occupants. It also uses Linear Regression and Multiple Regression to model and predict the occupant count based on the Wi-Fi data.

indoor location cisco catalyst
- https://crackedlabs.org/dl/CrackedLabs_Christl_IndoorTracking.pdf
  - Method: Using existing wireless networking infrastructure (specifically Wi-Fi Access Points and potentially Bluetooth/BLE beacons or badges) to perform indoor location tracking of employee-carried devices (laptops, smartphones) or dedicated badges. Can also integrate data from motion sensors, security cameras, and video conferencing devices.
  - Goal: To "gain insights into how people and things move throughout... physical spaces" and "understand the behavior and location of people (visitors, employees)" for various purposes including optimizing space utilization, monitoring employee performance, enhancing workplace safety/security, tracking customer behavior, and enabling targeted applications (e.g., smart cleaning, personalized promotions).
  - Privacy: The article describes these methods as "intrusive behavioral monitoring and profiling" raising "serious concerns about employee privacy". Systems typically collect device identifiers like MAC addresses by default, which are pseudonymous. While options like MAC randomization exist, vendors may discourage their use as they make analytics "unreliable". The potential to correlate location data with other systems (like HR) increases privacy risks. Repurposing data from security cameras is noted as particularly intrusive.
  - Analysis Methods: Systems process large volumes of "location data points" to provide real-time location maps , historical movement tracking , aggregate reports (e.g., counts per zone, dwell times, entry/exit times, flow between zones) , and behavioral profiling ("location personas") based on movement patterns. Specific features like proximity tracking and searching for individual devices/users are also available. Integration with third-party tools can add AI-based analysis like anomaly detection.

WiFi data student attendance monitoring university campus
- https://ieeexplore.ieee.org/abstract/document/9750047
- https://ieeexplore.ieee.org/abstract/document/8638098
- https://ieeexplore.ieee.org/abstract/document/7814796
- https://ieeexplore.ieee.org/abstract/document/8913341
- https://dl.acm.org/doi/abs/10.1145/2971648.2971657


WiFi access point data indoor localization classroom attendance
- https://ieeexplore.ieee.org/abstract/document/11030449
- https://arxiv.org/abs/2311.09815
- https://ualberta.scholaris.ca/items/9225340b-7e4d-4081-befa-36337a75ff2f
- https://dl.acm.org/doi/full/10.1145/3704522.3704523
- https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/46f84f5c-e32b-40af-9034-06633c91da3d/content
- https://peer.asee.org/a-tool-for-checking-attendance-of-students-in-classroom-automatically
- https://ieeexplore.ieee.org/abstract/document/8938387
- https://www.mdpi.com/2306-5729/2/4/32


indoor localization system using Wifi
- https://ieeexplore.ieee.org/abstract/document/6288374
- https://www.sciencedirect.com/science/article/abs/pii/S0167739X19324835


indoor location using Wifi data treatment using SGX
- https://dl.acm.org/doi/full/10.1145/3512892
- https://dl.acm.org/doi/abs/10.1145/3144730.3144739
- https://ieeexplore.ieee.org/abstract/document/9490363