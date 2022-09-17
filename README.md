# flashled-service
This is a service to flash an LED to indicate the system is up and running. Runs on Raspi 3B+/4

The script follows this tutorial: https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

To make the script a service copy the file flashled.service to /etc/systemd/system/ and reload the deamons, enable and start.
