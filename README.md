Applying zk-IoT on Siemens SIMATIC IOT2050 includes three steps: IOT2050 Registeration in an IoT server on Fidesinnove platfrom, Generating a commitment for IOT2050 program and submitting the commitment on fidesinnva network, Generating a proof for IOT2050 and submitting on fidesinnva network.

# Step 1: IOT2050 Registeration
In step 1, the OT2050 device should be added to a user account on an IoT server. 
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
- Log into your web account and see your IOT2050 device in 'Device List' section.

# Step 2: Commitment Generation
In this step, you should generate a commitment for your program on IOT2050 and submit it on the Fidesinnova public network.

- Install necessary libraries on IOT2050
```
sudo apt update && sudo apt install -y g++ libmosquitto-dev libmosquittopp-dev
```
- Edit the following items in `device_config.json` in the project root path:
```
- Class
- IoT Developer name:
- IoT Device name:
- Device Hardware Version:
- Firmware Version
- Code Block
```

- There is a sample program, `program.cpp`, in the project root path. The commitment will be generated for this program.
- Execute the wizardry.sh script to generate a commitment.
```
./wizardry.sh
```

- Subimit the commitment on Fidesinnova blockchain. To learn about this step, please follow: [A.8. Submit the commitment on blockchain](https://github.com/FidesInnova/zkiot-usage/blob/main/README_Program.md#a8-submit-the-commitment-on-blockchain)
  
# Step 3: Proof Generation
In this step, you should generate a proof for the program on IOT2050 and submit it on the Fidesinnova public network.
- Execute the program. For this demo, you can execute `wizardry.sh` script and choose option 3.
```
./wizardry.sh
```

# Browising Submitted Commitments and Proofs on Fidesinnova blockchain network explorer.

- Add some picture from explorer. 

  
