## Setup

1. Install the `boto3` and the `xmltodict` packages:

```
pip install boto3
pip install xmltodict
```

2. In your Bash profile (e.g., `~/.bash_profile` on most Macs), add the following two 
environment variables with your MTurk access key and MTurk secret:

```
export MTURK_ACCESS_KEY=<YOUR MTURK ACCESS KEY>
export MTURK_SECRET=<YOUR MTURK SECRET>
```

Then once you open up a new terminal, you should be able to use the tool.


## How to use supersubmiterator mturk tools

To post the HIT, first setup the config file.
Give this config file a unique label as its name: `[LABEL].config`.

    {
    "liveHIT":"no",
    "title":"a title to show to turkers",
    "description":"a description to show to turkers",
    "experimentURL":"https://www.stanford.edu/~you/path/to/experiment.html",
    "keywords":"language research stanford fun cognitive science university explanations",
    "USonly?":"yes",
    "minPercentPreviousHITsApproved":"95",
    "frameheight":"650",
    "reward":"0.00",
    "numberofassignments":"10",
    "assignmentsperhit": "9",
    "assignmentduration":"1800",
    "hitlifetime":"2592000",
    "autoapprovaldelay":"60000",
    "doesNotHaveQualification": "<ID_TO_MTURK_QUALIFICATION> or none"
    }

Then run the following commands in the terminal:

    python supersubmiterator.py posthit [LABEL]

And then when you want to get the results:

    python supersubmiterator.py getresults [LABEL]

This will create a long-form table of your data (several `[LABEL]-*.csv` files.)


##  How to make this even cooler

N.B. This will only work on unix.

If you want, you can make `submiterator` a system-wide command, so you can just type (for example):

	supersubmiterator posthit example
    supersubmiterator getresults example

To do this, save the Submiterator repo somewhere where it won't move, copy-paste and run the following command:

	chmod u+x supersubmiterator.py

Then make a directory called "bin" in your home folder and make sym-links to the Submiterator file:

	cd ~
	mkdir bin
	cd bin
	ln -s [PATH_TO_SUBMITERATOR_DIRECTORY]/supersubmiterator.py supersubmiterator

Then open up or create the file `.bash_profile` or `.bashrc` in your home directory and add the following line:

	PATH=$PATH:~/bin

Then once you open up a new terminal, you should be able to use the `supersubmiterator` command as above.
