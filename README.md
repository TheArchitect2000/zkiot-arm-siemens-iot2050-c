# Siemens SIMATIC IOT2050
- Install git
```
apt install git
```
- Clone the project
```
git clone https://github.com/FidesInnova/zkiot-siemens-simatic-iot2050.git
```

- Install necessary libraries
```
sudo apt update && sudo apt install -y g++ libmosquitto-dev libmosquittopp-dev
```
- Install `tmux` package to manage terminal sessions.
```
apt install tmux
tmux new -s mysession
```
- You can use this command to re-attach to an existing terminal session.
```
tmux attach -t mysession
```
- Pull this repository and run the following commands.
```
cd zkiot-siemens-simatic-iot2050
```
<!---chmod +x commitmentGenerator
chmod +x program
chmod +x install_device
chmod +x wizardry.sh --->
- Execute the wizardry.sh script to register your IoT device on the Fidesinnova platform, generate commitment, and generate proof for sensors
```
./wizardry.sh
```
- To submit a commitment to blockchain follow this [link](https://github.com/FidesInnova/zkiot-usage/blob/main/README_Program.md#a8-submit-the-commitment-on-blockchain)
