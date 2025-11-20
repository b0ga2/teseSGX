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
- https://ieeexplore.ieee.org/abstract/document/11030449 e https://arxiv.org/abs/2311.09815 (Praticamente o mesmo artigo :/)
  - Interessante fala do eduroam e algo chamado fine time measuremente que permite calcular a distância entre user e o AP
  - Method: The system, named EDUM, uses two primary data sources: 1) WLAN data (SNMP polls and traps) collected from all campus Access Points and 2) Crowd-sourced data from student volunteers via two mobile apps (TUNet and TUNow). It determines a student's location by generating and comparing RSSI fingerprints from their device's mobility traces . It also collects the phone's "interactive states" (SCREEN_ON/OFF) from the app to measure usage.
  - Goal: To measure and characterize classroom education behavior at a large scale. The system is designed to measure students' punctuality (attendance, late arrivals, and early departures) and the "attractiveness" of lectures by quantifying student distraction through mobile phone use.
  - Privacy: The entire system is built on an opt-in, volunteer-based model. Sensitive information, including the mapping of student IDs to device MAC addresses , course timetables , and personal attributes (like grade and gender) , is crowd-sourced from approximately 700 student volunteers who use the university's mobile apps.
  - Analysis Methods: EDUM infers a course's venue by merging the RSSI fingerprints of all registered students attending that course . It determines the fine-grained lecture end time by heuristically detecting a "dramatic drop (40% in our case) of the number of appeared students". It then calculates metrics like Attendance Ratio , Late Ratio , and ON Ratio (for distraction) , and correlates these with academic performance (GPA).

- https://ualberta.scholaris.ca/items/9225340b-7e4d-4081-befa-36337a75ff2f
  - Isto é uma tese (ler mais tarde)

- https://dl.acm.org/doi/full/10.1145/3704522.3704523
  - Method: Using Wi-Fi fingerprinting for "zone-based localization". The method has two phases:
    - Offline Profiling Phase: A "radio-map" is created by dividing a classroom and its perimeter into a virtual grid of zones. A custom mobile app is used at each grid point to scan and record a "Wi-Fi signal vector" (a fingerprint) containing the Received Signal Strength (RSS) from all detectable Access Points (APs).
    - Online Localization Phase: A student's app scans their current Wi-Fi vector. This vector is sent to a server, which compares it to the stored radio-map using a distance metric (like Manhattan distance). The system identifies the k-nearest reference points and uses "majority voting" to classify the student as "inside" or "outside" the room's boundary.
  - Goal: To create an automated attendance system for educational institutions that accurately confirms if a user is inside a designated area (like a classroom), rather than determining their precise location. The system is designed to "eliminate privacy risks, proxy attendance, and minimizing disruptions".
  - Privacy: The system is presented as an alternative to biometric systems, which raise "concerns related to privacy and data security". The method requires both teachers and students to use a custom Android app and actively log in to scan and send Wi-Fi data to the server, implying an opt-in model. The data collected consists of AP names (SSIDs) and their corresponding RSS values.
  - Analysis Methods: The core of the system is a k-Nearest Neighbors (kNN) binary classification algorithm (referred to as "Wi-Fi RSS-Based Location Classification"). The paper evaluates the accuracy of this algorithm using four different distance metrics to find the "nearest" neighbors: Euclidean distance, Manhattan distance, Cosine similarity, and Hamming distance. Experiments showed that Manhattan distance provided the highest accuracy.


- https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/46f84f5c-e32b-40af-9034-06633c91da3d/content
  - Isto é uma tese ler mais tarde (pdf 14_02)


- https://peer.asee.org/a-tool-for-checking-attendance-of-students-in-classroom-automatically
  - Muito focado em Bluetooth (mas fala de algumas desvantagens do Wifi)
  - Method: This paper explicitly rejects Wi-Fi due to high energy consumption and unstable signal strength. Instead, it uses a Bluetooth Low Energy (BLE) "geofencing" approach. The system requires students to install a smartphone app that measures the Received Signal Strength (RSS) from two BLE beacons: one placed inside the classroom and one outside the door .
  - Goal: To design a software tool that automatically checks the attendance of students by determining "whether a student is located inside or outside the classroom".
  - Privacy: The article does not explicitly discuss data privacy, security, or what personal data is sent to the server. The entire system is predicated on students installing a specific application on their smartphones to be tracked.Analysis Methods: The system uses a two-part algorithm to determine location :
    - An "Inside Detector" checks if the rate of observed beacon frames from the inside beacon is above a set threshold (e.g., more than 5 beacons in 10 seconds) .
    - An "Entry/Exit Detector" calculates the "RSS difference" between the inside and outside beacons; an increasing (positive) difference signals entry, while a decreasing (negative) difference signals an exit .
    - Attendance is only confirmed when both detectors agree the student is inside. The app also uses the phone's accelerometer to stop BLE scanning when the student is not moving, saving battery life.


