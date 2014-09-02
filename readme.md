## How to use submiterator mturk tools

To post the HIT, first setup the config file.

    {
    "rewriteProperties":"yes",
    "liveHIT":"no",
    "title":"a title to show to turkers",
    "description":"a description to show to turkers",
    "nameofexperimentfiles":"test",
    "experimentURL":"https://www.stanford.edu/~you/path/to/experiment.html",
    "keywords":"language research stanford fun cognitive science university explanations",
    "USonly?":"yes",
    "minPercentPreviousHITsApproved":"95",
    "frameheight":"650",
    "reward":"0.00",
    "numberofassignments":"1",
    "assignmentduration":"1800",
    "hitlifetime":"2592000",
    "autoapprovaldelay":"60000",
    "conditions":"cond"
    }

Then run the following commands in the terminal (from the top of the why directory):

    python submiterator.py [PATH_TO_CONFIG_FILE]
    sh posthit.sh [NAMEOFEXPERIMENTFILES]

And then when you want to get the results:

    sh getresults.sh [NAMEOFEXPERIMENTFILES]
    python scripts/_shared/mturk/reformat.py [PATH_TO_RESULTS_FILE]

This will create a bunch of .tsv files with data from your experiment.

For example:
    Post Hit:
        python submiterator.py example.config
        sh posthit.sh example
    Retrieve Data:
        sh getresults.sh example
        python reformat.py example.results example

##  How to make this even cooler

N.B. This will only work on unix.

If you want, you can make `submiterator`, `posthit`, `getresults`, and `reformat` system-wide commands, so you can just type (for example):

	submiterator example.config
	posthit example
	getresults example
	reformat example

To do this, save the Submiterator repo somewhere where it won't move, copy-paste and run the following command:

	chmod u+x submiterator.py posthit.sh getresults.sh reformat.py

Then make a directory called "bin" in your home folder and make sym-links to the Submiterator files:

	cd ~
	mkdir bin
	cd bin
	ln -s [PATH_TO_SUBMITERATOR_DIRECTORY]/submiterator.py submiterator
	ln -s [PATH_TO_SUBMITERATOR_DIRECTORY]/posthit.sh posthit
	ln -s [PATH_TO_SUBMITERATOR_DIRECTORY]/getresults.sh getresults
	ln -s [PATH_TO_SUBMITERATOR_DIRECTORY]/reformat.py reformat

Then open up or create the file `.bash_profile` or `.bashrc` in your home directory and add the following line:

	PATH=$PATH:~/bin

Then once you open up a new terminal, you should be able to use the submiterator commands as above.