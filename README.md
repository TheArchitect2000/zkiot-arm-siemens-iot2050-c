## Applying zk-IoT on Siemens SIMATIC IOT2050

The integration of zk-IoT with the Siemens SIMATIC IOT2050 involves the following three steps:
	1.	Register the IOT2050 Device:
	•	Register the Siemens IOT2050 with an IoT server on the FidesInnova platform.
	2.	Generate and Submit a Commitment:
	•	Create a cryptographic commitment for the IOT2050 program.
	•	Submit the generated commitment to the FidesInnova network.
	3.	Generate and Submit a Proof:
	•	Generate a zero-knowledge proof (ZKP) for the IOT2050.
	•	Submit the proof to the FidesInnova network for verification.

# Step 1: IOT2050 Registration
In step 1, the IOT2050 device should be added to a user account on an IoT server. 
- Create an account on an IoT server such as https://panel.motioncertified.online
- Connect to your IOT2050 and install the git application
```
apt install git
```
- Clone this GitHub repository.
```
git clone https://github.com/FidesInnova/zkiot-siemens-simatic-iot2050.git
```
- Execute the wizardry.sh script to register your IoT device on your account.
```
cd zkiot-siemens-simatic-iot2050
./wizardry.sh
```
- Log into your web account and see your IOT2050 device in the 'Device List' section.

# Step 2: Commitment Generation
In this step, you should generate a commitment for your program on IOT2050 and submit it on the Fidesinnova public network.

- Install necessary libraries on IOT2050
```
sudo apt update && sudo apt install -y g++ libmosquitto-dev libmosquittopp-dev
```
- Edit the following items in `device_config.json` in the project root path:
```
{
  "class": 1,
  "iot_developer_name": "Fidesinnova",
  "iot_device_name": "Siemens_IOT2050",
  "device_hardware_version": "1.0",
  "firmware_version": "1.7",
  "code_block": [
    19723,
    19724
  ]
}
```
Update the following parameter:
```
"iot_developer_name": Based on the Company Name
"iot_device_name": Your IoT device name
"device_hardware_version"
"firmware_version"
```

- The project root path has a sample program, `program.cpp`. The commitment will be generated for this program.
- Execute the wizardry.sh script to generate a commitment.
```
./wizardry.sh
```
You can find the commitment at `data/program_commitment.json`
- Submit the commitment on Fidesinnova blockchain. To learn about this step, please follow: [A.8. Submit the commitment on blockchain](https://github.com/FidesInnova/zkiot-usage/blob/main/README_Program.md#a8-submit-the-commitment-on-blockchain)
  
# Step 3: Proof Generation
In this step, you should generate proofs by running the program on IOT2050 and submit it on the Fidesinnova public network.
- For this demo, you can use `wizardry.sh` script and choose option 3 to execute the program.
```
./wizardry.sh
```

# Step 4: Browsing Submitted Commitment and Proofs
- Browse the submitted commitment and proofs using [Fidesinnova blockchain network explorer](https://explorer.fidesinnova.io).
- Add some pictures from explorer. 

  
