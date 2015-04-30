import subprocess
import moztrap_integration.moztrapcli.mtapi as mtapi
import os

#TODO: eliminate this tmp file
tmpfile="tmp.txt"
f = open(tmpfile, "w")

#FIXME: hardcoded feature file name
cases = subprocess.call(['./moztrap_integration/cucumber-js/bin/cucumber.js',
                         'fxos.rocketbar.feature',
                         '-r', './moztrap_integration/step_definitions/moztrap.steps.js'
                        ], stdout=f)
#TODO: detect for changed/added/delete case only and ignore the rest
f.close()

tmp = open(tmpfile, "r")
#FIXME: hardcoded username/apikey
mtapi.mtorigin = "https://moztrap-dev.allizom.org"
print tmp.readlines()
mtapi.create(tmpfile, {'username': os.getenv("mz_user_name"), 'api_key': os.getenv("mz_api_key")})
