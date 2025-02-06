# Siemens SIMATIC IOT2050
- Install `tmux' package to manage terminal sessions.
```
apt install tmux
tmux new -s mysession
```
- To re-attach to an exisitng terminal session, you can use this command.
```
tmux attach -t mysession
```
- Pull this repository and run the following commands.
```
cd IOT2050/gcc
chmod +x commitmentGenerator
chmod +x program
chmod +x install_device
chmod +x wizardry.sh
```
- Execure the wizardery.sh script to register your IoT device on Fidesinnova platform, generate commitemnt, and geneate proof for sensors
```
./wizardery.sh
```
or use it with `sudo`
```
sudo ./wizardery.sh
```
