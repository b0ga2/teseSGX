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
  - Method: Using Wi-Fi session logs from a university's existing infrastructure, combined with timetabling data and class enrollment lists. The method is a two-stage process:
    - AP Mapping: First, it uses unsupervised clustering (K-means, EM-GMM, HC) to automatically identify and map all relevant Access Points (including those in hallways or adjacent rooms) to a specific classroom.
    - Occupancy Estimation: It then applies a machine-learning pipeline to the data from those mapped APs. This involves classifying individual users as "occupants" or "bystanders" based on behavioral features (like % in time, % out time, Arrival delay, and Num. of devices ), followed by a regression model to predict the final count, which compensates for students not connected to Wi-Fi.
  - Goal: To develop a low-cost, scalable method to model and estimate classroom occupancy (i.e., class attendance) to help university estate managers optimize space utilization. It specifically aims to overcome the "pollution" and errors caused by simple connection counts, where signals from bystanders and adjoining rooms corrupt the data .
  - Privacy: The article acknowledges the "sensitive nature" of the Wi-Fi session logs, which contain User IDs and MAC addresses. The study received ethics approval to use "anonymized personal information" . The authors state that their method only measures "metadata of users' activity" and is therefore "less intrusive than camera-based counting methods". The model's reliance on class enrollment lists is also noted.
  - Analysis Methods: The system uses a chain of machine learning algorithms. Unsupervised Clustering (K-means, EM-GMM, Hierarchical Clustering) is used for the AP mapping phase. For the occupancy modeling, it uses Classification algorithms (Logistic Regression, SVM, and Linear Discriminant Analysis - LDA) to filter users , followed by Regression algorithms (Linear Regression - LR, and Support Vector Regression - SVR) to estimate the final count.


- https://ieeexplore.ieee.org/abstract/document/8638098
  - Method: Using Wi-Fi session logs from a university's existing infrastructure1111. The core of the method is a two-stage supervised learning approach2222:
    - Classification: First, a classifier (like LDA) is used to distinguish "occupants" from "bystanders"3333. This is based on a "rich set of features" 4extracted for each user, including RSSI 5, Arrival delay 6, Number of sessions 7, Number of devices 8, Percentage of 'in time' ($t_{in}$) 9, and Percentage of 'out time' ($t_{out}$)10.
    - Regression: The output count from the classifier is then fed into a regression model (like LR or SVR) 11111111 to produce the final occupancy estimate. This step is designed to "compensate for the room occupants who are not captured by WiFi"12121212.
  - Goal: To estimate room occupancy (specifically, class attendance) to help university estate managers "optimize the usage of classroom space"131313. The aim is to provide a low-cost "soft sensor" alternative to expensive hardware sensors 14141414so that rooms can be allocated based on actual attendance rather than just enrollment numbers15.
  - Privacy: The article acknowledges that the Wi-Fi logs contain "personal information", including a "unique user identifier" (student/employee ID) and device MAC addresses16161616161616. The researchers anonymized these user identifiers 17and obtained ethical clearance (UNSW HREAP approval number HC17140) to use the data18. The ethics application noted that a term of use for the university Wi-Fi is that "All activity on the wireless network is monitored," which implies users grant "explicit permission"19. To train the model, "class lists" (enrolled students) were used as ground truth to label Wi-Fi users as "occupants" or "bystanders"20202020.
  - Analysis Methods: The paper uses a two-stage machine learning pipeline21212121.
    - Stage 1 (Classification): Compares Logistic Regression, SVM, and Linear Discriminant Analysis (LDA)22222222. It found LDA performed best, achieving 84% accuracy in predicting occupants and 81% accuracy in predicting bystanders232323232323232323.
    - Stage 2 (Regression): Evaluates Linear Regression (LR) and Support Vector Regression (SVR)24242424. The final LR model (Y = 10.3 + 1.25X) "inflate[s]" the classifier's count (X) to produce the final estimate (Y), accounting for occupants not on Wi-Fi25252525.
    - Pearsons correlation is also used to prove the necessity of filtering: the correlation between actual occupancy and raw "WiFi Occupancy" is only 0.35, but it improves to 0.77 for "Enrolled WiFi Occupancy"26.

- https://ieeexplore.ieee.org/abstract/document/7814796
  - Não gostei, pouco relacionado

- https://ieeexplore.ieee.org/abstract/document/8913341
  - Method: Using metadata from existing WiFi Access Points (APs). At the room level, the occupancy is derived by summing the number of unique users connected to all APs inside a room, after filtering out sessions shorter than five minutes (to remove transient users). At the campus level, it uses hourly aggregate device counts from an API , which can be mapped to people counts using a proportionality factor (e.g., 1.3 devices per user).
  - Goal: To demonstrate the feasibility and effectiveness of using WiFi metadata for occupancy monitoring at both the room level (by comparing it to hardware beam counters) and the campus level (by analyzing broad applications for various stakeholders like students, estate managers, and retailers).
  - Privacy: The article acknowledges that WiFi metadata contains "user identifiers" which "can endanger students privacy". It contrasts this with beam counters, which are "privacy preserving" because they do not collect private data. The WiFi data collected included unique user IDs and device MAC addresses.
  - Analysis Methods: The study primarily uses direct comparison and correlation. It filters raw data (e.g., sessions < 5 min) and then sums unique users. The performance is evaluated by calculating the Pearson's product-moment correlation (R) and symmetric mean absolute percentage error (sMAPE) against ground-truth data (hardware beam counters and manual counts). The correlation (R) between WiFi-sensed occupancy and observed occupancy was 0.85.


- https://dl.acm.org/doi/abs/10.1145/2971648.2971657
  - Honestamente, fraco e pouco relacionado


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