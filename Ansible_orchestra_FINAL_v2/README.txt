author: Thomas Koh 329888
date: 29/4/2021

Team13 members:
Thomas Koh 329888
Alexander Lesaffre 1161899
Vishall Krishnan 1018473
Jothe Krishnan 1187902
Kwanhyoung Lee 992925

Purpose of this folder is to setup the environment in MRC so that we have instances with pre-installed dependencies

This DOES NOT do the analysis for us.

How to run on linux subsystem.

For submission purposes we have removed the .pem keys and the openrc.sh file from submission for secutiry reasons.

1. Run the following: . myopenrc.sh
(don't forget the dot before myopenrc.sh)
Good practice to check env via printenv that all the variables are imported correctly

2. Run the following: ansible-playbook create.yaml

Sit back and enjoy the show.

Notes:
Have only spun up one instance (instance 4). In theory can be used to spin up multiple number of instances with all sorts
of flavours and volume size.

To do this edit the following file /host_vars/mrc.yaml