- https://ieeexplore.ieee.org/abstract/document/8938387
  - Mais focado em IOT do que em Wifi (pouco util)
  - Method: Using a "device-free" Wireless Sensor Network (WSN) composed of low-cost NodeMCU microcontrollers (equipped with Wi-Fi). One node acts as a transmitter (AP) and three others act as receivers. The system detects occupancy by observing fluctuations in the Received Signal Strength Indicator (RSSI); the RSSI is stable when the room is empty but "dips below the threshold" when a human body is present and interferes with the radio signal.
  - Goal: To create a low-cost, efficient classroom automation system to minimize power consumption. The occupancy monitoring system is used to control a "localised power system," (e.g., turning on lights/AC) only for occupied zones within a classroom.
  - Privacy: The article contrasts its method with cameras, which are "expensive" and computationally complex. The proposed method is "device-free" , meaning it does not require occupants to carry a specific device (like an RFID tag ) or track their personal phones. It detects anonymous "presence" rather than individual identities.
  - Analysis Methods: The system uses a "mean algorithm" for detection. It calculates the "average RSSI value of 7 iterations" and compares this to a pre-calibrated "threshold value" (the stable RSSI in an empty room). If the average RSSI dips below this threshold, the system "acknowledges the presence of a person".

- https://www.mdpi.com/2306-5729/2/4/32
  - Fraco pouco relacionado
  - Method: Uses Wi-Fi fingerprinting collected via crowdsourcing. A custom Android application was used by volunteers to collect 4648 fingerprints in a university building. Users manually registered their exact location (x, y, z coordinates) in the app, and the app recorded the Received Signal Strength (RSS) vector from all heard Access Points (APs) at that point, along with the device model and date .
  - Goal: To create and make publicly available an open, benchmark Wi-Fi fingerprinting dataset to allow for fair testing and comparison of different indoor positioning algorithms.
  - Privacy: The article focuses on signal data collection and does not discuss user privacy. The collection method is based on crowdsourcing from volunteers who installed a specific Android app for this purpose. The data collected consists of the MAC addresses of the heard APs and their RSSI, the manually entered location (x,y,z), the device model, and the date . The building floor maps were not made publicly available "due to privacy and IP issues".
  - Analysis Methods: The article does not propose a new analysis method but instead benchmarks several existing algorithms using the collected dataset. The tested algorithms include: Weighted Centroid, Log-Gaussian Probabilistic, Clustering (Affinity Propagation and k-means), the UJI KNN algorithm, Rank-Based Fingerprinting (RBF), and Coverage Area-based algorithms

indoor localization system using Wifi
- https://ieeexplore.ieee.org/abstract/document/6288374
  - Method: Uses a Wi-Fi fingerprinting approach with two phases.
    - Offline Phase: A "radio map" is built by collecting multiple RSSI samples (e.g., 100 samples) at known, fixed locations Instead of just averaging the signal, this method captures the full signal strength probability distribution (as a histogram) for each Access Point (AP) at each location .
    - Online Phase: The user's phone collects a small number of samples (e.g., 5-20) to estimate its current RSSI probability distributions. These are then compared to the distributions stored in the radio map4.
  - Goal: To create a more accurate Wi-Fi-based indoor positioning system for applications like navigation in airports, classrooms, or supermarkets5555. The method is designed to be "superior to other proposed methods" by using the signal's variations rather than averaging them out6666.
  - Privacy: The article does not discuss user privacy. The data is collected by a "specifically-designed Java API implemented on an Android smartphone" and consists of RSSI measurements associated with the MAC addresses of detected APs7777.
  - Analysis Methods: The system calculates the similarity between the online and offline probability distributions for the q strongest APs using the Bhattacharyya coefficient 8. This is converted into an "average Bhattacharyya distance" ($d_l$) for each offline location9. The user's position is then estimated by taking a weighted average of the coordinates of the three nearest neighbors (the locations with the smallest $d_l$), where the weight is inversely proportional to the distance ($w_l = 1/d_l$) This method is shown to outperform the RADAR (Euclidean distance) and LOCATOR (joint probability).


- https://www.sciencedirect.com/science/article/abs/pii/S0167739X19324835
  - Pouco relacionado, mais de ML e tratamento de daoos
  - Method: Uses a Wi-Fi fingerprinting approach called the "random statistical method".
    - Offline Handling Process: A large number ($n=100$) of Wi-Fi RSSI samples are collected at each Reference Point (RP) under "different indoor noise conditions" (e.g., varying times of day, different numbers of people present) 1111111111111111. Instead of just storing the mean RSSI, this "standardization process" calculates the expected value ($m^{(t)}$) and the full covariance matrix ($\Sigma^t$) for the vector of AP signals at each RP. This creates the fingerprinting database.
    - Online Positioning Process: A user's smartphone captures a single, "actual" Wi-Fi signal vector ($x$). This vector is then compared to the statistical fingerprint of every RP in the database .
  - Goal: To propose an effective method for an Indoor Positioning System (IPS) that improves positioning accuracy by effectively handling the noise and fluctuations of Wi-Fi signals.
  - Privacy: The article does not discuss user privacy. The system is designed to track a "Smartphone/User" 5by having a "Mobile application" on the "Client" device collect RSSI values and send them to a "Server" for processing and location determination 
  - Analysis Methods: The core of the method is the use of Mahalanobis distance for the online positioning phase. Unlike Euclidean distance, the Mahalanobis distance ($d(x, m^{(t)})$) measures the distance between the user's current signal vector ($x$) and the statistical mean of a reference point ($m^{(t)}$), while accounting for the inter-correlation of AP signals (the covariance matrix $\Sigma^t$)8888. The user's estimated location is the RP with the minimum Mahalanobis distance9999. This method is shown to be more accurate than the Weighted K-Nearest Neighbor (WKNN) algorithm10101010.


