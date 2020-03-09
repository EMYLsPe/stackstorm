from st2common.runners.base_action import Action


appendSubjectTemplate = {
    "kind": "ServiceAccount",
    "name": "environment-operator",
    "namespace": ""
}


class EOIstioRoleBinding(Action):

    def run(self, namespace, istioRoleBinding):

        self.namespace         = namespace
        self.istioRoleBinding  = istioRoleBinding

        return (True, self._appendEOIstioRoleBindingConf())


    def _appendEOIstioRoleBindingConf(self):
        newServiceAccount = appendSubjectTemplate
        newServiceAccount['namespace'] = self.namespace
        self.istioRoleBinding['subjects'].append(newServiceAccount)

        return self.istioRoleBinding
