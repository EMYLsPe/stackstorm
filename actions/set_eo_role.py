roleTemplate = {
    "kind": "Role",
    "apiVersion": "rbac.authorization.k8s.io/v1",
    "metadata": {
        "namespace": "",
        "name": "environment-operator-namespace-access"
    },
    "rules": [
        {
            "apiGroups": ["*"],
             "verbs": ["*"],
             "resources": ["*"]
        }
    ]
}

class CreateEORole(Action):

    def run(self, namespace):

        self.namespace = namespace

        return (True, self._createRoleConfig())

    def _createRoleConfig(self):
        myconf = roleTemplate
        myconf['metadata']['namespace']    = self.namespace

        return myconf