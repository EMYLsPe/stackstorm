#!/bin/sh

st2 action delete bitesize.create_eo
st2 action delete bitesize.delete_eo
st2 action delete bitesize.set_eo_deployment
st2 action delete bitesize.set_eo_ingress
st2 action delete bitesize.set_eo_istio_role_binding
st2 action delete bitesize.set_eo_limits
st2 action delete bitesize.set_eo_role
st2 action delete bitesize.set_eo_secrets
st2 action delete bitesize.set_eo_svc

cd /opt/stackstorm/packs/bitesize/actions/
sudo ls | grep 'eo' | xargs rm

cd /opt/stackstorm/packs/bitesize/actions/workflows
sudo ls | grep 'eo' | xargs rm