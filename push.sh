reply=$(curl -X POST -H "Content-Type: application/json" --data '{"caseversion":"/api/v1/caseversion/68161/", "instruction":"Open phone app", "expected":"Phone app opened", "number":1}' https://moztrap-dev.allizom.org/api/v1/casestep/\?username\=$MTUSER\&api_key\=$APIKEY)
#reply=$(curl -X GET -H "Content-Type: application/json" https://moztrap-dev.allizom.org/api/v1/casestep/\?username\=$MTUSER\&api_key\=$APIKEY)
echo Acting as $MTUSER
echo Acting as ENV['MTUSER']
echo $reply
