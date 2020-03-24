from st2common.runners.base_action import Action

svc = {
    "kind": "Service",
    "apiVersion": "v1",
    "metadata": {
        "labels": {
            "name": "environment-operator"
        },
        "name": "environment-operator",
        "namespace": ""
    },
    "spec": {
        "ports": [
            {
                "protocol": "TCP",
                "targetPort": 8080,
                "port": 80
            }
        ],
        "selector": {
            "name": "environment-operator"
        }
    }
}


class CreateEOService(Action):

    def run(self, namespace):
        self.namespace = namespace

        return (True, self._createSVCConfig())

    def _createSVCConfig(self):
        myconf = svc
        myconf['metadata']['namespace'] = self.namespace

        return myconf
