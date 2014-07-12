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

    python submiterator.py [PATH_TO_CONFIG_FILE] [OUTPUT_DIRECTORY*]
    sh posthit.sh [PATH_TO_CONFIG_FILE] [OUTPUT_DIRECTORY*]

The [OUTPUT_DIRECTORY*] is the directory in which to save files that submiterator makes. This argument is optional; by default, files will be saved to the current directory.

And then when you want to get the results:

    sh getresults.sh [PATH_TO_CONFIG_FILE] [OUTPUT_DIRECTORY*]
    python scripts/_shared/mturk/reformat.py [NAME_OF_RESULTS_FILE] [LABEL_FOR_OUTPUT_FILES*]

The [LABEL_FOR_OUTPUT_FILES*] variable is options and will, by default, be the same as the results file.

For example:
    Post Hit:
        python submiterator.py example.config
        sh posthit.sh example
    Retrieve Data:
        sh getresults.sh example
        python reformat.py example.results example