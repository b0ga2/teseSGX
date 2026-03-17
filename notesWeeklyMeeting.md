## 2026/03/05
- A shorter meeting due to limited time by everyone
- In the day 2026/03/10 we will have a reunion with STIC to test the python Script, prof. André said it couldn't fail, that's nice
- Both professors agreed with usage and loading of static files (schedules and classes) to structures.
  - Although trying to align all its properties is not worth it.

### Questions for the next meeting
- Should I parse the content of the schedules, classes and logs inside or outside the enclave?
  - For now I will parse the classes and schedules outside the enclave, since they are public information.
  - For the wifi logs, I reckon everything should be done inside the enclave.

- Since Im parsing the classes and schedules outside the enclave, should I use an outside library to parse the Json, or do it myself?
  - I found this quite interesting library called cJson wich is only one C and  one header file. I will use it for now since this is only for developments purposes and will likely not be used in production.


## 2026/03/10
- Meeting with Carlos Costa from STIC to test the Python Script
  - Everything went accordingly :)

### Questions for the next meeting (Sames as previous week because I forgot)
- Should I parse the content of the schedules, classes and logs inside or outside the enclave?
  - For now I will parse the classes and schedules outside the enclave, since they are public information.
  - For the wifi logs, I reckon everything should be done inside the enclave.

- Since Im parsing the classes and schedules outside the enclave, should I use an outside library to parse the Json, or do it myself?
  - I found this quite interesting library called cJson wich is only one C and  one header file. I will use it for now since this is only for developments purposes and will likely not be used in production.

- The coverage of the APs can be hardcoded or should it be an input file to the enclave as well?

- The goal is to to calculate for each class measure the quantity of students that were present in each week, but this raises some questions:
  - I assume that a class refers to a specific set of students per course, example TP1 from AC2. Is this correct?
    - If it is how can I separate one from another? Filename?
  - What happens if a class occurs more then once a week? Should I calculate the average of classes or divide the statistics per day?
- Another similar goal is to calculate the graphic of frequence, which means X students went to Y classes. Is this also per class per course?

