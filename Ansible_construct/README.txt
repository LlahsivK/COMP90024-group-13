Sample codes for creating, retreiving facts and updating volume of instances in MRC using Ansible.

NOTE: you need to first create a key-pair in your instance in MRC.
Then you need to change the key-pair in mrc.yaml in host_vars to the key you created.

Run steps:
1) Download your openrc.sh file from MRC along with your code.
2) Before running Ansible, run your opnerc.sh via . ./my-openrc-file.sh (note the '.' before ./my-openrc.sh)
Enter password.
Check that your env has the various global variables initialised via printenv
3) Run playbook via ansible-playbook mrc-name.yaml
4) Sit back and relax

To access the instances in MRC:
1) You need to VPN into unimelb
2) use:
	 ssh -i demo.pem ubuntu@xxx.xx.xx.x
or: use mobaX if windows OS.

demo.pem is the key-pair that was used to create the current instances.