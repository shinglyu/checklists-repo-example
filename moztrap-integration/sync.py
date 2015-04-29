import subprocess

#TODO: eliminate this tmp file
tmpfile="tmp.txt"
f = open(tmpfile, "w")

#FIXME: hardcoded feature file name
cases = subprocess.call(['./moztrap-integration/cucumber-js/bin/cucumber.js',
                         'fxos.rocketbar.feature',
                         '-r', './moztrap-integration/step_definitions/moztrap.steps.js'
                        ],
                        stdout=f)
#TODO: detect for changed/added/delete case only and ignore the rest

#FIXME: hardcoded username/apikey
res = subprocess.call(['python', './moztrap-integration/moztrap-cli/moztrap.py',
                       'create',
                       '-u', 'admin-django',
                       '-k', 'c67c9af7-7e07-4820-b686-5f92ae94f6c9',
                       tmpfile])
#TODO: Change this subprocess call to directly use moztrap-cli's code
print res
