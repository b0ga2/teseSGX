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