
# generate-gitlab-ci.py
import json

SERVICES = [ "svc"+ i for i in range(50)]
def make_service(name):
    return {
        "build-%s" % name: {
            "stage": "build",
            "script":[
                "echo Build %s" % name,
            ]
        },
        "deploy-%s" % name: {
            "stage": "deploy",
            "script":[
                "echo Deploy %s" % name,
            ]
        }
    }

with open(".gitlab-ci.generated.yml", "w") as f:
    pipeline = {}
    pipeline.update({
        "stages": ["build", "deploy"]
    })
    for service in SERVICES:
        pipeline.update(make_service(service))
    f.write(json.dumps(pipeline))
