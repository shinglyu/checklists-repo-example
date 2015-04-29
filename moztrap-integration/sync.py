import subprocess
import moztrapcli.mtapi as mtapi
import os

#TODO: eliminate this tmp file
tmpfile="tmp.txt"
f = open(tmpfile, "w")

#FIXME: hardcoded feature file name
cases = subprocess.call(['./moztrap-integration/cucumber-js/bin/cucumber.js',
                         'fxos.rocketbar.feature',
                         '-r', './moztrap-integration/step_definitions/moztrap.steps.js'
                        ], stdout=f)
#TODO: detect for changed/added/delete case only and ignore the rest

#FIXME: hardcoded username/apikey

mtapi.create(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
