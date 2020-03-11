from st2common.runners.base_action import Action


appendSubjectTemplate = {
    "kind": "ServiceAccount",
    "name": "environment-operator",
    "namespace": ""
}


class EOIstioRoleBinding(Action):

    def run(self, namespace, istioRoleBinding, append):

        self.namespace         = namespace
        self.istioRoleBinding  = istioRoleBinding
        self.append            = append

        funct =  self._appendEOIstioRoleBindingConf() if append else self._removeEOIstioRoleBindingConf()

        return (True, funct)


    def _appendEOIstioRoleBindingConf(self):
        newServiceAccount = appendSubjectTemplate
        newServiceAccount['namespace'] = self.namespace
        self.istioRoleBinding['subjects'].append(newServiceAccount)

        return self.istioRoleBinding

    def _removeEOIstioRoleBindingConf(self):

        if self.istioRoleBinding['subjects'] is not None:
            sa = next((item for item in self.istioRoleBinding['subjects'] if item["namespace"] == self.namespace), None)

            if sa is not None:
                self.istioRoleBinding['subjects'].remove(sa)

        return self.istioRoleBinding
