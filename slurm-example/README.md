# Tools for running TensorFlow on graham

This zip file contains a small example for setting up and using TensorFlow on the Sharcnet grid computer "graham".

## Getting files onto graham

Copy this zip file to graham.  You can use "secure copy" to copy a file across the internet.  The "secure copy" program is part of the "ssh" toolset and works with any machine you can log into using `ssh`.

	scp graham-TF-tools.zip mylogin@graham.sharcnet.ca:.

This can be understood as:

* `scp`  --  *"secure copy"*
* `graham-TF-tools.zip`  --  *the file to copy from*
* `mylogin@graham.sharcnet.ca:.` -- the place to copy to, which in turn is:
	* mylogin -- replace this with your login name on graham
	* `@` -- delimiter between login name and machine name
	* `graham.sharcnet.ca` -- computer name holding the destination directory
	* `:` -- delimiter between computer and directory name
	* `.` -- short form for "right here" -- will place the file into your home directory.  Substitute another name if you want to put the file somewhere else

Note that this is similar to the `cp` command that operates locally -- you are supplying a source and a destination.  You can rewrite source and destination arguments to copy arbitrary files to and from any machine that supports `ssh`


# Setup the environment: install-TF-tools

The script `install-TF-tools` creates a working environment for you to run programs in, with specific versions of the tools you require, in a "packed up" environment for use with the `virtualenv` tool.

This script is readable with any text editor, and comments in the script explain what each step is doing.

Run the script to set up the environment:
	
	./install-TF-tools

Once you have done this once, you can reactivate the same install many times.  You do not need to re-run the install script unless you want to change the tools in your virtual environment.


# Run the sample program: run-TF-MNIST-on-slurm

The script `run-TF-MNIST-on-slurm` is NOT to be run directly. This is instead a script to be submitted to the run queue to be scheduled to run somewhere else on graham.

You can submit the script to be run using this command:

	sbatch run-TF-MNIST-on-slurm

When run, `sbatch` will add this program to the queue and print out the batch ID that the program was allocated.

It will not run immediately, but should be picked up within a few minutes.

You can run the command `mysqueue` in order to print out the portion of the slurm queue relevant to you.  This small script simply runs the `squeue` command and throws away all the lines pertaining to other users.  If you run it now, you will likely see your job in status "PD" (pending) while it is waiting.  Eventually it will enter "R" (running) status, and then complete.

When it is done, the output will appear in a file of the form

	slurm-99999999.out

with the 99999999 replaced with the actual job ID of your job.


# Python programs included in this file

There are several python programs included in this zip file:

* `TF-run-MNIST-withplot.py` -- run a simple Tensorflow setup based on the MNIST problem and create a plot (this is the script run by the `run-TF-MNIST-on-slurm` script -- edit that script or create your own to run the other programs)
* `TF-run-MNIST.py` -- run a simple Tensorflow setup based on the MNIST problem with no plotting
* `TF-peek.py` -- simply print out information about the GPUs on the assigned node

