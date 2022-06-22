# Getting started on "graham"

This project gives some basic instructions to getting logged into "graham" on sharcnet and running a simple example.

## Background

The compute cluster "graham" is part of the set of supercomputing tools available to academics here in Canada.  It is part of the consortium [Sharcnet](https://sharcnet.ca) which is available for use by students, staff and faculty at Canadian Universities.

The cluster is actually a collection of many computers, referred to as "nodes".  To access graham, you must use `ssh` (also called "secure shell") to establish a connection from the machine you are typing on (called the "local machine") to one of the login nodes of "graham" (called the "remote machine").


## Secure Shell

The "Secure Shell" program provies you command line access to another computer.  The other computer is called the "remote" machine, and the one you are typing on is the "local" machine.


#### Linux/MacOSX:
You should already have tools called `ssh` and `scp` installed.  You can test this by typing "`which ssh'" at a terminal prompt.

If (on Linux) it is not installed already, consult the tools for your distribution to acquire it.

MacOSX ships with this installed by default.

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![Image of the login widget for "PuTTY"](https://github.com/andrewhw/sharcnet-graham-getting-started/blob/main/images/putty.png "Putty Login Screen")

#### Windows:
You will need to download an ssh client.  By far the most popular and standard one is "PuTTY" which is available on this page: 
[https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

Once you have downloaded and installed this set of tools, you will have the utility "`putty.exe`" which will open a window as seen to the left.
Enter the name of the machine you wish to contact in "Host Name or IP Address".

To transfer files, you can use the "`pscp.exe`" tool, which works much as `scp` does as described below.


## Using ssh

The `ssh` tool runs in a terminal and connects that terminal to a text based command line on a remote machine.  For simple use to access the remote machine "`graham.sharcnet.ca`" with the account "`user123`" type:

    ssh user123@graham.shargnet.ca

This will connect you to the machine `graham.sharcnet.ca` over the internet, challenge you for your password and then give you a new prompt in your login shell.

Anything typed at this prompt is now being run on the remote machine.  If you type `exit` then the shell on the remote machine will exit, and the ssh connection will be shut down.

You can check what machine you are running on with the command `hostname`.  An example session logging into "graham" from my local machine "daphne" is shown here:
![Image of the login process](https://github.com/andrewhw/sharcnet-graham-getting-started/blob/main/images/on-graham.png "Mac Terminal program after running ssh to log into graham")


### Notes
If you leave out the `user123@` part, `ssh` assume that your login name is the same on both the local and remote computer.

If you are having trouble connecting, adding `-v` flags will make the connection more verbose, printing debugging info.  More than two -v flags may start to print debug information while commands are being processed, which can be quite annoying.


### Using PuTTY:
This tool is used very much like `ssh` with the following considerations:

* it provides its own window, and therefore doesn't need to be run within a terminal
* it will challenge you for your login information after connection, so this is not provided up front

## Using `scp`/`pcsp`:

These two commands work almost identically.  They copy files over a "tunnel" created using the secure shell protocol.  Both are run from a command line on the local computer.

The syntax of their use is similar to the `cp(1)` command, and follows one of these patterns:

* `scp` *<single file to copy>* *<destination filename>*
* `scp` *<list of source files to copy>* *<destination directory>*


The key difference between the local `cp` command and `scp` is that either source or destination may refer to a location on a remote machine.
The syntax for a file or directory is:
[*optionalUser*`@`*optionalMachine*`:`][*optionalPath*]*requiredName*

Items in [] are optional.

The name "`.`" simply refers to the "current directory".  When copying to a remote machine the "current directory" by default is the login directory.

### `ssh` Examples:

* to copy all of the Python source files in the current directory to the default (or login) directory on `graham.sharcnet.ca`:

	scp *.py myusername@graham.sharcnet.ca:.
        
* to recursively copy the entire directory `workbench/A1` from "`graham.sharcnet.ca`" to a local directory called `Assign1` (note that "Assign1" must exist prior to running this command to make this work):

	scp -r myusername@graham.sharcnet.ca:workbench/A1 Assign1


