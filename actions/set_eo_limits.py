from st2common.runners.base_action import Action

limitsTemplate = {
    "kind": "LimitRange",
    "apiVersion": "v1",
    "metadata": {
        "name": "guaranteed",
        "namespace": ""
    },
    "spec": {
		"limits": [
			{
				"default": {
					"cpu": "1",
					"memory": "4Gi"
				},
				"defaultRequest": {
					"cpu": "1",
					"memory": "4Gi"
				},
				"max": {
					"cpu": "4",
					"memory": "8Gi"
				},
				"type": "Container"
			}
		]
	}
}


class CreateEOLimits(Action):

    def run(self, namespace):

        self.namespace = namespace
    
        return (True, self._createLimitsConfig())

    def _createLimitsConfig(self):
        myconf = limitsTemplate
        myconf['metadata']['namespace'] = self.namespace

        return myconf