indoor location using Wifi data treatment using SGX
- https://dl.acm.org/doi/full/10.1145/3512892
  - Acho que não vale a pena


- https://dl.acm.org/doi/abs/10.1145/3144730.3144739
  - Interessante pelo conteudo do SGX e de como utilizar quando se protege serviços delocalização
  - Method: Proposes an architecture for private Location-Based Services (LBS) using Intel Software Guard eXtensions (SGX). The client's location query is encrypted (along with the response). The service provider's application and database are embedded and processed entirely inside a secure SGX enclave on an untrusted cloud server . This "reverse sandbox" isolates the code and data from the untrusted service provider, OS, and hypervisor.
  - Goal: To provide privacy-preserving LBS by protecting sensitive user location data from untrusted service providers. It aims to offer an efficient alternative to traditional privacy methods (like k-anonymity or cryptography) that often trade service accuracy or latency for privacy.
  - Privacy: The system is designed to provide "proactive and de-facto location-privacy". It enforces privacy by ensuring the service provider "cannot link a location to a particular user" (anonymity) or "distinguish between the actual and fake locations" (indistinguishability). The client can verify the application's security using remote attestation . Data stored outside the enclave is encrypted using sealing.
  - Analysis Methods: The system implements a Point-of-Interest (POI) Locator application inside the SGX enclave. This application computes nearby POIs using the client's decrypted location and a local database. The article evaluates this approach by benchmarking the SGX overhead (e.g., ECalls, OCalls, encryption) and comparing its precision against spatial cloaking with k-anonymity. The results show SGX adds only a "marginal overhead" (10-12% instruction rise) while achieving "near-to-the-perfect results," unlike k-anonymity, which sees precision drop as privacy (k-value) increases

- Intel SGX swapping
  - https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1416013&dswid=-3258(https://www.diva-portal.org/smash/get/diva2:1416013/FULLTEXT01.pdf)
  - 

- Intel SGX out-of-core processing
  - https://2025.eurosys.org/posters/final/eurosys25posters-final102.pdf

- Intel SGX limited memory
  - https://dl.acm.org/doi/abs/10.1145/2948618.2954331?casa_token=yCwrPnzdMMUAAAAA:EJeOSrEjGwTQD8_ERZK7jxtvKgQN3s0ZiW5IOMvDHxj9S18a8HdqpikuHegPmBB2agkIDxZXQPk
  - https://ieeexplore.ieee.org/abstract/document/7878255?casa_token=xtsrNEhy9fUAAAAA:LjdVrD9pFTgwFzmhHrLAKtWyoZTkBp21BLEbAiCosWfgn9Yuus9kuhHhaurd2aCTsWXURpO0
  - https://d1wqtxts1xzle7.cloudfront.net/96665723/ndss2018_06A-2_Ahmad_paper-libre.pdf?1672617144=&response-content-disposition=inline%3B+filename%3DOBLIVIATE_A_Data_Oblivious_Filesystem_fo.pdf&Expires=1763322899&Signature=gvJRlEbDFpa-3NGQqqljtReu~ccUu8Q4h6VXq0oW5H0F5MR1BZSzy-G1L1oiZcURVkQqiMTZkKsIEU3BSrp-D0wsBOlQiAER~MgfViPLgnCWqB8GGlOFerOtGwAmpqcj--DI8h9hFIVMRSc~QM7c8V3ktPnTAlDAfbLG0Yz7vHWjKqEIFBByZ8nFnH3Tb0MRg9bhW8xpR6ACltT5jhQ8pzsBTPUIv7I9Yai~6FJnuSVSIpUFmLmW6U3vgV1upjrWGbnaG0bkO~0cVTYMUrNaGxQ~U1tD2GCOze-PP8ge3yA1XFf8DW8TnOYq9shr28yackZdZYQVmShmrM1pEvhw~w__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

Some cool stuff:
- https://eprint.iacr.org/2016/086.pdf

D+uvidas:
- Deveria pesquisar algo como "data processing in SGX", "data ingestion and state management problem", "overcoming SGX memory limits" ou assim?